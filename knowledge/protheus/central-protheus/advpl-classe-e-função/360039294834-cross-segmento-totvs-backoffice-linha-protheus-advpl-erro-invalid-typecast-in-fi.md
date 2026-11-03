---
article_id: 360039294834
category: ADVPL - Classe e Função
content_hash: fbd9c52d3e51df9a27ca666f49a69a3ad6a22df795e54d303a41031d9cc9fd09
fetched_at: '2026-06-28T22:40:15.812320+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro invalid typecast
  in file ao executar SIGARPM
type: support-article
updated_at: '2021-12-30T18:47:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039294834-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-invalid-typecast-in-file-ao-executar-SIGARPM
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min** **Ocorrência**

THREAD ERROR ([XXXXX], usuario, maquinaXXX)

invalid typecast in file d:\bamboo-agent-5.7.2\xml-data\build-dir\tp11-tecx17v3-tecxwin64\advpl\instrvar.inl at line 932

on SENDPRTINFO(APLIB080.PRW) 18/11/2019 18:56:02 line : 3112

**Ambiente**Protheus –  ADVPL – A partir da versão 12.1.25  
  
**Causa**Erro ocorre devido a um parâmetro **MV\_CANSALT** esta como do tipo data e conteúdo logico

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052626413/mceclip0.png)  
  
**Solução**

Neste caso é necessário alterar o parâmetro **MV\_CANSALT** para tipo Logico e conteúdo logico

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052626813/mceclip1.png)

**Saiba Mais**

[Invalid typecast in file XYZ on SENDPRTINFO](https://tdn.totvs.com/display/PROT/Invalid+typecast+in+file+XYZ+on+SENDPRTINFO)
