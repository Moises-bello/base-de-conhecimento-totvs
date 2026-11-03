---
content_hash: 0b7b5a2127ec30e19b99eed84d25d08d5be0811c260eb58177efa0138ea17a46
fetched_at: '2026-06-29T00:12:10.227828+00:00'
page_id: '953000380'
product: rm
source: tdn-rm
title: Grupo G –  Identificação do Local de Entrega
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953000380
version: 1
---

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo G –  Identificação do Local de Entrega** | | | | | | | |
| **#** | **ID** | **Campo** | **Descrição** | **Observação** | **Campo de Origem** | **Campo na Aplicação** | **Mais Informações** |
| 89 | G01 | entrega | Identificação do Local de entrega | Informe apenas quando for diferente do endereço do destinatário. |  |  |  |
| 90 | G02 | CNPJ | CNPJo | Informar CNPJ ou CPF. Preencher os zeros não significativos. (v2.0) | TMOVTRANSP.CNPJCPFENTREGA | Campo CNPJ/CPF do Local de Entrega. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 90a | G02a | CPF | CPF | TMOVTRANSP.CNPJCPFENTREGA |
| 90b | G02b | xNome | Razão Social ou Nome do Recebedor | - | TMOVTRANSP.NOMEENTREGA | Campo Nome/Razão Social do Local de Entrega. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 91 | G03 | xLgr | Logradouro | - | TMOVTRANSP.RUAENTREGA | Campo Logradouro do Local de Entrega. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 92 | G04 | nro | Número | - | TMOVTRANSP.NUMEROENTREGA | Campo Número do Local de Entrega. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 93 | G05 | xCpl | Complemento | - | TMOVTRANSP.COMPLENTREGA | Campo Complemento do Local de Entrega. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 94 | G06 | xBairro | Bairro | - | TMOVTRANSP.BAIRROENTREGA | Campo Bairro do Local de Entrega. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 95 | G07 | cMun | Código do município | Utilizar a Tabela do IBGE (Anexo IX - Tabela de UF, Município e País). Informar ‘9999999 ‘para operações com o exterior. | TMOVTRANSP.CODMUNICIPIOENTREGA | Campo Município do Local de Entrega. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 96 | G08 | xMun | Nome do município | Informar ‘EXTERIOR ‘para operações com o exterior. | GMUNICIPIO.NOMEMUNICIPIO | Nome do município seguido do código do Local de Coleta. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 97 | G09 | UF | Sigla da UF | Informar ‘EX’ para operações com o exterior. | TMOVTRANSP.CODETDENTREGA | Campo Estado do Local de Entrega | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 97a | G10 | CEP | Código do CEP | Informar os zeros não significativos. | TMOVTRANSP.CEPENTREGA | Campo CEP do Local de Entrega | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 97b | G11 | cPais | Código do País | Utilizar a Tabela do Bacen (Anexo IX - Tabela de UF, Município e País). | DPAIS.CODPAIS | País selecionado no endereço do cadastro da Transportadora selecionada no campo Coleta. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 97c | G12 | xPais | Nome do Pais |  |  |  | Tag não gerada. |
| 97d | G13 | fone | Telefone | Preencher com o Código DDD + número do telefone. Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone (v2.0). | TMOVTRANSP.TELEFONEENTREGA | Campo Telefone do Local de Entrega. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 97e | G14 | email | Endereço de e-mail do Recebedor |  | TMOVTRANSP.EMAILENTREGA | Campo Email do Local de Entrega. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 97f | G15 | IE | Inscrição Estadual do Estabelecimento Recebedor |  | TMOVTRANSP.INSCRESTENTREGA | Campo Inscrição Estadual do Local de Entrega. | Movimento | pasta Transporte | aba Coleta e Entrega. |
