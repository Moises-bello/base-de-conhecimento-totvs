---
content_hash: 9e7dde40ec1e768b1ce279949d60760d03dccf525bbd83232de01da7d340d9ac
fetched_at: '2026-06-29T00:11:18.259577+00:00'
page_id: '684341557'
product: rm
source: tdn-rm
title: DE/PARA COMPLETO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=684341557
version: 3
---

3De/ParaDe/Para

**1 - PESSOAS**

**1.1 - DADOS ENVIADOS NO ENDPOINT DE PESSOAS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFUNC.CODCOLIGADA |
| name | Nome | PPESSOA.NOME |
| socialName | Nome de preferência (apelido) | PPESSOA.NOMESOCIAL |
| email | Email | PPESSOA.EMAIL |
| admissionDate | Data de admissão | PFUNC.DATAADMISSAO |
| lastRaiseDate | Data de último aumento | PFHSTSAL.DATAMUDANCA |
| birthDate | Data de aniversário | PPESSOA.DTNASCIMENTO |
| demissionDate | Data de demissão | PFUNC.DATADEMISSAO |
| experienceEndDate | Data do fim do período de experiência | PFUNC.FIMPRAZOCONTR |
| dismissalType | Tipo de demissão: 1 - Pedido de desligamento, 2 - Sem justa caua, 3 - Com justa causa. | PFUNC.TIPODEMISSAO |
| hiringTypeIntegrationId | Identificador único de integração do regime de contratação |  |
| departmentIntegrationId | Identificador único de integração da área da pessoa | PFUNC.CODSECAO |
| positionIntegrationId | Identificador único de integração do cargo da pessoa | PFUNC.CODFUNCAO |
| positionLevelIntegrationId | Identificador único de integração do nível cargo da pessoa | PFUNC.CODNIVELSAL |
| facilityIntegrationId | Identificador único de integração da unidade da pessoa | PFUNC.CODFILIAL |
| managerIntegrationId | Identificador único de integração do líder imediato da pessoa |  |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**2 - REGISTROS AUXILIARES**

**2.1 - DADOS ENVIADOS NO ENDPOINT DE CARGOS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFUNCAO.CODIGO |
| name | Nome | PFUNCAO.NOME |
| positionGroupIntegrationId | Identificador único de integração do grupo de cargo do cargo | PFUNCAO.CARGO |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**2 - REGISTROS AUXILIARES**

**2.2 - DADOS ENVIADOS NO ENDPOINT DE NÍVEIS DE CARGOS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | VNIVELFUNCAO.CODNIVEL |
| name | Nome | VNIVELFUNCAO.NOMENIVEL |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**2 - REGISTROS AUXILIARES**

**2.3 - DADOS ENVIADOS NO ENDPOINT DE GRUPOS DE CARGOS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PCARGO.CODIGO |
| name | Nome | PCARGO.NOME |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**2 - REGISTROS AUXILIARES**

**2.4 - DADOS ENVIADOS NO ENDPOINT DE UNIDADES**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | GFILIAL.CODFILIAL |
| name | Nome | GFILIAL.NOME |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**2 - REGISTROS AUXILIARES**

**2.5 - DADOS ENVIADOS NO ENDPOINT DE ÁREAS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PSECAO.CODIGO |
| name | Nome | PSECAO.DESCRICAO |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**2 - REGISTROS AUXILIARES**

**2.6 - DADOS ENVIADOS NO ENDPOINT DE REGIMES DE CONTRATAÇÕES**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M |  |
| name | Nome |  |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**3 - HISTÓRICO DE REGISTROS AUXILIARES POR PESSOAS**

**3.1 - DADOS ENVIADOS NO ENDPOINT DE MOVIMENTAÇÃO DE PESSOAS PARA CARGOS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFHSTFCO.CODCOLIGADA |
| positionIntegrationId | Identificador único de integração do cargo da pessoa | PFHSTFCO.CODFUNCAO |
| personIntegrationId | Identificador único de integração da pessoa | PFUNC.CODPESSOA |
| changeDate | Data de alteração da pessoa para o cargo | PFHSTFCO.DTMUDANCA |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**3.2 - DADOS ENVIADOS NO ENDPOINT DE MOVIMENTAÇÃO DE PESSOAS PARA NÍVEIS DE CARGOS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFHSTFCO.CODCOLIGADA |
| positionLevelIntegrationId | Identificador único de integração do nível de cargo da pessoa | PFHSTFCO.CODNIVEL |
| personIntegrationId | Identificador único de integração da pessoa | PFUNC.CODPESSOA |
| changeDate | Data de alteração da pessoa para o nível de cargo | PFHSTFCO.DTMUDANCA |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**3.3 - DADOS ENVIADOS NO ENDPOINT DE MOVIMENTAÇÃO DE PESSOAS PARA GRUPOS DE CARGOS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFHSTFCO.CODCOLIGADA |
| positionGroupIntegrationId | Identificador único de integração do grupo de cargo da pessoa | VGRUPOOCUPACIONAL.CODGRUPOOCUP |
| personIntegrationId | Identificador único de integração da pessoa | PFUNC.CODPESSOA |
| changeDate | Data de alteração da pessoa para o grupo de cargo | PFHSTFCO.DTMUDANCA |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**3.4 - DADOS ENVIADOS NO ENDPOINT DE MOVIMENTAÇÃO DE PESSOAS PARA UNIDADES**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFHSTSEC.CODCOLIGADA |
| facilityIntegrationId | Identificador único de integração da unidade da pessoa | GFILIAL.CODFILIAL |
| personIntegrationId | Identificador único de integração da pessoa | PFUNC.CODPESSOA |
| changeDate | Data de alteração da pessoa para a unidade | PFHSTSEC.DTMUDANCA |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**3.5 - DADOS ENVIADOS NO ENDPOINT DE MOVIMENTAÇÃO DE PESSOAS PARA ÁREAS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFHSTSEC.CODCOLIGADA |
| departmentIntegrationId | Identificador único de integração da área da pessoa | PFHSTSEC.CODSECAO |
| personIntegrationId | Identificador único de integração da pessoa | PFUNC.CODPESSOA |
| changeDate | Data de alteração da pessoa para a área | PFHSTSEC.DTMUDANCA |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**4 - AFASTAMENTOS POR PESSOAS**

**4.1 - DADOS ENVIADOS NO ENDPOINT DE AFASTAMENTOS POR PESSOAS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFHSTAFT.CODCOLIGADA |
| personIntegrationId | Identificador único de integração da pessoa | PFUNC.CODPESSOA |
| type | Tipo do afastamento, podendo ser:   * Acidente de trabalho = 1 * Doença ocupacional = 2 * Doença = 3 * Licença maternidade = 4 * Licença paternidade = 5 * Licença não remunerada = 6 | PFHSTAFT.TIPO |
| startDate | Data de início do afastamento | PFHSTAFT.DTINICIO |
| endDate | Data de término do afastamento | PFHSTAFT.DTFINAL |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**5 - FALTAS POR PESSOAS**

**5.1 - DADOS ENVIADOS NO ENDPOINT DE FALTAS POR PESSOAS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFHSTFALTA. CODCOLIGADA |
| personIntegrationId | Identificador único de integração da pessoa | PFUNC.CODPESSOA |
| year | Ano de ocorrência da falta | PFHSTFALTA.ANOCOMPFALTA |
| month | Mês de ocorrência da falta | PFHSTFALTA.MESCOMPFALTA |
| daysNotWorked | Total de dias não trabalhados para o ano e mês informados | CALCULADO PELO SISTEMA |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |
