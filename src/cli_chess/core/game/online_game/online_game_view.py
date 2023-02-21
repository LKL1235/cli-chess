# Copyright (C) 2021-2023 Trevor Bayless <trevorbayless1@gmail.com>
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
from cli_chess.core.game import PlayableGameViewBase
from cli_chess.utils.ui_common import handle_mouse_click
from prompt_toolkit.layout import Window, FormattedTextControl, VSplit, D
from prompt_toolkit.formatted_text import StyleAndTextTuples
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.filters import Condition
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cli_chess.core.game.online_game import OnlineGamePresenter


class OnlineGameView(PlayableGameViewBase):
    def __init__(self, presenter: OnlineGamePresenter):
        self.presenter = presenter
        super().__init__(presenter)
