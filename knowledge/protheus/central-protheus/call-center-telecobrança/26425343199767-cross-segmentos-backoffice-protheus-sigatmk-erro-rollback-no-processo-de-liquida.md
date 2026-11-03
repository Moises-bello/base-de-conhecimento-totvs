---
article_id: 26425343199767
category: Call Center - Telecobrança
content_hash: 886a06d1adf84644eff50d73716828ef6723539e1b5cd709044d76ad2b101916
fetched_at: '2026-06-28T22:41:28.716152+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Erro Rollback no processo
  de Liquidação / Renegociação no processo de Telecobrança
type: support-article
updated_at: '2024-09-17T13:50:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26425343199767-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Erro-Rollback-no-processo-de-Liquida%C3%A7%C3%A3o-Renegocia%C3%A7%C3%A3o-no-processo-de-Telecobran%C3%A7a
---

*****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26425343185943)*** Tempo aproximado para leitura: 00:02:00 min****Dúvida**Qual o motivo do erro de Rollback de Renegociação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center - a partir da versões.  
  
**Solução**Como solucionar o erro abaixo (RollBack) no processo de renegociação do Call Center?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26425351682455)

No processo padrão de renegociação do Call Center deve ser realizado o preenchimento dos seguintes parâmetros, para finalização e geração da renegociação dos títulos.

MV\_TMKNTCB - Definir a natureza que será utilizada na liquidação do título através do parâmetro.

MV\_TMKPRTR - Definir o prefixo utilizado nos títulos gerados pela liquidação através do parâmetro. Caso não seja definido, o padrão será REN

MV\_TMKTPTR - Definir o tipo utilizado nos títulos gerados pela liquidação através do parâmetro. Caso não seja definido, o padrão será BOL.

Sendo que o erro de Rollback pode ocorrer por algum tipo de inconsistência no processo, neste caso, tratava-se de um conteúdo indevido no parâmetro **MV\_TMKNTCB.** Então é importante se certificar que o conteúdo seja válido para concluir o processo.

**Saiba mais:  
[Liquidação/Renegociação no Telecobranças (SIGATMK)](https://tdn.totvs.com/x/cfQJE)**
