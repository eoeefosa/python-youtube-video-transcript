# import the library
from parrot import Parrot

# initialize the library with a model name and a device (cpu or cuda)
parrot = Parrot(model_name="t5-base", device="cuda")

# read the input text file as a string
with open("input.txt", "r") as f:
    text = f.read()

# split the text into sentences
sentences = text.split(".")

# create an empty list to store the paraphrases
paraphrases = []

# loop through each sentence and generate one paraphrase with pegasus as the rephraser
for sentence in sentences:
    # skip empty sentences
    if sentence.strip() == "":
        continue
    # generate one paraphrase
    paraphrase = parrot.augment(input_text=sentence, num_return_sequences=1, rephraser_name="pegasus")[0]
    # append the paraphrase to the list
    paraphrases.append(paraphrase)

# join the paraphrases into a single string
output = ". ".join(paraphrases)

# write the output string to a new text file
with open("output.txt", "w") as f:
    f.write(output)
