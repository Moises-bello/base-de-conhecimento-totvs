---
content_hash: 585414b294add3a14b5dac37f798590775a407f3ef71ef80f92db690432cde4e
fetched_at: '2026-06-29T00:11:11.761106+00:00'
page_id: '649299107'
product: rm
source: tdn-rm
title: SPED Fiscal Alterações do Layout 2022 - Versão 3.0.8
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=649299107
version: 9
---

Anualmente é instituído, através de ato cotepe, atualização no layout do arquivo digital da EFD ICMS IPI. Para a competência de 2022, foi definido através do [ATO COTEPE/ICMS 44, DE 07 DE AGOSTO DE 2018](https://www.confaz.fazenda.gov.br/legislacao/atos/2018/ato-cotepe-icms-44-18 "Follow link") e disponibilizado através do [Guia Prático EFD ICMS IPI - v 3.0.8](http://sped.rfb.gov.br/estatico/8D/519392B83F160FA92AF2A21532ADDC16703E1B/Guia%20Pr%c3%a1tico%20EFD%20-%20Vers%c3%a3o%203.0.8.pdf)

Abaixo estão listadas as alterações Realizadas na geração do SPED Fiscal, através do TOTVS Gestão Fiscal, para atender o layout 3.0.8 com efeito a partir de Janeiro de 2022

1lefttrue1Bloco 0

* Registro 0000:

Na tela de geração da rotina, alterado a versão para “**016**”. Essa versão só é válida a partir de 01/01/2022.

* Registro 0210:

A partir de janeiro de 2022, este registro não será mais gerado, devido ao novo Layout do SPED.

* Registro 0220:

A partir de 2022 o registro vai receber um quarto campo que vai ter o código de barras do produto.

2Bloco 1

* Registro 1600 - Incluída a regra por data, em que registros anteriores a 01/01/2022 o registro será gerado e os posteriores a 31/12/2021 o registro não será gerado
* Inclusão do Novo Registro 1601 - o mesmo só será gerado a partir de 2022 -
3Bloco C

* Registro C500:

A partir de 2022 não será gerado valores para os campos 15, 16 e 17, os novos campos de 34, 35, 36, 37, 38, 39 e 40 também vão ser gerados sem valores.

Informações

Documentação: 

As alterações estão disponíveis a partir dos patches:

* 12.1.32.228
* 12.1.33.158
