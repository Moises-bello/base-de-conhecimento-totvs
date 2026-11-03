---
content_hash: 802dcc38b239156e6604dde02230cdd05bbce6297783189f3156338257e2deef
fetched_at: '2026-06-29T00:08:58.726015+00:00'
page_id: '361434700'
product: rm
source: tdn-rm
title: 2475022 MATESTCNTFTOF01-1872 DT Erro na integração de funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=361434700
version: 10
---

# INTEGRAÇÃO DE FUNCIONÁRIO (EMPLOYEE 2.003)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Funcionário. | FopFuncAction. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cargos. | RhuCargoAction. | | Funções | FopFuncaoAction. | | Horários |  | | Seções | FopSecaoAction | |
| **Cadastros Iniciais:** | Para que seja integrado um Funcionário são necessários realizar a integração dos seguintes cadastros no módulo Folha de Pagamento. Acesse RM \ RH \ Folha de Pagamento e realize a inclusão de registros nas rotinas:   * Cargos (menu Administração de Pessoal \ Cargos/Funções \ Cargo) * Funções  (menu Administração de Pessoal \ Cargos/Funções \ Funções) * Horários  (menu Administração de Pessoal \ Horários) * Seções  (menu Administração de Pessoal \ Seções)   **Observação:** antes de realizar os cadastros consulte o tópico Procedimentos para Configuração |
| **Parâmetro(s):** | Acesse RM \ RH \ Folha de Pagamento \ Ambiente \ Parâmetros \ Folha de Pagamento \ 06.02 - Integrações \ 06.02.06 - Outros BackOffice e marque o parâmetro **Utilizar Fórmula Visual em Integração (SIGAMNT)** |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabelas Utilizadas:** | PCARGO - Cargos.  PFUNCAO - Funções.  AHORARIO - Horários.  PSECAO - Seções.  PFUNC - Funcionários. |
| **Sistema(s) Operacional(is):** | Windows 7 ou superior. |

## Descrição

Disponibilizar no pacote de integração Manutenção de Ativos x BackOffice RM, a integração de Funcionário via mensagem única utilizando o adapter Employee versão 2.003.

**Configurador de Integração**

Realizar um ajuste no Configurador de Integração Manutenção de Ativos x BackOffice RM para contemplar a nova versão Employee 2.003.

* Apagar a Employee versão 2.001.
* Inserir o mapeamento das mensagens\_versão: Employee\_2.003 (funcionário), EmployeePosition\_1.000 (cargo), Role\_1.000 (função), ShifWork\_1.000 (horário),  e Departament\_2.001 (seções).

**Fórmulas Visuais de Integração**

Realizar ajuste nas fórmulas visuais de integração de Funcionário (exclusão e inclusão) para considerar a versão 2.003. As fórmulas visuais que serão ajustadas são:

* MOVWKF0008 - Employee.TotvsWF
* MOVWKF0009 - Employee\_Delete.TotvsWF
* MOVWKF0040 - Departament\_2.001.TotvsWF (cadastro)
* MOVWKF0041 - Department\_2.001 - Carga\_Inicial.TotvsWF

## Procedimento para Configuração

**CONFIGURAÇÃO DE INTEGRAÇÃO PROTHEUS**

1. No **Configurador (SIGACFG)**, acesse **Ambientes/Schedule/Adapter E.a.i**. Configure a rotina do Adapter  de acordo com  os dados abaixo fornecidos  e que já foram pré estabelecidos na aplicação do patch de atualização do Protheus:

   |  |  |  |  |  |  |  |  |  |  |  |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | **Mensagem Única** | **Rotina Protheus** | **Mensagem** | **Descrição** | **Envia** | **Recebe** | **Método Protheus** | **Operação** | **Canal de Envio** | **Adapter Protheus** | **Versão** |
   | Sim | GPEA370 | EMPLOYEEPOSITION | Cargo | Não | Sim | Síncrono | Todas | EAI | GPEA370 | 1.000 |
   | Sim | GPEA030 | ROLE | Função | Não | Sim | Síncrono | Todas | EAI | GPEA030 | 1.000 |
   | Sim | GPEA010 | EMPLOYEE | Funcionário | Não | Sim | Síncrono | Todas | EAI | GPEA010 | 2.003 |
   | Sim | GPEA080 | SHIFTWORK | Turno | Não | Sim | Síncrono | Todas | EAI | GPEA080 | 1.000 |
   | Sim | CSAA100 | DEPARTAMENT | Departamento | Não | Sim | Síncrono | Todas | EAI | CSAA100 | 2.001 |
2. Acesse **Base de Dados/Dicionário/Base de dados**, em **Dicionário de Dados** e altere o compartilhamento das tabelas conforme abaixo:

   | Tabela | Filial | Unidade | Empresa |
   | --- | --- | --- | --- |
   | SQ3 (Cargos) | Compartilhado | Compartilhado | Exclusivo |
   | SRJ (Funções) | Compartilhado | Compartilhado | Exclusivo |
   | SR6 (Turnos de trabalho) | Compartilhado | Compartilhado | Exclusivo |
   | SQB (Departamento) | Exclusivo | Exclusivo | Exclusivo |
   | SRA (Funcionário) | Compartilhado | Compartilhado | Exclusivo |

**CONFIGURAÇÃO DE INTEGRAÇÃO RM**

Para que a integração **TOTVS Manutenção de Ativos x BackOffice RM** utilize o novo adapter de Employee versão 2.003 serão necessários realizar os seguintes passos:

1. Excluir o arquivo de transformação Employee 2.003  
     
   Acesse **RM \ Integração \ Mensagem Única \ Transformação**, execute o filtro pesquisando pelo **Id** Employee e **Versão** 2.003  
     
     
   Selecione o registro na visão de **Transformação** e execute **Excluir** e confirme a exclusão**.**
2. Excluir o arquivo de código fonte Employee 2.003  
     
   Acesse **RM \ Integração \ Mensagem Única \ Integrações**, selecione a integração **TOTVS Manutenção de Ativos x BackOffice RM (Identificador = 1001).**  
   Acesse **Anexos \ Mapeamento de Entidades**, clique em **Incluir** e no campo **Eventos** pesquise pela descrição **Employee Adapter 2.003.**  
   Clique sobre o link para abrir a tela de **Cadastro de códigos fontes** e clique em **Excluir**, confirmando a exclusão.  
     
   Após este procedimento cancele a inclusão de mapeamento.
3. Executar o configurador de integração do projeto **TOTVS Manutenção de Ativos x BackOffice RM**  
     
   Acesse **RM \ Integração \ Ferramentas \ Configurar**, avance até a etapa Projetos de Integração.  
   Selecione o item **TOTVS Manutenção de Ativos x BackOffice RM** e execute o processo para que o Mapeamento de Entidades seja atualizado.
