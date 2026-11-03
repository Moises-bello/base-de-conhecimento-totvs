---
article_id: 8864282518935
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 42e829389bd50d43bef6cc607c68db6ef9f859dc5282852e62beaae0addcae3a
fetched_at: '2026-06-28T22:42:08.930578+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 020 da DAPIMG?
type: support-article
updated_at: '2022-09-14T12:02:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8864282518935-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-020-da-DAPIMG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **linha 020** da **DAPIMG**?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) -Livros Fiscais – A partir da versão 12  
  
**Solução**

A linha **20 - Comunicação** da **DAPI MG** é gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Entradas** com algumas **CFOPs** específicas.

Para que o valor de um documento fiscal componha os valores da **Linha 20**, no campo **Cod. Fiscal - D1\_CF** do lançamento deve conter uma das seguintes **CFOPs**:1301/1302/1303/1304/1305/1306.
