---
article_id: 9064245850519
category: Gestão de Transportes (TMS)
content_hash: eba1bc2109de412adc83c667c342caf4be0e9d8c1d29741e81a757f43719ae0b
fetched_at: '2026-06-28T22:45:29.291025+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Help TMSAF6415
type: support-article
updated_at: '2022-09-26T19:45:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9064245850519-Log%C3%ADstica-Linha-Protheus-TMS-Help-TMSAF6415
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como resolver o alerta **TMSAF6415 - Viagem não poderá ser excluída pois existem lotes vinculados a ela**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O help **TMSAF6415** ocorre na validação do conteúdo presente no campo **DTP\_VIAGEM**, onde o Sistema informa a seguinte mensagem: **Viagem não poderá ser excluída pois existem lotes vinculados a ela.**Este *Help* é apresentado pois em seu ambiente há algum lote **Tabela DTP** que possui o campo **DTP\_VIAGEM** preenchido com a viagem em questão.  
Este é um lote vazio vinculado à viagem ou este lote do documento que está vinculado à viagem através do campo **DTP\_VIAGEM** e não está carregado nela.  
Verifique se este lote não está vinculado à viagem pelo campo **DTP\_VIAGEM**. O ideal é desvincular o documento deste lote da viagem ou excluir o lote caso ele não esteja vinculado à nenhum documento para que possa realizar a exclusão da viagem.
