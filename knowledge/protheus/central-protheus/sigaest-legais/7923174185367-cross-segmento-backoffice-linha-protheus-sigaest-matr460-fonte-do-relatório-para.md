---
article_id: 7923174185367
category: SIGAEST - LEGAIS
content_hash: 0878cac447c3eca8439e4de8a3d66270d63f29b271efde037a04d351ddd07d5e
fetched_at: '2026-06-28T22:38:51.743124+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Fonte do
  Relatório para download
type: support-article
updated_at: '2022-08-03T20:16:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7923174185367-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Fonte-do-Relat%C3%B3rio-para-download
---

**Dúvida**Onde posso baixar o fonte do relatório MATR460?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - Todas as versões  
  
**Solução**

O relatório MATR460 *não possui fonte disponível para envio por se tratar de um relatório fiscal*.  
   
Caso tenha necessidade de alteração, deverá abrir chamado para o suporte enviando o embasamento legal para tal alteração, pois este relatório somente é modificado de acordo com a legislação.

Obs.:

O Registro de Inventário MOD 7 (MATR460) é um relatório de característica fiscal regulamentado pela União. Ele tem como objetivo demonstrar os valores contábeis do estoque (custo médio) numa determinada data.  
   
A União solicita este relatório para que este seja confrontado com o balanço da empresa, ou seja, ele deve retratar as contas do ativo referente aos custos do estoque.  
   
O programa parte de um saldo inicial na data selecionada como início nos parâmetros e a partir desta data lista os movimentos que ocorreram para o produto em questão no almoxarifado.  
   
Com estas informações o usuário pode saber qual o seu saldo em quantidade e valor numa determinada data, obtendo assim um controle geral de tudo que entrou e saiu do almoxarifado, em que dia e em que documento.  
   
Para visualizar sem o saldo deduzido de poder de terceiros, basta alterar a parametrização do relatório.  
   
O processo está correto, mas a montagem do relatório faz um cálculo onde aparece na coluna "Em estoque" o saldo de poder de terceiros subtraindo o saldo atual do produto, o que gera um estoque negativo, mas não significa que está negativo.  
   
Ou seja, apenas *através de legislação o relatório poderá ser alterado*, pois o formato atual é justamente para atender a legislação em vigor.  
   
Se esse saldo de poder de terceiros já foi devolvido, utilizando o parâmetro MV\_SDTESN3 irá resolver o problema.  
   
Você poderá também verificar outro relatório que apresente informações semelhantes a este e utilizar o fonte para customização. Caso desejar, ***[clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058126794-MP-SIGAEST-Fontes-de-relat%C3%B3rios-Estoque-para-altera%C3%A7%C3%A3o-ou-customiza%C3%A7%C3%A3o-fora-do-padr%C3%A3o?source=search)*** para fazer o download dos fontes disponíveis. Por exemplo o POSIÇÃO DE ESTOQUE (MATR260).

Saiba Mais:  
*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001533821-Estoque-e-Custos-SIGAEST-)*
