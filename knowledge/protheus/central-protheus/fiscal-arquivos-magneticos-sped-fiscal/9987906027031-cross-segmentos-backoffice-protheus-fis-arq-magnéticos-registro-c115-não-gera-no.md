---
article_id: 9987906027031
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: a0c04214ea79f54bd8a79698bc1b90369e33e7ce538b2f5cbcc1f96244dc3338
fetched_at: '2026-06-28T22:42:00.995689+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Registro C115
  não gera no Sped Fiscal
type: support-article
updated_at: '2022-11-03T18:49:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9987906027031-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Registro-C115-n%C3%A3o-gera-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min****Ocorrência**Ao gerar o arquivo texto referente ao **Sped Fiscal**, o registro **C115 - Local da Coleta e/ou entrega** não é apresentado.  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**Esse incidente ocorre, pois a configuração do sistema está incorreta para a **Espécie** da Nota Fiscal utilizada na escrituração.  
  
**Solução**Escriture a NF de saída informando **Espécie** **NFE ou NF (modelo 01)**. Notas escrituradas como **SPED** são consideradas como **modelo 55** e dessa forma **não** geram o registro **C115**, ainda que sejam seguidas as demais orientações do link abaixo. 

[MP-FIS-SPED-FISCAL-Registro-C115-Local-da-Coleta-e-ou-entrega](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010161372-MP-FIS-SPED-FISCAL-Registro-C115-Local-da-Coleta-e-ou-entrega)

Isso ocorre devido a regra fiscal do **Guia Prático do Sped Fiscal** que determina quais modelos de nota devem gerar o registro.
