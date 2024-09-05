from GameManager import GameManager
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
def main():
    
    st.title("Minesweeper")
    empty = st.empty()
    if 'status' not in st.session_state:
        st.session_state["status"] = "Game Over"
    
    if st.session_state["status"] == "Game Over":
        grid_size = st.slider("Grid Size", 3, 10, 5)
        no_of_mines = st.slider("No. of Mines", 1, (grid_size * grid_size) - 1, grid_size)
        gameManager = GameManager(grid_size,no_of_mines, "ai")
        st.session_state["gameManager"] = gameManager
        if st.button("Start Game"):
            st.session_state["status"] = "Playing"
        
    if st.session_state["status"] == "Playing" and st.button("Next Move"):
        st.session_state["gameManager"].nextMove()
        board = st.session_state["gameManager"].getBoard()
        
        # random_data = np.random.rand(10, 3)
        # # Reset figure
        # fig = go.Figure()

        # # Create dataframe
        # df = pd.DataFrame(random_data, columns=["PC1", "PC2", "PC3"])

        # # Add new points to figure
        # fig.add_trace(
        #     go.Scatter3d(x=df["PC1"], y=df["PC2"], z=df["PC3"], mode="markers")
        # )

        with empty.container():
            st.table(board)
            # st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()
