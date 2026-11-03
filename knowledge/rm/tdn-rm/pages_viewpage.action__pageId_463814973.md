---
content_hash: d5e49a294c1e2f51c00e2fb8559458074a6ed4b4ebe862ed648cdf2fc401093f
fetched_at: '2026-06-29T00:10:15.151822+00:00'
page_id: '463814973'
product: rm
source: tdn-rm
title: Utilizando a atividade "Executar Relatório"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463814973
version: 23
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Este documento tem como objetivo trazer uma visão de como funciona a atividade Executar Relatório.

# Introdução:

---

       Essa atividade permite que um relatório seja gerado, com a passagem de parâmetros e filtros previamente cadastrados na estrutura do relatório.

# Utilizando a atividade:

---

       Primeiro, é necessário arrastar a  atividade "Executar Relatório" para o fluxo de trabalho sequencial da Fórmula Visual. Em seguida, é preciso configurar as propriedades da atividade.

***Código da aplicação:***Aplicação na qual o relatório a ser utilizado pela atividade foi criado.

***Código da coligada:***Coligada em que o relatório foi criado.

***Código do relatório:***Código do relatório a ser gerado pela atividade.

***Formato do arquivo:***Formato em que o relatório será gerado (PDF, JPEG, RTF, TXT, etc).

Caso prefira, é possível efetuar a pesquisa do relatório a ser gerado pela FV ao clicar com o botão direito na atividade pelo fluxo de trabalho e em seguida clicar na opção "Selecionar Relatório".

# Filtros e Parâmetros:

       Após os campos de parâmetro da atividade serem preenchidos, dois novos grupos de propriedades serão exibidos: "**Filtro(s) do relatório**" e "**Parâmetro(s) do relatório**", isso só acontece caso o relatório tenha parâmetros e/ou filtros cadastrados em sua estrutura.

Não é possível criar parâmetros e filtros para um relatório através dessa atividade.

12Filtros

Para o uso um filtro na atividade, é necessário preencher o campo da seguinte forma:

**NOMETABELA.CAMPO (SINAL) 'VALOR'**

Como no exemplo acima, para trazer Chapa menor que 00005, será escrito:

**PFUNC.CHAPA < '00005'**

3Parâmetros

Para parâmetros, é possível digitar apenas o valor desejado.

Os sinais que serão usados na geração do relatório correspondem aos escritos na consulta SQL, não sendo necessário digitá-los na atividade.

       Exemplo de uso dos parâmetros e filtros descritos:

# Envio de relatório por e-mail:

---

       O relatório gerado pela atividade "Executar Relatório" não é exibido após o fim da execução do processo de geração, no entanto, uma forma de conseguir visualizar o relatório gerado é enviá-lo por e-mail após a execução do processo.

       Para isso, é necessário adicionar a atividade "Enviar E-mail" ao fluxo de trabalho. Após isso, pode-se configurar para que o relatório seja enviado da seguinte forma:

       Na propriedade "**Anexar Arquivo**", ao clicar em "**Propriedade de Associação**" uma tela de seleção será aberta, assim, selecione a opção "**Relatório Gerado**" mostrada ao expandir a atividade de geração de relatório.

       Após preencher os campos necessários para o envio do e-mail (para mais informações, consulte a página "[Utilizando a atividade Enviar E-mail](http://tdn.totvs.com/pages/releaseview.action?pageId=146184224#CriandoaF%C3%B3rmulaVisual--1542145415)"), ainda nas propriedades dessa atividade, é necessário informar o **Nome do Arquivo Anexo**.

45Nome do Arquivo Anexo

Nessa propriedade, ao inserir o nome do arquivo, é preciso que a extensão também seja informada.

Nos parâmetros da atividade "Executar Relatório" foi informado o formato de arquivo em que o relatório será gerado (por exemplo, o formato PDF). Então agora, na atividade "Enviar e-mail" o nome do arquivo deve contar com a extensão "**.pdf**"

# Binding de parâmetros e filtros:

---

       Para o uso de parâmetros e filtros, há também a possibilidade de ligá-los a outros campos da própria FV. No caso dos filtros, eles devem ser montados a partir da atividade "Expressão", já os parâmetros podem ser ligados diretamente a um campo da FV.

       No exemplo a seguir, foi criada uma FV exemplo, trazendo os 3 primeiros funcionários da tabela PFUNC e para cada um deles, com o uso da atividade "Para cada Iteração" será gerado um relatório e enviado por e-mail.

6tFiltros

Foi adicionada a atividade "Expressão" antes da atividade "Executar Relatório" no fluxo de trabalho, onde o filtro foi montado para ser usado posteriormente.

Em seguida, na propriedade "Filtro(s) do relatório" foi feita a ligação com a atividade "Expressão" através do botão "**Propriedade de Associação**". Onde foi selecionada a atividade Expressão e usada a propriedade de conversão do valor para string.

Assim, o campo será exibido da seguinte forma:

8Parâmetros

Para os parâmetros, os campos foram ligados diretamente pela "**Propriedade de Associação**". Foi selecionada a atividade "Para cada Iteração", em seguida na propriedade "Campos" foi colocado o nome do parâmetro usado entre aspas e selecionado o valor como string.

Exemplo do campo CODSECAO após expandir a atividade "Para cada Iteração":

Após as ligações, os filtros e parâmetros serão exibidos da seguinte forma na aba de Propriedades da Atividade:

# Envio de relatório por requisição HTTP:

---

       O relatório gerado pela atividade "Executar Relatório" também pode consumido por uma requisição HTTP.

       Para isso, é necessário adicionar a atividade "Executar Requisição HTTP" ao fluxo de trabalho. Em seguida, pode-se configurar para que o relatório fique disponível para a atividade "Executar Requisição HTTP":

       Na propriedade "**Resultado do relatório**", ainda na atividade "Executar Relatório", ao clicar em "**Propriedade de Associação**" uma tela de seleção será aberta, assim, selecione a opção "**RequestData**" mostrada ao expandir a atividade "Executar Requisição HTTP".

Após preencher o campo necessário para que o relatório gerado fique disponível para ser utilizado pela atividade "Executar Requisição HTTP" deveremos preencher algumas informações nessa atividade:

* **Tipo de conteúdo da requisição**: multipart/form-data
* **Nome chave do arquivo de formulário**: "nome da chave que por padrão é file (padrão utilizado)"
* **Nome do arquivo de formulário**: Nome dado ao arquivo que será enviado.

Para o preenchimento das demais informações da atividade "Executar Requisição HTTP", consulte a página "[Utilizando a atividade Executar Requisição HTTP](https://tdn.totvs.com/pages/viewpage.action?pageId=368083652)".

# Envio de arquivo utilizando a atividade "Transformar Arquivo em Cadeia de Bytes" por requisição HTTP:

---

O arquivo escolhido para ser gerado na atividade "**Transformar Arquivo em Cadeia de Bytes**" também pode consumido por uma requisição HTTP. Para isso, é necessário adicionar as atividade "**Transformar Arquivo em Cadeia de Bytes**" e "**Executar Requisição HTTP**" ao fluxo de trabalho.

       Na propriedades da atividade "**Transformar Arquivo em Cadeia de Bytes**" é necessário preencher o seguinte campo: 

**Parâmetros da Atividade:**

* **Nome do Arquivo fixo:** Selecionar o arquivo que será gerado.

       Em seguida, vamos configurar para que o arquivo seleciona na atividade "**Transformar Arquivo em Cadeia de Bytes**" fique disponível para a atividade "**Executar Requisição HTTP**".

       Nas propriedades  da atividade "**Executar Requisição HTTP**", é necessário preencher os seguintes campos:

      **Parâmetros da Atividade:**

* **Dados (Binário):** Selecionar o ByteArray da atividade "Transformar Arquivo em Cadeia de Byte".
* **Nome chave do arquivo de formulário:** Nome da chave que por padrão é file (padrão utilizado)
* **Nome do arquivo de formulário (com extensão. ex.: arquivo.pdf ):**Nome dado para o seu arquivo que será gerado.

      **Requisição:**

* **Endereço da requisição:**Endereço de requisição utilizado para fazer a chamado HTTP.
* **Método de Requisição:** Método que será utilizado a requisição.

**Tipo de Conteúdo:**

* **Tipo de Conteúdo da requisição:** multipart/form-data

       Realizada as configurações necessárias, execute a fórmula e verifique que o arquivo foi gerado corretamente no caminho padrão da API utilizada e aberta corretamente no browser.

Para entender mais sobre a atividade "[Utilizando a atividade "Transformar Arquivo em Cadeia de Bytes"](https://tdn.totvs.com/x/C5OZH)".

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.24

false

**Processo:** Utilizando a atividade "Executar Relatório.

falsefalse

**Status:** Pendente

false

**Data:** 04/03/2019

false

**Autores:**
