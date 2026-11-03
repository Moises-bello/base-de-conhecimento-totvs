---
article_id: 36280320922391
category: Financeiro - Contas a Pagar - Comunicação Bancária Online
content_hash: cfb3cec07bd411f4d8350423f73bf0c37ee301ccab73c014b68341723ae6c318
fetched_at: '2026-06-28T22:37:49.924787+00:00'
product: protheus
section_id: 26656222001687
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA717 -Número da
  requisição de API já foi utilizado anteriormente
type: support-article
updated_at: '2025-11-12T17:45:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36280320922391-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA717-N%C3%BAmero-da-requisi%C3%A7%C3%A3o-de-API-j%C3%A1-foi-utilizado-anteriormente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36280320916503) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33.  
  
**Solução**  
A mensagem exibida está relacionada ao campo **numeroRequisicao**.  
Ela indica que já foram enviadas requisições ao banco para a respectiva conta, sendo que os números são gerados de forma sequencial, incrementando uma unidade a cada nova requisição.

Neste caso, é necessário verificar junto ao banco qual foi o **último número de requisição** transmitido e realizar o ajuste no **cadastro de parâmetros de bancos (FINA130 → Aba: Outros)**, para a **subconta** utilizada no momento da geração do **Borderô (FINA240)**.

Atualize o campo **EE\_IDTRANS – Número da Requisição** com o próximo número disponível informado pelo banco ou, alternativamente, incremente manualmente a numeração e retransmita o título até que o status **“Em Processamento”** seja apresentado.

**Observação:** se a conta for de **homologação**, ela poderá ser **compartilhada entre vários clientes**, o que pode gerar conflitos na sequência de numeração.

**Saiba mais**

[Financeiro (SIGAFIN)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001545422-Financeiro-SIGAFIN)
