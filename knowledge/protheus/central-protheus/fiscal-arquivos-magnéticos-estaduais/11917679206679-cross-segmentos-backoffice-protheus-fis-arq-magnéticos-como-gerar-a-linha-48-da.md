---
article_id: 11917679206679
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: deabf3aff67694e3bf978e7ec1f4131543eadc396f44113c46f8f004e8fae1bb
fetched_at: '2026-06-28T22:42:09.042066+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 48 da DAPI?
type: support-article
updated_at: '2023-01-25T12:45:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11917679206679-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-48-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **linha** **48 - Comunicação** da DAPI?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **L****inha** **48 - Comunicação** é  gerada com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** com algumas **CFOPs** específicas.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 48**, no campo **Cod. Fiscal - D2\_CF** do lançamento deve conter uma das seguintes **CFOPs**:

**5301/5302/5303/5304/5305/5306/5307**
