---
article_id: 12160330114199
category: RH - Dissídio
content_hash: caa871f6c5fd6da9e3cc317f3a5ef6b4ccf43a055d61ff9ba8816c9c914444a7
fetched_at: '2026-06-28T22:43:43.400802+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Na coluna Valor Origem para encargos no dissídio
  o valor é demonstrado a maior quando há cálculo da 2ª parcela
type: support-article
updated_at: '2023-02-03T21:56:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12160330114199-RH-Linha-Protheus-GPE-Na-coluna-Valor-Origem-para-encargos-no-diss%C3%ADdio-o-valor-%C3%A9-demonstrado-a-maior-quando-h%C3%A1-c%C3%A1lculo-da-2%C2%AA-parcela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Na coluna Valor origem na rotina de dissídio, os valores de encargos de INSS empresa, acidente de trabalho e terceiros são demonstrados a maior na folha de dezembro após pagamento da 2ª parcela, deixando a coluna Valor a Pagar negativo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12160255822999)  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Causa**As verbas de encargos estão com SIM no campo Ref 13º.  
  
**Solução**Deixe o campo Ref 13 com Não no cadastro das verbas de encargos de INSS empresa, acidente de trabalho e terceiros, para isso, entre na rotina de **Verbas** pelo caminho **>Atualizações >Definições de cálculos >Verbas**, e na aba **Incidências** deixei o campo com Não:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12160289876503)
