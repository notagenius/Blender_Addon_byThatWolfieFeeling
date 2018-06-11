import bpy

bl_info = {
    "name": "Select Current Active Object",
    "author": "ThatWolfieFeeling",
    "category": "Object",
}

class Active_Object_Selection(bpy.types.Operator):
    """Select Current Active Object"""
    bl_idname = "object.select_active"
    bl_label = "Select Active"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.select_all(action = 'DESELECT')
        bpy.context.active_object.select = True
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(Active_Object_Selection.bl_idname)

# store keymaps here to access after registration
addon_keymaps = []

def register():
    bpy.utils.register_class(Active_Object_Selection)
    bpy.types.VIEW3D_MT_object.append(menu_func)

    # handle the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(Active_Object_Selection.bl_idname, 'SPACE', 'PRESS', ctrl=True, shift=True)
    addon_keymaps.append(km)

def unregister():
    bpy.utils.unregister_class(Active_Object_Selection)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

    # handle the keymap
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    # clear the list
    del addon_keymaps[:]


if __name__ == "__main__":
    register()
