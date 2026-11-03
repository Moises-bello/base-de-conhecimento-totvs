---
article_id: 360021542151
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 126379c1175292a434adfa7e57966980d6da270162978fe120d3f8e5fc6977c3
fetched_at: '2026-06-28T22:38:38.492066+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como fica o
  saldo das despesas acessórias (Frete/Seguro/Despesa) na planilha financeira
type: support-article
updated_at: '2022-08-26T12:57:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021542151-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-fica-o-saldo-das-despesas-acess%C3%B3rias-Frete-Seguro-Despesa-na-planilha-financeira
---

**Dúvida**Como fica o saldo das despesas acessórias (Frete/Seguro/Despesa) na planilha financeira?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**Nessa FAQ vamos destacar 3 pontos:

**1.** A planilha financeira não efetua cálculo de saldos das despesas acessórias do pedido de venda, pois a planilha baseia-se somente nos dados do cabeçalho **SC5** e itens **SC6** e também não faz nenhum tipo de consulta em outras tabelas, como por exemplo as tabelas de Notas Fiscais **SF2**e **SD2**para verificar os itens que já foram faturados.

**2.**Quando é utilizado a pergunta: **Planilha Financeira? igual a Saldo** via <**F12**> a planilha simplesmente verifica se algum item já foi entregue **C6\_QTDENT** e em seguida subtrai do valor da quantidade vendida **C6\_QTDVEN** para efetuar o cálculo dos saldos restantes do pedido de venda.

**3.**A planilha financeira não tem como prever o saldo restante das despesas, pois o cálculo das despesas acessórias são feitas no momento de efetuar a emissão do documento de saída e dependendo da forma que os itens forem liberados e faturados, as despesas acessórias podem ser rateadas ou não entre os itens do pedido de venda.

Veja o link para maiores detalhes sobre o rateio das despesas acessórias

**Saiba Mais:**  
**[Cálculo do Rateio das Despesas Acessórias (Frete / Seguro / Despesa) na Geração do Documento de Saída](http://tdn.totvs.com/pages/viewpage.action?pageId=239024024)**
