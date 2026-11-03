---
content_hash: 46ba5b0f3b165c396e507262f5c7c652061c7712374b04b695f9e9db6ee06c36
fetched_at: '2026-06-29T00:12:10.219539+00:00'
page_id: '953000372'
product: rm
source: tdn-rm
title: Grupo F – Identificação do Local de Retirada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953000372
version: 1
---

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo F – Identificação do Local de Retirada** | | | | | | | |
| # | **ID** | **Campo** | **Descrição** | **Observação** | **Campo de Origem** | **Campo na Aplicação** | **Mais Informações** |
| 80 | F01 | retirada | Identificação do Local de retirada | Informe apenas quando for diferente do endereço do remetente. |  |  |  |
| 81 | F02 | CNPJ | CNPJ | Informar CNPJ ou CPF. Preencher os zeros não significativos. (v2.0). | TMOVTRANSP.CNPJCPFCOLETA | Campo CNPJ/CPF do Local de Coleta. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 81a | F02a | CPF | CPF | TMOVTRANSP.CNPJCPFCOLETA |
| 81b | F02b | xNome | Razão Social ou Nome do Expedidor | - | TMOVTRANSP.NOMECOLETA | Campo Nome/Razão Social do Local de Coleta. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 82 | F03 | xLgr | Logradouro | - | TMOVTRANSP.RUACOLETA | Campo Logradouro do Local de Coleta. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 83 | F04 | nro | Número | - | TMOVTRANSP.NUMEROCOLETA | Campo Número do Local de Coleta. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 84 | F05 | xCpl | Complemento | - | TMOVTRANSP.COMPLCOLETA | Campo Complemento do Local de Coleta. | Movimento | pasta Transporte | aba Coleta e Entrega.. |
| 85 | F06 | xBairro | Bairro | - | TMOVTRANSP.BAIRROCOLETA | Campo Bairro do Local de Coleta. | Movimento | pasta Transporte | aba Coleta e Entrega.. |
| 86 | F07 | cMun | Código do município | Utilizar a Tabela do IBGE (Anexo IX - Tabela de UF, Município e País). Informar ‘9999999 ‘para operações com o exterior. | TMOVTRANSP.CODMUNICIPIOCOLETA | Campo Município do do Local de Coleta. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 87 | F08 | xMun | Nome do município | Informar ‘EXTERIOR ‘para operações com o exterior. | GMUNICIPIO.NOMEMUNICIPIO | Nome do município seguido do código do Local de Coleta.. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 88 | F09 | UF | Sigla da UF | Informar ‘EX’ para operações com o exterior. | TMOVTRANSP.CODETDCOLETA | Campo Estado do Local de Coleta. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 88a | F10 | CEP | Código do CEP | Informar os zeros não significativos. | TMOVTRANSP.CEPCOLETA | Campo CEP do Local de Coleta | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 88b | F11 | cPais | Código do País | Utilizar a Tabela do BACEN (Anexo IX - Tabela de UF, Município e País). | DPAIS.CODPAIS | País selecionado no endereço do cadastro da Transportadora selecionada no campo Coleta. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 88c | F12 | xPais | Nome do País |  |  |  |  |
| 88d | F13 | fone | Telefone | Preencher com o Código DDD + número do telefone. Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone (v2.0) | TMOVTRANSP.TELEFONECOLETA | Campo Telefone do Local de Coleta. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 88e | F14 | email | Endereço de e-mail do Expedidor |  | TMOVTRANSP.EMAILCOLETA | Campo Email do Local de Coleta. | Movimento | pasta Transporte | aba Coleta e Entrega. |
| 88f | F15 | IE | Inscrição Estadual do Estabelecimento Expedidor |  | TMOVTRANSP.INSCRETCOLETA | Campo Inscrição Estadual do Local de Coleta. | Movimento | pasta Transporte | aba Coleta e Entrega. |
