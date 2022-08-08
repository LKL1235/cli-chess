# Copyright (C) 2021-2022 Trevor Bayless <trevorbayless1@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations
from . import GameView, GameModel
from .board import BoardPresenter
from .move_list import MoveListPresenter
from .material_difference import MaterialDifferencePresenter
from chess import WHITE, BLACK


class GamePresenter:
    def __init__(self, game_model: GameModel):
        self.game_model = game_model

        self.board_presenter = BoardPresenter(self.game_model.board_model)
        self.move_list_presenter = MoveListPresenter(self.game_model.move_list_model)
        self.material_diff_presenter_white = MaterialDifferencePresenter(self.game_model.material_diff_model, WHITE)
        self.material_diff_presenter_black = MaterialDifferencePresenter(self.game_model.material_diff_model, BLACK)

        self.game_view = GameView(self,
                                  self.board_presenter.view,
                                  self.move_list_presenter.view,
                                  self.material_diff_presenter_white.view,
                                  self.material_diff_presenter_black.view)

    def input_received(self, input: str) -> None:
        # TODO: Determine if this is a move, or other type of input
        self.make_move(input)

    def make_move(self, move: str) -> None:
        self.board_presenter.make_move(move)
