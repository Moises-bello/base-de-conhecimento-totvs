---
article_id: 24798570091927
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 1a691396db57a962ec3ad6a5d709ee35c85f7c690ae06ee9ae43ad37263c1337
fetched_at: '2026-06-28T22:38:45.339099+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Erro "tipo inconsistência
  em MV_PAR21 usando SetMVValue on SETMVVARS" ao faturar
type: support-article
updated_at: '2024-07-10T21:05:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24798570091927-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Erro-tipo-inconsist%C3%AAncia-em-MV-PAR21-usando-SetMVValue-on-SETMVVARS-ao-faturar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24798607546775) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como resolver o erro "tipo inconsistência em MV\_PAR21 usando SetMVValue on SETMVVARS"?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**Verifique se não há perguntas duplicadas com valores inválidos na tabela "SXK - Controle de perguntes por usuário":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24798570045335)

* XK\_GRUPO = Grupo de perguntes (SX1 - Perguntes)
* XK\_SEQ = Posição do pergunte dentro de seu grupo de pergunte (XK\_GRUPO)
* XK\_IDUSER = Usuário afetado
* XK\_CONTEUD = Conteúdo que ficará no pergunte
* XK\_FORM = Fórmula customizada

Dúvidas em como visualizar pelo configurar a tela de "Controle de perguntes por usuário" orientamos que contate a Equipe Protheus Framework!
