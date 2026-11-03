---
content_hash: 525d05ecc33ddce8959ba559201a7889f2ef7d672834ff37567ba6aa6a2d583b
fetched_at: '2026-07-02T19:24:21.379279+00:00'
page_id: '266982892'
product: protheus
source: tdn-tec
title: '#define'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266982892
version: 2
---

INLINE

Define a manifest constant or pseudofunction.

## Syntax

 []]]>([]) []]]>

## Arguments

| Name | Description |
| --- | --- |
| <idConstant> | <idConstant> is the name of an identifier to define. |
| <resultText> | <resultText> is the optional replacement text to substitute whenever a valid <idConstant> is encountered. |

| Name | Description |
| --- | --- |
| <idFunction> | <idFunction> is a pseudofunction definition with an optional argument list (<arg list>). If you include <arg list>, it is delimited by parentheses ("(" and ")") immediately following <idFunction>. |
| <exp> | <exp> is the replacement expression to substitute when the pseudofunction is encountered.  Enclose this expression in parentheses to guarantee precedence of evaluation when the pseudofunction is expanded. |

## Description

The #define directive defines an identifier and, optionally, associates a text replacement string. If specified, replacement text operates much like the search and replace operation of a text editor. As each source line from a program file is processed by the preprocessor, the line is scanned for identifiers. If a currently defined identifier is encountered, the replacement text is substituted in its place.

Defined identifiers can contain any combination of alphabetic and numeric characters, including underscores. Defined identifiers, however, differ from other identifiers by being case-sensitive. As a convention, defined identifiers are specified in uppercase to distinguish them from other identifiers used within a program.

When specified, each definition must occur on a line by itself. Unlike statements, more than one directive cannot be specified on the same source line. You may continue a definition on a subsequent line by employing a semicolon (;). Each #define directive is specified followed by one or more white space characters (spaces or tabs), a unique identifier, and optional replacement text. Definitions can be nested, allowing one identifier to define another.

A defined identifier has lexical scope like a filewide static variable. It is only valid in the program (.prw) file in which it is defined. Unlike a filewide static variable, a defined identifier is visible from the point where it is defined in the program file until the end of the program file is reached.

#define directives have three basic purposes:

* To define a control identifier for #ifdef and #ifndef

* To define a manifest constant - An identifier defined to represent a constant value

* To define a compiler pseudofunction

### Preprocessor Identifiers

The most basic #define directive defines an identifier with no replacement text. You can use this type of identifier when you need to test for the existence of an identifier with either the #ifdef or #ifndef directives. This is useful to either exclude or include code for conditional compilation.

### Manifest Constants

The second form of the #define directive assigns a name to a constant value. This form of identifier is referred to as a manifest constant. For example, you can define a manifest constant for the inkey() code associated with a key press:

endif]]>

Whenever the preprocessor encounters a manifest constant while scanning a source line, it replaces it with the specified replacement text.

Although you can accomplish this by defining a variable, there are several advantages to using a manifest constant: the compiler generates faster and more compact code for constants than for variables; and variables have memory overhead where manifest constants have no runtime overhead, thus saving memory and increasing execution speed. Furthermore, using a variable to represent a constant value is conceptually inconsistent. A variable by nature changes and a constant does not.

Use a manifest constant instead of a constant for several reasons. First, it increases readability. In the example above, the manifest constant indicates more clearly the key being represented than does the inKey() code itself. Second, manifest constants localize the definition of constant values, thereby making changes easier to make, and increasing reliability. Third, and a side effect of the second reason, is that manifest constants isolate implementation or environment specifics when they are represented by constant values.

To further isolate the effects of change, manifest constants and other identifiers can be grouped together into header files allowing you to share identifiers between program (.prw) files, applications, and groups of programmers. Using this methodology, definitions can be standardized for use throughout a development organization. Merge header files into the current program file by using the #include directive.

### Compiler Pseudo-functions

In addition to defining constants as values, the #define directive can also define pseudofunctions that are resolved at compile time. A pseudofunction definition is an identifier immediately followed by an argument list, delimited by parentheses, and the replacement expression.

For example:

 y, x, y))]]>

Pseudofunctions differ from manifest constants by supporting arguments. Whenever the preprocessor scans a source line and encounters a function call that matches the pseudofunction definition, it substitutes the function call with the replacement expression. The arguments of the function call are transported into the replacement expression by the names specified in the argument list of the identifier definition. When the replacement expression is substituted for the pseudofunction, names in the replacement expression are replaced with argument text. For example, the following invocations,

are replaced by:

 9, 10, 9))]]>
