DefaultKeyBindings.dict file (`~/Library/KeyBindings/DefaultKeyBindings.dict`) for Mac OS X, created by [Brett Terpstra][] and based heavily on work done by [Lri][lrikeys].
Please note that these bindings won't work in all applications: TextWrangler and TextMate, for example, override these with their own settings.
See Lri's [gists][lrigists] and [website][lriweb] for more coding madness.

[lrikeys]: http://www.cs.helsinki.fi/u/lranta/keybindings/
[lriweb]: http://www.cs.helsinki.fi/u/lranta/
[lrigists]: https://gist.github.com/Lri
[brett terpstra]: http://brettterpstra.com

<b>Installation</b>: Copy the DefaultKeyBindings.dict file to the `~/Library/KeyBindings/` directory (create `KeyBindings` if it doesn't already exist). 
Any open applications will need to be re-started before the key bindings will take effect -- or log out and log back in.

<b>Documentation</b> <i>(last updated 01/02/2014.)</i>

*Grouped items begin with the groups shortcut (if exists), followed by a subgroup (if exists) followed by the keys specified.*

<table>
<caption id="generalcommands"> General Commands </caption>
<colgroup>
<col style="text-align:center;"/>
<col style="text-align:left;"/>
</colgroup>

<thead>
<tr>
	<th style="text-align:center;" colspan="2">General Commands</th>
</tr>
<tr>
	<th style="text-align:center;">Key</th>
	<th style="text-align:left;">Function</th>
</tr>
</thead>

<tbody>
<tr>
	<td style="text-align:center;">^y</td>
	<td style="text-align:left;">replace yank: command with yankAndSelect for use with the kill ring ( defaults write -g NSTextKillRingSize -string 6)</td>
</tr>
<tr>
	<td style="text-align:center;">⌥f</td>
	<td style="text-align:left;">Move forward word</td>
</tr>
<tr>
	<td style="text-align:center;">⌥b</td>
	<td style="text-align:left;">Move backword word</td>
</tr>
<tr>
	<td style="text-align:center;">⌥v</td>
	<td style="text-align:left;">Page Up</td>
</tr>
<tr>
	<td style="text-align:center;">^v</td>
	<td style="text-align:left;">Page Down</td>
</tr>
<tr>
	<td style="text-align:center;">^/</td>
	<td style="text-align:left;">Undo</td>
</tr>
<tr>
	<td style="text-align:center;">^<em>|Undo |
|^w|delete word before cursor |
|⌥\⇧u007⇧f|delete word before cursor |
|⌥d|delete word before cursor |
|⌥w|select word |
|⌥⇧w|select word backward and modify selection |
|⌥⇧s|select entire line/paragraph |
|⌥s|select from beginning of paragrah to last character |
|^⌥⇧s|select paragraph excluding leading/trailing whitespace (same as ^$@\UF701) |
|^u|delete line/paragraph |
|⌥y|copy paragraph |
|⌥x|cut paragraph |
|⌥p|paste paragraph below |
|⌥⇧p|paste paragraph above |
|^⇧a|select to beginning of paragraph and copy |
|^⇧e|select to end of paragraph and copy |
|⌥q|cut to beginning of paragraph |
|⌥k|cut to end of paragraph |
|⌥o|blank line after current |
|⌥⇧o|blank line before current |
|^⌘k|move line up |
|^⌘j|move line down |
|^⌘l|indent line |
|^⌘h|outdent line (one tab or char) |
|^⌘↑|move line up ( same commands but with arrow keys)|
|^⌘↓|move line down |
|^⌘→|indent line |
|^⌘←|outdent line (one tab or char) |
|^⇧⌘←|Full outdent - Deletes all leading space of line/paragraph (updated) ( Control-shift-command-left arrow)|
|^⇧⌘→|Delete trailing space |
|^⌘⇧↑|Delete leading and trailing whitespace for paragraph |
|^⌘⇧↓|Select paragraph without leading or trailing whitespace |
|^⌥⇧↑|modify selection up by paragraph (Control Option Shift Up) |
|^⌥⇧↓|modify selection down by paragraph (Control Option Shift Down) |
|^⌥⇧←|modify selection left by word |
|^⌥⇧→|modify selection right by word |
|⌘⌥<sup>←</sup>|Move to first Alphanumeric character of line (new) |
|⌘⌥←|Move to first non-whitespace character of line (new) |
|⌘⌥⇧←|Select to first character of line with leading space (new) |
|⌥⌘→|Move to last non-whitespace character of paragraph (new) |
|^⌥→|Move to end of paragraph and delete trailing whitespace (new) |
|⌘↩|TextMate Command-Return (Command Enter) |
|⌘⇧↩|Insert blank line above paragraph (Command Shift Enter) |
|⌘⌥</em></td>
	<td style="text-align:left;">hyphenate next space and move to next word ( this will kill non alphanumeric symbols and punctuation, use only on <em>words</em>)</td>
</tr>
<tr>
	<td style="text-align:center;">⌥1</td>
	<td style="text-align:left;">bookmark</td>
</tr>
<tr>
	<td style="text-align:center;">⌥2</td>
	<td style="text-align:left;">jump to bookmark</td>
</tr>
<tr>
	<td style="text-align:center;">⌥⌘↩</td>
	<td style="text-align:left;">Continue a list item with indentation and include the same delimiter ( Command Option Enter)</td>
</tr>
<tr>
	<td style="text-align:center;">⇧⇥</td>
	<td style="text-align:left;">remove one tab (or character) from start of line (outdent) ( Shift Tab)</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="text-align:center;"/>
<col style="text-align:center;"/>
<col style="text-align:center;"/>
<col style="text-align:left;"/>
</colgroup>

<thead>
<tr>
	<th style="text-align:center;" colspan="4">EMACS style C-x shortcuts (^x)</th>
</tr>
</thead>

<tbody>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">u</td>
	<td style="text-align:left;">Undo</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">k</td>
	<td style="text-align:left;">Close window</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">^f</td>
	<td style="text-align:left;">Open ( find file )</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">^x</td>
	<td style="text-align:left;">Swap with mark</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">^m</td>
	<td style="text-align:left;">Select to mark</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">^s</td>
	<td style="text-align:left;">Save</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">^w</td>
	<td style="text-align:left;">Save as</td>
</tr>
<tr>
	<td style="text-align:center;" colspan="3">Commenting commands (^⌘c)</td>
	<td style="text-align:center;"></td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘c</td>
	<td style="text-align:center;">/</td>
	<td style="text-align:left;">comment with &#8220;//&#8221;</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘c</td>
	<td style="text-align:center;">\</td>
	<td style="text-align:left;">comment with &#8220;#&#8221;</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘c</td>
	<td style="text-align:center;">!</td>
	<td style="text-align:left;">HTML commenting</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘c</td>
	<td style="text-align:center;">*</td>
	<td style="text-align:left;">Css Commenting</td>
</tr>
<tr>
	<td style="text-align:center;" colspan="4"></td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">⌘⌥b</td>
	<td style="text-align:left;">bold selection (Markdown)</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">⌘⌥i</td>
	<td style="text-align:left;">italicize selection (Markdown)</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">⌘⌥=</td>
	<td style="text-align:left;">increase markdown header level</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">⌘⌥-</td>
	<td style="text-align:left;">decrease markdown header level</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">⌘⌥&gt;</td>
	<td style="text-align:left;">increase blockquote header level</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">⌘⌥&lt;</td>
	<td style="text-align:left;">decrease blockquote level</td>
</tr>
<tr>
	<td style="text-align:center;" colspan="3">Multi-stroke Markdown commands (^⌘w)</td>
	<td style="text-align:center;"></td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">␍</td>
	<td style="text-align:left;">force carriage return in text field</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">⇥</td>
	<td style="text-align:left;">force tab in text field</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">\</td>
	<td style="text-align:left;">insert reference link <code>[selection][[cursor]]</code></td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">\</td>
	<td style="text-align:left;">insert reference <code>[selection]: [cursor]</code></td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">+</td>
	<td style="text-align:left;">Unordered list item with</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">-</td>
	<td style="text-align:left;">Unordered list item with -</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">*</td>
	<td style="text-align:left;">Unordered list item with *</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">8</td>
	<td style="text-align:left;">convert current numbered list item to bullet, handles indentation</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">1</td>
	<td style="text-align:left;">convert current bullet list item to numbered</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">h,1</td>
	<td style="text-align:left;">#</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">h,2</td>
	<td style="text-align:left;">##</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">h,3</td>
	<td style="text-align:left;">###</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">h,4</td>
	<td style="text-align:left;">####</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">h,5</td>
	<td style="text-align:left;">#####</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">h,6</td>
	<td style="text-align:left;">######</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">l,t</td>
	<td style="text-align:left;">create a link for selected text, cursor between () <code>[selected text]([cursor])</code> ( links without selected text first, these can produce a mess using multiple clipboards make a text selection before you run them)</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">l,c</td>
	<td style="text-align:left;">create a link for selected text, inserting clipboard as url <code>[[cursor]selected text](clipboard contents)</code></td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">i,t</td>
	<td style="text-align:left;">same as lt, but with image syntax <code>![selected text]([cursor])</code></td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">i,c</td>
	<td style="text-align:left;">same as lc, but with image syntax <code>![selected text](clipboard)</code></td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">:,t</td>
	<td style="text-align:left;">create a reference from selected text</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘w</td>
	<td style="text-align:center;">:,c</td>
	<td style="text-align:left;">create a reference from selected text, clipboard as url</td>
</tr>
<tr>
	<td style="text-align:center;" colspan="4"></td>
</tr>
<tr>
	<td style="text-align:center;" colspan="3">HTML commands (^⌘e)</td>
	<td style="text-align:center;"></td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘e</td>
	<td style="text-align:center;">:,=</td>
	<td style="text-align:left;">=&#8220;[cursor]&#8221;</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘e</td>
	<td style="text-align:center;">:,e</td>
	<td style="text-align:left;">entity &amp;[cursor];</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘e</td>
	<td style="text-align:center;">:,/</td>
	<td style="text-align:left;">http://</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘e</td>
	<td style="text-align:center;">:,t</td>
	<td style="text-align:left;">Make previous word into paired HTML tag</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘e</td>
	<td style="text-align:center;">a,t</td>
	<td style="text-align:left;">Insert HTML link for selected text, leave cursor in the href with &#8220;http://&#8221; selected</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘e</td>
	<td style="text-align:center;">a,c</td>
	<td style="text-align:left;">Insert HTML link with clipboard as href</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘e</td>
	<td style="text-align:center;">i,t</td>
	<td style="text-align:left;">Insert image tag, any selected text is alt text, leave cursor in src attribute</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘e</td>
	<td style="text-align:center;">i,c</td>
	<td style="text-align:left;">Insert image tag, clipboard as src, any selected text as alt, leave cursor at beginning of alt attribute</td>
</tr>
<tr>
	<td style="text-align:center;" colspan="4"></td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">i,^&lt;</td>
	<td style="text-align:left;">Make selected text into paired HTML tag. Allows attributes, only dupes first word into closing tag (caveat: overwrites your pasteboard)</td>
</tr>
<tr>
	<td style="text-align:center;" colspan="3">Surround commands (^⌘s)</td>
	<td style="text-align:center;"></td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘s</td>
	<td style="text-align:center;">i,(</td>
	<td style="text-align:left;">wrap () with spaces</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘s</td>
	<td style="text-align:center;">i,)</td>
	<td style="text-align:left;">wrap () no spaces</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘s</td>
	<td style="text-align:center;">i,\</td>
	<td style="text-align:left;">wrap [] with spaces</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘s</td>
	<td style="text-align:center;">i,\</td>
	<td style="text-align:left;">wrap [] no spaces</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘s</td>
	<td style="text-align:center;">i,{</td>
	<td style="text-align:left;">wrap {} with spaces</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘s</td>
	<td style="text-align:center;">i,}</td>
	<td style="text-align:left;">wrap {} no spaces</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘s</td>
	<td style="text-align:center;">i,&lt;</td>
	<td style="text-align:left;">wrap &lt;&gt; with spaces</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘s</td>
	<td style="text-align:center;">i,&gt;</td>
	<td style="text-align:left;">wrap &lt;&gt; no spaces</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘s</td>
	<td style="text-align:center;">i,&#8217;</td>
	<td style="text-align:left;">wrap single quotes</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;">^⌘s</td>
	<td style="text-align:center;">i,`</td>
	<td style="text-align:left;">wrap backticks</td>
</tr>
<tr>
	<td style="text-align:center;" colspan="4"></td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">i,⌥r</td>
	<td style="text-align:left;">repeat character before cursor</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">i,⌘⇧⌦</td>
	<td style="text-align:left;">Forward delete to end of paragraph</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">i,⌘⇧⌫</td>
	<td style="text-align:left;">Delete to beginning of paragraph</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">i,⌘⌥7</td>
	<td style="text-align:left;">Right mouse click (useless, doesn&#8217;t maintain cursor position)</td>
</tr>
<tr>
	<td style="text-align:center;">^x</td>
	<td style="text-align:center;"></td>
	<td style="text-align:center;">i,⌘⌥⇧s</td>
	<td style="text-align:left;">Real, honest-to-goodnes Save As&#8230;</td>
</tr>
</tbody>
</table>


This documentation is generated automatically from the comments and commands in the DefaultKeyBinding.dict file. The script `document_keybindings.rb` is free for use, but it's specifically designed for use with my formatting in the bindings plist (i.e. it's a little finicky).

