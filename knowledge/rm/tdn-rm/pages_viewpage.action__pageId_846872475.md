---
content_hash: 9b99b2c6cf713ae22b71dab1dc0be1462fdbbd152eb2cf86735d932cb9ed8031
fetched_at: '2026-06-29T00:11:50.947654+00:00'
page_id: '846872475'
product: rm
source: tdn-rm
title: API do Processo de Retornar para "Em Edição"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=846872475
version: 1
---

# Sumário

---

Sumário

# Objetivo

---

      Esse documento tem o objetivo de exemplificar o uso da API de Retornar para "Em Edição" alterando o seu status de maneira que fique disponível novamente para edições. Mais detalhes em [Fluxo de aprovação | Processos | 05. Processos](https://tdn.totvs.com/pages/viewpage.action?pageId=838210925#FluxodeAprova%C3%A7%C3%A3odeLan%C3%A7amentosManuais-05.Processos)

Importante

Recurso disponível a partir da release 12.1.2406.

# 1 - Campos e Parâmetros

---

      Descrição detalhada dos campos da API de Retornar para "Em Edição".

false

As tabelas abaixo são divididas da seguinte maneira:

* **Campo:** Identificação do campo no Json.
* **Identificador:** Identificação do campo no banco de dados RM correspondente ao campo Json.
* **Tipo:** Tipo de valor aceito no campo, podendo ser numérico (Int, Decimal), condicionais (Boolean), texto (String, Datetime), além do tipo List, para esse último, é esperado uma nova sequência de dados (Bloco interno).
* **Descrição:** Fornece uma descrição do campo.
* **Obrigatório:** Especifica se a informação é obrigatória durante operações de envio (POST, PUT, PATCH). Caso a informação seja obrigatória condicionalmente essa informação será descrita no campo Observação.
* **Observação:** Informações condicionais ou importantes para o funcionamento da API serão apresentadas nesse campo.

falseRetornar em edição

Tipo: POST

| Lote | | | | |
| --- | --- | --- | --- | --- |
| Campo | Tipo | Descrição | Obrigatório | Observação |
| Lotes  | Lote | | | | | --- | --- | --- | --- | | Campo | Tipo | Descrição | Observação | | CompanyId | Int | Código da Coligada | - | | BatchId | Int | Código do Lote | - | | Lista | Lista com os lotes que serão processados | Sim | - |
| Message | String | Observação, complemento, mensagem a ser enviada junto ao e-mail | Não | No caso de aprovação este campo não é utilizado |

# 2 - Métodos

---

      Métodos disponíveis na API de Retornar para "Em Edição":

falsefalsePost (Retornar em edição)

**POST:** Retornar para "Em Edição"

falsePost

**Máscara de Url:** http://{domínio}:{porta}/api/ctb/v1/batchLancApproval/returnToEditing

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Url Utilizada:** <http://localhost:8052/api/ctb/v1/batchLancApproval/returnToEditing>

falseExemplo de EntradaVer resultado JSON...

O JSON abaixo contém uma lista com os lotes que serão submetidos ao processo de retornar em edição. A lista é composta dos identificadores de cada lote (chave primária) composto do código da coligada e o código do lote e a mensagem que será enviada no e-mail.

jsEmacs1Resultado (JSON)truefalseExemplo de ResultadoVer resultado JSON...

A saída, ou retorno da API, é uma estrutura com a lista lotes processados, sua respectiva descrição e o status de seu processamento. Caso tenha ocorrido um erro no processamento então teremos um campo mensagem com o log/descrição da situação.

jsRDark1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...jsFadeToGrey1500 Internal Server Error - Resultado (JSON)true
