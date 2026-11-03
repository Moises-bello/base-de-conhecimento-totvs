---
content_hash: ad77ba678acc23d6f9846df8e07cd69ae714d453c1d9216802e79cd1bc49a00d
fetched_at: '2026-06-29T00:08:40.054661+00:00'
page_id: '286204811'
product: rm
source: tdn-rm
title: DT Geração de Usuários Nova Opção Primeiro Nome + Último Nome + Sequencial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286204811
version: 104
---

# GERAÇÃO DE USUÁRIOS - NOVA OPÇÃO: PRIMEIRO NOME + ÚLTIMO NOME + SEQUENCIAL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração de Usuários* | *Geração de Usuários* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Cadastro de Alunos** | *Cadastro de Alunos* | | *Cadastro de Professores* | *Cadastro de Professores* | | **Cadastro de Funcionários da Empresa** | **Cadastro de Funcionários da Empresa** | |
| **Cadastros Iniciais:** | * *Para geração de usuários para cada entidades é necessário o cadastro dos itens:*   + *Aluno;*   + *Responsáveis do aluno;*   + *Responsável financeiro do aluno;*   + *Professor;*   + *Funcionários da Empresa;*   + *Coordenador;*   + *Pesquisador.* |
| **Parâmetro(s):** | * *Parametrização de geração automática*    + *Configurações | Parâmetros | Geração e Usuários:*     - *Alunos;*     - *Professores;*     - *Funcionários da empresa.* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *EDUCACIONAL01-665* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows 7, 8 e 10* |

## Descrição

Evolução no processo de geração de usuário (alunos, responsáveis do aluno, responsável financeiro do aluno, professores, coordenadores, funcionários da empresa e pesquisadores) para que passe a contemplar nas prioridades a opção **Primeiro Nome + Último Nome + Sequencial**.

Sendo que foi evoluído na geração automática dos alunos, responsáveis do aluno, responsável financeiro do aluno, professores e funcionários da empresa para também contemplar a nova opção.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da release 12.1.17.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

### ***Geração Automática de Usuários***

A geração automática de usuários somente é feita para as seguintes entidades:

* Alunos;
* Responsáveis do aluno;
* Responsável financeiro do aluno;
* Professores;
* Funcionários da empresa.

Para configurar a geração automática de usuários com a nova opção **Primeiro Nome + Último Nome + Sequencial**é necessário a seguinte configuração nos parâmetros.

falseConfiguraçãoAlunosAlunosfalse

Em Configurações | Parâmetros | Geração de Usuários | Alunos:

| Alunos | Responsáveis do Aluno | Responsável Financeiro do Aluno |
| --- | --- | --- |
|  |  |  |

ProfessoresProfessoresfalse

Em Configurações | Parâmetros | Geração de Usuários | Professores:

FuncEmpFuncionários da Empresafalse

Em Configurações | Parâmetros | Geração de Usuários | Funcionários da Empresa:

## Procedimento para Utilização

1. Caso o sistema esteja parametrizado para geração automática de usuários para alunos, responsáveis do aluno, responsável financeiro do aluno, professores e/ou funcionários da empresa com a nova opção Primeiro Nome + Último Nome + Sequencial ao se cadastrar uma das entidades citadas o sistema automaticamente irá criar o usuário respectivo a sua entidade;
2. Para geração de usuário de forma manual em todas as entidades é necessário os seguintes passos:
   1. Alunos:
      1. Acessar o cadastro de aluno e ir em Processos | Geração de Usuários (Aluno) | No passo da **Opção de geração do usuário do aluno** selecionar **Personalizado** e mover a opção **Primeiro Nome + Último Nome + Sequencial** para o início da lista e executar o processo.
   2. Responsáveis do aluno:
      1. Acessar o cadastro de aluno e ir em Processos | Geração de Usuários (Aluno) | Marcar a opção para gerar usuários para responsáveis (Pai, Mãe e responsável acadêmico) | No passo da **Opção de geração do usuário do responsável** selecionar Personalizado e mover a opção Primeiro Nome + Último Nome + Sequencial? para o início da lista e executar o processo.
   3. Responsável financeiro do aluno:
      1. Acessar o cadastro de aluno e ir em Processos | Geração de Usuários (Aluno) | Marcar a opção para gerar usuários para responsável financeiro | No passo da **Opção de geração do usuário do responsável financeiro** selecionar Personalizado e mover a opção Primeiro Nome + Último Nome + Sequencial? para o início da lista e executar o processo.
   4. Professores:
      1. Acessar o cadastro de professor e ir em Processos | Geração de Usuários (Professor) | No passo da **Opção de geração do usuário do professor** selecionar Personalizado e mover a opção **Primeiro Nome + Último Nome + Sequencial** para o início da lista e executar o processo;
   5. Funcionários da empresa:
      1. Acessar o cadastro da empresa parceira onde o funcionário está cadastrado e ir em Processos | Geração de Usuários (Funcionários) | No passo da **Opção de geração do usuário do funcionário**selecionar Personalizado e mover a opção **Primeiro Nome + Último Nome + Sequencial** para o início da lista e executar o processo.
   6. Pesquisador:
      1. Acessar o cadastro do pesquisador e ir em Processos | Geração de Usuários (Pesquisador) | No passo da **Opção de geração do usuário do pesquisador**selecionar Personalizado e mover a opção **Primeiro Nome + Último Nome + Sequencial** para o início da lista e executar o processo.
   7. Coordenador:
      1. Acessar Currículo e Oferta | Estrutura Curricular | Mais | Geração de Usuários para Coordenadores | No passo da **Opção de geração do usuário do coordenador**selecionar Personalizado e mover a opção **Primeiro Nome + Último Nome + Sequencial** para o início da lista e executar o processo.
3. Após a execução do processo, o usuário será criado conforme parametrizado.

Importante

O número sequencial somente será exibido se o usuário a ser criado já existir na base de dados, ou seja, se foi criado um usuário com o nome josesouza, o próximo usuário com este mesmo nome será josesouza1 e assim por diante, sempre somando o número sequencial a cada josesouza criado.

divs
