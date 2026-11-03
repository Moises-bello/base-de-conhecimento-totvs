---
content_hash: 7e9105b13157af35951b0bb9c3e27078f8ed90f8bf3c79e04d87622c87ea49c0
fetched_at: '2026-06-29T00:08:18.658058+00:00'
page_id: '266964251'
product: rm
source: tdn-rm
title: DT_TOTEM_Com_Registro_de_Atendimento_Automático
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266964251
version: 117
---

# TOTEM com leitora de carteirinha e registro de atendimento automático

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Toten de Pronto Atendimento |  |  | | --- | | **Rotina(s) envolvida(s)** | | Unidades de Atendimento | | Valores Padrão para Atendimento | |
| **Cadastros Iniciais:** | **Cadastros / Uso Geral / Unidades de Atendimento,** aba **Outros Dados**  ****Cadastros / Uso Geral / Valores Padrão para Atendimento**** |
| **Parâmetro(s):** | *“Registra Atendimento automático via TOTEM”* |
| **Requisito (ISSUE):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-555 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Tabelas Utilizadas:** | SZATENDIMENTO, SZANSATEND, SZATENDAUTORIZ, SZSENHACLASSIF |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementação no Totem de Pronto Atendimento para realizar o registro de atendimento automaticamente através da leitura da carteirinha do convênio do paciente.

## Procedimento para Utilização

1. Acesse **Cadastros / Uso Geral / Unidades de Atendimento**. Selecione uma unidade de atendimento e acesse a aba **Outros Dados**. Marque o parâmetro **Registra Atendimento automático via TOTEM**.
2. Acesse **Cadastros / Uso Geral / Valores Padrão para Atendimento**. Clique em **Novo** caso deseje criar uma nova parametrização de valores padrão e informe o Tipo de Paciente\*, Unidade de Atendimento e Convênio obrigatoriamente. Em seguida, para preenchimento automático informe valores para Tipo de Atendimento e Tipo de Guia/Autorização. Para convênios que faturam TISS é possível informar também o Tipo de Atendimento ANS, Tipo de Consulta, Indicador de Acidente e Tipo de Saída.  

   \*para o TOTEM o tipo de paciente será **sempre EXTERNO.**
3. Salve o cadastro e acesse **Anexos / Item por Especialidade.** Clique me **Novo** e informe a Especialidade, o Tipo Item Autorização, o Tipo de Guia, a Vigência, o procedimento default que será lançado bem como a quantidade e salve.  
     
     

   Após este cadastro será possível acessar o TOTEM na unidade de atendimento parametrizada e com os valores default para atender um paciente emitindo senha com o registro de atendimento realizado e com o paciente já visível no Painel de Classificação de Risco para triagem.
4. Acesse **Atendimento / Pronto Atendimento/Ambulatório / Toten de Pronto Atendimento**.
5. Selecione a unidade de atendimento configurada anteriormente.
6. Selecione a especialidade configurada anteriormente.
7. Selecione o tipo de senha preferencial ou normal.
8. Informe a carteirinha do paciente (capturada pelo leitor).
9. Ao localizar o paciente, clique em **Prosseguir.**
10. Selecione a data de nascimento do paciente.
11. Selecione o nome da mãe do paciente.
12. Após responder as perguntas o sistema efetuou o registro do atendimento do paciente. Ao acessar **Atendimento / Pronto Atendimento/Ambulatório /****Painel de Classificação de Risco** é possível visualizar o paciente na aba **triagem**.

**Atendimento do paciente registrado automaticamente com os dados parametrizados:**

divs
