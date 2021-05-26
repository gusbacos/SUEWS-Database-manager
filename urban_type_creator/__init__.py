# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Urban_type_creator
                                 A QGIS plugin
 This plugin prepare suews lib data
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-05-20
        copyright            : (C) 2021 by GU
        email                : oskar.backlin@gu.se
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Urban_type_creator class from file Urban_type_creator.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Urban_type_creator import Urban_type_creator
    return Urban_type_creator(iface)
