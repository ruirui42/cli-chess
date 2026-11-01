"""Variant-aware validation for offline custom starting positions."""
from cli_chess.modules.board.board_model import BoardModel


def validate_starting_fen(fen: str, variant: str) -> str:
    """Return a normalized legal FEN, or raise ValueError before starting."""
    fen = fen.strip()
    if not fen:
        raise ValueError("Enter a FEN before starting a custom-position game")
    if fen.lower() == "startpos":
        raise ValueError("Enter a complete FEN instead of 'startpos'")

    try:
        board = BoardModel._initialize_board(variant, fen)
    except (ValueError, KeyError, TypeError) as exc:
        raise ValueError(f"Invalid FEN for {variant}: {exc}") from exc

    if not board.is_valid():
        raise ValueError(f"Invalid {variant} position: the board setup is not legal")
    if board.is_game_over():
        raise ValueError("The selected position is already game over")
    return board.fen()
