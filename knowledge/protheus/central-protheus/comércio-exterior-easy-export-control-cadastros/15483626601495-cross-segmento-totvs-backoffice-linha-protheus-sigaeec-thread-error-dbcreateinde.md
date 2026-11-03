---
article_id: 15483626601495
category: Comércio Exterior - Easy Export Control - Cadastros
content_hash: e00585bc3448c5b4c51c74076236d7dc68b9798a4765a995eab45ee330f692d7
fetched_at: '2026-06-28T22:36:57.381501+00:00'
product: protheus
section_id: 1500001549302
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus  - SIGAEEC - Thread error
  DBCreateIndex - Create index file error - dbo##  on INDREGUA(MSLIB.PRW)
type: support-article
updated_at: '2023-06-21T20:00:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15483626601495-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Thread-error-DBCreateIndex-Create-index-file-error-dbo-on-INDREGUA-MSLIB-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15484373666967)Tempo aproximado para leitura:**00:02:00 min****Dúvida**Ao tentar incluir um registro na EECAC100/EECAC115 disparado erro no campo EE3\_SEQ, como resolver ?  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – A partir da 12.1.33.  
  
**Solução** Para solucionar o erro "*Thread error DBCreateIndex - Create index file error - dbo## on INDREGUA***(MSLIB.PRW)**" ao tentar incluir um novo registro na rotina EECAC100/EECAC115, verifique se o campo EE3\_SEQ está selecionado como usado, browse e todos os módulos no configurador:

1. Acesse o módulo SIGACFG em Base de Dados, selecione Dicionário / Base de dados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15484357687063)

2. Selecione Dicionário de Dados

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15484373673111)

3. Selecione a lupa

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15484357691415)

4. Selecione Procurar Por e informe a tabela EE3, após selecione Buscar. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15484356751383)

5. Posicione no campo EE3\_SEQ e selecione a folha com o lápis

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15484167530007)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15484204718743)

6. Na Aba **Uso,** marque o campo como **Usado e Browse**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15484246709655)

7. Na Aba **Módulos** , marque o campo como **Utilizado para todos os módulos**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15484373680919)
