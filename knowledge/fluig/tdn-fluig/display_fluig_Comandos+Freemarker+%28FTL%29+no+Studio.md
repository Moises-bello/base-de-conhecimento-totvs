---
content_hash: c5b490de548f282ce6d71d150a75f821ef14ba700e0ce6774b996789279539c2
fetched_at: '2026-06-28T21:35:18.904316+00:00'
page_id: '185748598'
product: fluig
source: tdn-fluig
title: Comandos Freemarker (FTL) no Studio
type: documentation
url: https://tdn.totvs.com/display/fluig/Comandos+Freemarker+%28FTL%29+no+Studio
version: 18
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é apresentar alguns comandos do Freemarker que podem ser utilizados no fluig Studio.

# Comandos

A seguir são apresentados os comandos e sua utilização:

| Comando | Descrição |
| --- | --- |
| @wcm.header | Macro especial do fluig, insere o cabeçalho no *layout*. Veja mais em [Biblioteca WCM](http://tdn.totvs.com/display/fluig/Biblioteca+WCM). |
| @wcm.menu | Macro especial do fluig, insere o menu no *layout*. Veja mais em . |
| @wcm.renderSlot | Macro especial do fluig, insere um *slot* no *layout*. Veja mais em . |
| @wcm.footer | Macro especial do fluig, insere o rodapé no layout. Veja mais em . |
| assign | Cria uma variável, ou substitui uma variável existente, veja mais em *[Assign](http://freemarker.org/docs/ref_directive_assign.html#ref.directive.assign)*. |
| attemptattempt | Faz com que a página renderize, mesmo que uma parte da renderização falhe. Veja mais em *[Attempt](http://freemarker.org/docs/ref_directive_attempt.html#ref.directive.attempt)*. |
| break | Veja  ou . |
| case | Veja . |
| compress | Remove espaços em branco desnecessários. Veja mais em *[Compress](http://freemarker.org/docs/ref_directive_compress.html#ref.directive.compress)*. |
| default | Veja . |
| else / elseif | Veja . |
| functionfunction | Cria um método. Se o método não contém um retorno, então é retornada uma variável *undefined*. Veja mais em *[Function](http://freemarker.org/docs/ref_directive_function.html#ref.directive.function)*. |
| flush | Quando o Freemarker gera o *output*, geralmente ele guarda esse *output* gerado e envia para o *client* em um ou mais pedaços. Esse ato se chama fazer o *flush*. Normalmente ele ocorre automaticamente. Veja mais em *[Flush](http://freemarker.org/docs/ref_directive_flush.html#ref.directive.flush)*. |
| global  ifif | Você pode utilizar as diretivas *if*, *elseif* e *else* para condicionalmente pular uma seção do template. As condições devem traduzir para um valor *booleano*, caso contrário, um erro irá interromper o processamento do *template*. Os *elseif* e *else* devem ocorrer dentro de um *if* (ou seja, entre as tags de inicio e fim do *If*). O *if* pode conter qualquer numero de *elseif* (incluindo 0) e, no final, opcionalmente, um *else*. Veja mais em [If](http://freemarker.org/docs/ref_directive_if.html#ref.directive.if). |
| import | Importa uma biblioteca. Veja mais em *[Import](http://freemarker.org/docs/ref_directive_import.html#ref.directive.import)* e . |
| include | Inclui outro *template* Freemarker dentro do seu *template*. Veja mais em *[Include](http://freemarker.org/docs/ref_directive_include.html#ref.directive.include)*. |
| listlist | Processa uma seção de *template* para cada variável contida dentro de uma sequência. Veja mais em *[List](http://freemarker.org/docs/ref_directive_list.html#ref.directive.list)*. |
| local | Cria ou substitui uma variável local. Funciona apenas dentro de uma  ou . Veja mais em [Local](http://freemarker.org/docs/ref_directive_local.html#ref.directive.local). |
| lt | *Left Trim*: ignora todos os espaços em branco precedentes na linha. Veja mais em [LT](http://freemarker.org/docs/ref_directive_t.html#ref.directive.lt). |
| macromacro | Cria uma variável de macro. Veja mais em [Macro](http://freemarker.org/docs/ref_directive_macro.html#ref.directive.macro) e . |
| nested | Executa o fragmento do *template*. Veja a diretiva . |
| nt | *No Trim*: desabilita a remoção de espaços em branco na linha onde ele é utilizado. Ele também desabilita os efeitos de outras diretivas de *trim*. Veja mais em [NT](http://freemarker.org/docs/ref_directive_nt.html#ref.directive.nt). |
| recover | Veja . O bloco de *recover* é executado no lugar do bloco *attempt*. Caso nenhum erro ocorra durante a execução do bloco *attempt* então o bloco *recover* é ignorado. |
| recurse | Percorre todos os nós filhos de um nó. Veja mais em *[Recurse](http://freemarker.org/docs/ref_directive_visit.html#ref.directive.recurse)*. |
| return | Veja  e . |
| rt | *Right Trim*: ignora todos os espaços em branco procedentes na linha. Veja mais em [RT](http://freemarker.org/docs/ref_directive_t.html#ref.directive.rt). |
| stop | Interrompe o processo de renderização do *template*. Veja mais em *[Stop](http://freemarker.org/docs/ref_directive_stop.html#ref.directive.stop)*. |
| switchswitch | *Switch* é utilizado para selecionar um fragmento do template dependendo do valor de uma expressão. Veja mais em *[Switch](http://freemarker.org/docs/ref_directive_switch.html#ref.directive.switch)*. |
| t | *Trim*: ignora os espaços em branco precedentes e procedentes na linha. Veja mais em [T](http://freemarker.org/docs/ref_directive_t.html#ref.directive). |
