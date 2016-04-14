#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime, re

def translate_command(line):
    line = line.replace('~','⌥').replace('@','⌘').replace('$','⇧').replace('^','⌃').replace('\UF700','↑').replace('\UF701','↓').replace('\UF703','→').replace('\UF702','←').replace('\U0009','⇥').replace('\U000D','↩').replace('\U001B','⎋').replace('\U000A','␍').replace('\UF728','⌦').replace('\U007F','⌫')
#    line = line.replace('~',u'\u2325').replace('@',u'\u2318').replace('$',u'\u21E7').replace('^',u'\u2303').replace('\UF700',u'\u2191').replace('\UF701',u'\u2193').replace('\UF703',u'\u2192').replace('\UF702', u'\u2190').replace('\U0009',u'\u21E5').replace('\U000D',u'\u21A9').replace('\U001B',u'\u238B').replace('\U000A',u'\u2305').replace('\UF728',u'\u2326').replace('\U007F',u'\u232B')
    # Translate "A" into "⇧a"
    UPPER = re.compile("[A-Z]")
    if UPPER.search(line):
        S = UPPER.search(line).group()
        line = line.replace(S, "⇧" + S.lower())
        # Translate '_' into '⇧-'
        line = line.replace('_','⇧-')
    return line

def comment_filter(text):
    """Regex from http://ostermiller.org/findcomment.html"""
    # TODO: It looks sucks
    pattern = r'''^\s*(?P<code>(?!(?:\s*(?:(?:\/\*(?:[^*]|(?:\*+[^*\/]))*\*+\/)|(?:\/\/.*)))\n).*[\{\};])\n?|(?P<comment>(?:(?:\/\*(?:[^*]|(?:\*+[^*\/]))*\*+\/)|(?:\/\/.*)))\n'''
    regex = re.compile(pattern, re.VERBOSE|re.MULTILINE)
    return [[m.group('comment'), m.group('code')] for m in regex.finditer(text) if m.groups()]

def mdrender(text):
    import subprocess, json
    """Render markdown text using Github's API"""
    PAYLOAD = json.dumps({'text': text, 'mode': 'gfm'})
    return subprocess.check_output(["curl", "--silent", "-d {}".format(F), "https://api.github.com/markdown"])

def transfer(lines):
    """ Transfer lines in list into markdown string """
    note_regex = re.compile(r'''^\s*\/\/\s*>\s*(.*)\n?''')
    level_down_regex = re.compile(r'''^\s*\};\s*\n?''')
    LEVEL = 0
    OUTPUT = ""
    SUBGROUP_COMMAND = ""
    SUBGROUP_DESC = ""
    GROUP_COMMAND = ""
    GROUP_DESC = ""
    NOTE = ""
    PREFIX = ""
    TOPLEVEL = []
    cnt = 0 
    for line in lines:
        print line
        COMMENT = line[0]
        CODE = line[1]
        if COMMENT:
            # if it is a todo list, omit.
            if re.findall(r'''^\s*//(TODO)''', COMMENT):
                continue
            # if it likes "// > foo ", treat it as a note.
            # TODO: It looks suck.
            elif re.findall(r'''^\s*//\s*>(.*)$''', COMMENT):
                NOTE += " " + re.findall(r'''^\s*//\s*>(.*)$''', COMMENT)[0]
            elif re.findall(r'''^\s*//\s*(.*)$''', COMMENT):
                DESC = re.findall(r'''^\s*//\s*(.*)$''', COMMENT)[0]
        if CODE:
            # if it is end of a block
            if re.findall(r'''^\s*};\s*$''', CODE):
                # level up
                LEVEL -= 1
                if LEVEL == 1:
                    SUBGROUP_COMMAND = ""
                    SUBGROUP_DESC = ""
                    OUTPUT += "|||||\n"
                # if it is the root group ( level == 0 )
                elif LEVEL == 0:
                    OUTPUT += "[ {GROUP_DESC} ]\n\n".format(GROUP_DESC=GROUP_DESC)
                    GROUP_COMMAND = ""
                    GROUP_DESC = ""
                continue
            elif re.findall(r'''^\s*"([^"]+)"\s*=\s*{.*?//\s*(.*)''', CODE):
                MATCH = re.findall(r'''^\s*"([^"]+)"\s*=\s*{.*?//\s*(.*)''', CODE)
                LEVEL += 1
                if LEVEL == 1:
                    GROUP_COMMAND = translate_command(MATCH[0])
                    GROUP_DESC = MATCH[1]
                    OUTPUT += "\n| {GROUP_DESC} ( {GROUP_COMMAND})||||\n|:----:|:----:|:----:|:----|\n".format(GROUP_DESC=GROUP_DESC, GROUP_COMMAND=GROUP_COMMAND)
                elif LEVEL == 2:
                    SUBGROUP_COMMAND = translate_command(MATCH[0])
                    SUBGROUP_DESC = MATCH[1]
                    OUTPUT += "\n| {SUBGROUP_DESC} ( {SUBGROUP_COMMAND})||| |\n".format(SUBGROUP_DESC=SUBGROUP_DESC, SUBGROUP_COMMAND=SUBGROUP_COMMAND)
                else:
                    PREFIX == MATCH[0]
                MATCH = ''
                continue
            elif re.findall(r'''^\s*"([^"]+)"\s*=\s*\(''', CODE):
                MATCH = re.findall(r'''^\s*"([^"]+)"\s*=\s*\(''', CODE)
                COMMAND = translate_command(MATCH[0])
                if NOTE:
                    NOTE = "( {NOTE} )".format(NOTE=NOTE)
                if LEVEL == 0:
                    TOPLEVEL.append("|{COMMAND}|{DESC} {NOTE}|\n".format(COMMAND=COMMAND,DESC=DESC,NOTE=NOTE))
                    COMMAND = ""
                    DESC = ""
                    NOTE = ""
                else:
                    if PREFIX:
                        COMMAND = PREFIX + "," + COMMAND
                    OUTPUT += "|{GROUP_COMMAND} |{SUBGROUP_COMMAND} |{COMMAND} |{DESC} {NOTE}|\n".format(GROUP_COMMAND=GROUP_COMMAND, SUBGROUP_COMMAND=SUBGROUP_COMMAND, COMMAND=COMMAND, DESC=DESC, NOTE=NOTE)
                NOTE = ''
                MATCH = ''
        TOPOUTPUT = "|General Commands||\n|Key|Function|\n|:----:|:----|\n"

    for LINE in TOPLEVEL:
        TOPOUTPUT += LINE
    TOPOUTPUT += "[ General Commands ]\n\n"

    OUTPUT = TOPOUTPUT + OUTPUT
    return(OUTPUT)

if __name__ == "__main__":
    INFILE = open('DefaultKeyBinding.dict', 'r')
    INPUT = INFILE.read()
    INFILE.close()

    UPDATE_TIME = datetime.datetime.now().strftime('%Y-%m-%d')

    STYLE = """<style>
    table { margin-bottom:20px; border:none; width: 100%; }

    caption { text-align:left; padding:5px; font-weight:bold; border: dotted 1px #777;background:#eee; margin-bottom:10px }
    td,th { font-weight:bold; padding:3px; border: solid 1px #ccc; padding:4px }
    td:nth-child(1),td:nth-child(2),td:nth-child(3) { width:40px}
    td:first-child {font-weight:bold !important}
    td:last-child { font-weight:normal;width:auto }
    """

    INTRO = """DefaultKeyBindings.dict file (`~/Library/KeyBindings/DefaultKeyBindings.dict`) for Mac OS X, created by [Brett Terpstra][brett terpstra] and based heavily on work done by [Lri][lrikeys].
    Please note that these bindings won't work in all applications: TextWrangler and TextMate, for example, override these with their own settings.
    See Lri's [gists][lrigists] and [website][lriweb] for more coding madness.

    [lrikeys]: http://www.cs.helsinki.fi/u/lranta/keybindings/
    [lriweb]: http://www.cs.helsinki.fi/u/lranta/
    [lrigists]: https://gist.github.com/Lri
    [brett terpstra]: http://brettterpstra.com

    ## Installation
    ### Using the install.sh script

    Open Terminal.app or something else like this ( such as iTerm2.app or so ).

    Run the command below:

    > curl https://raw.githubusercontent.com/zer4tul/KeyBindings/master/install.sh -L -o - | bash

    ### Manually

    Copy the DefaultKeyBindings.dict file to the `~/Library/KeyBindings/` directory (create `KeyBindings` if it doesn't already exist).
    Any open applications will need to be re-started before the key bindings will take effect -- or log out and log back in.

    ## Documentation *(last updated {UPDATE_TIME}.)*

    Grouped items begin with the groups shortcut (if exists), followed by a subgroup (if exists) followed by the keys specified.
    """.format(UPDATE_TIME=UPDATE_TIME)

    OUTRO ="""This documentation is generated automatically from the comments and commands in the DefaultKeyBinding.dict file. The script `document_keybindings.rb` is free for use, but it's specifically designed for use with my formatting in the bindings plist (i.e. it's a little finicky).
    """

    INPUT = comment_filter(INPUT)
    transfer(INPUT)
