---
article_id: 360022840892
category: Financeiro - Viagens
content_hash: 59d50ad56880cd5f96f678918a7600deda1dca535353b97797827c0e25188ca5
fetched_at: '2026-06-28T22:38:21.227805+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  Alteração de adiantamento
  de viagem exibe o help FIXVALDTPC
type: support-article
updated_at: '2022-08-18T00:28:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022840892-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Altera%C3%A7%C3%A3o-de-adiantamento-de-viagem-exibe-o-help-FIXVALDTPC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**No módulo Financeiro, na rotina de Adiantamentos de viagens, ao alterar um adiantamento é exibido o HELP **FIXVALDTPC - O Participante possui pendências na prestação de contas.**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**   
Esse incidente ocorre, quando o participante do adiantamento possui uma ou mais prestações em atraso. Deste modo o sistema bloqueia o adiantamento até que seja finalizada a prestação de contas anterior.

**Importante**Os parâmetros **MV\_RESPCAT** e**MV\_RESQTPC**, determinam em que momento o bloqueio ocorrerá, conforme abaixo:  
**MV\_RESPCAT** - Define a quantidade máxima de dias que a prestação de contas pode ficar em aberto após o termino da viagem.  
**MV\_RESQTPC** - Define a quantidade máxima de prestações de contas em aberto por participante.

**Para maiores informações sobre o desbloqueio do adiantamento de viagem, consulte: [Adiantamento de viagem bloqueado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023083091-MP-SIGAFIN-ADIANTAMENTO-DE-VIAGEM-COM-STATUS-BLOQUEADO)**
