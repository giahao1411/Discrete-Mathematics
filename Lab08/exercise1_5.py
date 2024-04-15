Andersen = {
    "The Emperor's New Clothes",
    "The Little Mermaid",
    "The Little Match Girl",
    "The Snow Queen",
}

Shakespeare = {
    "Romeo and Juliet",
    "Hamlet",
    "King Lear",
    "Macbeth",
    "A Midsummer Night's Dream",
    "A Comedy of Errors",
}

Tragedy = {"Medea", "Octavia", "Oedipus", "Ur-Hamlet"}
Comedy = {
    "A Midsummer Night's Dream",
    "A Comedy of Errors",
    "The Three Musketeer",
    "The Clouds",
}
Uncategory = {"Don Quixote", "Rapunzel", "Cinderella"}

Shakespeare_Tragedy = Shakespeare.intersection(Tragedy)

Andersen_Comedy = Andersen.intersection(Comedy)
