---
content_hash: 67780cfcde65b705dd5312b5abf4d82116a83e51fb52d69a3227b2419a5ecb96
fetched_at: '2026-06-29T00:11:23.044315+00:00'
page_id: '706918892'
product: rm
source: tdn-rm
title: Alterações S-1210-S-1.1
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=706918892
version: 14
---

false

**A partir das Versões:**

* 12.1.34.232
* 12.1.2205.175
* 12.1.2209.117
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-1210 para o leiaute do eSocial Versão S-1.1.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {**infoPgto**}: Campo **{paisResidExt**}   Incluído campo | - | Informar o código do país de residência para fins fiscais, quando no exterior, conforme Tabela 06. Somente informar este campo caso o país de residência para fins fiscais seja diferente de Brasil. Se não informado, implica que o país de residência fiscal é Brasil. Validação: O campo apenas pode ser preenchido se perApur >= [2023-03]. Se informado, deve ser um código válido e existente na Tabela 06, exceto [105]. |
| Grupos {**infoPgtoExt**}: Campo **{indNIF}**   Incluído campo | - | Indicativo do Número de Identificação Fiscal (NIF). Valores válidos: 1 - Beneficiário com NIF 2 - Beneficiário dispensado do NIF 3 - País não exige NIF |
| Grupos {**infoPgtoExt**}: Campo **{nifBenef**}   Incluído campo | - | Número de Identificação Fiscal (NIF). Validação: Preenchimento obrigatório se indNIF = [1]. |
| Grupos {**infoPgtoExt**}: Campo {**frmTribut** }   Incluído campo | - | Forma de tributação, conforme opções disponíveis na Tabela 30. Validação: Deve ser um código válido e existente na Tabela 30. |
| Grupos {**endExt**: Campo { **endDscLograd**}   Incluído campo | - | Descrição do logradouro |
| Grupos {**endExt**: Campo { **endNRLograd**}   Incluído campo |  | Numero do Logradouro.  Validação: Devem ser utilizados apenas caracteres alfanuméricos com pelo menos, um caractere numérico. |
| Grupos {**endExt**: Campo { **endComplem**}   Incluído campo | - | Complemento do logradouro. |
| Grupos {**endEx**t: Campo { **endBairro**}   Incluído campo | - | Nome do bairro/distrito |
| Grupos **{endExt**: Campo { **endCidade**}   Incluído campo | - | Nome da cidade. |
| Grupos **{endExt**: Campo { **endEstado**}   Incluído campo | - | Nome da província/estado. |
| Grupos {**endExt**: Campo { **endCodPostal**}   Incluído campo | - | Código de Endereçamento Postal. Validação: Devem ser informados apenas caracteres numéricos. |
| Grupos {**endExt**: Campo { **telef** }   Incluído campo | - | Número do telefone. Validação: Devem ser informados apenas caracteres numéricos. |

Preenchendo o anexo do cadastro do funcionário Dados do residente ou Domiciliado no exterior o grupo {**infoPgtoExt**} será gerado no XML

  XML:
