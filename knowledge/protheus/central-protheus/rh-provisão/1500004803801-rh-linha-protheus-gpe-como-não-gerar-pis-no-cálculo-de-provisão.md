---
article_id: 1500004803801
category: RH - Provisão
content_hash: ed58bc0f4101552c98b6fb6ec244dd7a904918c267a2fcb3ec42d4b8138ffbf3
fetched_at: '2026-06-28T22:43:55.828810+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como não gerar PIS no cálculo de provisão
type: support-article
updated_at: '2025-09-23T12:18:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004803801-RH-Linha-Protheus-GPE-Como-n%C3%A3o-gerar-PIS-no-c%C3%A1lculo-de-provis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32904661661719)** Tempo aproximado para leitura: **00:00:30 min**

**Dúvida**Como não gerar PIS no cálculo de provisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Quando no Cálculo das Provisões o Protheus apresenta verbas referentes ao PIS, existe percentual configurado na verba com o ID de Cálculo 0229-PIS Empresa.  
  
Se a empresa não realiza recolhimento de PIS, será necessário realizar os procedimentos abaixo:  
  
1 - Acesse Atualização / Definição de Cálculo / Verbas e localize o cadastro da verba com Identificador de Cálculo **0229;**

2 - Verifique se a verba tem o campo **Percentual (RV\_PERC)** preenchido e deixe o conteúdo com zero;

3 - Verifique se há outras verbas com o campo **PIS (RV\_PIS)** preenchidos com Sim e altere para Não;

3 - Após salvar as alterações nos cadastros das verbas, exclua o cálculo das Provisões, e calcule novamente.

**Saiba Mais:**[RH-Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
