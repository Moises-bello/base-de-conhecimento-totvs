---
article_id: 8998298766359
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 35d20cc24a04733986244d93043b49f628354622b53b63e6af5735e24f6eaeea
fetched_at: '2026-06-28T22:42:00.992537+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Registro 1100
  não gerado no Sped Fiscal
type: support-article
updated_at: '2022-09-20T12:13:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8998298766359-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Registro-1100-n%C3%A3o-gerado-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min****Ocorrência**Ao emitir uma nota de **exportação** via **Faturamento** e gerar o **Sped Fiscal** não á apresentado o registro **1100.**  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) -Livros Fiscais – A partir da versão 12  
  
**Causa**Esse incidente ocorre, pois falta informação nos **Complementos da Nota Fiscal**.   
  
**Solução**Acesse os **Complementos da Nota Fiscal** e verifique se  o campo **Data de Averbação - CDL\_DTAVB** está preenchido para as Notas Fiscais que não geraram o registro **1100**.  
  
O Protheus leva em consideração este campo como principal com relação as datas para geração do **1100.**Caso o campo não esteja preenchido, proceda com o preenchimento seguindo o caminho abaixo:

**Caminho:**

**Livros Fiscais >> Atualizações  >> Movimentos >> NF manual de saída >> Outras ações >> Complementos >> Exportações.**

Após, gere o arquivo txt do **Sped Fiscal**, valide se a pergunta **Gera Registro 1100 - Exportação** está como **SIM**

**![](https://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2014%3A4%3A20.png?version=1&modificationDate=1465142308000&api=v2)**
