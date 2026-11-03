---
content_hash: 84428c8f1d7a15dbd38d072143d8dfbdf77b011f3cf82184f4f587162fc2c9f0
fetched_at: '2026-06-29T00:11:46.499511+00:00'
page_id: '822687871'
product: rm
source: tdn-rm
title: atvEvento/end
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822687871
version: 5
---

Grupo responsável por informar o endereço da atividade do evento, seja ela nacional ou no exterior. O grupo `end` é referente ao endereço nacional. O grupo `endExt` refere-se ao exterior e só pode existir se o CEP **não** for informado.

| Nome | Pai | Obrigatório | Origem | Descrição |
| --- | --- | --- | --- | --- |
| CEP | NFSe/infNFSe/DPS/infDPS/serv/atvEvento/end | Não |  | CEP Nacional. |
| endExt | NFSe/infNFSe/DPS/infDPS/serv/atvEvento/end | Não |  | Grupo de endereço exterior. |
| xLgr | NFSe/infNFSe/DPS/infDPS/serv/atvEvento/end | Sim |  | Logradouro |
| nro | NFSe/infNFSe/DPS/infDPS/serv/atvEvento/end | Sim |  | Número |
| xCpl | NFSe/infNFSe/DPS/infDPS/serv/atvEvento/end | Não |  | Complemento |
| xBairro | NFSe/infNFSe/DPS/infDPS/serv/atvEvento/end | Sim |  | Bairro. |

| Nome | Pai | Obrigatório | Origem | Descrição |
| --- | --- | --- | --- | --- |
| cEndPost | NFSe/infNFSe/DPS/infDPS/serv/atvEvento/end/endExt | Sim |  | Código Postal Exterior. |
| xCidade | NFSe/infNFSe/DPS/infDPS/serv/atvEvento/end/endExt | Sim |  | Cidade no Exterior. |
| xEstProvReg | NFSe/infNFSe/DPS/infDPS/serv/atvEvento/end/endExt | Sim |  | Estado/Província Exterior. |
