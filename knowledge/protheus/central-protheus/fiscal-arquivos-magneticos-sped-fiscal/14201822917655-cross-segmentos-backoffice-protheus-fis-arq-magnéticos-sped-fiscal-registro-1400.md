---
article_id: 14201822917655
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: f9466ceec30494bc1664af1e3ba4f58bf0a7d93aad96f65a7fc39d627194e3f7
fetched_at: '2026-06-28T22:42:02.390163+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED Fiscal
  - Registro 1400 gerado indevidamente no Sped Fiscal
type: support-article
updated_at: '2023-04-27T19:49:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14201822917655-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-Fiscal-Registro-1400-gerado-indevidamente-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02:00 min****Ocorrência**Ao gerar o arquivo txt do **Sped Fiscal** sem informar o código **IPM** no cadastro de **TES** está sendo gerado, indevidamente, o registro **1400 - Informação sobre valores agregados**  no arquivo.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois a parametrização do sistema está incorreta no cadastro de **TES** utilizado na escrituração dos documentos com dados gerados indevidamente.  
  
**Solução**O problema está ocorrendo devido a configuração do campo **Agr. Vlr. Mun -** **F4\_VLAGREG**. Quando este incidente ocorre, o campo se encontra como **S = Soma**Com esta configuração, o registro **1400** é gerado sem o **código IPM**, mas com o produto utilizado na escrituração.

   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14201708738967)  
   
No padrão, o campo **Agr. Vlr. Mun.** (Valores agregados por Município -**F4\_VLAGREG**) é Branco, conforme abaixo:  
 ![](https://totvssuporte.zendesk.com/attachments/token/SWvA08SYGG98x6US07pbOWzfS/?name=image.png)  
  
Para que o erro não ocorra, altere essa informação nos cadastro de **TES** em que o campo está como **S** e  gere novamente o **Sped Fiscal.**
