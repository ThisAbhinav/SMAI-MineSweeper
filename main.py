from GameManager import GameManager
import streamlit as st

def main():
    st.title("Minesweeper")
    grid_size = st.slider("Grid Size", 3, 10, 5)
    no_of_mines = st.slider("No. of Mines", 1, (grid_size*grid_size) -1, grid_size)
    gameManager = GameManager(grid_size, no_of_mines, "ai")
    # gameManager.startPlay()
    if st.button("Next Move"):
        gameManager.nextMove()

if __name__ == "__main__":
    main()
