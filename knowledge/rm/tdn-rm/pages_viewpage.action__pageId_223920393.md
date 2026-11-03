---
content_hash: 5abd453660255a14d414abe6d2a61a52b6974ee0ea7a0bb71d63f634155b235d
fetched_at: '2026-06-29T00:06:22.533371+00:00'
page_id: '223920393'
product: rm
source: tdn-rm
title: TTU264_Geração_Usuário_Responsável_Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223920393
version: 125
---

# NOME DO REQUISITO

## Gerar usuário para Responsável Financeiro do aluno

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | *Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração de Usuário* | *Geração de Usuário para Responsável Financeiro* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Geração de Usuário* | *Processo de Geração de Usuário* | | *Contexto do Corpore.NET* | Contexto de usuário | | *Contexto do Educa Mobile* | Contexto de usuário | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *GUSUARIO* |
| **Sistema(s) Operacional(is):** | *Windows* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.8.113* |
| **Versão Expedida:** | *12.1.8.113* |

## Descrição

Foi realizado uma melhoria no processo de Geração de Usuário para Alunos, onde possibilita gerar usuários também para os Responsáveis Financeiros do aluno (Cliente/Fornecedor). Desta forma, ao gerar usuário para um aluno, será possível escolher 3 opções simultaneamente.

* Usuário para o aluno
* Usuário para o Responsável Acadêmico
* Usuário para o Responsável Financeiro

Um aluno pode ter mais de um responsável financeiro, caso seja definido no cadastro do aluno um Responsável Financeiro (Cliente/Fornecedor), e nos contratos do aluno estejam definidos outros responsáveis em cada contrato. Nesta condição, o processo irá gerar usuários para todos os cliente/fornecedor diferentes retornados para o aluno.

As parametrizações para geração de usuário para responsável financeiro são independentes dos outros tipos de usuários, porém, apenas as permissões iniciais definidas na primeira tela são as mesmas permissões que serão dadas aos usuários para Responsável Acadêmico, caso sejam criados ambos usuários na mesma execução do processo.

As definições de senha, e ordem para geração do nome de usuário são independentes para todos os tipos de usuários do aluno: usuário para o aluno, para o responsável acadêmico e responsável financeiro.

## Procedimento para utilização

**Detalhando as etapas do processo:**

       1.            Para gerar usuário para um responsável financeiro, o aluno deve possuir pelo menos um responsável financeiro cadastrado em um contrato qualquer do aluno, ou ter definido no cadastro do aluno um Responsável Financeiro.

       2.            Selecione um aluno e execute o processo "Geração de Usuários (Alunos)".

       3.            Na primeira tela do processo é possível marcar os tipos de usuário que serão gerados para este aluno: para o próprio aluno, para o responsável acadêmico e responsável financeiro.

       4.            Se for gerado usuário para o responsável acadêmico e responsável financeiro ao mesmo tempo, as definições de permissão para este usuários serão os mesmos.

       5.            Na próxima etapa do processo, é possível definir algumas parametrizações que são gerais para todos os usuários e todos os tipos de usuários do processo: Forçar a troca de senhas a cada X dias, Obrigar a alteração de senha no primeiro login, Regerar a senha do usuário e Período de validade do usuário. O parâmetro de Regerar a senha do usuário, irá atualizar a senha conforme a parametrização de senha Fixa ou por Data de Nascimento definida a cada tipo de usuário.

       6.            Abaixo das opções, são divididos as parametrizações de modo de geração do código do usuário e senha para cada tipo de usuário. Cada uma delas separadas por sua aba, onde é possível especificar a ordem de priorização da escolha do código do usuário que será gerado, e definição de senha para cada um deles.

divs
