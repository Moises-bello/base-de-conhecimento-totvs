---
content_hash: de3b1d1c9b3c2f7706f6e0cae40bcd4c67e8bc9d1a6108e3c1c91538271d635f
fetched_at: '2026-07-02T19:24:21.423989+00:00'
page_id: '267782291'
product: protheus
source: tdn-tec
title: '#xcommand'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267782291
version: 2
---

INLINE

Specify a user-defined command directive.

## Syntax

 => ]]>

## Arguments

| Name | Description |
| --- | --- |
| <matchPattern> | <matchPattern> is the pattern the input text should match. |
| <resultPattern> | <resultPattern> is the text produced if a portion of input text matches the <matchPattern>. |

The => symbol between <matchPattern> and <resultPattern> is a literal part of the syntax that must be specified in a #xcommand directive. The symbol consists of an equal sign followed by a greater than symbol with no intervening spaces. Do not confuse the symbol with the >= or the <= comparison operators.

## Description

#xcommand is a translation directive that define commands and pseudofunctions. Each directive specifies a translation rule. The rule consists of two portions: a match pattern and a result pattern. The match pattern matches a command specified in the program (.prw) file and saves portions of the command text (usually command arguments) for the result pattern to use. The result pattern then defines what will be written to the result text and how it will be written using the saved portions of the matching input text.

#xcommand and #xtranslate are similar, but differ in the circumstance under which their match patterns match input text. A #xcommand directive matches only if the input text is a complete statement, while #xtranslate matches input text that is not a complete statement. #xcommand defines a complete command and #xtranslate defines clauses and pseudofunctions that may not form a complete statement. In general, use #xcommand for most definitions and #xtranslate for special cases.

#xcommand and #xtranslate are similar to but more powerful than the #define directive.

#xcommand and #xtranslate directives have the same scope as the #define directive. The definition is valid only for the current program (.prw) file. If defined elsewhere, the definition is valid from the line where it is specified to the end of the program file.

When defining a command, there are several prerequisites to properly specifying the command definition. Many preprocessor commands require more than one #xcommand directive because mutually exclusive clauses contain a keyword or argument. For example, the @...GET command has mutually exclusive VALID and RANGE clauses and is defined with a different #xcommand rule to implement each clause.

This also occurs when a result pattern contains different expressions, functions, or parameter structures for different clauses specified for the same command (e.g., the @...SAY command). For example, there is a #xcommand rule for @...SAY specified with the PICTURE clause and another for @...SAY specified without the PICTURE clause. Each formulation of the command is translated into a different expression. Because directives are processed in stack order, when defining more than one rule for a command, place the most general case first, followed by the more specific ones. This ensures that the proper rule will match the command specified in the program (.prw) file.

### Match Pattern

The <matchPattern> portion of a translation directive is the pattern the input text must match. A match pattern is made from one or more of the following components, which the preprocessor tries to match against input text in a specific way:

* Literal values are actual characters that appear in the match pattern. These characters must appear in the input text, exactly as specified to activate the translation directive.
* Words are keywords and valid identifiers (case-insensitive, recognize keywords of more than four significant letters, etc.). The match pattern must start with a Word.
* Match markers are label and optional symbols delimited by angle brackets (<>) that provide a substitute (idMarker) to be used in the <resultPattern> and identify the clause for which it is a substitute. Marker names are identifiers and must, therefore, follow the identifier naming conventions. In short, the name must start with an alphabetic or underscore character, which may be followed by alphanumeric or underscore characters.  
  This table describes all match marker forms:

  | Match Marker | Name |
  | --- | --- |
  | <idMarker> | Regular match marker |
  | <idMarker, ...> | List match marker |
  | <idMarker:word list> | Restricted match marker |
  | <\*idMarker\*> | Wild match marker |
  | <(idMarker)> | Extended Expression match marker |

  + Regular match marker: Matches the next legal expression in the input text. The regular match marker, a simple label, is the most general and, therefore, the most likely match marker to use for a command argument. Because of its generality, it is used with the regular result marker, all of the stringify result markers, and the blockify result marker.
  + List match marker: Matches a comma-separated list of legal expressions. If no input text matches the match marker, the specified marker name contains nothing. You must take care in making list specifications because extra commas will cause unpredictable and unexpected results.
  + Restricted match marker: Matches input text to one of the words in a comma-separated list. If the input text does not match at least one of the words, the match fails and the marker name contains nothing.
  + Wild match marker: Matches any input text from the current position to the end of a statement. Wild match markers generally match input that may not be a legal expression, such as #xcommand NOTE <\*x\*>, gather the input text to the end of the statement, and write it to the result text using one of the stringify result markers.
  + Extended expression match marker: Matches a regular or extended expression, including a file name or path specification. It is used with the smart stringify result marker to ensure that extended expressions will not get stringified, while normal, unquoted string file specifications will.
* Optional match clauses are portions of the match pattern enclosed in square brackets ([ ]). They specify a portion of the match pattern that may be absent from the input text. An optional clause may contain any of the components allowed within a <matchPattern>, including other optional clauses.  
  Optional match clauses may appear anywhere and in any order in the match pattern and still match input text. Each match clause may appear only once in the input text. There are two types of optional match clauses: one is a keyword followed by match marker, and the other is a keyword by itself. These two types of optional match clauses can match all of the traditional command clauses typical of command set.   
  Optional match clauses are defined with a regular or list match marker to match input text if the clause consists of an argument or a keyword followed by an argument. If the optional match clause consists of a keyword by itself, it is matched with a restricted match marker.   
  In any match pattern, you may not specify adjacent optional match clauses consisting solely of match markers, without generating a compiler error. You may repeat an optional clause any number of times in the input text, as long as it is not adjacent to any other optional clause. To write a repeated match clause to the result text, use repeating result clauses in the <resultPattern> definition.

### Result Pattern

The <resultPattern> portion of a translation directive is the text the preprocessor will produce if a piece of input text matches the <matchPattern>. <resultPattern> is made from one or more of the following components:

* Literal tokens are actual characters that are written directly to the result text.
* Words are keywords and identifiers that are written directly to the result text.
* Result markers: refer directly to a match marker name. Input text matched by the match marker is written to the result text via the result marker.  
  This table lists the Result marker forms:

  | Regular result marker | Name |
  | --- | --- |
  | <idMarker> | Regular result marker |
  | #<idMarker> | Dumb stringify result marker |
  | <"idMarker"> | Normal stringify result marker |
  | <(idMarker)> | Smart stringify result marker |
  | <{idMarker}> | Blockify result marker |
  | <.idMarker.> | Logify result marker |

  + Regular result marker: Writes the matched input text to the result text, or nothing if no input text is matched. Use this, the most general result marker, unless you have special requirements. You can use it with any of the match markers, but it almost always is used with the regular match marker.
  + Dumb stringify result marker: Stringifies the matched input text and writes it to the result text. If no input text is matched, it writes a null string (""). If the matched input text is a list matched by a list match marker, this result marker stringifies the entire list and writes it to the result text.
  + Normal stringify result marker: Stringifies the matched input text and writes it to the result text. If no input text is matched, it writes nothing to the result text. If the matched input text is a list matched by a list match marker, this result marker stringifies each element in the list and writes it to the result text.  
    The normal stringify result marker is most often used with the blockify result marker to compile an expression while saving a text image of the expression.
  + Smart stringify result marker: Stringifies matched input text only if source text is enclosed in parentheses. If no input text matched, it writes nothing to the result text. If the matched input text is a list matched by a list match marker, this result marker stringifies each element in the list (using the same stringify rule) and writes it to the result text.
  + Blockify result marker: Writes matched input text as a code block without any arguments to the result text. For example, the input text x + 3 would be written to the result text as {|| x + 3 }. If no input text is matched, it writes nothing to the result text. If the matched input text is a list matched by a list match marker, this result marker blockifies each element in the list.
  + Logify result marker: Writes true (.T.) to the result text if any input text is matched; otherwise, it writes false (.F.) to the result text. This result marker does not write the input text itself to the result text.
* Repeating result clauses are portions of the <resultPattern> enclosed by square brackets ("[" and "]"). The text within a repeating clause is written to the result text as many times as it has input text for any or all result markers within the clause. If there is no matching input text, the repeating clause is not written to the result text. Repeating clauses, however, cannot be nested. If you need to nest repeating clauses, you probably need an additional #xcommand rule for the current command.  
  Repeating clauses are the result pattern part of the #xcommand facility that create optional clauses which have arguments. You can match input text with any match marker other than the restricted match marker and write to the result text with any of the corresponding result markers.

## Notes

* Less than operator: If you specify the less than operator (<) in the <resultPattern> expression, you must precede it with the escape character (\).
* Multistatement lines: You can specify more than one statement as a part of the result pattern by separating each statement with a semicolon. If you specify adjacent statements on two separate lines, the first statement must be followed by two semicolons.
