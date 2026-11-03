---
article_id: 18743242304663
category: Materiais - Compras (SIGACOM)
content_hash: 1d8140d57b9c478a27e5f78a4983b66de266a76df9d35ecc51911987f43d044a
fetched_at: '2026-06-28T22:41:20.121979+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - MATA116 - Ocorrências
  do help A116VLDATF
type: support-article
updated_at: '2023-11-03T19:59:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18743242304663-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-MATA116-Ocorr%C3%AAncias-do-help-A116VLDATF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18743274642711) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Quais são as causas da ocorrência do help **A116VLDATF**?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18802752384791)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - a partir da 12.1.33  
  
**Causa**

Existem dois cenários que podem causar a ocorrência do help A116VLDATF, são eles:

1º Cenário: *"O status do ativo  #  vinculado a este documento, não permite alteração."*

Quando tentar excluir um CTE na rotina MATA116 e o parâmetro MV\_AGVLATF = .T., a espécie = CTE, o ativo não existir no sistema existir ou estiver classificado.

2º Cenário: *"O status do ativo  #  não permite alteração."*

Ao tentar gerar um conhecimento de frete de uma nota cujo ativo já está classificado.

**Solução**

Para solucionar as ocorrências acima, basta seguir os passos abaixo.

1. Será necessário desabilitar o parâmetro **MV\_AGVLATF = .F.**

2. Incluir o conhecimento de frete (MATA116) para a nota de compra do ativo.

3. Acessar a rotina ATFA251 (Aquisição por transferência) para aglutinar o valor do frete ao valor do ativo.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Ocorrências do help A103VLDATF](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX59j4mg86D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE3MTU4Mjc0MzQ0NzI3LUNyb3NzLVNlZ21lbnRvcy1UT1RWUy1CYWNrb2ZmaWNlLVByb3RoZXVzLVNJR0FDT00tT2NvcnIlQzMlQUFuY2lhcy1kby1oZWxwLUExMDNWTERBVEYGOwhUOg5zZWFyY2hfaWRJIikyNWZjNTA3ZC0xZGNhLTRhMzMtYjY1Yi1hNDVkMTcxNzU5MWMGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIg9hMTAzdmxkYXRmBjsIVDoScmVzdWx0c19jb3VudGkG--5669a5636d4d650ed98c56b2e8632a0ef4da3991)
* [Cross Segmento - Backoffice Linha Protheus - SIGAATF - Tabelas do Ativo Fixo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020439351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Tabelas-do-Ativo-Fixo?source=search)
* [Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA251 - Agregar, Aglutinar ou Desmembrar bens do ativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006767052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA251-Agregar-Aglutinar-ou-Desmembrar-bens-do-ativo?source=search)
