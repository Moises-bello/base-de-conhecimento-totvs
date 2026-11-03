---
article_id: 9454418408215
category: SIGAEST - MOVIMENTAÇÕES
content_hash: d6edd5a77c286a001c50d522b9dc70157c7a667499e58230e53ad787d83c64f4
fetched_at: '2026-06-28T22:38:58.556833+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAEST - Help: DCHVNFE ao gerar
  documento de entrada pela rotina Transferência entre Filiais (MATA310)'
type: support-article
updated_at: '2022-10-10T18:42:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9454418408215-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAEST-Help-DCHVNFE-ao-gerar-documento-de-entrada-pela-rotina-Transfer%C3%AAncia-entre-Filiais-MATA310
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:54 min** **Dúvida**Help: DCHVNFE ao gerar documento de entrada pela rotina Transferência entre Filiais (MATA310)  
  
**Ambiente**Protheus – Estoque – A partir da versão 12  
  
**Solução**Esse help ocorre devido a validação do parâmetro MV\_DCHVNFE estar ativo na classificação da nota de entrada, no qual exige o preenchimento obrigatorio do campo **chave NFE** na aba "Informações DANFE" quando o campo Form. Prop. é **NÃO** e Espec. Docum. é preenchido como **SPED.**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9454298128535)**

A rotina Transferência entre filiais (MATA310) tem objetivo de gerar a nota fiscal de saida na filial origem, e dar entrada na filial destino. Porém essa saida realizada na filial de origem não é transmitida ao governo de forma automatica, então quando existe o uso do parametro MV\_DCHVNFE, não será possivel gerar uma nota fiscal de entrada classificada na filial de destino.

Neste caso, na rotina transferência entre filiais ajuste o parâmetro "**Gera documento de entrada**" de "**Classificado**" para "**A Classificar**".

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9454239986327)

Desta forma, o sistema irá gerar uma pré-nota, onde será possivel classificar após o recebimento da nota fiscal emitida pela filial origem contendo a **chave NFe**.

Outra alternativa de contorno é gerar um documento de entrada utilizando uma especie diferente de SPED, pois neste caso o parâmetro MV\_DCHVNFE não fará a validação da chave Nfe.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9454417297431)

***Saiba Mais:***

* [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310 / MATA311 - Como configurar a Transferência entre Filiais (MATA310 / MATA311) no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-a-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus-)
