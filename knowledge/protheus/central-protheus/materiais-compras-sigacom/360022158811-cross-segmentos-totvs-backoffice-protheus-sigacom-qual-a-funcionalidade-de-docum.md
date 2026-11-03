---
article_id: 360022158811
category: Materiais - Compras (SIGACOM)
content_hash: c9841649f810a18560c23d8a6f9e2aea0aea8481bff338096fb4efdb4cdaf4b8
fetched_at: '2026-06-28T22:41:10.377027+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual a Funcionalidade
  de Documento Vinculado da rotina Documento de Entrada (MATA103) ?
type: support-article
updated_at: '2024-09-04T14:21:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022158811-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-a-Funcionalidade-de-Documento-Vinculado-da-rotina-Documento-de-Entrada-MATA103
---

**Dúvida**Qual a Funcionalidade de Documento Vinculado da rotina Documento de Entrada (MATA103) ?  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**

O processo de industrialização por conta e ordem de terceiro exige que haja três pessoas:

* O ***encomendante*** (aquele que solicita a industrialização)
* O ***fornecedor*** (quem fornece a matéria prima)
* O ***industrializador***  (quem fará o processo de beneficiamento/industrialização)

**CONCEITO SOBRE O PROCESSO COMO ENCOMENDANTE:**

1. Recebe Documento de Entrada do fornecedor. Este documento deve citar a Nota Fiscal emitida pelo fornecedor ao industrializador e utilizar uma TES que atualize o estoque, sem controlar poder de terceiros.
2. Vincula os dois documentos emitidos pelo fornecedor, por meio da opção Documento Vinculado / Vínculo / Alterar. No campo "Operação" deve ser selecionado "Encomendante". É necessário informar o Industrializador (no campo "Cliente") e o número do documento emitido ao industrializador.
3. Emite Documento de Saída de Cobertura para o industrializador, por meio da opção Documento Vinculado / Cobertura / Documento de Saída. A TES será preenchida automaticamente, conforme a configuração do campo "Tes Rem. Sim.".
4. Recebe o Documento de Entrada do industrializador. Este documento deve utilizar uma TES que atualize o estoque e controle poder de terceiros (Devolução).
5. ***Importante**:*A TES utilizada no Documento de Entrada deve ter o campo "Tes Rem. Sim." (Tes Remessa Simbólica - F4\_TESE3) configurado com uma TES de saída, que será a TES utilizada na emissão do documento de Cobertura, esta deve atualizar o estoque e controlar poder de terceiros (Remessa). Este campo deve ser habilitado, como "Usado", por meio do ambiente Configurador.

*Procedimentos***:**

1. Inclusão da NF da compra da mercadoria;
2. Incluir o Doc. Vinculado no qual o fornecedor mandou a NF ao fornecedor industrializador;
3. Incluir a nf da remessa de cobertura para o fornecedor industrializador visando que seja registrada a simples remessa de saída e permitir após algum processo por parte do industrializador, que o mesmo efetue a devolução da remessa;
4. Após emissão da NF e envio ao industrializador, quando o fornecedor industrializar ele irá encaminhar a NF da Devolução da Simples Remessa, onde devemos efetuar o retorno via Doc. Entrada.

**CONCEITO SOBRE O PROCESSO COMO INDUSTRIALIZADOR:**

1. Recebe Documento de Entrada do fornecedor. Este documento deve citar a Nota Fiscal emitida pelo fornecedor ao encomendante (cliente) e utilizar uma TES que atualize o estoque, sem controlar poder de terceiros, pois o documento somente é utilizado para o acompanhamento do material.
2. Vincula os dois documentos emitidos pelo fornecedor, por meio da opção Documento Vinculado/Vínculo/Alterar. No campo "Operação" deve ser selecionado "Industrializador".  
   É necessário informar o encomendante (no campo "Cliente") e o número do documento emitido ao encomendante.
3. Recebe a nota de cobertura emitida pelo encomendante, por meio da opção Documento Vinculado / Cobertura / Documento de Entrada. Este documento deve utilizar uma TES que não atualize o estoque, mas que controle poder de terceiros (Remessa).
4. Emite Documento de Saída ao encomendante. Este documento deve utilizar uma TES que atualize estoque e controle poder de terceiros (Devolução).

*Procedimentos:*

1. Após posicionar no doc. E Doc. Vinculado – Vincular – Alterar, informar o processo como “Industrializador” e os dados da NF emitida pelo fornecedor ao cliente envolvido na Remessa.  
   Esse cliente irá encaminhar uma NF de Remessa de Entrada, e após o industrializador irá realizar a devolução da simples remessa no fim do processo;
2. Posicionar na nf do fornecedor e selecionar Doc. Vinculado – Cobertura – Doc. Entrada;
3. Selecionar o processo do cliente visando emissão da NF de Entrada par beneficiamento;
4. Gerar a NF de Entrada de simples remessa do cliente;
5. Em pedido de vendas, efetuar o pedido de vendas visando gerar a NF de devolução de simples remessa para o cliente;
6. Emissão de NF de Saída.

***Vincular/Cobertura:***  
Estas funcionalidades, da opção "Doc. Vinculado", devem ser atribuídas ao Documento de  
Entrada, de acordo com trâmite dos produtos.  
  
A função "**Vincular**" permite vincular as Notas Fiscais emitidas pelo fornecedor. As opções  
disponíveis para esta função são: Visualizar, Alterar ou Excluir.  
  
A função "**Cobertura**" permite, ao encomendante/industrializador, emitir/dar entrada à Nota Fiscal  
de Remessa e Nota Fiscal de Retorno de Cobertura, para os produtos enviados/recebidos para a  
industrialização por encomenda.

***Fluxo:***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018993231)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018993971)

***Saiba Mais :***

***[Industrialização por encomenda](https://tdn.totvs.com/pages/viewpage.action?pageId=440846500)***
