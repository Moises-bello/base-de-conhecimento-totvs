---
article_id: 360006986031
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 7462897f5a87314f9bf8116ff873e78e789f6efdd3c4d8231ae95f8ee618c662
fetched_at: '2026-06-28T22:40:47.533799+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS410-  ECF Como gerar
  o bloco W
type: support-article
updated_at: '2021-06-29T23:33:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006986031-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS410-ECF-Como-gerar-o-bloco-W
---

Através da rotina *CTBS410 realize o cadastro do bloco W*

![](https://tdn.totvs.com/download/attachments/379320276/image2018-7-4_18-8-1.png?version=1&modificationDate=1530739242000&api=v2)

![](https://tdn.totvs.com/download/attachments/379320276/image2018-7-4_18-9-55.png?version=1&modificationDate=1530739242000&api=v2)

Ao Gerar a revisão através da rotina de escrituração contábil (CTBS001)

![](https://tdn.totvs.com/download/attachments/379320276/image2018-7-4_18-11-2.png?version=1&modificationDate=1530739242000&api=v2)

Registro        Tabela/CTB   TAFST1/TAFST2

Reg 0020             CSZ        T127

Verifique se o registro foi gerado na tabela da contabilidade

![](https://tdn.totvs.com/download/attachments/379320276/image2018-7-4_18-12-18.png?version=1&modificationDate=1530739241000&api=v2)

* Verifique também se as tabelas *CQM / CQN / CQO / CQP foram alimentadas*
* Verifique  se a tabela TAFST1 e TAFST2 foi alimentada:
* Link abaixo veja a estrutura do bloco T132 - verifique se o registro foi gerado corretamente
* [01. Layout Único Atual](https://tdn.totvs.com/pages/releaseview.action?pageId=379320276#)
* No registro da conta verifique T0132 – Tabela TAFST1

    \*posicione o Mouse no  "TAFKEY"  na Conta que possui amarração

       \* Editar > Alterar -  Verifique  se foi gerado os dados

  Ex: |T132|W100 - GRUPO 01|1|||11233|1|1|||| | | |PT|

  |T132AA||1500|150|150|150|1650|300|0|1000|1100|10|155|15|115|115|115|115|115|222|22|

  |T132AB||RAZAO W100|1233|||||OECD303|RUA XX|||2|2|2|2|2|2|2|2|2|2|2|2|2|||

  |T132AC||2|2|2|2|2|2|2|2|2|2|teste|

![](https://tdn.totvs.com/download/attachments/379320276/image2018-7-4_18-13-59.png?version=1&modificationDate=1530739241000&api=v2)

* Blocos/Registros /Rotinas – geração no TAF ou na integração

[http://tdn.totvs.com/pages/releaseview.action?pageId=192089512](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512)

* Através da rotina abaixo  verifique se o registro foi gerado na rotina do TAF

Bloco W - Declaração País-a-País (Novo bloco à partir do layout 3.0.0)

Registro W001 - Abertura do Bloco W

Registro W100: Informações sobre o Grupo Multinacional e a Entidade Declarante – Declaração País-a-País

* Tabela - T67 (INFO. GRUP. MULT. ENTDAD. DEC )
* Registro do Layout TOTVS - T132
* Rotina - TAFA471 (Declaração País-a-País)

Registro W200: Declaração País-a-País

* Tabela - T68 (DECLARACAO PAIS-A-PAIS )
* Registro do Layout TOTVS - T132AA
* Rotina - TAFA471 (Declaração País-a-País)

Registro W250: Declaração País-a-País – Entidades Integrantes

* Tabela - T68 (ENTIDADES ENTEGRATES )
* Registro do Layout TOTVS - T132AB
* Rotina - TAFA471 (Declaração País-a-País)

Registro W300: Observações Adicionais – Declaração País-a-País

* Tabela - T68 (OBS. ADICIONAIS PAIS-A-PAIS    )
* Registro do Layout TOTVS - T132AC
* Rotina - TAFA471 (Declaração País-a-País)

Registro W990 - Encerramento do Bloco W

* Posteriormente gere um revisão e verifique se o registro foi gerado
