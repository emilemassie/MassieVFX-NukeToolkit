# -*- coding: utf-8 -*-

def main():
    '''
        This takes takes the selected node (checks of it's a corner pin) and add functionnalities to it.
        Mainly reference frame, auto set to bbox and more.
    
    '''
    import nuke
    try :
        node = nuke.selectedNode()
        if node.Class() == "CornerPin2D":
            ref_frame = nuke.frame()

            try:
                node['advanced_tab'].name()
            
            except:

                autopinScript = """

node=nuke.thisNode()

node['selected'].setValue(True)
node['disable'].setValue(True)

autocropper = nuke.createNode("CurveTool",'''operation 0 ROI {0 0 input.width input.height} Layer alpha label "Processing Crop..." selected true''', False)

# Execute the CurveTool node for the frame.
nuke.executeMultiple([autocropper,], ([nuke.frame(), nuke.frame(), 1],))

# Get the data
autocropbox = autocropper.knob("autocropdata").getValue()

# Leave no traces
nuke.delete(autocropper)

# Copy The data into the CornerPin

node['from1'].setValue([autocropbox[0],autocropbox[1]], nuke.frame())
node['from2'].setValue([autocropbox[2],autocropbox[1]], nuke.frame())
node['from3'].setValue([autocropbox[2],autocropbox[3]], nuke.frame())
node['from4'].setValue([autocropbox[0],autocropbox[3]], nuke.frame())

node['to1'].setValue([autocropbox[0],autocropbox[1]], nuke.frame())
node['to2'].setValue([autocropbox[2],autocropbox[1]], nuke.frame())
node['to3'].setValue([autocropbox[2],autocropbox[3]], nuke.frame())
node['to4'].setValue([autocropbox[0],autocropbox[3]], nuke.frame())

node['selected'].setValue(True)
node['disable'].setValue(False)
"""



                initKeysScript = '''

node=nuke.thisNode()

# Set Keys on the initial frame

for knob in [node['from1'],node['from2'],node['from3'],node['from4'],node['to1'],node['to2'],node['to3'],node['to4']]:
    knob.setKeyAt(nuke.frame())


'''


                node.addKnob(nuke.Tab_Knob('advanced_tab', 'Advanced Settings'))
                node.addKnob(nuke.Int_Knob('rframe', 'Reference frame : '))
                node.addKnob(nuke.PyScript_Knob('setFrameButton', 'set to current frame', '''nuke.thisNode()['rframe'].setValue(nuke.frame())'''))
                node.addKnob(nuke.Text_Knob('',''))

                node.addKnob(nuke.nuke.PyScript_Knob('autopin', 'ðŸ“Œ AutoPin', autopinScript))
                node.addKnob(nuke.nuke.PyScript_Knob('autopin', 'ðŸ”‘ Set Initial Keys', initKeysScript))
                
            node['from1'].setExpression('to1(rframe)')
            node['from2'].setExpression('to2(rframe)')
            node['from3'].setExpression('to3(rframe)')
            node['from4'].setExpression('to4(rframe)')
            node['rframe'].setValue(ref_frame)
            node['label'].setValue('[value rframe]')

        else:
            nuke.message('The selected node is not a CornerPin2D')
    except:
        nuke.message('Please select a CornerPin2D')

