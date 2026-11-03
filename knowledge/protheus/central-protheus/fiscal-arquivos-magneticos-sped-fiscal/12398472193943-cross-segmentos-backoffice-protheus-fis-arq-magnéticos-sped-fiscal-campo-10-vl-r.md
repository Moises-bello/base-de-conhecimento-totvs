---
article_id: 12398472193943
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 2c28c16289602be513862c5000b05257ab48be7b09d0dbe2ccdd42c1cbb9d799
fetched_at: '2026-06-28T22:42:01.126148+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED Fiscal
  - Campo 10, VL_RED_BC, do C190 com centavos de diferença
type: support-article
updated_at: '2023-02-14T13:39:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12398472193943-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-Fiscal-Campo-10-VL-RED-BC-do-C190-com-centavos-de-diferen%C3%A7a
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar o Sped Fiscal, o campo **10 - VL\_RED\_BC** é apresentado com centavos de diferença em relação ao valor do documento fiscal.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**Esse incidente ocorre, devido a parametrização incorreta do sistema, quanto à qual tabela deve ser considerada para cálculo da redução.   
  
**Solução**Altere o conteúdo do parâmetro **MV\_NRPRBIC,** para que o Protheus altere a tratativa com relação ao cálculo da redução de base de cálculo de acordo com os dados da tabela **SFT - Livro Fiscal do Item por NF** ou **CD2  - Livro Digital de Impostos.**
