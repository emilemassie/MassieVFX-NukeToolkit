def main():
    """ 
        This Tool takes a corner pin as an input and then references all the knobs to the desired frame.
        This is very usefull when getting corner pins from mocha and/or wanting to change reference frame after the fact.
    """
    import nuke
    try :
        node = nuke.selectedNode()
        if node.Class() == "CornerPin2D":
            ref_frame = nuke.frame()
            k = nuke.Int_Knob("rframe", '<b>FRAME : ')
            tab = nuke.Tab_Knob('reference_tab', 'REFERENCE FRAME')
            
            try:
                node['from1'].setExpression('to1(rframe)')
                node['from2'].setExpression('to2(rframe)')
                node['from3'].setExpression('to3(rframe)')
                node['from4'].setExpression('to4(rframe)')
                node['rframe'].setValue(ref_frame)
                node['label'].setValue('[value rframe]')
            except:
                node.addKnob(tab)
                node.addKnob(k)

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

