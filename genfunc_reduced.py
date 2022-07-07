
def format_fn_text(zap, shake):
    return """biased_{zap}_zap_to_{shake}_shake,""".format(zap=zap, shake=shake)

if __name__ == "__main__":
    for zap in range(10,100, 10):
        shake = 100 - zap
        text = format_fn_text(zap, shake)
        print(text)
