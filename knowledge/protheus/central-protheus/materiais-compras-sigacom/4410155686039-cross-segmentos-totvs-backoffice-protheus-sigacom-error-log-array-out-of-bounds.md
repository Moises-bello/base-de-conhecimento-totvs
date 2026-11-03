---
article_id: 4410155686039
category: Materiais - Compras (SIGACOM)
content_hash: a225941ebec983e88db6d2ff578282c4fc1b003a282340f9951f4a82b37c51fd
fetched_at: '2026-06-28T22:41:17.651854+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Error log: array out
  of bounds  on A103TEMBLQ ( MATA103.PRW ) no Documento de Entrada'
type: support-article
updated_at: '2021-10-13T19:03:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410155686039-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Error-log-array-out-of-bounds-on-A103TEMBLQ-MATA103-PRW-no-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 01:00 **Dúvida**

Ocorrência  do errolog: array out of bounds ( 0 of 227 )  on A103TEMBLQ(MATA103.PRW)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões

**Solução**

Uma possibilidade existente para a ocorrência deste erro se trata da situação abaixo em que os campos indicados não estão como "Usado" no Dicionário de Dados do ambiente em questão:

Dessa forma, acesse o módulo configurador e marque os campos mencionados abaixo como usado:

**"D1\_SERIE"**  
**"D1\_FORNECE"**  
**"D1\_LOJA"**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410156059415/mceclip0.png)

Recomenda-se também estar com o pacote de Expedição Continua de Compras mais atual no ambiente em estão sempre aplicando primeiramente me ambiente de homologação:   
  
COM: [Pacotes de Atualização - Compras](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)  
LIB Atual - <https://suporte.totvs.com/portal/p/10098/download?e=989259>

***Saiba Mais :***

[PÁGINA CENTRALIZADORA DO](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS) [COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
