---
article_id: 360007549351
category: Gestão de Transportes (TMS)
content_hash: fb978c9e2e4c12b13c5ba76dc59b71d3d2179f82761cc58b8cf9105ed3491a94
fetched_at: '2026-06-28T22:45:32.178758+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM250BCO Customização nos
  Campos do Banco
type: support-article
updated_at: '2022-09-13T11:55:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007549351-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM250BCO-Customiza%C3%A7%C3%A3o-nos-Campos-do-Banco
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:10 min  
  
Dúvida**Como implementar o ponto de entrada **TM250BCO** - Customização nos Campos do Banco?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM250BCO** se encontra na rotina **TMSA250 - Contrato de Carreteiro**, e tem como objetivo definir os campos do **Banco**, **Agência** e **Conta** na rotina de **Pagamento de Saldo**, além de permitir digitar os dados ou apenas visualizá-los. Este somente será considerado se o retorno for um vetor contendo 5 posições com as seguintes variáveis de controle: **cBanco**, **cAgencia**, **cConta**, **lAltera** (onde **lAltera**, variável lógica para definir se os campos serão alterados) e **cCheque**.  
  
**Anexo**Exemplo do ponto de entrada **TM250BCO:**
