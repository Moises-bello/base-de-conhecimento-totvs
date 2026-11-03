---
article_id: 1500004782221
category: RH – DIRF
content_hash: 556730cbe88e433857b8029bce87874e558497afa8f786a5139c75904146d63a
fetched_at: '2026-06-28T22:44:07.837725+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Valores indevidos sendo gerados na DIRF
type: support-article
updated_at: '2025-08-20T11:13:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004782221-RH-Linha-Protheus-GPE-Valores-indevidos-sendo-gerados-na-DIRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34312590751383)** Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Valores indevidos sendo gerados na DIRF.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Causa**  
Campo Gerar CPMF preenchido com SIM na geração da DIRF  
  
**Solução**O campo **Gerar CPMF** nos parâmetros de Gerar Arquivo (GPEM550) deve estar configurado com **NÃO**, pois se este campo estiver com SIM será calculado valores indevidos para a DIRF.  
  
Para ajuste, entre na rotina **Gerar Arquivo** pelo caminho **>Miscelânea >Dirf >Gerar Arquivo** e gere novamente os dados da DIRF cm a pergunta com Não:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006610461)

**Saiba Mais**  
[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
