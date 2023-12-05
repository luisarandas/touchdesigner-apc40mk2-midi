

# luis arandas 04-12-2023
# startup script for apc40mk4-midi io

# Targeting functions, using the container path 

def concatenate_strings(string_list):
    return ', '.join(string_list)


def set_channames(op_name, string_list):
    """
    Sets the 'channames' parameter for a given CHOP select based on a list of strings.

    Args:
    op_name (str): The name of the operator.
    string_list (list): A list of strings to be concatenated and set as 'channames'.
    """
    concatenated_string = concatenate_strings(string_list)
    op_obj = op(str('/project1/akai_apc50mk2_midi/') + op_name) 
    if op_obj is not None:
        op_obj.par.channames = concatenated_string
    else:
        print(f"Operator {op_name} not found")


# Fixed codes for input channels

master_knobs = ['ch1ctrl49', 'ch1ctrl50', 'ch1ctrl51', 'ch1ctrl52', 'ch1ctrl53', 'ch1ctrl54', 'ch1ctrl55', 'ch1ctrl56']
master_sliders = ['ch1ctrl8', 'ch2ctrl8', 'ch3ctrl8', 'ch4ctrl8', 'ch5ctrl8', 'ch6ctrl8', 'ch7ctrl8', 'ch8ctrl8', 'ch1ctrl15']

master_panel_1 = ['ch1n92', 'ch1n94', 'ch1n103']
master_panel_2 = ['ch1n88', 'ch1n89', 'ch1n90', 'ch1n91', 'ch1n100', 'ch1n101', 'ch1n102']
master_panel_3 = ['ch1n95', 'ch1n96', 'ch1n97', 'ch1n98']
master_panel_4 = ['ch1n99', 'ch1n104', 'ch1ctrl16']

track_pads_1 = ['ch1n33', 'ch1n25', 'ch1n17', 'ch1n9', 'ch1n1', 'ch1n53', 'ch1n51', 'ch1n67', 'ch1n50', 'ch1n49']
track_pads_2 = ['ch1n34', 'ch1n26', 'ch1n18', 'ch1n10', 'ch1n2', 'ch2n53', 'ch2n51', 'ch2n67', 'ch2n50', 'ch2n49']
track_pads_3 = ['ch1n35', 'ch1n27', 'ch1n19', 'ch1n11', 'ch1n3', 'ch3n53', 'ch3n51', 'ch3n67', 'ch3n50', 'ch3n49']
track_pads_4 = ['ch1n36', 'ch1n28', 'ch1n20', 'ch1n12', 'ch1n4', 'ch4n53', 'ch4n51', 'ch4n67', 'ch4n50', 'ch4n49']
track_pads_5 = ['ch1n37', 'ch1n29', 'ch1n21', 'ch1n13', 'ch1n5', 'ch5n53', 'ch5n51', 'ch5n67', 'ch5n50', 'ch5n49']
track_pads_6 = ['ch1n38', 'ch1n30', 'ch1n22', 'ch1n14', 'ch1n6', 'ch6n53', 'ch6n51', 'ch6n67', 'ch6n50', 'ch6n49']
track_pads_7 = ['ch1n39', 'ch1n31', 'ch1n23', 'ch1n15', 'ch1n7', 'ch7n53', 'ch7n51', 'ch7n67', 'ch7n50', 'ch7n49']
track_pads_8 = ['ch1n40', 'ch1n32', 'ch1n24', 'ch1n16', 'ch1n8', 'ch8n53', 'ch8n51', 'ch8n67', 'ch8n50', 'ch8n49']
track_pads_9 = ['ch1n83', 'ch1n84', 'ch1n85', 'ch1n86', 'ch1n87', 'ch1n82']

selector_ops = {
	"master_knobs": master_knobs, 
	"master_sliders": master_sliders, 
	"master_panel_1": master_panel_1,
	"master_panel_2": master_panel_2,
	"master_panel_3": master_panel_3,
	"master_panel_4": master_panel_4,
	"track_pads_1": track_pads_1,
	"track_pads_2": track_pads_2,
	"track_pads_3": track_pads_3,
	"track_pads_4": track_pads_4,
	"track_pads_5": track_pads_5,
	"track_pads_6": track_pads_6,
	"track_pads_7": track_pads_7,
	"track_pads_8": track_pads_8,
	"track_pads_9": track_pads_9
}


def onStart():
    print("Starting!")
    
    for op_name in selector_ops:
        if op_name in selector_ops:
            set_channames(op_name, selector_ops[op_name])
        else:
            print(f"Mapping for {op_name} operator not found.")
    
    return

def onCreate():
	return

def onExit():
	return

def onFrameStart(frame):
	return

def onFrameEnd(frame):
	return

def onPlayStateChange(state):
	return

def onDeviceChange():
	return

def onProjectPreSave():
	return

def onProjectPostSave():
	return

	