

def hangman_drawing(x):
    graphics = [
        """
         +--------+
         |        
         |
         |
         |
        ============
        """,
        """
         +--------+
         |        |
         |
         |
         |
         |
        ============
        """,
        """
         +--------+
         |        |
         |        O
         |      
         |       
         |
        ============
        """,
        """
         +--------+
         |        |
         |        O
         |        |
         |       
         |
        ============
        """,
        """
         +--------+
         |        |
         |        O
         |       -|-
         |      
         |
        ============
        """,
        """
         +--------+
         |        |
         |        O
         |       -|-
         |       /-\\
         |
        ============
        """,
        """
         +--------+
         |        |
         |       * *
         |       -|-
         |       /-\\
         |
        ============
        """,

    ]
    return graphics[x]