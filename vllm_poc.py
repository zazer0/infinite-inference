from vllm import LLM
model = LLM("./EvilAlpacaRight-L3_2-3B-W4A16-s30")
output = model.generate("My name is")


print("GOT OUTPUT:", output)
