def format_fn_text(zap, shake): 
    return """strategy_random_choice_{zap}_to_{shake},""".format(zap=zap, shake=shake)

if __name__ == "__main__":
    for zap in range(1,100):
        shake = 100 - zap
        text = format_fn_text(zap, shake)
        print(text)
