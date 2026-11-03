---
article_id: 360024025292
category: ADVPL - Ponto de Entrada
content_hash: a8e08d2c268462097c89b2a51047ea17036b993e199c059bab1879781e30303f
fetched_at: '2026-06-28T22:40:11.843196+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  M460MARK não funciona na rotina de faturamento de carga.
type: support-article
updated_at: '2021-12-29T19:40:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024025292-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-M460MARK-n%C3%A3o-funciona-na-rotina-de-faturamento-de-carga
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**O PE M460MARK trazia a marca da tabela DAK\_OK (quando no modulo OMS) e agora só traz o que foi gravado na rotina SC9, houve alguma mudança?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa** Em setembro do ano passado removemos do fonte MATA461 as regras relacionadas ao faturamento por carga e transferimos para um fonte nosso, com objetivo de componentizar as funcionalidades e facilitar a manutenção dessas regras por parte da equipe do OMS.

Isso acabou gerando um impacto na informação que é enviada como parâmetro para o ponto de entrada M460MARK.  
  
**Solução**A partir de agora é necessário trabalhar com base na tabela de Pedidos Liberados (SC9). Ela contém a informação da carga gravada no campo C9\_CARGA e todos os registros relacionados à carga selecionada para faturamento estarão com o C9\_OK preenchido.

Na rotina Faturamento por carga o PE M460MARK grava primeiro na DAK\_OK e depois na C9\_OK

A partir de agora não teremos mais mudanças nesse sentido para o ponto de entrada M460MARK.
