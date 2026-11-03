---
article_id: 37694053096087
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: cbffa1bc5bae6491e378b10bd91493d348d1cc6b5020d4860cc462d069935a84
fetched_at: '2026-06-28T22:37:20.323348+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - AJUDA:C5_TPFRETE Tipo
  do frete utilizado no encerramento da Medição
type: support-article
updated_at: '2026-01-15T11:30:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37694053096087-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-AJUDA-C5-TPFRETE-Tipo-do-frete-utilizado-no-encerramento-da-Medi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37694053094295) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**

AJUDA:C5\_TPFRETE - Tipo do frete utilizado ao encerrar uma Medição no Gestão de Contratos

**AJUDA:C5\_TPFRETE**  
Tipo do frete utilizado:  
C = CIF  
F = FOB  
T = Por conta de terceiros  
R = Por conta remetente  
D = Por conta destinatário  
S = Sem frete

Tabela SC5 13/01/2026 05:15:44  
Tipo Pedido          - C5\_TIPO      := N  
Cliente              - C5\_CLIENTE   := 001489  
Loja Entrega         - C5\_LOJAENT   := 01  
Loja                 - C5\_LOJACLI   := 01  
Data Emissao         - C5\_EMISSAO   := 13/01/2026  
Cond. Pagto          - C5\_CONDPAG   := 002  
Moeda                - C5\_MOEDA     := 1  
Tipo Frete           - C5\_TPFRETE   :=   < -- Invalido  
Num.Contrato         - C5\_MDCONTR   := 000000000000005  
Num.Medicao          - C5\_MDNUMED   := 000013  
Num.Planilha         - C5\_MDPLANI   := 000001  
Natureza             - C5\_NATUREZ   := 102

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Causa**

Tipo Frete           - C5\_TPFRETE   :=   < -- Invalido

Esse Help ocorre , pois, o tipo de frete está inválido ou não foi preenchido.

**Solução**  
  
1. Para preencher automaticamente o campo **C5\_TPFRETE, e**xiste no cadastro de cliente, o campo **A1\_TPFRET**. Quando configurado, o conteúdo deste campo é transferido para o campo **C5\_TPFRETE**.

Já para alteração dos campo do Pedido de venda gerado pelo Encerramento de medição no módulo pode se utilizar o ponto de entrada [GCTPEDCPO - Liberar campos para alteração de pedidos de venda oriundos do SIGAGCT](https://tdn.totvs.com/pages/viewpage.action?pageId=658231372)

Veja mais detalhes no artigo: [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Alteração de Pedidos de Vendas / Compras gerados pelo Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000675988-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Altera%C3%A7%C3%A3o-de-Pedidos-de-Vendas-Compras-gerados-pelo-Gest%C3%A3o-de-Contratos)

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Documentação Gestão de Contratos do TDN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441027145623)

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[FAQs - Gestão de Contratos](https://tdn.totvs.com/x/O_tgDQ)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
