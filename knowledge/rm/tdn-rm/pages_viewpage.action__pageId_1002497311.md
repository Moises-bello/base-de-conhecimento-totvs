---
content_hash: 7c9174d9f83cd3cd43de8f60aa64e894568fac6eb02e96d8f00297c931bcec40
fetched_at: '2026-06-29T00:05:45.046595+00:00'
page_id: '1002497311'
product: rm
source: tdn-rm
title: Exemplo de Movimento Ct-e OS(básico)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1002497311
version: 5
---

Durante a criação do movimento de CT-e OS será necessário preencher corretamente alguns campos (outros campos poderão ser de preenchimento obrigatório, de acordo com a regra de negócio da empresa):

* Na aba Integrações | Fiscal, informar o Cod. Natureza de Operação válido para CT-e OS
* Na aba Transporte | Identificação, informar o Tipo de Frete e o campo Quantidade.

* Informar o campo Tipo CT-e OS, que é utilizado para definir se o registro é Normal, Complementar ou Substituição.

* Informar no Tipo do Serviço CT-e OS – A opção **Transporte de Pessoas**

Quando for um movimento de **"****CT-e OS****"** e o campo **”****Tipo do Serviço CT-e OS****"** for definido como **"****Transporte de Pessoas****"**, será apresentado o campo **"****Tipo do Fretamento de Pessoas****"** com duas opções: **Contínuo e Eventual**.

Quando o tipo do fretamento for definido como "**Eventual**" será exibido um novo campo na tela "**Data e Hora da Viagem**" e o seu preenchimento é opcional.

* Informar no Tipo do Serviço CT-e OS – A opção  **Excesso de Bagagem**

Quando o tipo do CT-e OS for igual a "Excesso de Bagagem", será disponibilizado no movimento a aba CTRC Saída.   
Podendo ser preenchida de duas formas:

**1 - Clicando no botão: +**

As informações devem ser preenchidas de forma manual. Caso o tipo de documento possua um modelo de documento (CODMODDOC) que seja de documento eletrônico, será habilitado a aba Documento Auxiliar Eletrônico, onde deve ser preenchido o campo: Chave de Acesso do BP-e. 

Caso tipo de documento não possua um modelo de documento (CODMODDOC) que seja eletrônico, os campos: Data Emissão , Número Nota, Série, Sub Série e Valor Total, devem ser preenchidos.

**2- Clicando no botão: CTRC Saída**

Preencha o filtro de forma a encontra o(s) movimento(s) que queira associar ao CT-e OS. Feito isso, os campos da tela de identificação serão preenchidos automaticamente de acordo com os dado(s) do(s) movimento(s) associado(s). 

***Observação***: Para esse tipo de CT-e OS as abas Informações Contingência e Documento Auxiliar Eletrônico não serão exibidas na tela de Notas Fiscais Conhec. Transporte. Na aba CTRC | CT-e não será exibida a tela Informações de percurso.

Consistências:

O campo "Tipo do Serviço CT-e OS" é de preenchimento obrigatório.

Em tipos de movimento parametrizados como "**Emitir CT-e OS**" será obrigatório o preenchimento do campo "**Tipo do Serviço CT-e OS**" no movimento e não mais nos parâmetros e caso não seja preenchido, será apresentado a mensagem de consistência abaixo:

Imagem

O campo "Tipo do Fretamento de Pessoas" é de preenchimento obrigatório.

Em tipos de movimento parametrizados como "**Emitir CT-e OS**" onde o  campo "**Tipo do Serviço CT-e OS**" esteja preenchido como "**Transporte de Pessoas**", o campo "**Tipo do Fretamento de Pessoas**" será de preenchimento obrigatório e caso não seja preenchido, será apresentado a mensagem de consistência abaixo:

Imagem

* Ainda em Transporte | Identificação, deverá ser relacionado um Cliente/Fornecedor como tomador do serviço, no grupo Dados do Tomador de Serviço.

* Na aba CRTC | Coleta e Entrega informar o Estado e Município de início (Coleta) e o Estado e Município de fim (Entrega).

* Na aba CTRC | Outros Dados informar os valores da Composição do Frete (é necessário pelo menos um deles preenchido).

* Na aba CTRC | CT-e | Seguro de Carga, incluir as informações do Seguro do Transporte.

* Na aba CTRC | CT-e | Informações de Percurso: **Apresentada somente quando o "Tipo do Serviço CT-e OS" for Transporte de Pessoas.**

          Incluir as informações dos estados contidos no Percurso entre as UF de Origem e a UF de Destino. É necessário informar também qual a ordem em que cada estado será  parte do percurso.

Salve o movimento e realize a transmissão do CT-e OS.

**CT-e OS Complementar**

Para enviar um CT-e OS do tipo Complemento de Valores, é necessário configurar um novo Tipo de Movimento com o  Motivo de Referência → 6 - NF Complementar / Retificadora. Esse Motivo de Referência é configurado na etapa Mov - Outros Dados.  
Assim, deve-se gerar uma cópia por referência nesse novo Tipo de Movimento selecionando como movimento base o movimento do CT-e OS a que se deseja complementar. Nesse Movimento, deve-se selecionar na etapa Transporte | Identificação e selecionar o Tipo CT-e como "Complemento de Valores"  
Após realizar essas parametrizações, o envio do CT-e OS Complementar é igual ao de um CT-e OS normal.
