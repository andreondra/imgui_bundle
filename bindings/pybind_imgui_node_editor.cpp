#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <pybind11/numpy.h>

#include "imgui-node-editor/imgui_node_editor_internal.h"
#include "imgui-node-editor/imgui_node_editor.h"


namespace py = pybind11;


namespace ax
{
    namespace NodeEditor
    {
        // using EditorContext = Detail::EditorContext;
        struct EditorContext: public Detail::EditorContext {};
    }
}


namespace
{
    uintptr_t _next_id = 1;

    uintptr_t get_next_id()
    {
        uintptr_t r = _next_id;
        ++ _next_id;
        return r;
    }
}

PYBIND11_MAKE_OPAQUE(ax::NodeEditor::Detail::EditorContext);
PYBIND11_MAKE_OPAQUE(ax::NodeEditor::EditorContext);


// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// <litgen_glue_code>  // Autogenerated code below! Do not edit!

// </litgen_glue_code> // Autogenerated code end
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


void py_init_module_imgui_node_editor(py::module& m)
{
    py::class_<ax::NodeEditor::EditorContext>(m, "EditorContext");

    py::class_<ax::NodeEditor::NodeId>(m, "NodeId")
        .def(py::init<>())
        .def(py::init<uintptr_t>())
        .def("create", []() { return ax::NodeEditor::NodeId(get_next_id()); })
        .def("id", [](const ax::NodeEditor::NodeId& self) { return self.Get(); })
        .def("__eq__", [](const ax::NodeEditor::NodeId& self, const ax::NodeEditor::NodeId& other) {
            return self.Get() == other.Get();
        })
        .def("__str__", [](const ax::NodeEditor::NodeId& self) { return std::to_string(self.Get()); })
        ;
    py::class_<ax::NodeEditor::LinkId>(m, "LinkId")
        .def(py::init<>())
        .def(py::init<uintptr_t>())
        .def("create", []() { return ax::NodeEditor::LinkId(get_next_id()); })
        .def("id", [](const ax::NodeEditor::LinkId& self) { return self.Get(); })
        .def("__eq__", [](const ax::NodeEditor::LinkId& self, const ax::NodeEditor::LinkId& other) {
            return self.Get() == other.Get();
        })
        .def("__str__", [](const ax::NodeEditor::LinkId& self) { return std::to_string(self.Get()); })
        ;
    py::class_<ax::NodeEditor::PinId>(m, "PinId")
        .def(py::init<>())
        .def(py::init<uintptr_t>())
        .def("create", []() { return ax::NodeEditor::PinId(get_next_id()); })
        .def("id", [](const ax::NodeEditor::PinId& self) { return self.Get(); })
        .def("__eq__", [](const ax::NodeEditor::PinId& self, const ax::NodeEditor::PinId& other) {
            return self.Get() == other.Get();
        })
        .def("__str__", [](const ax::NodeEditor::PinId& self) { return std::to_string(self.Get()); })
        ;


    // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    // <litgen_pydef> // Autogenerated code below! Do not edit!
    ////////////////////    <generated_from:imgui_node_editor.h>    ////////////////////
    py::enum_<ax::NodeEditor::PinKind>(m, "PinKind", py::arithmetic(), "------------------------------------------------------------------------------")
        .value("input", ax::NodeEditor::PinKind::Input, "")
        .value("output", ax::NodeEditor::PinKind::Output, "");


    py::enum_<ax::NodeEditor::FlowDirection>(m, "FlowDirection", py::arithmetic(), "")
        .value("forward", ax::NodeEditor::FlowDirection::Forward, "")
        .value("backward", ax::NodeEditor::FlowDirection::Backward, "");


    py::enum_<ax::NodeEditor::CanvasSizeMode>(m, "CanvasSizeMode", py::arithmetic(), "")
        .value("fit_vertical_view", ax::NodeEditor::CanvasSizeMode::FitVerticalView, "Previous view will be scaled to fit new view on Y axis")
        .value("fit_horizontal_view", ax::NodeEditor::CanvasSizeMode::FitHorizontalView, "Previous view will be scaled to fit new view on X axis")
        .value("center_only", ax::NodeEditor::CanvasSizeMode::CenterOnly, "Previous view will be centered on new view");


    py::enum_<ax::NodeEditor::SaveReasonFlags>(m, "SaveReasonFlags", py::arithmetic(), "------------------------------------------------------------------------------")
        .value("none", ax::NodeEditor::SaveReasonFlags::None, "")
        .value("navigation", ax::NodeEditor::SaveReasonFlags::Navigation, "")
        .value("position", ax::NodeEditor::SaveReasonFlags::Position, "")
        .value("size", ax::NodeEditor::SaveReasonFlags::Size, "")
        .value("selection", ax::NodeEditor::SaveReasonFlags::Selection, "")
        .value("add_node", ax::NodeEditor::SaveReasonFlags::AddNode, "")
        .value("remove_node", ax::NodeEditor::SaveReasonFlags::RemoveNode, "")
        .value("user", ax::NodeEditor::SaveReasonFlags::User, "");


    auto pyClassConfig =
        py::class_<ax::NodeEditor::Config>
            (m, "Config", "")
        .def_readwrite("settings_file", &ax::NodeEditor::Config::SettingsFile, "")
        .def_readwrite("user_pointer", &ax::NodeEditor::Config::UserPointer, "")
        .def_readwrite("custom_zoom_levels", &ax::NodeEditor::Config::CustomZoomLevels, "")
        .def_readwrite("canvas_size_mode", &ax::NodeEditor::Config::CanvasSizeMode, "")
        .def_readwrite("drag_button_index", &ax::NodeEditor::Config::DragButtonIndex, "Mouse button index drag action will react to (0-left, 1-right, 2-middle)")
        .def_readwrite("select_button_index", &ax::NodeEditor::Config::SelectButtonIndex, "Mouse button index select action will react to (0-left, 1-right, 2-middle)")
        .def_readwrite("navigate_button_index", &ax::NodeEditor::Config::NavigateButtonIndex, "Mouse button index navigate action will react to (0-left, 1-right, 2-middle)")
        .def_readwrite("context_menu_button_index", &ax::NodeEditor::Config::ContextMenuButtonIndex, "Mouse button index context menu action will react to (0-left, 1-right, 2-middle)")
        .def(py::init<>())
        ;


    py::enum_<ax::NodeEditor::StyleColor>(m, "StyleColor", py::arithmetic(), "------------------------------------------------------------------------------")
        .value("bg", ax::NodeEditor::StyleColor_Bg, "")
        .value("grid", ax::NodeEditor::StyleColor_Grid, "")
        .value("node_bg", ax::NodeEditor::StyleColor_NodeBg, "")
        .value("node_border", ax::NodeEditor::StyleColor_NodeBorder, "")
        .value("hov_node_border", ax::NodeEditor::StyleColor_HovNodeBorder, "")
        .value("sel_node_border", ax::NodeEditor::StyleColor_SelNodeBorder, "")
        .value("node_sel_rect", ax::NodeEditor::StyleColor_NodeSelRect, "")
        .value("node_sel_rect_border", ax::NodeEditor::StyleColor_NodeSelRectBorder, "")
        .value("hov_link_border", ax::NodeEditor::StyleColor_HovLinkBorder, "")
        .value("sel_link_border", ax::NodeEditor::StyleColor_SelLinkBorder, "")
        .value("highlight_link_border", ax::NodeEditor::StyleColor_HighlightLinkBorder, "")
        .value("link_sel_rect", ax::NodeEditor::StyleColor_LinkSelRect, "")
        .value("link_sel_rect_border", ax::NodeEditor::StyleColor_LinkSelRectBorder, "")
        .value("pin_rect", ax::NodeEditor::StyleColor_PinRect, "")
        .value("pin_rect_border", ax::NodeEditor::StyleColor_PinRectBorder, "")
        .value("flow", ax::NodeEditor::StyleColor_Flow, "")
        .value("flow_marker", ax::NodeEditor::StyleColor_FlowMarker, "")
        .value("group_bg", ax::NodeEditor::StyleColor_GroupBg, "")
        .value("group_border", ax::NodeEditor::StyleColor_GroupBorder, "")
        .value("count", ax::NodeEditor::StyleColor_Count, "");


    py::enum_<ax::NodeEditor::StyleVar>(m, "StyleVar", py::arithmetic(), "")
        .value("node_padding", ax::NodeEditor::StyleVar_NodePadding, "")
        .value("node_rounding", ax::NodeEditor::StyleVar_NodeRounding, "")
        .value("node_border_width", ax::NodeEditor::StyleVar_NodeBorderWidth, "")
        .value("hovered_node_border_width", ax::NodeEditor::StyleVar_HoveredNodeBorderWidth, "")
        .value("selected_node_border_width", ax::NodeEditor::StyleVar_SelectedNodeBorderWidth, "")
        .value("pin_rounding", ax::NodeEditor::StyleVar_PinRounding, "")
        .value("pin_border_width", ax::NodeEditor::StyleVar_PinBorderWidth, "")
        .value("link_strength", ax::NodeEditor::StyleVar_LinkStrength, "")
        .value("source_direction", ax::NodeEditor::StyleVar_SourceDirection, "")
        .value("target_direction", ax::NodeEditor::StyleVar_TargetDirection, "")
        .value("scroll_duration", ax::NodeEditor::StyleVar_ScrollDuration, "")
        .value("flow_marker_distance", ax::NodeEditor::StyleVar_FlowMarkerDistance, "")
        .value("flow_speed", ax::NodeEditor::StyleVar_FlowSpeed, "")
        .value("flow_duration", ax::NodeEditor::StyleVar_FlowDuration, "")
        .value("pivot_alignment", ax::NodeEditor::StyleVar_PivotAlignment, "")
        .value("pivot_size", ax::NodeEditor::StyleVar_PivotSize, "")
        .value("pivot_scale", ax::NodeEditor::StyleVar_PivotScale, "")
        .value("pin_corners", ax::NodeEditor::StyleVar_PinCorners, "")
        .value("pin_radius", ax::NodeEditor::StyleVar_PinRadius, "")
        .value("pin_arrow_size", ax::NodeEditor::StyleVar_PinArrowSize, "")
        .value("pin_arrow_width", ax::NodeEditor::StyleVar_PinArrowWidth, "")
        .value("group_rounding", ax::NodeEditor::StyleVar_GroupRounding, "")
        .value("group_border_width", ax::NodeEditor::StyleVar_GroupBorderWidth, "")
        .value("highlight_connected_links", ax::NodeEditor::StyleVar_HighlightConnectedLinks, "")
        .value("snap_link_to_pin_dir", ax::NodeEditor::StyleVar_SnapLinkToPinDir, "")
        .value("count", ax::NodeEditor::StyleVar_Count, "");


    auto pyClassStyle =
        py::class_<ax::NodeEditor::Style>
            (m, "Style", "")
        .def_readwrite("node_padding", &ax::NodeEditor::Style::NodePadding, "")
        .def_readwrite("node_rounding", &ax::NodeEditor::Style::NodeRounding, "")
        .def_readwrite("node_border_width", &ax::NodeEditor::Style::NodeBorderWidth, "")
        .def_readwrite("hovered_node_border_width", &ax::NodeEditor::Style::HoveredNodeBorderWidth, "")
        .def_readwrite("selected_node_border_width", &ax::NodeEditor::Style::SelectedNodeBorderWidth, "")
        .def_readwrite("pin_rounding", &ax::NodeEditor::Style::PinRounding, "")
        .def_readwrite("pin_border_width", &ax::NodeEditor::Style::PinBorderWidth, "")
        .def_readwrite("link_strength", &ax::NodeEditor::Style::LinkStrength, "")
        .def_readwrite("source_direction", &ax::NodeEditor::Style::SourceDirection, "")
        .def_readwrite("target_direction", &ax::NodeEditor::Style::TargetDirection, "")
        .def_readwrite("scroll_duration", &ax::NodeEditor::Style::ScrollDuration, "")
        .def_readwrite("flow_marker_distance", &ax::NodeEditor::Style::FlowMarkerDistance, "")
        .def_readwrite("flow_speed", &ax::NodeEditor::Style::FlowSpeed, "")
        .def_readwrite("flow_duration", &ax::NodeEditor::Style::FlowDuration, "")
        .def_readwrite("pivot_alignment", &ax::NodeEditor::Style::PivotAlignment, "")
        .def_readwrite("pivot_size", &ax::NodeEditor::Style::PivotSize, "")
        .def_readwrite("pivot_scale", &ax::NodeEditor::Style::PivotScale, "")
        .def_readwrite("pin_corners", &ax::NodeEditor::Style::PinCorners, "")
        .def_readwrite("pin_radius", &ax::NodeEditor::Style::PinRadius, "")
        .def_readwrite("pin_arrow_size", &ax::NodeEditor::Style::PinArrowSize, "")
        .def_readwrite("pin_arrow_width", &ax::NodeEditor::Style::PinArrowWidth, "")
        .def_readwrite("group_rounding", &ax::NodeEditor::Style::GroupRounding, "")
        .def_readwrite("group_border_width", &ax::NodeEditor::Style::GroupBorderWidth, "")
        .def_readwrite("highlight_connected_links", &ax::NodeEditor::Style::HighlightConnectedLinks, "")
        .def_readwrite("snap_link_to_pin_dir", &ax::NodeEditor::Style::SnapLinkToPinDir, "when True link will start on the line defined by pin direction")
        .def(py::init<>())
        ;


    m.def("set_current_editor",
        ax::NodeEditor::SetCurrentEditor, py::arg("ctx"));

    m.def("get_current_editor",
        ax::NodeEditor::GetCurrentEditor, pybind11::return_value_policy::reference);

    m.def("create_editor",
        ax::NodeEditor::CreateEditor,
        py::arg("config") = py::none(),
        pybind11::return_value_policy::reference);

    m.def("destroy_editor",
        ax::NodeEditor::DestroyEditor, py::arg("ctx"));

    m.def("get_config",
        ax::NodeEditor::GetConfig,
        py::arg("ctx") = py::none(),
        pybind11::return_value_policy::reference);

    m.def("get_style",
        ax::NodeEditor::GetStyle, pybind11::return_value_policy::reference);

    m.def("get_style_color_name",
        ax::NodeEditor::GetStyleColorName,
        py::arg("color_index"),
        pybind11::return_value_policy::reference);

    m.def("push_style_color",
        ax::NodeEditor::PushStyleColor, py::arg("color_index"), py::arg("color"));

    m.def("pop_style_color",
        ax::NodeEditor::PopStyleColor, py::arg("count") = 1);

    m.def("push_style_var",
        py::overload_cast<ax::NodeEditor::StyleVar, float>(ax::NodeEditor::PushStyleVar), py::arg("var_index"), py::arg("value"));

    m.def("push_style_var",
        py::overload_cast<ax::NodeEditor::StyleVar, const ImVec2 &>(ax::NodeEditor::PushStyleVar), py::arg("var_index"), py::arg("value"));

    m.def("push_style_var",
        py::overload_cast<ax::NodeEditor::StyleVar, const ImVec4 &>(ax::NodeEditor::PushStyleVar), py::arg("var_index"), py::arg("value"));

    m.def("pop_style_var",
        ax::NodeEditor::PopStyleVar, py::arg("count") = 1);

    m.def("begin",
        ax::NodeEditor::Begin, py::arg("id"), py::arg("size") = ImVec2(0, 0));

    m.def("end",
        ax::NodeEditor::End);

    m.def("begin_node",
        ax::NodeEditor::BeginNode, py::arg("id"));

    m.def("begin_pin",
        ax::NodeEditor::BeginPin, py::arg("id"), py::arg("kind"));

    m.def("pin_rect",
        ax::NodeEditor::PinRect, py::arg("a"), py::arg("b"));

    m.def("pin_pivot_rect",
        ax::NodeEditor::PinPivotRect, py::arg("a"), py::arg("b"));

    m.def("pin_pivot_size",
        ax::NodeEditor::PinPivotSize, py::arg("size"));

    m.def("pin_pivot_scale",
        ax::NodeEditor::PinPivotScale, py::arg("scale"));

    m.def("pin_pivot_alignment",
        ax::NodeEditor::PinPivotAlignment, py::arg("alignment"));

    m.def("end_pin",
        ax::NodeEditor::EndPin);

    m.def("group",
        ax::NodeEditor::Group, py::arg("size"));

    m.def("end_node",
        ax::NodeEditor::EndNode);

    m.def("begin_group_hint",
        ax::NodeEditor::BeginGroupHint, py::arg("node_id"));

    m.def("get_group_min",
        ax::NodeEditor::GetGroupMin);

    m.def("get_group_max",
        ax::NodeEditor::GetGroupMax);

    m.def("get_hint_foreground_draw_list",
        ax::NodeEditor::GetHintForegroundDrawList, pybind11::return_value_policy::reference);

    m.def("get_hint_background_draw_list",
        ax::NodeEditor::GetHintBackgroundDrawList, pybind11::return_value_policy::reference);

    m.def("end_group_hint",
        ax::NodeEditor::EndGroupHint);

    m.def("get_node_background_draw_list",
        ax::NodeEditor::GetNodeBackgroundDrawList,
        py::arg("node_id"),
        "TODO: Add a way to manage node background channels",
        pybind11::return_value_policy::reference);

    m.def("link",
        ax::NodeEditor::Link, py::arg("id"), py::arg("start_pin_id"), py::arg("end_pin_id"), py::arg("color") = ImVec4(1, 1, 1, 1), py::arg("thickness") = 1.0f);

    m.def("flow",
        ax::NodeEditor::Flow, py::arg("link_id"), py::arg("direction") = ax::NodeEditor::FlowDirection::Forward);

    m.def("begin_create",
        ax::NodeEditor::BeginCreate, py::arg("color") = ImVec4(1, 1, 1, 1), py::arg("thickness") = 1.0f);

    m.def("query_new_link",
        py::overload_cast<ax::NodeEditor::PinId *, ax::NodeEditor::PinId *>(ax::NodeEditor::QueryNewLink), py::arg("start_id"), py::arg("end_id"));

    m.def("query_new_link",
        py::overload_cast<ax::NodeEditor::PinId *, ax::NodeEditor::PinId *, const ImVec4 &, float>(ax::NodeEditor::QueryNewLink), py::arg("start_id"), py::arg("end_id"), py::arg("color"), py::arg("thickness") = 1.0f);

    m.def("query_new_node",
        py::overload_cast<ax::NodeEditor::PinId *>(ax::NodeEditor::QueryNewNode), py::arg("pin_id"));

    m.def("query_new_node",
        py::overload_cast<ax::NodeEditor::PinId *, const ImVec4 &, float>(ax::NodeEditor::QueryNewNode), py::arg("pin_id"), py::arg("color"), py::arg("thickness") = 1.0f);

    m.def("accept_new_item",
        py::overload_cast<>(ax::NodeEditor::AcceptNewItem));

    m.def("accept_new_item",
        py::overload_cast<const ImVec4 &, float>(ax::NodeEditor::AcceptNewItem), py::arg("color"), py::arg("thickness") = 1.0f);

    m.def("reject_new_item",
        py::overload_cast<>(ax::NodeEditor::RejectNewItem));

    m.def("reject_new_item",
        py::overload_cast<const ImVec4 &, float>(ax::NodeEditor::RejectNewItem), py::arg("color"), py::arg("thickness") = 1.0f);

    m.def("end_create",
        ax::NodeEditor::EndCreate);

    m.def("begin_delete",
        ax::NodeEditor::BeginDelete);

    m.def("query_deleted_link",
        ax::NodeEditor::QueryDeletedLink, py::arg("link_id"), py::arg("start_id") = py::none(), py::arg("end_id") = py::none());

    m.def("query_deleted_node",
        ax::NodeEditor::QueryDeletedNode, py::arg("node_id"));

    m.def("accept_deleted_item",
        ax::NodeEditor::AcceptDeletedItem, py::arg("delete_dependencies") = true);

    m.def("reject_deleted_item",
        ax::NodeEditor::RejectDeletedItem);

    m.def("end_delete",
        ax::NodeEditor::EndDelete);

    m.def("set_node_position",
        ax::NodeEditor::SetNodePosition, py::arg("node_id"), py::arg("editor_position"));

    m.def("set_group_size",
        ax::NodeEditor::SetGroupSize, py::arg("node_id"), py::arg("size"));

    m.def("get_node_position",
        ax::NodeEditor::GetNodePosition, py::arg("node_id"));

    m.def("get_node_size",
        ax::NodeEditor::GetNodeSize, py::arg("node_id"));

    m.def("center_node_on_screen",
        ax::NodeEditor::CenterNodeOnScreen, py::arg("node_id"));

    m.def("set_node_z_position",
        ax::NodeEditor::SetNodeZPosition,
        py::arg("node_id"), py::arg("z"),
        "Sets node z position, nodes with higher value are drawn over nodes with lower value");

    m.def("get_node_z_position",
        ax::NodeEditor::GetNodeZPosition,
        py::arg("node_id"),
        "Returns node z position, defaults is 0.0");

    m.def("restore_node_state",
        ax::NodeEditor::RestoreNodeState, py::arg("node_id"));

    m.def("suspend",
        ax::NodeEditor::Suspend);

    m.def("resume",
        ax::NodeEditor::Resume);

    m.def("is_suspended",
        ax::NodeEditor::IsSuspended);

    m.def("is_active",
        ax::NodeEditor::IsActive);

    m.def("has_selection_changed",
        ax::NodeEditor::HasSelectionChanged);

    m.def("get_selected_object_count",
        ax::NodeEditor::GetSelectedObjectCount);

    m.def("get_selected_nodes",
        ax::NodeEditor::GetSelectedNodes, py::arg("nodes"), py::arg("size"));

    m.def("get_selected_links",
        ax::NodeEditor::GetSelectedLinks, py::arg("links"), py::arg("size"));

    m.def("is_node_selected",
        ax::NodeEditor::IsNodeSelected, py::arg("node_id"));

    m.def("is_link_selected",
        ax::NodeEditor::IsLinkSelected, py::arg("link_id"));

    m.def("clear_selection",
        ax::NodeEditor::ClearSelection);

    m.def("select_node",
        ax::NodeEditor::SelectNode, py::arg("node_id"), py::arg("append") = false);

    m.def("select_link",
        ax::NodeEditor::SelectLink, py::arg("link_id"), py::arg("append") = false);

    m.def("deselect_node",
        ax::NodeEditor::DeselectNode, py::arg("node_id"));

    m.def("deselect_link",
        ax::NodeEditor::DeselectLink, py::arg("link_id"));

    m.def("delete_node",
        ax::NodeEditor::DeleteNode, py::arg("node_id"));

    m.def("delete_link",
        ax::NodeEditor::DeleteLink, py::arg("link_id"));

    m.def("has_any_links",
        py::overload_cast<ax::NodeEditor::NodeId>(ax::NodeEditor::HasAnyLinks),
        py::arg("node_id"),
        "Returns True if node has any link connected");

    m.def("has_any_links",
        py::overload_cast<ax::NodeEditor::PinId>(ax::NodeEditor::HasAnyLinks),
        py::arg("pin_id"),
        "Return True if pin has any link connected");

    m.def("break_links",
        py::overload_cast<ax::NodeEditor::NodeId>(ax::NodeEditor::BreakLinks),
        py::arg("node_id"),
        "Break all links connected to this node");

    m.def("break_links",
        py::overload_cast<ax::NodeEditor::PinId>(ax::NodeEditor::BreakLinks),
        py::arg("pin_id"),
        "Break all links connected to this pin");

    m.def("navigate_to_content",
        ax::NodeEditor::NavigateToContent, py::arg("duration") = -1);

    m.def("navigate_to_selection",
        ax::NodeEditor::NavigateToSelection, py::arg("zoom_in") = false, py::arg("duration") = -1);

    m.def("show_node_context_menu",
        ax::NodeEditor::ShowNodeContextMenu, py::arg("node_id"));

    m.def("show_pin_context_menu",
        ax::NodeEditor::ShowPinContextMenu, py::arg("pin_id"));

    m.def("show_link_context_menu",
        ax::NodeEditor::ShowLinkContextMenu, py::arg("link_id"));

    m.def("show_background_context_menu",
        ax::NodeEditor::ShowBackgroundContextMenu);

    m.def("enable_shortcuts",
        ax::NodeEditor::EnableShortcuts, py::arg("enable"));

    m.def("are_shortcuts_enabled",
        ax::NodeEditor::AreShortcutsEnabled);

    m.def("begin_shortcut",
        ax::NodeEditor::BeginShortcut);

    m.def("accept_cut",
        ax::NodeEditor::AcceptCut);

    m.def("accept_copy",
        ax::NodeEditor::AcceptCopy);

    m.def("accept_paste",
        ax::NodeEditor::AcceptPaste);

    m.def("accept_duplicate",
        ax::NodeEditor::AcceptDuplicate);

    m.def("accept_create_node",
        ax::NodeEditor::AcceptCreateNode);

    m.def("get_action_context_size",
        ax::NodeEditor::GetActionContextSize);

    m.def("get_action_context_nodes",
        ax::NodeEditor::GetActionContextNodes, py::arg("nodes"), py::arg("size"));

    m.def("get_action_context_links",
        ax::NodeEditor::GetActionContextLinks, py::arg("links"), py::arg("size"));

    m.def("end_shortcut",
        ax::NodeEditor::EndShortcut);

    m.def("get_current_zoom",
        ax::NodeEditor::GetCurrentZoom);

    m.def("get_hovered_node",
        ax::NodeEditor::GetHoveredNode);

    m.def("get_hovered_pin",
        ax::NodeEditor::GetHoveredPin);

    m.def("get_hovered_link",
        ax::NodeEditor::GetHoveredLink);

    m.def("get_double_clicked_node",
        ax::NodeEditor::GetDoubleClickedNode);

    m.def("get_double_clicked_pin",
        ax::NodeEditor::GetDoubleClickedPin);

    m.def("get_double_clicked_link",
        ax::NodeEditor::GetDoubleClickedLink);

    m.def("is_background_clicked",
        ax::NodeEditor::IsBackgroundClicked);

    m.def("is_background_double_clicked",
        ax::NodeEditor::IsBackgroundDoubleClicked);

    m.def("get_background_click_button_index",
        ax::NodeEditor::GetBackgroundClickButtonIndex, "-1 if none");

    m.def("get_background_double_click_button_index",
        ax::NodeEditor::GetBackgroundDoubleClickButtonIndex, "-1 if none");

    m.def("get_link_pins",
        ax::NodeEditor::GetLinkPins,
        py::arg("link_id"), py::arg("start_pin_id"), py::arg("end_pin_id"),
        "pass None if particular pin do not interest you");

    m.def("pin_had_any_links",
        ax::NodeEditor::PinHadAnyLinks, py::arg("pin_id"));

    m.def("get_screen_size",
        ax::NodeEditor::GetScreenSize);

    m.def("screen_to_canvas",
        ax::NodeEditor::ScreenToCanvas, py::arg("pos"));

    m.def("canvas_to_screen",
        ax::NodeEditor::CanvasToScreen, py::arg("pos"));

    m.def("get_node_count",
        ax::NodeEditor::GetNodeCount, "Returns number of submitted nodes since Begin() call");

    m.def("get_ordered_node_ids",
        ax::NodeEditor::GetOrderedNodeIds,
        py::arg("nodes"), py::arg("size"),
        "Fills an array with node id's in order they're drawn; up to 'size` elements are set. Returns actual size of filled id's.");
    ////////////////////    </generated_from:imgui_node_editor.h>    ////////////////////

    // </litgen_pydef> // Autogenerated code end
    // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
}