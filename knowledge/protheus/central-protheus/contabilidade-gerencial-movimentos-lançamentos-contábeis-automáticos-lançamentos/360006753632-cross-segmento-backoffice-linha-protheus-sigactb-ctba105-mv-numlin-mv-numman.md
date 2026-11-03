---
article_id: 360006753632
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: e2052beacef15030c909d658c2277aa632cca92a0047504631227f59d17b5b69
fetched_at: '2026-06-28T22:40:32.495625+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA105 - MV_NUMLIN
  MV_NUMMAN
type: support-article
updated_at: '2022-06-01T12:35:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006753632-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA105-MV-NUMLIN-MV-NUMMAN
---

***Dúvida***No Lançamento contábil qual o tratamento para o Numero de linhas e colunas por Documento?

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - TOTVS Contabilidade Gerencial - A partir da versão 12.1.17

**Solução**  
O Parâmetro **MV\_NUMLIN e MV\_NUMMAN** me permite definir quantas linhas poderei trabalhar com os lançamentos contábeis.

-**MV\_NUMLIN** - Limita o número de linhas por documento em lançamentos contábeis de integração vindo de outros módulos. O limite máximo para o parâmetro é de 35657 linhas.

<http://tdn.totvs.com/pages/releaseview.action?pageId=6068568>

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=233757409>

No caso do número de linhas, o campo **CT2\_LINHA** é alfanumérico, ou seja, ao permitir através da configuração do parâmetro que o lançamento aceite mais que 999 linhas, ao ultrapassar este valor, será gerados lançamentos com as linhas 99A, 99B, 99C e assim por diante.

-**MV\_NUMMAN** - Define o número de linhas por documento a ser utilizado para Lançamentos Contábeis Manuais

<http://tdn.totvs.com/pages/releaseview.action?pageId=6068569>
