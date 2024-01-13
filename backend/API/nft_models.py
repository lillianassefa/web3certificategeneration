from pydantic import BaseModel


class NFTIssueRequest(BaseModel):
    trainee_public_key: str
    nft_metadata: dict


class TraineeOptInRequest(BaseModel):
    trainee_public_key: str


class ApprovalRequest(BaseModel):
    trainee_public_key: str
    approval_status: str
