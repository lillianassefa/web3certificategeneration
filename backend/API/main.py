from fastapi import FastAPI
from fastapi.middleware import CORSMiddleware
from API import nft_router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(nft_router.router)

ALGORAND_NODE = ""
ALGORAND_TOKEN = ""

alogod_client = algod.AlgodClient(ALGORAND_TOKEN, ALGORAND_NODE)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5143)
