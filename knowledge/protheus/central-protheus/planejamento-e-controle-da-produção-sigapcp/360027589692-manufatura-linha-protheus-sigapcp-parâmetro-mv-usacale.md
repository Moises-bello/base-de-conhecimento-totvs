---
article_id: 360027589692
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a15dcc756715e704ad68096af3370782ebee6597246c6642bf738f9b32b22c0d
fetched_at: '2026-06-28T22:42:44.736941+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Parâmetro MV_USACALE
type: support-article
updated_at: '2024-07-02T19:04:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027589692-Manufatura-Linha-Protheus-SIGAPCP-Par%C3%A2metro-MV-USACALE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24593551608343) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Qual a finalidade do parâmetro **MV\_USACALE - Define se no Apontamento de Produção Mod 2 terá o tratamento do calendário na contagem do tempo decorrido. Se Falso considera tempo corrido**?     
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Todas as versões   
  
**Solução**O parâmetro **MV\_USACALE** indica se nas rotinas de apontamento de tempo **MATA680 - Produção PCP MOD 1** e **MATA681 - Produção PCP MOD 2**, para o cálculo do tempo transcorrido, deve ser utilizado o calendário cadastrado no **MATA780 - Cadastro de****Calendários** ou realizar uma subtração simples entre a **data e hora inicial** e **data e hora final**.  
  
O parâmetro **MV\_USACALE** é usado em todas as rotinas que fazem leitura do calendário, como as rotinas de apontamento do **SIGAPCP - Planejamento e Controle da Produção**, **SIGAACD** **- Automação** e **Coleta de Dados** e **SIGAPMS - Gestão de Projetos**.  
  
Exemplo de uso:  
No calendário é definido que o turno de trabalho é das 08h00 até 12h00, retomando as 13h30 até 18h00.  
No apontamento de produção é informada a hora inicial 07h30 e hora final 08h30.

* Se o parâmetro **MV\_USACALE** for **.F.** o Sistema calculará o tempo transcorrido de 01h00, ou seja, das 07h30 às 08h30.
* Se o parâmetro **MV\_USACALE** for **.T.** o Sistema calculará o tempo transcorrido de 00h30, ou seja, das 08h00 às 08h30, pois o turno inicia somente às 08h00. O tempo apontado antes do início do turno é ignorado.
