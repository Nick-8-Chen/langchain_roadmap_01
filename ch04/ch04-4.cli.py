from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/chain/")
resp = remote_chain.invoke({"language": "Traditional Chinese", "text": "The key question isn't what AI can do, but what we should do with it."})
print(resp)
