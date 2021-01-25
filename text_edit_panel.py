# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "Text Edit Panel",
    "author": "todashuta",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "3D View > Side Bar > Item > Text",
    "description": "",
    "warning": "",
    "wiki_url": "https://github.com/todashuta/blender-addon-text-edit-panel/wiki",
    "tracker_url": "https://github.com/todashuta/blender-addon-text-edit-panel/issues",
    "category": "Text"
}


import bpy


class TEXT_EDIT_PT_panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Item"
    bl_label = "Text"

    @classmethod
    def poll(self, context):
        ob = context.active_object
        return ob and ob.type == "FONT" and ob.mode == "OBJECT"

    def draw(self, context):
        layout = self.layout
        layout.prop(context.active_object.data, "body")


classes = (
        TEXT_EDIT_PT_panel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
