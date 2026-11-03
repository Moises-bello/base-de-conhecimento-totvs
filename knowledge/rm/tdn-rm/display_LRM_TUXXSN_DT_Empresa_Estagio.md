---
content_hash: fc3682207a95dad113870a648e8e8be984df90fc4ba62fc53ef5d7a56d052e5c
fetched_at: '2026-06-29T00:08:09.125026+00:00'
page_id: '239024906'
product: rm
source: tdn-rm
title: TUXXSN_DT_Empresa_Estagio
type: documentation
url: https://tdn.totvs.com/display/LRM/TUXXSN_DT_Empresa_Estagio
version: 116
---

# CADASTRO DE EMPRESA - ESTÁGIO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **Totvs Gestão Educacional*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de Empresa - Estágio* | *Cadastro de Empresa - Estágio* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Candidatos às Vagas - Estágio* | *Candidatos às Vagas - Estágio* | | *Solicitação de Estágio* | *Solicitação de Estágio* | | *Solicitação de Estágio - Portal* | *Solicitação de Estágio - Portal* | | *Termo de Compromisso - Estágio* | *Termo de Compromisso - Estágio* | | *Relatório - EDUREL0054 - Termo de Compromisso de Estágio* | *Relatório - EDUREL0054 - Termo de Compromisso de Estágio* | | *Relatório - EDUREL0059 - Formulário para cadastro de vaga de estágio* | *Relatório - EDUREL0059 - Formulário para cadastro de vaga de estágio* | | *Relatório - EDUREL0060 - Formulário de atividades desempenhadas no estágio* | *Relatório - EDUREL0060 - Formulário de atividades desempenhadas no estágio* | |
| **Cadastros Iniciais:** | *1) Aluno cadastrado;*  *2) Empresa cadastrada;*  *3) Convênio cadastro;*  *4) Vaga cadastrada;*  *5) Alunos cadastrados na vaga;*  *6) Solicitação de estágio efetuada por um aluno.* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *TUAGYC e TUOMD2* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *SEMPRESA, SESTAGIOSOLICITACAO* |
| **Sistema(s) Operacional(is):** | *Windows 7* |

SEMPRESA

## Descrição

Melhoria no cadastro de empresa para que seja possível cadastrar uma empresa / profissional liberal / autônomo com CPF, Inscrição Estadual e Número do Conselho (CREA, CRM e outros) além do CNPJ, que já é permitido.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(12.1.12)* deste chamado.

## Procedimento para Utilização

**Para a rotina Cadastro de Empresa - Estágio:**

1. Acessar o TOTVS Educacional;
2. Acessar Atividades Acadêmicas | Empresa | Visão;
3. A coluna CNPJ da visão passará a chamar CNPJ / CPF / Inscrição Estadual / Número do Conselho;
4. Ao inserir ou editar uma empresa o campo CNPJ passará a chamar CNPJ / CPF / Inscrição Estadual / Número do Conselho, entretanto será validado o CNPJ e CPF, de acordo com o tamanho do campo.

**Para a rotina Candidatos às Vagas - Estágio:**

1. Acessar o TOTVS Educacional;
2. Acessar Atividades Acadêmicas | Estágio | Vagas | Anexo Candidatos às Vagas | Inserir ou Editar ou Acessar Atividades Acadêmicas | Estágio | Candidatos às Vagas | Inserir ou Editar;
3. O campo CNPJ passará a chamar CNPJ / CPF / Inscrição Estadual / Número do Conselho e será preenchido com seu respectivo valor.

**Para a rotina Solicitação de Estágio:**

1. Acessar o TOTVS Educacional;
2. Acessar Atividades Acadêmicas | Estágio | Solicitação de Estágio | Inserir ou Editar | Aba Empresa;
3. O campo CNPJ passará a chamar CNPJ / CPF / Inscrição Estadual / Número do Conselho.

**Para a rotina Solicitação de Estágio - Portal:**

1. Acessar o Portal e logar com usuário de aluno;
2. Acessar o Menu | Acadêmico | Estágio e Emprego | Solicitação | Incluir ou Editar;
3. No grupo Empresa ao incluir ou editar ou selecionar uma existente, o campo CNPJ passará a chamar CNPJ / CPF / Inscrição Estadual / Número do Conselho.

**Para a rotina Termo de Compromisso - Estágio:**

1. Acessar o TOTVS Educacional;
2. Acessar Atividades Acadêmicas | Estágio | Termo de Compromisso | Inserir ou Editar;
3. O campo CNPJ passará a chamar CNPJ / CPF / Inscrição Estadual / Número do Conselho.

**Para a rotina Relatório - EDUREL0054 - Termo de Compromisso de Estágio:**

1. Ao gerar o relatório do book EDUREL0054 - Termo de Compromisso de Estágio o campo CNPJ passará a chamar CNPJ / CPF / Inscrição Estadual / Número do Conselho
2. Relatório poderá ser gerado ao acessar Gestão | RM Reports | Relatórios ou pelo **Portal** | Menu | Acadêmico | Estágio e Emprego | Acompanhamento | Aba Estágios clicar na imagem  (Caso seja parametrizado o termo de compromisso no Educacional | Configurações | Parâmetros | Estágio | Estágio 4/7.

**Para a rotina Relatório - EDUREL0059 - Formulário para cadastro de vaga de estágio:**

1. Ao gerar o relatório do book EDUREL0059 - Formulário para cadastro de vaga de estágio o campo CNPJ passará a chamar CNPJ / CPF / Inscrição Estadual / Número do Conselho
2. Relatório poderá ser gerado ao acessar Gestão | RM Reports | Relatórios.

**Para a rotina Relatório - EDUREL0060 - Formulário de atividades desempenhadas no estágio:**

1. Ao gerar o relatório do book EDUREL0060 - Formulário de atividades desempenhadas no estágio o campo CNPJ passará a chamar CNPJ / CPF / Inscrição Estadual / Número do Conselho
2. Relatório poderá ser gerado ao acessar Gestão | RM Reports | Relatórios.
3. Para exibição deste relatório é necessário cadastrar um plano de atividade para aluno no Educacional | Atividades Acadêmicas | Estágio | Plano de Atividade.

divs
