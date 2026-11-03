---
content_hash: a33a88984dab4580ebcd9f2c6d30a485047aebb2286f88cd246cb02ebc9eab56
fetched_at: '2026-06-29T00:06:01.171538+00:00'
page_id: '198937304'
product: rm
source: tdn-rm
title: DT_CAPTACAO_ESTAGIO_BASEADA_ALUNO
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CAPTACAO_ESTAGIO_BASEADA_ALUNO
version: 14
---

# Captação de estágio baseada no aluno

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Totvs Educacional |
| **Módulo:** | Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Termo de compromisso | Termo de compromisso | | Solicitação de estágio | Solicitação de estágio | | Aprovação da solicitação de estágio | Aprovação da solicitação de estágio | | Solicitação de orientador do estágio | Solicitação de orientação | | Aprovação da solicitação de orientador | Aprovação da solicitação de orientação |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Empresa | Cadastro de empresa | | Funcionário | Cadastro de funcionário | |
| **Cadastros Iniciais:** | Cadastro de empresas, funcionários e convênios. |
| **Parâmetro(s):** | Permitir informar empresa/funcionário que não esteja cadastrada para estágio na solicitação |
| **Requisito (ISSUE):** | [PCREQ-5450](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-5450 "PCREQ-5450") |
| **País(es):** | Brasil |
| **Tabelas utilizadas:** | SESTAGIOSOLICITACAO, SESTAGIOORIENTADOR |
| **Versões/Release:** | 12.1.7 |

## Descrição

O processo de captação de estágio baseado no aluno, se caracteriza pelo processo de estágio sem a necessidade de candidatura de vagas, ou seja, o próprio aluno identifica uma oportunidade de estágio, muitas vezes já participou de um processo de seleção, ou até mesmo já trabalha em uma empresa e necessita realizar os trâmites legais para registrar o estágio em seu curso.

**Solicitação de estágio (aluno):** Rotina que permite a solicitação de estágio feita pelo aluno, através do portal.

1º Passo) Logar no portal como aluno e acessar o menu: Estágio/Emprego | Solicitação.

2º Passo) Serão listadas todas as solicitações de estágio, com a opção de inserir e excluir os registros.

3º Passo) Inserindo um novo registro, será exibido uma nova página, onde será necessário descrever todas as informações do estágio, empresa e funcionário. Será permitido informar dados de uma nova empresa e funcionário, mediante configuração do sistema (vide parâmetro 1).

4º Passo) Para poder visualizar o menu, o usuário deve ter permissão no seu perfil no seguinte caminho: Educacional | Outras permissões | RM Portal | Portal | Acadêmico | Estágio/Emprego | Solicitação de estágio.

**Solicitação de orientador:** Rotina que permite o aluno, realizar uma solicitação para que um determinado professor seja orientador do seu estágio.

1º Passo) Logar no portal como aluno e acessar o menu: Estágio/Emprego | Solicitação.

2º Passo) Serão listadas todas as solicitações de estágio, com a opção de inserir e excluir os registros.

3º Passo) Para a solicitação de estágio, será possível expandir o registro para visualizar os professores orientadores (primeira coluna, botão "+").

4º Passo) Será possível enviar o convite de orientação do estágio, somente para professores que ainda não foi convidado. Não será possível realizar novos convites, caso algum professor aceite.

**Aprovação de solicitação de orientação**: Rotina que permite o professor aceitar ou reprovar o convite de orientação de estágio feito pelo aluno.

1º Passo) Logar no portal como professor, e acessar o menu: Estágio | Convites orientação.

2º Passo) Serão listadas todas as solicitações de orientação.

3º Passo) Para aprovar a solicitação de orientação, o professor deve marcar a opção "Convite Aceito", para recusar a opção deve estar desmarcada e a justificativa deve ser informada.

4º Passo) Para poder visualizar o menu, o usuário deve ter permissão no seu perfil no seguinte caminho: Educacional | Outras permissões | RM Portal | Portal | Professor | Estágio | Convites para orientação.

**Aprovação da solicitação de estágio:** Rotina que permite o usuário do sistema, aprovar ou reprovar uma solicitação de estágio feita pelo aluno.

1º Passo) Acessar o aplicativo e entrar na visão de Solicitação de estágio no menu: Atividades acadêmicas | Estágio | Solicitação de estágio.

2º Passo) Serão listadas todas as solicitações de estágio para aprovação e reprovação.

3º Passo) Para aprovar a solicitação de estágio, deve-se alterar o status para Aprovado, e informar o valor do campo Código do contrato. Na aprovação é verificado se existe a necessidade de criação de uma nova empresa e funcionário conforme informações passadas e definido no parâmetro (vide parâmetro 1), e em seguida é gerado o termo de compromisso.

4º Passo) Para poder visualizar o menu, o usuário deve ter permissão no seu perfil no seguinte caminho: Educacional | Atividades acadêmicas | Acadêmico | Estágio | Solicitação de estágio.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No Totvs Educacional, acesse **Configurações/Parâmetros/Estágio (Estágio 2/8)**.

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Permitir informar empresa/funcionário que não esteja cadastrada para estágio na solicitação |
| **Tipo:** | Booleano (True/False) |
| **Cont. Por.:** | False |
| **Descrição:** | Esse parâmetro definirá se na solicitação de estágio o aluno poderá informar os dados da empresa e funcionário, para que sejam cadastros e utilizados em seu estágio. |
