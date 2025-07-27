from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from app.services.bot.constants import STARTING_FEN 
import chess

ptop = {
    "w": "white",
    "b": "black",
}

def run_hf(hf: str, model: str, player='w', opponent='b', fen = STARTING_FEN):
    '''
    query llm for move
    
    @param: hf          hugging face api key
    @param: model       llm model
    @param: player      player color
    @param: opponent    opponent color
    @param: fen         current game fen
    '''
    res = {
        "fen": "",
        "resp": "",
        "isvalid": False,
        "iserr": False,
        "err": ""
    }

    llm = HuggingFaceEndpoint(
        repo_id=model,
        huggingfacehub_api_token=hf,
        task="text-generation",
        do_sample=False,
    )

    chat = ChatHuggingFace(llm=llm, verbose=True)


    template = PromptTemplate(
        input_variables=["fen", "player", "bot"],
        template='''We are playing a chess game (me vs you). I am {player}, and you are {bot}. It is your turn to move. Respond with your move in standard chess notation (e.g., 'e4') followed by the FULL FEN string after your move. The current FEN is: "{fen}"
        Format your response exactly as follows:
        Move: [your move]
        FEN: [resulting FEN string]
        '''
        # template="We are playing a chess game. I am {player}, you are {bot}. Make a move and respond with the FULL FEN string resulting from your move. The current FEN is {fen}"
    )

    invoked = template.invoke(
        {"fen": f"{STARTING_FEN}",
        "player": "black",
        "bot": "white"}
    )


    try:
        resp = llm.invoke(invoked)
        valid = chess.Board(resp.split('FEN: ')[-1].strip()).is_valid()
        new_fen = resp.split('FEN: ')[-1].strip()
        
        if not valid:
            res["isvalid"] = False
        else:
            res["isvalid"] = True
        
        res["iserr"] = False
        res["resp"] = resp
        res["fen"] = new_fen

        print(resp)
    except Exception as e:
        res["iserr"] = True
        res["err"] = e
        print(f"Model unavailable\n{e}")

    return res

def run_gemini(gem: str, model: str="gemini-2.0-flash-lite", player='w', opponent='b', fen = STARTING_FEN):
    '''
    query llm for move
    
    @param: gem         gemini api key
    @param: model       llm model
    @param: player      player color
    @param: opponent    opponent color
    @param: fen         current game fen
    '''
    res = {
        "fen": "",
        "move": "",
        "resp": [],
        "isvalid": False,
        "iserr": False,
        "err": "",
    }

    # llm = HuggingFaceEndpoint(
    #     repo_id=model,
    #     huggingfacehub_api_token=hf,
    #     task="text-generation",
    #     do_sample=False,
    # )
    llm = ChatGoogleGenerativeAI(
        model=model,
        google_api_key=gem

    )


    template = PromptTemplate(
        input_variables=["fen", "player", "bot"],
        template='''We are playing a chess game (me vs you). I am {player}, and you are {bot}. It is your turn to move. Respond with your move in standard chess notation (e.g., 'e4') followed by the FULL FEN string after your move. The current FEN is: "{fen}"
        Format your response exactly as follows:
        Move: [your move]
        FEN: [resulting FEN string]
        '''
        # template="We are playing a chess game. I am {player}, you are {bot}. Make a move and respond with the FULL FEN string resulting from your move. The current FEN is {fen}"
    )

    invoked = template.invoke({
        "fen": f"{fen}",
        "player": ptop[player.lower()],
        "bot": ptop[opponent.lower()]
    })


    try:
        resp = llm.invoke(invoked)
        valid = chess.Board(resp.content.split('FEN: ')[-1].strip()).is_valid()
        content = resp.content.split('FEN: ')
        res["resp"] = content
        new_fen = content[-1].strip()
        move_str = content[0].strip()
        
        if not valid:
            res["isvalid"] = False
        else:
            res["isvalid"] = True
        
        res["iserr"] = False
        res["move"] = move_str
        res["fen"] = new_fen

        print(f"\n\n{resp}\n\n")
    except Exception as e:
        res["iserr"] = True
        res["err"] = f"{type(e).__name__}: {e}"
        print(f"\n\nModel unavailable\n{e}\n\n")

    return res

