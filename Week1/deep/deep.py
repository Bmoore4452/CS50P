txt = str(
    input(
        "What is the Answer to the Great Question of Life, The Universe, and Everything? "
    )
    .casefold()
    .strip()
)


if txt == "42" or txt == "forty two" or txt == "forty-two":
    print("Yes")
else:
    print("No")
