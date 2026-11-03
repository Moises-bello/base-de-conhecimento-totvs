---
article_id: 360034970673
category: Financeiro
content_hash: e1035b8a4840c58847e73f4a8ad2563e0b1bdc20b699b2717dd13bcaa65cc80f
fetched_at: '2026-06-28T22:38:00.898338+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como alterar a quantidade
  de Casas Decimais de moeda estrangeira '
type: support-article
updated_at: '2024-02-22T18:33:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034970673-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-alterar-a-quantidade-de-Casas-Decimais-de-moeda-estrangeira
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como alterar a quantidade de casas decimais no módulo SIGAFIN?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Para o correto funcionamento do sistema, é importante que todos os campos abaixo sejam ajustados:

|  |  |  |
| --- | --- | --- |
|  | **Passo a passo:** | **Tabelas relacionadas:**  **SC3** - Contrato de Parceria  **SC5** - Pedidos de Vendas  **SC7** - Ped, Compra/ Aut. Entrega  **SC8** - Cotações  **SCJ** - Orçamentos  **SCR** - Documentos com Alçadas  **SCY** - Histórico Pedidos de Compras  **SE1** - Contas a Receber  **SE2** - Contas a Pagar  **SE5** - Movimentos Bancários  **SEI** - Movimento Aplicações/Emprestimo  **SEL** -Recibos de Cobrança  **SF1** - Cabeçalho das NF de Entrada  **SF2** - Cabeçalho de NF de Saída  **SGV** - Histórico Aprovação Pedido de Compra  **SL1** - Orçamento  **SLQ** - Orçamento  **SM2** - Cadastro de Moedas  **Ao alterar algum(s) dos campo(****s) abaixo, é necessário alterar os demais também**.  **SC3**: C3\_TXMOEDA  **SC5**: C5\_TXMOEDA  **SC7**: C7\_TXMOEDA  **SC8**: C8\_TXMOEDA  **SCJ**: CJ\_TXMOEDA  **SCR**: CR\_TXMOEDA  **SCY**: CY\_TXMOEDA  **SE1**: E1\_TXMOEDA  **SE2**: E2\_TXMOEDA  **SE5**: E5\_TXMOEDA  **SEI**: EI\_TXMOEDA  **SEL**: EL\_TXMOEDA  **SF1**: F1\_TXMOEDA  **SF2**: F2\_TXMOEDA  **SGV**: GV\_TXMOEDA  **SL1**: L1\_TXMOEDA  **SLQ**: LQ\_TXMOEDA.  **SM2:** M2\_MOEDA1, M2\_MOEDA2, M2\_MOEDA3, M2\_MOEDA4 e M2\_MOEDA5  No Protheus 11 existe o compatibilizador **U\_UPDFINTM:**  **[Aumento de decimais nos campos de taxa de moeda](https://tdn.totvs.com/display/public/mp/Aumento+de+decimais+nos+campos+de+taxa+de+moeda)** |
