---
article_id: 360060836993
category: Inspeção de Entradas (SIGAQIE)
content_hash: 593aa6b2dc75fb5eb1c3642ef2c857b8fb826b7d118f5f56d3cbe97eb0f530e1
fetched_at: '2026-06-28T22:42:27.078114+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAQIE - Mensagem: SIGAQIE - O campo QEK_LOTE
  - Lote, deve ter o tamanho igual ao campo D1_LOTECTL - Lote + D1_NUMLOTE - Sub-lote'
type: support-article
updated_at: '2023-11-13T12:17:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060836993-Manufatura-Linha-Protheus-SIGAQIE-Mensagem-SIGAQIE-O-campo-QEK-LOTE-Lote-deve-ter-o-tamanho-igual-ao-campo-D1-LOTECTL-Lote-D1-NUMLOTE-Sub-lote
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18958051827351)***Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Ao realizar entrada de documento na rotina **MATA103 - Documento de Entrada**, ocorre a mensagem **SIGAQIE - Ocorrência na Integração: O campo QEK\_LOTE - Lote, deve ter o tamanho igual ao campo D1\_LOTECTL - Lote + D1\_NUMLOTE - Sub-lote. Favor efetuar o ajuste do grupo de campo 069, conforme procedimentos descritos em Boletim Técnico.**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**Esta ocorrência é ocasionada pela divergência de tamanho do campo **QEK\_LOTE** em relação a soma de tamanho dos campos **D1\_LOTECTL** e **D1\_NUMLOTE**.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

* Acesse o **SIGACFG - Configurador**
* Visualize o tamanho dos campos **D1\_LOTECTL** e do campo **D1\_NUMLOTE**.
* Ajuste o tamanho do campo **QEK\_LOTE** para ser igual a soma do tamanho dos campos **D1\_LOTECTL** e **D1\_NUMLOTE**.
