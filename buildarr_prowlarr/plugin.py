# Copyright (C) 2023 Callum Dickinson
#
# Buildarr is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
#
# Buildarr is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Buildarr.
# If not, see <https://www.gnu.org/licenses/>.


"""
Prowlarr plugin interface.
"""


from __future__ import annotations

from buildarr.plugins import Plugin

from . import __version__
from .cli import prowlarr
from .config import ProwlarrConfig
from .manager import ProwlarrManager
from .secrets import ProwlarrSecrets


class ProwlarrPlugin(Plugin):
    """
    Prowlarr plugin class that Buildarr reads to process Prowlarr instances.
    """

    cli = prowlarr
    config = ProwlarrConfig
    manager = ProwlarrManager
    secrets = ProwlarrSecrets
    version = __version__
