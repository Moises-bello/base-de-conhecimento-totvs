---
article_id: 7408549780631
category: Faturamento - Cadastros
content_hash: fb743e73e4e250d1785519f0fabaf852724d3b70507cebf454695c998acae449
fetched_at: '2026-06-28T22:38:36.499903+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAFAT - Lista de Pontos de
  Entrada da rotina de Cadastro de Clientes (MATA030)
type: support-article
updated_at: '2022-07-13T12:55:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7408549780631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFAT-Lista-de-Pontos-de-Entrada-da-rotina-de-Cadastro-de-Clientes-MATA030
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:25 min** **Dúvida**Quais os pontos de entrada existentes na rotina Cadastro de Clientes (MATA030)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Faturamento (SIGAFAT) - A partir da versão 12.  
  
**Solução**

Segue a abaixo a lista dos pontos de entrada da rotina e suas documentações no TDN:

* [DT\_PE\_MT030INT - Permite a alteração do cadastro de cliente para registros gerados via integração](https://tdn.totvs.com/pages/viewpage.action?pageId=236421731)
* [M030SAO - Exclusão de dados](https://tdn.totvs.com/pages/viewpage.action?pageId=6784137)
* [MA030DBT - Remover botões de Outras Ações](https://tdn.totvs.com/pages/viewpage.action?pageId=6784248)
* [MA030REF - Restringir exibição de campos](https://tdn.totvs.com/pages/viewpage.action?pageId=6784250)
* [MATA030IPG](https://tdn.totvs.com/pages/releaseview.action?pageId=285650355)

Lista dos pontos de entrada específicos de manipulação e alteração do cadastro do cliente:

**[Cross-Se](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466954-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-entrada-para-altera%C3%A7%C3%A3o-do-cadastro-do-cliente)****[gmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-entrada-para-alteração-do-cadastro-do-cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466954-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-entrada-para-altera%C3%A7%C3%A3o-do-cadastro-do-cliente)**

***Observação:*** *O mata030 foi descontinuado em 04/04/22 a partir da release 12.1.27, precisando utilizar a rotina crma980 ativando o parâmetro mv\_mvcsa1 igual a .T.  A partir da nova release 12.1.2210 , o menu já estará tratando a rotina crma980, sem a necessidade de ativa o parâmetro. Com isso, há a necessidade de readequar pontos de entrada do fonte MATA030 para o novo fonte CRMA980.*

Ponto de entrada em MVC: [Pontos de Entrada - MVC](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=604230458)
