---
article_id: 360020387892
category: ADVPL - Classe e Função
content_hash: 59491baa86373a135eb5451d59db34d31fb1ae46cb7110b35fcfe615206e1f9c
fetched_at: '2026-06-28T22:40:15.462519+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Classe TSimpleEditor
  metodo SaveToPDF
type: support-article
updated_at: '2022-01-04T20:58:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020387892-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-TSimpleEditor-metodo-SaveToPDF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**  
THREAD ERROR (XXXX, XXXXXX, XXXXXX) XX/XX/XX XX:XX:XX  
Cannot find method TSIMPLEEDITOR:SAVETOPDF on U\_TSTTPDF(TSTTPDF.PRW)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**O erro ocorre pois a classe ainda não esta disponível no binário atual.

**Solução**De acordo com a documentação disponível no Tdn a Classe [TSimpleEditor:SaveToPDF](http://tdn.totvs.com/display/tec/TSimpleEditor%3ASaveToPDF)

```
Abrangência  
Disponível somente em builds superiores à 7.00.131227A.
```
