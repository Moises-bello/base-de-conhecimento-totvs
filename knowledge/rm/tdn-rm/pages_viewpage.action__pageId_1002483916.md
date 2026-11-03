---
content_hash: 9e58175013cc9446561b57620b63ae3713b29252e3c66b919f33b034adc2b7b4
fetched_at: '2026-06-29T00:05:45.025709+00:00'
page_id: '1002483916'
product: rm
source: tdn-rm
title: Hierarquia de preenchimento da tag  <cBenef>
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1002483916
version: 32
---

Para o correto preenchimento da tag **<cBenef>**, é necessário que no cadastro do código de ajuste seja informar o tipo de crédito como **"Não se aplica"** e que o campo **"Estado"** seja o mesmo do emitente ou destinatário da NFCom.

A tag **<cBenef>** pode ser preenchida de três maneiras diferentes:

LayoutPrimeira Opção

1 -  Podemos vincular o código do benefício fiscal ao produto através do Anexo: **Benefício Fiscal**

Este é o primeiro local onde o sistema verificará a existência de algum benefício. Não encontrando seguirá para a segunda opção.

-

**Nesta opção não é possível configurar códigos de ajuste distintos para uma mesma CST, garantindo assim a consistência e integridade das regras fiscais aplicadas.**

Segunda Opção

2 -  Podemos vincular o código do benefício fiscal ao produto através do Anexo: **Dados Fiscais por UF**

Este é o segundo local onde o sistema verificará a existência de algum benefício. Não encontrando seguirá para a terceira opção.

Terceira Opção

3 -  Podemos vincular o código do benefício fiscal à CFOP através do Anexo: **Associação Natureza de Operação X Código Ajuste Sped Fiscal**

**Esta é a opção ideal para produtos que tenham código de ajustes distintos com o mesmo CST**
