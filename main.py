from GameManager import GameManager
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def generate_board_figure(board, last_move=None):
    fig = go.Figure()
    square_size = 70
    piece_font_size = 30
    colors = {
        "0": "#555555",
        "1": "#ffcc00",
        "2": "#ff9900",
        "3": "#ff6600",
        "4": "#ff3300",
        "5": "#ff0000",
        "6": "#cc0000",
        "7": "#990000",
        "8": "#660000",
        "U": "gray",
        "M": "#ffff00",
        "T": "red",
    }
    for row_index in range(len(board)):
        for col_index in range(len(board)):
            display_row_index = abs(len(board) - row_index - 1)
            cell = board[row_index][col_index]
            cell_color = colors[cell]
            fig.add_trace(
                go.Scatter(
                    x=[col_index/2 + 0.5],
                    y=[display_row_index + 0.5],
                    marker=dict(color=cell_color, size=square_size),
                    mode="markers",
                    marker_symbol="square",
                    line=dict(width=1),
                )
            )
            color = "white" 
            symbol = "" if cell == "U" else cell
            fig.add_trace(go.Scatter(
                    x=[col_index/2 + 0.5],
                    y=[display_row_index+ 0.5],
                    text=[symbol],
                    mode="text",
                    textfont=dict(color=color, size=piece_font_size),
                    textposition="middle center",
                    showlegend=False,
                    name=symbol,
                )
            )
    fig.update_layout(
        margin={"l": 0, "r": 0, "b": 0, "t": 0},
        height=square_size * len(board),
        width=square_size * len(board),
        dragmode=False,
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, len(board)]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, len(board)]),
    )
    return fig


def main():

    st.title("Minesweeper")
    if "status" not in st.session_state:
        st.session_state["status"] = "Game Over"
        
    if st.session_state["status"] == "Game Over":
        grid_size = st.slider("Grid Size", 3, 10, 5)
        no_of_mines = st.slider(
            "No. of Mines", 1, (grid_size * grid_size) - 1, grid_size
        )
        gameManager = GameManager(grid_size, no_of_mines, "ai")
        st.session_state["gameManager"] = gameManager
        if st.button("Start Game"):
            st.session_state["status"] = "Playing"
            
    if st.session_state["status"] == "Playing" and st.button("Next Move"):
        gameManager = st.session_state["gameManager"]
        st.write(
            f"Config: \n Grid Size: {gameManager.size}x{gameManager.size} \n No. of Mines: {gameManager.noMines}"
        )
        st.session_state["gameManager"].nextMove()
        board = st.session_state["gameManager"].getBoard()

        fig = generate_board_figure(board)
        empty = st.empty()
        with empty.container():
            st.plotly_chart(fig, use_container_width=True)
            st.table(board) # temporary dev only


if __name__ == "__main__":
    main()
