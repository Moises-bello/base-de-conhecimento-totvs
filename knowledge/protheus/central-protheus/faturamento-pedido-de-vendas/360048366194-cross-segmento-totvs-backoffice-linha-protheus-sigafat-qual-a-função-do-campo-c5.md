---
article_id: 360048366194
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 032bc280895e949561b8738eb34fbda01cbf02d1c5416d6442fc6ffc9195ccc4
fetched_at: '2026-06-28T22:38:38.426137+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -  Qual a função
  do campo C5_TIPOCLI
type: support-article
updated_at: '2024-08-22T20:31:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048366194-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Qual-a-fun%C3%A7%C3%A3o-do-campo-C5-TIPOCLI
---

**Dúvida**

Qual a função do campo C5\_TIPOCLI ?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

É possível classificar os clientes em cinco tipos: Consumidor Final, Produtor Rural,  
Revendedor, Solidário e Exportação. Essa divisão foi feita em função do cálculo dos  
impostos, tratado de forma diferenciada para cada tipo.  
Conceitualmente, a maioria das vezes em que é emitido um Documento de Saída, o destinatário é considerado um cliente, independentemente do tipo que ele possua, ou da denominação que a empresa tenha determinado para ele.  
• Pasta Cadastrais : Tipo  
A seleção do campo Tipo, influencia diretamente no tipo do documento a ser emitido.  
Pode ser informado:

• **F - Consumidor Final**  
O tipo de cliente consumidor final é importante para a geração das Notas Fiscais de Venda ao Consumidor Final. Pedido para geração de nota fiscal de venda ao consumidor:  
As Notas de Vendas para consumo podem ocorrer em três situações, em que o TES indica na saída, que o IPI incide na base do ICMS e na entrada que não tem crédito.  
1. O cliente compra para Consumo e tem Inscrição Estadual. A venda é normal se for dentro do Estado. Fora do Estado, além do código fiscal 6 no lugar de 5, difere a alíquota de imposto.  
2. O cliente compra para Consumo e não tem Inscrição Estadual (empresas do governo,  
empresas de serviço, etc.). A venda é normal, se for dentro do Estado. Fora do Estado é tributada a alíquota interna.  
3. O cliente é Pessoa Física, compra para Consumo. Sendo assim, no campo Inscrição Estadual há o número do RG. A venda é normal, sendo dentro do Estado. Fora do Estado é tributada a alíquota diferenciada de 17% para 18% (Inscrição do Cliente em branco ou Tipo de Cliente igual a F).

• **L - Produtor Rural**  
O tipo de cliente produtor rural é importante para a geração das Notas Fiscais de Venda  
ao Produtor Rural.  
Pedido para geração de nota fiscal de C.S.S.R:  
Na geração de notas fiscais é calculado o valor do imposto de Contribuição de  
Seguridade Social Rural e armazenado no arquivo Cabeçalho de Notas fiscais de  
Venda (SF2, campo F2\_CONTSOC).  
Procedimentos  
Para emissão da Nota Fiscal de Venda ao Produtor Rural configure:  
1. No Cadastro de Clientes, o campo:  
• **Tipo = L - Produtor Rural**  
2. No Cadastro de Produtos, o campo:  
• Cont. Seg. Soc. = Sim  
Este campo indica se no produto incide a Contribuição de Seguridade Social

• **R - Revendedor**  
O tipo de cliente revendedor pode ser utilizado em várias situações tributárias distintas,  
o que irá definir o cálculo dos impostos e taxas. A forma de tributação é o TES de saída  
utilizado na emissão da nota fiscal

• **S - Solidário**  
O tipo de cliente solidário é importante para a geração das Notas Fiscais de Venda com  
Substituição Tributária, ou seja, com o cálculo de ICMS Solidário ou Retido na Fonte.

• **X - Exportação**  
O tipo de cliente exportação é importante para a geração das Notas Fiscais de Exportação.
