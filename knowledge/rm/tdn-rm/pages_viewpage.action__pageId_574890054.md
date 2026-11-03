---
content_hash: 30ffbaa446214fd3290a7b670949ad2c7a6be4c76e277d1fc248dcf220226613
fetched_at: '2026-06-29T00:10:53.077541+00:00'
page_id: '574890054'
product: rm
source: tdn-rm
title: Cabeçalho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=574890054
version: 7
---

**Manter Preço Unitário (Preço Editado)**

A **Flag** disponibilizada no item de movimento, tem por finalidade informar se o preço unitário retornado pela formula foi editado e que o valor editado deve ser mantido.

**Como habilitar:** Para que a **Flag** seja apresentada no item de movimento, é necessário que o tipo de movimento desejado, esteja parametrizado na **Etapa: Item - Preços 1/2**, em **"Buscar Preço Em"** , esteja marcado **somente** a opção **"Formula de Preço 1"** ou **somente** a opção **"Formula de Preço 2"**.

**Importante**: ao marcar mais de uma opção, o **Flag** Manter Preço unitário, **não** será apresentado no item de movimento.

Após a parametrização descrita acima, ao editar o item de movimento, o **Flag** estará disponível. Ao realizar a inclusão do item, o campo preço unitário será preenchido com o valor retornado pela formula e o **Flag** desmarcado, uma vez, que o preço foi calculado e não editado.

Ao alterar o valor do campo "Preço Unitário", automaticamente o **Flag** "Manter Preço Unitário" e marcado. Informando assim que o preço unitário foi editado e que deve ser mantido.

**Descrição do produto no fornecedor**

Ao realizar a inclusão de um movimento de Nota Fiscal de Entrada através de um XML, o nome do produto no fornecedor será preenchido no item de movimento.

**xProd:** Tag do XML que retorna o nome do produto no fornecedor.

**Nos parâmetros do tipo de movimento dever ser cadastrado pelo menos um Modelo de Documentos Fiscais ou pelo menos um dos tributos, conforme descritos abaixo:**

55 – Nota Fiscal Eletrônica (NF-e)

65 – Nota Fiscal do Consumidor Eletrônica (NFC-e)

67 - CT-eOs

66 - Nota Fiscal de Energia Elétrica Eletrônica (NF3-e)

ou Cupom Fiscal e Sat

**Tributo:**

ISS no Movimento

ISS no Item

### Repositório de Arquivos

A partir da versão 12.1.2402 a visão do anexo do Item de Movimento passa a exibir a nova funcionalidade [Repositório de Arquivos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=784778828).
