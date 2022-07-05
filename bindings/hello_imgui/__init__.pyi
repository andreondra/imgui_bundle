# type: ignore
import sys
from typing import Literal, List, Any, Optional, Tuple
import numpy as np
from enum import Enum
import numpy

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:hello_imgui_amalgamation.h>    ####################
# THIS FILE WAS GENERATED AUTOMATICALLY. DO NOT EDIT.

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui.h                                                                          //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


# <Namespace HelloImGui>
#*
#@@md#AssetsStructure
#
#Assets located beside the application CMakeLists are embedded automatically.
#
#For example, you can have the following project structure:
#````
#my_app/
#├── CMakeLists.txt        # Your app's CMakeLists
#├── assets/               # Its assets: for mobile devices and emscripten
#│   └── fonts/            # they are embedded automatically by hello_imgui_add_app.cmake
#│       └── my_font.ttf
#├── my_app.main.cpp       # Its source code
#````
#
#Then you can load the asset "fonts/my_font.ttf", on all platforms.
#@@md
#


#*
#@@md#LoadAssetFileData
#
#* `AssetFileData LoadAssetFileData(const char *assetPath)` will load an entire asset file into memory.
# This works on all platforms, including android.
# ````cpp
#    struct AssetFileData
#    {
#        None * data = None;
#        size_t dataSize = 0;
#    };
# ````
#* `FreeAssetFileData(AssetFileData * assetFileData)` will free the memory.
#
#  Note about ImGui: "ImGui::GetIO().Fonts->AddFontFromMemoryTTF" takes ownership of the data
#  and will free the memory for you.
#
#@@md
#*
class AssetFileData:
    data:Any = None
    data_size:int = 0

def load_asset_file_data(asset_path: str) -> AssetFileData:
    pass
def free_asset_file_data(asset_file_data: AssetFileData) -> None:
    pass



#*
#@@md#assetFileFullPath
#  `std::string assetFileFullPath(const std::string& assetRelativeFilename)` will return the path to assets.
#
# This works under all platforms __except Android__.
# For compatibility with Android and other platforms, prefer to use `LoadAssetFileData` whenever possible.
#
#* Under iOS it will give a path in the app bundle (/private/XXX/....)
#* Under emscripten, it will be stored in the virtual filesystem at "/"
#* Under Android, assetFileFullPath is *not* implemented, and will throw an error:
#  assets can be compressed under android, and you cannot use standard file operations!
#  Use LoadAssetFileData instead
#@@md
#
def asset_file_full_path(asset_relative_filename: str) -> str:
    pass



def override_assets_folder(folder: str) -> None:
    """ Advanced: forces the assets folder location
     (when using this, automatic assets installation on mobile platforms may not work)
    """
    pass

# </Namespace HelloImGui>
# namespace HelloImGui

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui.h continued                                                                //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/hello_imgui_error.h included by hello_imgui.h                              //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////




#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui.h continued                                                                //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/icons_font_awesome.h included by hello_imgui.h                             //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Generated by https://github.com/juliettef/IconFontCppHeaders script
# GenerateIconFontCppHeaders.py for language C89 from
# https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/metadata/icons.yml
# for use with
# https://github.com/FortAwesome/Font-Awesome/blob/master/webfonts/fa-solid-900.ttf,
# https://github.com/FortAwesome/Font-Awesome/blob/master/webfonts/fa-regular-400.ttf,


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui.h continued                                                                //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/image_gl.h included by hello_imgui.h                                       //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui.h continued                                                                //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/image_from_asset.h included by hello_imgui.h                               //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#*
#@@md#HelloImGui::ImageFromAsset
#
#* `HelloImGui::ImageFromAsset(const char *assetPath, size, ...)`: will display a static image from the assets.
#* `bool HelloImGui::ImageButtonFromAsset(const char *assetPath, size, ...)`: will display a button using an image from the assets.
#* `ImTextureID HelloImGui::ImTextureIdFromAsset(const char *assetPath)`: will return a texture ID for an image loaded from the assets.
#
#Images are loaded when first displayed, and then cached (they will be freed just before the application exits).
#
#For example, given this files structure:
#````
#├── CMakeLists.txt
#├── assets/
#│   └── my_image.jpg
#└── my_app.main.cpp
#````
#
#then, you can display "my_image.jpg", using:
#
#````cpp
#HelloImGui::ImageFromAsset("my_image.jpg");
#````
#
#*Note: HelloImGui::ImageFromAsset only works with OpenGL backends. It will throw an exception on other backends*
#@@md
#

# <Namespace HelloImGui>
def image_from_asset(
    asset_path: str,
    size: ImVec2 = ImVec2(0, 0),
    uv0: ImVec2 = ImVec2(0, 0),
    uv1: ImVec2 = ImVec2(1,1),
    tint_col: ImVec4 = ImVec4(1,1,1,1),
    border_col: ImVec4 = ImVec4(0,0,0,0)
    ) -> None:
    pass
def image_button_from_asset(
    asset_path: str,
    size: ImVec2 = ImVec2(0, 0),
    uv0: ImVec2 = ImVec2(0, 0),
    uv1: ImVec2 = ImVec2(1,1),
    frame_padding: int = -1,
    bg_col: ImVec4 = ImVec4(0,0,0,0),
    tint_col: ImVec4 = ImVec4(1,1,1,1)
    ) -> bool:
    pass
def im_texture_id_from_asset(asset_path: str) -> ImTextureID:
    pass

# <Namespace internal>
def free_image_from_asset_map() -> None:
    pass
# </Namespace internal>
# </Namespace HelloImGui>

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui.h continued                                                                //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/runner_params.h included by hello_imgui.h                                  //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/app_window_params.h included by hello_imgui/runner_params.h                //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# <Namespace HelloImGui>
#*
#@@md#AppWindowParams
#__AppWindowParams__ is a struct that defines the application window display params.
#
#Members:
#* `windowTitle`: _string, default=""_. Title of the application window
#* `windowSize`: _ImVec2, default (800,600)_. Size of the window.
#* `maximized`: _bool, default=false_. If this boolean flag is True, the application window
#   will occupy the full space of the primary screen
#* `fullScreen`: _bool, default=false_. If this boolean flag is True, the application window
#   will be full screen, with no decorations.
#    _Note: on a mobile device, the application will always be full screen._
#* `windowPosition`: _ImVec2, default=(-11000, -1)_. Position of the window if x >= -1000,
#   else let the OS decide
#@@md
#*
class AppWindowParams:

    window_title:str = ""
    window_size:ImVec2 = {800., 600.}
    maximized:bool = False
    full_screen:bool = False
    window_position:ImVec2 = {-11000., -1.}

# </Namespace HelloImGui>
# namespace HelloImGui
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/runner_params.h continued                                                  //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


# <Namespace HelloImGui>
#*
#@@md#DefaultImGuiWindowType
# __DefaultImGuiWindowType__ is an enum class that defines whether or not a full screen background window is provided.
#
# Values:
#  * _ProvideFullScreenWindow_: a full window is provided in the background
#  * _ProvideFullScreenDockSpace_: a full screen dockspace is provided in the background
#  * _NoDefaultWindow_: No default window is provided (except for ImGui's default "debug" window)
#@@md
#
class DefaultImGuiWindowType(Enum):
    provide_full_screen_window = 0
    provide_full_screen_dock_space = 1
    no_default_window = 2

#*
#@@md#ImGuiWindowParams
#__ImGuiWindowParams__ is a struct that defines the ImGui inner windows params
#These settings affect the imgui inner windows inside the application window.
#In order to change the application window settings, change the _AppWindowsParams_
#
# Members:
#
#  * `defaultImGuiWindowType`: _DefaultImGuiWindowType, default=ProvideFullScreenWindow_.
#      By default, a full window is provided in the background. You can still
#      add windows on top of it, since the Z-order of this background window is always behind
#
#  * `backgroundColor`: _ImVec4, default=ImVec4(0.45, 0.55, 0.60, 1.00)_.
#      This is the "clearColor", only visible is defaultImGuiWindowType is NoDefaultWindow.
#
#  * `showMenuBar`: _bool, default=false_.
#    Show Menu bar on top of imgui main window
#    You can customize the menu via `RunnerCallbacks.ShowMenus()`
#
#  * `showMenu_App`: _bool, default=true_.
#    If menu bar is shown, include or not the default app menu (with Quit button)
#
#  * `showMenu_View`: _bool, default=true_.
#    If menu bar is shown, include or not the default _View_ menu, that enables to change the layout and
#    set the docked windows and status bar visibility)
#
#  * `showStatusBar`: _bool, default=false_.
#    Flag that enable to show a Status bar at the bottom. You can customize the status bar
#    via RunnerCallbacks.ShowStatus()
#
#  * `showStatus_Fps`: _bool, default=true_. If set, display the FPS in the status bar.
#
#  * `configWindowsMoveFromTitleBarOnly`: _bool, default=true_.
#    Make windows only movable from the title bar
#@@md
#
class ImGuiWindowParams:
    default_im_gui_window_type:DefaultImGuiWindowType = DefaultImGuiWindowType::ProvideFullScreenWindow

    background_color:ImVec4 = ImVec4(0.45, 0.55, 0.60, 1.00)

    show_menu_bar:bool = False
    show_menu_app:bool = True
    show_menu_view:bool = True

    show_status_bar:bool = False
    show_status_fps:bool = True

    config_windows_move_from_title_bar_only:bool = True

# </Namespace HelloImGui>
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/runner_params.h continued                                                  //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/runner_callbacks.h included by hello_imgui/runner_params.h                 //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/imgui_default_settings.h included by hello_imgui/runner_callbacks.h        //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
# <Namespace HelloImGui>
def load_font_ttf(
    font_filename: str,
    font_size: float,
    use_full_glyph_range: bool = False,
    config: ImFontConfig = ImFontConfig()
    ) -> ImFont:
    pass
def load_font_ttf_with_font_awesome_icons(
    font_filename: str,
    font_size: float,
    use_full_glyph_range: bool = False,
    config_font: ImFontConfig = ImFontConfig(),
    config_icons: ImFontConfig = ImFontConfig()
    ) -> ImFont:
    pass
def merge_font_awesome_to_last_font(
    font_size: float,
    config: ImFontConfig = ImFontConfig()
    ) -> ImFont:
    pass

# <Namespace ImGuiDefaultSettings>
def load_default_font_with_font_awesome_icons() -> None:
    pass
def setup_default_im_gui_config() -> None:
    pass
def setup_default_im_gui_style() -> None:
    pass
# </Namespace ImGuiDefaultSettings>
# </Namespace HelloImGui>

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/runner_callbacks.h continued                                               //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# <Namespace HelloImGui>
#*
#@@md#VoidFunction_AnyEventCallback
#**VoidFunctionPointer** can hold any None(None) function.
#````cpp
#using VoidFunction = std::function<None(None)>
#````
#
#**AnyEventCallback** can hold any bool(None *) function.
#  It is designed to handle callbacks for a specific backend.
#````cpp
#using AnyEventCallback = std::function<bool(None * backendEvent)>
#````
#
#@@md
#*

#*
#@@md#MobileCallbacks
#**MobileCallbacks** is a struct that contains callbacks that are called by the application
# when running under "Android, iOS and WinRT".
# These events are specific to mobile and embedded devices that have different requirements
# than your usual desktop application. These events must be handled quickly,
# since often the OS needs an immediate response and will terminate your process shortly
# after sending the event if you do not handle them apprpriately.
#
# Note: on mobile devices, it is not possible to "Quit" an application, it can only be put on Pause.
#
# * `OnDestroy`: _VoidFunction, default=empty_. The application is being terminated by the OS.
# * `OnLowMemory`: _VoidFunction, default=empty_. The application is low on memory, free memory if possible.
# * `OnPause`: _VoidFunction, default=empty_. The application is about to enter the background.
# * `OnResume`: _VoidFunction, default=empty_. The application is has come to foreground and is now interactive.
#
# Note: 'OnPause' and 'OnResume' are called twice consecutively under iOS (before and after entering background
# or foreground).
# @@md
#
class MobileCallbacks:
    on_destroy:VoidFunction = {}
    on_low_memory:VoidFunction = {}
    on_pause:VoidFunction = {}
    on_resume:VoidFunction = {}

#*
# @@md#RunnerCallbacks
# **RunnerCallbacks** is a struct that contains the callbacks that are called by the application
#
# _Members_
#
#* `ShowGui`: *VoidFunction, default=empty*.
#  Fill it with a function that will add your widgets.
#
#* `ShowMenus`: *VoidFunction, default=empty*.
#    A function that will render your menus. Fill it with a function that will add ImGui menus by calling:
#    _ImGui::BeginMenu(...) / ImGui::MenuItem(...) / ImGui::EndMenu()_
#
#    _Notes:_
#    * you do not need to call _ImGui::BeginMenuBar_ and _ImGui::EndMenuBar_
#    * Some default menus can be provided: see _ImGuiWindowParams_ options
#      (_showMenuBar, showMenu_App_QuitAbout, showMenu_View_)
#
#* `ShowStatus`: *VoidFunction, default=empty*.
#  A function that will add items to the status bar. Use small items (ImGui::Text for example),
#  since the height of the status is 30. Also, remember to call ImGui::SameLine() between items.
#
#* `PostInit`: *VoidFunction, default=empty*.
#    You can here add a function that will be called once after OpenGL and ImGui are inited
#
#* `BeforeExit`: *VoidFunction, default=empty*.
#    You can here add a function that will be called once before exiting (when OpenGL and ImGui are
#    still inited)
#
#* `AnyBackendEventCallback`: *AnyBackendCallback, default=empty*.
#  Callbacks for events from a specific backend. _Only implemented for SDL, where the event
#  will be of type 'SDL_Event *'_
#  This callback should return True if the event was handled and shall not be processed further.
#
#* `LoadAdditionalFonts`: *VoidFunction, default=_LoadDefaultFont_WithFontAwesome*.
#   A function that is called when fonts are ready to be loaded.
#   By default, _LoadDefaultFont_WithFontAwesome_ is called but you can copy-customize it.
#
#* `SetupImGuiConfig`: *VoidFunction, default=_ImGuiDefaultSettings::SetupDefaultImGuiConfig*.
#    If needed, change ImGui config via SetupImGuiConfig (enable docking, gamepad, etc)
#
#* `SetupImGuiStyle`: *VoidFunction, default=_ImGuiDefaultSettings::SetupDefaultImGuiConfig*.
#    If needed, setup your own style by providing your own SetupImGuiStyle callback
#
#
#* `mobileCallbacks`: *_MobileCallbacks_*. Callbacks that are called by the application
#    when running under "Android, iOS and WinRT".
#Notes:
#  * 'mobileCallbacks' is present only if the target device is a mobile device (iOS, Android).
#     Use `#ifdef HELLOIMGUI_MOBILEDEVICE` to detect this.
#  * These events are currently handled only with SDL backend.
#@@md
#
class RunnerCallbacks:
    show_gui:VoidFunction = {}
    show_menus:VoidFunction = {}
    show_status:VoidFunction = {}
    post_init:VoidFunction = {}
    before_exit:VoidFunction = {}

    any_backend_event_callback:AnyEventCallback = {}

    load_additional_fonts:VoidFunction = ImGuiDefaultSettings::LoadDefaultFont_WithFontAwesomeIcons
    setup_im_gui_config:VoidFunction = ImGuiDefaultSettings::SetupDefaultImGuiConfig
    setup_im_gui_style:VoidFunction = ImGuiDefaultSettings::SetupDefaultImGuiStyle


# </Namespace HelloImGui>
# namespace HelloImGui

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/runner_params.h continued                                                  //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/docking_params.h included by hello_imgui/runner_params.h                   //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# <Namespace HelloImGui>
#*
#@@md#DockingIntro
#
#HelloImGui facilitates the use of dockable windows (based on ImGui [docking branch](https://github.com/ocornut/imgui/tree/docking)).
#
#You can easily specify the default layout of the dockable windows, as well as their GUI code.
#HelloImGui will then provide a "View" menu with options in order to show/hide the dockable windows, and to restore the default layout
#
#![demo docking](../../docs/images/docking.gif)
#
#Source for this example: [src/hello_imgui_demos/hello_imgui_demodocking](../../src/hello_imgui_demos/hello_imgui_demodocking)
#
#This is done via the `DockingParams` struct: its member `dockingSplits` specifies the layout,
#and its member `dockableWindows` specifies the list of dockable windows, along with their default location,
#and their code (given by lambdas). See doc below for more details.
#@@md
#
#
#Docking params: Example usage
#@@md#DockingExample
#
#````cpp
#HelloImGui::RunnerParams runnerParams;
#runnerParams.imGuiWindowParams.defaultImGuiWindowType =
#    HelloImGui::DefaultImGuiWindowType::ProvideFullScreenDockSpace;
#
#runnerParams.dockingParams.dockingSplits =
#{
#    // First, add a bottom space whose height is 25% of the app height
#    // This will split the preexisting default dockspace "MainDockSpace"
#    // in two parts.
#    { "MainDockSpace", "BottomSpace", ImGuiDir_Down, 0.25 },
#    // Then, add a space to the left which occupies a column
#    // whose width is 25% of the app height
#    { "MainDockSpace", "LeftSpace", ImGuiDir_Left, 0.25 }
#    // We now have three spaces: "MainDockSpace", "BottomSpace", and "LeftSpace"
#};
#runnerParams.dockingParams.dockableWindows =
#{
#    // A Window named "Main" will be placed in "MainDockSpace".
#    // Its Gui is provided by the VoidFunction "MainGui"
#    {"Main", "MainDockSpace", MainGui},
#    // A Log  window named "Logs" will be placed in "BottomSpace".
#    // Its Gui is provided by the VoidFunction "ShowLogs"
#    {"Logs", "BottomSpace", ShowLogs},
#    // A Command panel named "Commands" will be placed in "LeftSpace".
#    // Its Gui is provided by the VoidFunction "ShowCommandsPanel"
#    {"Commands", "LeftSpace", ShowCommandsPanel}
#};
#
#runnerParams.imGuiWindowParams.showMenuBar = True;
#runnerParams.imGuiWindowParams.showStatusBar = True;
#
#HelloImGui::Run(runnerParams);
#````
#
#@@md
#

#***************************************************************************


#*
#@@md#DockingSplit
# **DockingSplit** is a struct that defines the way the docking splits should be applied on the screen
# in order to create new Dock Spaces. _DockingParams_ contains a _vector[DockingSplit]_,
# in order to partition the screen at your will.
#
#_Members:_
#
#* `initialDock`: _DockSpaceName (aka string)_
#
#    id of the space that should be split.
#    At the start, there is only one Dock Space named "MainDockSpace".
#    You should start by partitioning this space, in order to create a new dock space.
#
#* `newDock`: _DockSpaceName (aka string)_. id of the new dock space that will be created
#* `direction`: *ImGuiDir_ (enum with ImGuiDir_Down, ImGuiDir_Down, ImGuiDir_Left, ImGuiDir_Right)*.
#Direction where this dock space should be created
#* `ratio`: _float, default=0.25_. Ratio of the initialDock size that should be used by the new dock space
#@@md
#
class DockingSplit:

    initial_dock:DockSpaceName
    new_dock:DockSpaceName
    direction:ImGuiDir_
    ratio:float = 0.25

#*
#@@md#DockableWindow
# **DockableWindow** is a struct that represents a window that can be docked.
#
#_Members:_
#
#* `label`: _string_. Title of the window.
#* `dockSpaceName`: _DockSpaceName (aka string)_. Id of the dock space where this window
#   should initialy be placed
#* `GuiFunction`: _VoidFuntion_. Any function that will render this window's Gui.
#* `isVisible`: _bool, default=true_. Flag that indicates whether this window is visible or not.
#* `canBeClosed`: _bool, default=true_. Flag that indicates whether the user can close this window.
#* `callBeginEnd`: _bool, default=true_. Flag that indicates whether ImGui::Begin and ImGui::End
#   calls should be added automatically (with the given "label"). Set to False if you want to call
#   ImGui::Begin/End yourself
#* `includeInViewMenu`: _bool, default=true_. Flag that indicates whether this window should be mentioned
#   in the view menu.
#* `imGuiWindowFlags`: _ImGuiWindowFlags, default=0_. Window flags, see enum ImGuiWindowFlags_
#* `windowSize`: _ImVec2, default=(0., 0.) (i.e let the app decide)_. Window size (unused if docked)
#* `windowSizeCondition`: _ImGuiCond, default=ImGuiCond_FirstUseEver_. When to apply the window size.
#* `windowPos`: _ImVec2, default=(0., 0.) (i.e let the app decide)_. Window position (unused if docked)
#* `windowPosCondition`: _ImGuiCond, default=ImGuiCond_FirstUseEver_. When to apply the window position.
#* `focusWindowAtNextFrame`: _bool, default = false_. If set to True this window will be focused at the next frame.
#@@md
#*
class DockableWindow:

    label:str

    dock_space_name:DockSpaceName

    gui_fonction:VoidFunction = {}

    is_visible:bool = True
    can_be_closed:bool = True
    call_begin_end:bool = True
    include_in_view_menu:bool = True
    im_gui_window_flags:ImGuiWindowFlags = 0

    window_size:ImVec2 = ImVec2(0., 0.)
    window_size_condition:ImGuiCond = ImGuiCond_FirstUseEver

    window_position:ImVec2 = ImVec2(0., 0.)
    window_position_condition:ImGuiCond = ImGuiCond_FirstUseEver

    focus_window_at_next_frame:bool = False

#*
#@@md#DockingParams
# **DockingParams** contains all the settings concerning the docking,
# together _with the Gui functions for the docked windows_.
#
# _Members:_
#
#* `dockingSplits`: _vector[DockingSplit]_.
#  Defines the way docking splits should be applied on the screen in order to create new Dock Spaces
#* `dockableWindows`: _vector[DockableWindow]_.
#  List of the dockable windows, together with their Gui code
#* `resetUserDockLayout`: _bool, default=true_.
#  Reset user layout at application startup
#
# _Helpers:_
#
# * `DockableWindow * dockableWindowOfName(const std::string & name)`: returns a pointer to a dockable window
# * `None focusDockableWindow(const std::string& name)`: will focus a dockable window
#
#@@md
#
class DockingParams:
    docking_splits:List[DockingSplit]

    dockable_windows:List[DockableWindow]

    reset_user_dock_layout:bool = True

    # wasDockLayoutApplied is an internal variable
    was_dock_layout_applied:bool = False

    def dockable_window_of_name(self, name: str) -> DockableWindow:
        pass
    def focus_dockable_window(self, window_name: str) -> None:
        pass
# </Namespace HelloImGui>

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/runner_params.h continued                                                  //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/backend_pointers.h included by hello_imgui/runner_params.h                 //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# <Namespace HelloImGui>

#*
# @@md#BackendPointers
#**BackendPointers** is a struct that contains optional pointers to the backend implementations (for SDL and GLFW).
#
#These pointers will be filled when the application starts, and you can use them to customize
#your application behavior using the selected backend.
#
# Members:
#* `glfwWindow`: _void *, default=nullptr_. Pointer to the main GLFW window (of type `GLFWwindow*`).
#  Only filled if the backend is GLFW.
#* `sdlWindow`: _void *, default=nullptr_. Pointer to the main SDL window (of type `SDL_Window*`).
#  Only filled if the backend is SDL (or emscripten + sdl)
#* `sdlGlContext`: _void *, default=nullptr_. Pointer to SDL's GlContext (of type `SDL_GLContext`).
#  Only filled if the backend is SDL (or emscripten + sdl)
#@@md
#
class BackendPointers:
    # GLFWwindow*
    glfw_window:Any = None

    # SDL_Window*
    sdl_window:Any = None
    # SDL_GLContext
    sdl_gl_context:Any = None

# </Namespace HelloImGui>

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui/runner_params.h continued                                                  //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
# <Namespace HelloImGui>

#*
# @@md#RunnerParams
# **RunnerParams** is a struct that contains all the settings and callbacks needed to run an application.
#
# Members:
#* `callbacks`: _see [runner_callbacks.h](runner_callbacks.h)_.
#    callbacks.ShowGui() will render the gui, ShowMenus() will show the menus, etc.
#* `appWindowParams`: _see [app_window_params.h](app_window_params.h)_.
#    application Window Params (position, size, title)
#* `imGuiWindowParams`: _see [imgui_window_params.h](imgui_window_params.h)_.
#    imgui window params (use docking, showMenuBar, ProvideFullScreenWindow, etc)
#* `dockingParams`: _see [docking_params.h](docking_params.h)_.
#    dockable windows content and layout
#* `backendPointers`: _see [backend_pointers.h](backend_pointers.h)_.
#   A struct that contains optional pointers to the backend implementations. These pointers will be filled
#   when the application starts
#* `appShallExit`: _bool, default=false_.
#   will be set to True by the app when exiting.
#   _Note: 'appShallExit' has no effect on Mobile Devices (iOS, Android) and under emscripten, since these apps
#   shall not exit._
#* `fps`: _int, default = 0` when applicable, set the application refresh rate
#   (only used on emscripten for the moment: 0 stands for "let the app or the browser decide")
#@@md
#
class RunnerParams:
    callbacks:RunnerCallbacks
    app_window_params:AppWindowParams
    im_gui_window_params:ImGuiWindowParams
    docking_params:DockingParams
    backend_pointers:BackendPointers
    app_shall_exit:bool = False
    fps:int = 0

# </Namespace HelloImGui>
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       hello_imgui.h continued                                                                //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#*
#@@md#HelloImGui::Run
#__HelloImGui::Run()__ will run an application with a single call.
#
#Two signatures are provided:
#
#* `HelloImGui::Run(RunnerParams &)`: full signature, the most customizable version.
#   Runs an application whose params and Gui are provided
#by runnerParams.
#
#* `HelloImGui::Run(guiFunction, windowSize, windowTitle)`: simple signature
#in order to start a simple application with ease.
#@@md
#
# <Namespace HelloImGui>
def run(runner_params: RunnerParams) -> None:
    pass

def run(
    gui_fonction: VoidFunction,
    window_size: ImVec2 = ImVec2(800., 600.),
    window_title: str = ""
    ) -> None:
    pass
# </Namespace HelloImGui>

#*
#@@md#SDLMain
#Warning for SDL apps under iOS and Android:
#
#SDL uses a dirty hack in order to _replace your main() function by its own main() function_,
#which will then call your own main !
#
#Please make sure that the signature of your main() function is *exactly*
#    `int main(int argc, char **argv)`
#and that your main() function returns an int.
#@@md
#
####################    </generated_from:hello_imgui_amalgamation.h>    ####################

# </litgen_stub>
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
