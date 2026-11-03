---
article_id: 360018740331
category: Escrita Fiscal - Error.log
content_hash: f5aaa6df097310c0fcf6cdcc853c8fe6edef9cf040d1311cf2cfd4fbe94004bf
fetched_at: '2026-06-28T22:39:32.905027+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: MP - FIS - CONTABILIZAÇÃO ATRAVÉS DAS ROTINAS NOTA FISCAL MANUAL DE ENTRADA
  E SAÍDA
type: support-article
updated_at: '2021-04-28T15:44:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018740331-MP-FIS-CONTABILIZA%C3%87%C3%83O-ATRAV%C3%89S-DAS-ROTINAS-NOTA-FISCAL-MANUAL-DE-ENTRADA-E-SA%C3%8DDA
---

**Dúvida**Como realizar a contabilização através das rotinas de NF Manual de Entrada (MATA910) e NF Manual de Saída (MATA920)?

**Ambiente**Protheus - Livros Fiscais - A partir da versão 11.80

**Solução**

Para contabilizar os lançamentos através da rotina MATA910 ou MATA920, utilize os **Lançamentos Padrões 6A7 e 6B7**. Estes códigos apenas permitirão a contabilização offline.

Obs.: Estes códigos substituem o LP anterior **607 \***.

1)      Acesse a rotina CTBA080 -  Lançamento Padrão.

![](http://tdn.totvs.com/download/attachments/164004469/image2014-9-26%2017%3A46%3A52.png?version=1&modificationDate=1411764490000&api=v2)

Selecione o **LP 6A7**com a descrição "NF.Manual de Entrada - itens" e o **LP 6B7** com a descrição "NF.Manual de Saída - itens"

Configure as demais informações sobre conta débito/conta crédito, valores, histórico, etc.

Sugestão para Valores:

SD1->D1\_TOTAL (para entradas)

SD2->D2\_TOTAL ou SFT->FT\_TOTAL (para saídas)

2)      Após realizar o cadastro, acesse a rotina MATA910 – NF Manual Entrada ou MATA920 – NF Manual Saída e realize as movimentações.

3)  ***Configuração de Histórico:***

Para trazer o histórico correto utilize a função POSICIONE conforme exemplo abaixo:  
  
SD2->D2\_DOC+"  "+POSICIONE('SA1',1,xFilial('SA1')+SD2->D2\_CLIENTE+SD2->D2\_LOJA,'A1\_NOME')       

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059189813/mceclip0.png)      
  
  
<https://tdn.totvs.com/pages/viewpage.action?pageId=25165872>  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/0zmFQkQiPGAtUkVwHuClfFtSV/?name=inline-58872915.png)

4)      Acesse a rotina **MATA997 (Contabilização)** para processar os lançamentos contábeis gerados a partir das rotinas de Nf Manual Entrada e/ou Saída. Informe os parâmetros de acordo com a necessidade.

![](http://tdn.totvs.com/download/attachments/164004469/image2014-9-26%2017%3A46%3A44.png?version=1&modificationDate=1411764490000&api=v2)

Após realizar o processamento, confirme os lançamentos apresentados no grid.

**Importante:**

Para versão 12.1.17 ou superior, foram incluídas perguntas conforme abaixo nos parâmetros da rotina **MATA997 (Contabilização)**para definir os códigos de entrada e saída, caso não sejam preenchidos serão considerados padrões:

**6A7** - Documento de Entrada Manual - Inclusão de Documento Itens

**6B7** - Documento de Saída Manual - Inclusão de Documento Itens

![](http://tdn.totvs.com/download/attachments/164004469/image2018-5-18_18-22-14.png?version=1&modificationDate=1526678536000&api=v2)

**Importante**

1) Caso a nomenclatura do LP 607 esteja como "Apuração de PIS-Estorno", ela precisa ser alterada, pois esta operação é feita pelo LP 611. Por este motivo, acesse a rotina CTBA085 – Pontos de Lançamento e altere a descrição destes dois códigos.

Por exemplo:

607 – NF Manual Entr./Saída (leitura de registros pela tab.SF3)

611 – Apuração de PIS-Estorno

Obs.: Caso o 611 não exista em seu ambiente, ele poderá ser criado nesta mesma rotina.

2) Caso sejam criados os LPs 6A7 e 6B7, também altere a situação do LP 607 para 'inativo', na rotina CTBA080 -  Lançamento Padrão.

<http://tdn.totvs.com/pages/releaseview.action?pageId=164004469>
