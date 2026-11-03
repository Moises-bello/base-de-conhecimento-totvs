---
content_hash: fdc2deb8799d6affc9345620e991c7545ed4acac852142408de9159295981e9a
fetched_at: '2026-06-29T00:08:39.036605+00:00'
page_id: '286005617'
product: rm
source: tdn-rm
title: Factory
type: documentation
url: https://tdn.totvs.com/display/LRM/Factory
version: 9
---

Após Instalar o TOTVS RM Portal deverá ser realizado os passos abaixo:

**1º-** Acesse o caminho: "**C:\totvs\CorporeRM\FrameHTML\Web\app\Edu\PortalEducacional\js\aluno\ocorrencias**". Crie uma pasta com o nome "**custom**".

**2º-**Acesse o caminho "**C:\totvs\CorporeRM\FrameHTML\Web\app\Edu\PortalEducacional\js\templates**" e faça uma cópia do arquivo "**ocorrencias.factory.js**" para a pasta "**custom**".

Template

 

**3º-** Edite o arquivo com o editor da sua preferência e faça as alteração desejadas.

 

**Exemplo:**

 

 

 

**4º-** No controller, inclua a referência da factory customizada.

 

 

**Exemplo:**

 Como exemplo, iremos consumir uma API pública (Consulta de CEP) e exibir na tela o resultado nos campos.

**Factory**

**Controller**

 

**Tela**
