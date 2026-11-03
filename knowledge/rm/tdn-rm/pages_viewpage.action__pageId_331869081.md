---
content_hash: 284d931b12fb424a5ea463c529ed3b189c129a5a8763f83123686f8f73ec626c
fetched_at: '2026-06-29T00:08:50.202523+00:00'
page_id: '331869081'
product: rm
source: tdn-rm
title: Utilizando a atividade "Executar Transformação XSLT"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331869081
version: 24
---

# Objetivo:

---

     Este documento tem como finalidade, demonstrar o uso da atividade **"Executar Transformação XSLT"**.

# Configuração:

---

## Informações Gerais

### Objetivo:

A finalidade da atividade "Executar Transformação XSLT" é permitir que um XML de entrada possa ser transformado em um XML totalmente diferente, de acordo com o algoritmo escrito em um arquivo (ou conteúdo) .XSLT.

### Passo a Passo:

Primeiramente é necessário arrastar a atividade "Executar Transformação XSLT" para o "Fluxo de Trabalho Sequencial" em sua fórmula visual.

Após atividade ter sido adicionada ao fluxo de trabalho, é necessário configurar as propriedades da atividade.

Vamos agora, preencher essas propriedades. Iniciaremos preenchendo a propriedade "XmlIn".

Ao clicar no botão [...] a tela abaixo será apresentada:

Nessa tela, adicione o XML de Entrada.

150

Após preencher a propriedade XmlIn, preencha a propriedade "Xls".

Ao clicar no botão [...] a tela abaixo será apresentada:

Nessa tela, adicione o XLS.

150

Após preencher as propriedades, salve e execute a Fórmula Visual. Verifique o resultado do processo. A Fórmula Visual deverá executar com sucesso.

### Exemplos de Uso:

1 - Atividade **"Executar Transformação XSLT"** com Atividade **"Gerar Exceção"**:

Após preencher todas as propriedades:

Vincule a Propriedade XmlOut da Atividade Executar Transformação XSLT na Propriedade Mensagem de Erro da atividade Gerar Exceção

Após o preenchimento da propriedade "Mensagem de Erro", salve e execute a fórmula visual. Observe que o resultado será esse:

O novo XML gerado será apresentado como uma exceção.

150

## Parâmetros

### XmlIn (Obrigatório)

*Descrição*: XML de Entrada.  
*Tipo*: Cadeia de Caracteres (String)  
*Como usar*: Esse parâmetro é do tipo Cadeia de Caracteres, ou seja, deve-se utilizar um valor alfanumérico que represente o XML de entrada, ou seja, o XML que será transformado pelo algoritmo escrito no arquivo .XLST.

### XmlOut (Opcional)

*Descrição*: XML de Saída.  
*Tipo*: Cadeia de Caracteres (String)  
*Como usar*: Esse parâmetro é do tipo Cadeia de Caracteres e é o retorno da transformação do XML configurado através da propriedade XmlIn. </div>

### Xsl (Obrigatório)

*Descrição*: Conteúdo XSL.  
*Tipo*: Cadeia de Caracteres (String)  
*Como usar*: Esse parâmetro é do tipo Cadeia de Caracteres, ou seja, deve-se utilizar um valor alfanumérico que represente o XSL que transformará o XML de entrada em um XML totalmente diferente, de acordo com o algoritmo escrito.
