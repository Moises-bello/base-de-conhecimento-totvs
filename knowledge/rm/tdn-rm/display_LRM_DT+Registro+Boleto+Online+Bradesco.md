---
content_hash: 5530522fe3c86c9a123ce4ca28bfa7fde439370873414bb42f8f9e3236607be1
fetched_at: '2026-06-29T00:08:34.655073+00:00'
page_id: '274830131'
product: rm
source: tdn-rm
title: DT Registro Boleto Online Bradesco
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Registro+Boleto+Online+Bradesco
version: 113
---

# Registro Boleto Online Bradesco

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção & Projetos* |
| **Módulo:** | **TOTVS Gestão Financeira** |
| **Requisito/S****tory/Issue:** | *FINANCEIRO01-40* |

## Descrição

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada do Banco Bradesco.

## Procedimento para Configuração

No TOTVS Gestão Financeira, menu *Movimentações Bancárias | Controle Bancário | Convênio,* devem ser feitas as configurações do convênio para o registro de boleto online:

* **Permite registro de boleto online*:*** Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **URL do serviço de registro do boleto**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco. <https://cobranca.bradesconetempresa.b.br/ibpjregistrotitulows/registrotitulo>
* **URL do homologação do serviço de registro de cobrança**: Deve ser informado a URL de homologação do serviço de registro do boleto fornecida pelo banco. <https://cobranca.bradesconetempresa.b.br/ibpjregistrotitulows/registrotitulohomologacao>
* **Impressão digital**: Deve ser informado a impressão digital do certificado que será usado para assinatura da mensagem enviada para o serviço de registro de cobrança.

**Atenção**:

* Deve ser adquirido um certificado digital ICP-Brasil, preferencialmente modelo A1. O certificado deverá ser incluído no cadastro de Certificado Digital no TOTVS Gestão Fiscal.
* Quanto Ambiente Teste o código de barras será gerado com uma sequência de 44 caracteres '9'.
* O campo Data da Multa será calculado a partir da Data de Vencimento do boleto acrescido do parâmetro *Dias de Atraso* configurado na etapa Valor Líquido do Lançamento Financeiro.

divs
