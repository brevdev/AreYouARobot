def format_text(zap, shake):
    return """
def biased_{zap}_zap_to_{shake}_shake(player, hist):
    if not player.is_human: return Choices.Shake
    return choices(
        population=[Choices.Zap, Choices.Shake],
        weights=[0.{zap},0.{shake}],
        k=1
    )[0]
""".format(zap=zap, shake=shake)

if __name__ == "__main__":
    for zap in range(1,100):
        shake = 100 - zap
        text = format_text(zap, shake)
        print(text)
