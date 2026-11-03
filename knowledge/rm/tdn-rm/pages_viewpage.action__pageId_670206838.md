---
content_hash: 5009a3581e2449471c8a3e6862027ef86a14cc9043318dcb6f28dfa99fa9e7c1
fetched_at: '2026-06-29T00:11:16.512270+00:00'
page_id: '670206838'
product: rm
source: tdn-rm
title: Férias em dobro para funcionário com contrato de trabalho intermitente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=670206838
version: 8
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Cadastro individual de Férias |
| País: | Brasil |
| Ticket: | 10191303 |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-123](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-123) |

## **02. SITUAÇÃO/REQUISITO**

Ao abrir o cadastro Individual de férias de um funcionário contrato para trabalho intermitente são apresentadas as mensagens **'As férias do funcionário deverão ser pagas em dobro no caso de ultrapassar o prazo limite estabelecido em xx/xx/xxxx. Obs. Este prazo poderá ser prorrogado no caso de Licença Maternidade durante o período aquisitivo.'** e **'Funcionário deverá iniciar suas férias até xx/xx/xxxx devido à férias em dobro!'** . O cliente deseja que seja dada a opção da apresentação das mensagens, quando o funcionário for contratado para trabalho intermitente, pois esse tipo de funcionário tem a opção de receber as 1/12 avos de férias mensalmente. 

## **03. SOLUÇÃO**

Será criado em  **RH | Folha de Pagamento | Configurações | Parametrizador | Folha de Pagamento | Férias | Férias em Dobro**, o parâmetro **'Não exibir mensagens de férias em dobro para funcionários intermitentes no cadastro individual de férias**'. Com este parâmetro marcado, não serão apresentadas as mensagens relacionadas a férias em dobro para funcionários com o tipo de contrato de trabalho intermitente.

**Observação:**

Para que seja habilitado o parâmetro **'Não exibir mensagens de férias em dobro para funcionários intermitentes no cadastro individual de férias**' deverão ser confirmados os parâmetros 'Ativar alterações da Reforma Trabalhista de acordo com a Lei Nº 13.467 de 13 de Julho de 2017', disponível em **RH | Folha de Pagamento | Configurações | Parametrizador | Folha de Pagamento | Geral** e'Usa Trabalho Intermitente' e 'Trata cadastro de férias para contrato intermitente' disponível em **RH | Folha de Pagamento | Configurações | Parametrizador | Folha de Pagamento | Funcionário | Trabalho Intermitente | Parâmetros do Trabalho Intermitente** e 'Regime de Trabalho Intermitente' disponível em **RH | Folha de Pagamento | Administração de Pessoal | Funcionários |  Informações Contratuais | Salário / Jornada**.

**Passos:**

**1º)** Marcar o parâmetro '**Ativar alterações da Reforma Trabalhista de acordo com a Lei Nº 13.467 de 13 de Julho de 2017**', disponível em **RH | Folha de Pagamento | Configurações | Parametrizador | Folha Normal | Geral**:

**2º)** Marcar os parâmetros '**Usa Trabalho Intermitente**' e '**Trata cadastro de férias para contrato intermitente**' disponível em **RH | Folha de Pagamento | Configurações | Parametrizador | Folha de Pagamento | Funcionário | Trabalho Intermitente | Parâmetros do Trabalho Intermitente:**

**3º)** Marcar o  parâmetro '**Regime de Trabalho Intermitente**' disponível em **RH | Folha de Pagamento | Administração de Pessoal | Funcionários |  Informações Contratuais | Salário / Jornada:**

**4º)** Marcar o **NOVO** parâmetro '**Não exibir mensagens de férias em dobro para funcionários intermitentes no cadastro individual de férias**', criado em **RH | Folha de Pagamento | Configurações | Parametrizador | Folha de Pagamento | Férias | Férias em Dobro:**

**Exemplo:**

**1)** Com o parâmetro '**Não exibir mensagens de férias em dobro para funcionários intermitentes no cadastro individual de férias**',  **DESMARCADO**:

**Tela de Cadastro individual de Férias:**

**2) Com o parâmetro 'Não exibir mensagens de férias em dobro para funcionários intermitentes no cadastro individual de férias',  MARCADO:**

**Tela de Cadastro individual de Férias:**

## **04. DEMAIS INFORMAÇÕES**

O default do parâmetro será desmarcado. Caso o usuário queira utilizar o recurso, deverá marcar os parâmetros, conforme parametrização.

## **05. ASSUNTOS RELACIONADOS**

[Atualizações - Reforma Trabalhista](https://tdn.totvs.com/pages/viewpage.action?pageId=287073735)

[Trabalho Intermitente](https://tdn.totvs.com/display/LRM/Trabalho+Intermitente)

[Férias em Dobro](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719558)
