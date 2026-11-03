---
article_id: 4436226330263
category: Materiais - Compras (SIGACOM)
content_hash: fd4a0164bac360632c97be221cdd11beffa2a51e65a1638d48e3904d085f678c
fetched_at: '2026-06-28T22:41:14.567937+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como dar entrada em
  uma nota fiscal recusada quando foi emitida com Faturamento para um cliente de um
  Estado e Remessa para cliente de outro Estado?
type: support-article
updated_at: '2022-02-17T13:11:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4436226330263-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-dar-entrada-em-uma-nota-fiscal-recusada-quando-foi-emitida-com-Faturamento-para-um-cliente-de-um-Estado-e-Remessa-para-cliente-de-outro-Estado
---

**Dúvida**

Como efetuar a entrada de um documento formulário próprio (recusada) de uma nota fiscal de saída que foi emitida para um cliente de um Estado e Remessa de entrega para outro Estado diferente?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões.

**Solução**

Conforme o Exemplo abaixo:NF de saída que foi emitida para um cliente de SP   
Remessa do material faturada para o cliente Entrega BA (Operação Interestadual)

Basicamente nesse caso seguiremos as instruções no documento [Cross Segmento - Backoffice Protheus - SIGACOM - Como realizar uma Devolução de Vendas na rotina de Documento de Entrada ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010638982)

Porém deve ser informado no documento de entrada os campos em vermelho selecionando o cliente que foi faturado a Remessa e informando se foi entregue ou não  mercadoria:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4436168929559/mceclip0.png)

Vincule a nota fiscal de Origem de Faturamento:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4436186062871/mceclip1.png)

E conclua fazendo a transmissão da nota fiscal de entrada (se for o caso formulário próprio = SIM).

**OBS:**

Sem essa amarração ao transmitir é gerado a Rejeição 772: Operação Interestadual e UF destino igual à UF de origem.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)

[SIGACOM - Como realizar uma Devolução de Vendas na rotina de Documento de Entrada ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010638982)

[SIGACOM - Como emitir a Nota de Devolução de Venda quando a Filial da Nota Origem mudou ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416801082007-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-emitir-a-Nota-de-Devolu%C3%A7%C3%A3o-de-Venda-quando-a-Filial-da-Nota-Origem-mudou-?source=search)

[Tratamento dos Campos UF Origem Transporte (F1\_UFORITR), Município Origem Transporte (F1\_MUORITR), UF Destino Transporte (F1\_UFDESTR) e Município Destino Transporte (F1\_MUDESTR)](https://tdn.totvs.com/display/public/PROT/DOC0055+Tratamento+dos+Campos+F1_UFORITR%2C+F1_UFDESTR%2C+F1_MUORITR+e+F1_MUDESTR)
