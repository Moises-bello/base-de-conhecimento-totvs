---
article_id: 360051997154
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 93ba8d1c6a721bf464b59da8e51181228981e0689c7c7f78e7b1f2f716a14536
fetched_at: '2026-06-28T22:42:43.330808+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Funcionamento do parâmetro Qtd da Geração
  OPs e Scs
type: support-article
updated_at: '2023-04-25T16:43:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051997154-Manufatura-Linha-Protheus-SIGAPCP-Funcionamento-do-par%C3%A2metro-Qtd-da-Gera%C3%A7%C3%A3o-OPs-e-Scs
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:15 min**  
**Dúvida**Como é o funcionamento de cada opção do parâmetro **Qtd da Geração OPs e Scs?** ao abrir uma **OP** por **Vendas**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O parâmetro **Qtd da Geração OPs e Scs?** significa se as **OPs** e **SCs** deverão considerar o **LE**ou não e como gerará esses documentos abertos via **MATA650 > Outras Ações > Vendas**.

* Opção: **LE padrão**Se os parâmetro **MV\_QUEBROP** e **MV\_QUEBRSC** estiverem ativos as **OPs** e **SCs** serão quebradas pelo lote econômico.  
  Exemplo:  
  **Lote econômico** de 50  
  **MV\_QUEBROP** = S  
  **Pedido de venda:** 125  
  O Sistema irá abrir 3 **OPs**, 2 de 50 unidades e 1 de 25 unidades.
* Opção: **Sem LE**Serão geradas as **OPs** conforme a necessidade do documento, sem considerar o lote econômico  
  O Sistema irá abrir apenas uma **OP** correspondente a necessidade**.**
* Opção: **LE Somados**Serão somados as quantidades da quebra, porém será gerada apenas um documento.  
  Exemplo:  
  **Lote econômico** de 50  
  **MV\_QUEBROP** = S  
  **Pedido de venda:** 125  
  O Sistema irá abrir 1 **OP** de 125 unidades.

**Importante**  
Para que as **OPs** e **SCs** sejam quebradas é necessário que o parâmetro **MV\_FORCALM** esteja desativado.  
  
**Glossário  
OP** - Ordem de Produção; **SC** - Solicitação de Compra; **LE** - Lote econômico; **MATA650** - Ordem de Produção;**MATA410** - Pedido de Vendas; **MV\_QUEBROP** - Indica se deve quebrar as ordens de produção em lotes econômicos, ou gerar uma única ordem de produção;**MV\_QUEBRSC** - Indica se deve quebrar as solicitações de compra em lotes econômicos, ou gerar uma única solicitação;  
**MV\_FORCALM** - Força a quebra do valor informado no lote econômico pelo lote mínimo/quantidade atendida.
