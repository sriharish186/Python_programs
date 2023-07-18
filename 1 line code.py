text = "X-DSPAM-Confidence:    0.8475";
#str2=float(text[text.find(':')+1:].strip())
print(float(text[text.find(':')+1:].strip()))