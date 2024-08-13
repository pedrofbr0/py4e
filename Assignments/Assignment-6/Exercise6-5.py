text = "X-DSPAM-Confidence:    0.8475";
colonPos = text.find(":")
numb_wspace = text[colonPos+1:]
#numb = float(numb_wspace.lstrip())
print(float(numb_wspace))