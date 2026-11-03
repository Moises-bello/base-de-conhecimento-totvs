---
content_hash: effb9944112d4bce3377f1c1d68c53412505c775c4c2edf68402111264bc4907
fetched_at: '2026-06-29T00:11:50.909339+00:00'
page_id: '845419257'
product: rm
source: tdn-rm
title: API do Processo de Solicitação de Aprovação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=845419257
version: 19
---

# Sumário

---

Sumário

# Objetivo

---

      Esse documento tem o objetivo de exemplificar o uso da API de Solicitação de Aprovação de Lotes utilizando todos os métodos implementados.

Importante

Recurso disponível a partir da release 12.1.2406.

# 1 - Campos e Parâmetros

---

      Descrição detalhada dos campos da API de Solicitação de Aprovação de Lotes.

false

As tabelas abaixo são divididas da seguinte maneira:

* **Campo:** Identificação do campo no Json.
* **Identificador:** Identificação do campo no banco de dados RM correspondente ao campo Json.
* **Tipo:** Tipo de valor aceito no campo, podendo ser numérico (Int, Decimal), condicionais (Boolean), texto (String, Datetime), além do tipo List, para esse último, é esperado uma nova sequência de dados (Bloco interno).
* **Descrição:** Fornece uma descrição do campo.
* **Obrigatório:** Especifica se a informação é obrigatória durante operações de envio (POST, PUT, PATCH). Caso a informação seja obrigatória condicionalmente essa informação será descrita no campo Observação.
* **Observação:** Informações condicionais ou importantes para o funcionamento da API serão apresentadas nesse campo.

falseSolicitação

Tipo: POST

| Lote | | | | |
| --- | --- | --- | --- | --- |
| Campo | Tipo | Descrição | Obrigatório | Observação |
| Lotes  | Lote | | | | | --- | --- | --- | --- | | Campo | Tipo | Descrição | Observação | | CompanyId | Int | Código da Coligada | - | | BatchId | Int | Código do Lote | - | | Lista | Lista com os lotes que serão processados | Sim | - |
| Message | String | Observação, complemento, mensagem a ser enviada junto ao e-mail | Não | O campo é opcional, sendo utilizado no corpo do email. |

# 2 - Métodos

---

      Métodos disponíveis na API de Solicitação de Aprovação de Lotes:

falsefalsePost (Solicitar Aprovação do Lote)

**POST:**Solicita a Aprovação dos Lotes enviados

falsePost

**Máscara de Url:** http://{domínio}:{porta}/api/ctb/v1/batchLancApproval/requestApproval

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** [http://localhost:8051/api/ctb/v1/batchLancApproval/requestApproval](http://localhost:8051/api/ctb/v1/AccountingEntries/6)

falseExemplo de EntradaVer resultado JSON...

O JSON abaixo contém os dados para solicitar a aprovação de Lotes Contábeis.

jsEmacs1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...

Na resposta do resultado, são retornadas as informações dos Lotes que foram processados com sucesso.

jsRDark1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...jsFadeToGrey1Resultado (JSON)true
