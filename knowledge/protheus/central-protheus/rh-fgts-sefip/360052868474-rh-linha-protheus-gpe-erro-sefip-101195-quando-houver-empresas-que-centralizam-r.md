---
article_id: 360052868474
category: RH - FGTS / SEFIP
content_hash: 4e070fa725309eb9db2a4f5b481a8185ffeda863d336637470a3f39a6bd484f0
fetched_at: '2026-06-28T22:43:41.267054+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Erro SEFIP 101195 -Quando houver empresas que centralizam
  recolhimento, indicador A ou P de alteração cadastral do CNAE preponderante deverá
  ser informado para um único estabelecimento de empresa
type: support-article
updated_at: '2025-08-14T17:38:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052868474-RH-Linha-Protheus-GPE-Erro-SEFIP-101195-Quando-houver-empresas-que-centralizam-recolhimento-indicador-A-ou-P-de-altera%C3%A7%C3%A3o-cadastral-do-CNAE-preponderante-dever%C3%A1-ser-informado-para-um-%C3%BAnico-estabelecimento-de-empresa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34185468211735)** Tempo aproximado para leitura: **00:01:30 min**  
**Ocorrência****pprotheus\_redu101195** - quando houver empresas que centraliza recolhimento o indicador A ou P de alteração cadastral co CNAE preponderante deverá ser informado para um único estabelecimento da empresa  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Esse erro ocorre pois nos parâmetros para a geração do SEFIP, o campo **Indicador Alt. CNAE estava preenchido como não altera.**

**Solução**

Veja as opções para gerar o arquivo diferente de "A" ou "P", corrigindo assim o erro apresentado.

![](https://totvssuporte.zendesk.com/attachments/token/Lb6fYdm0A2m1F2kVxRIXGDJX5/?name=inline819250036.png)​  
  
"S" Altera o CNAE  
"N" Não Alt. CNAE  
"A" Alt. CNAE Prep.  
"P" Não Alt. Prep. 

**Saiba Mais:   
[FGTS](https://tdn.totvs.com/display/public/PROT/FGTS)**
