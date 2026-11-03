---
content_hash: 7b3d9d0ccc1f5a298c3ed17f6d54fc73316c9cc51fd0002945cf7792c529e72d
fetched_at: '2026-06-29T00:08:40.765215+00:00'
page_id: '286503249'
product: rm
source: tdn-rm
title: DT Leitura da Carteirinha do Convênio do Paciente no Registro Atendimento Interno
  e Externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286503249
version: 112
---

# Leitura da Carteirinha do Convênio do Paciente no Registro Atendimento Interno e Externo

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Registro de Atendimento Interno | | Registro de Atendimento Externo |  |  | | --- | | **Rotina(s) envolvida(s)** | | Configuração da Carteira do Convênio | |
| **Cadastros Iniciais:** | Configuração da Carteira do Convênio |
| **Parâmetro(s):** | Lê Carteira do Convênio no Registro de Atendimento Interno  Lê Carteira do Convênio no Registro de Atendimento Externo |
| **Tickets relacionados** | [Ticket #775042](https://totvssuporte.zendesk.com/agent/tickets/775042 "Open ticket in Zendesk Support") |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1291  JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1290 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® E ORACLE® |
| **Tabelas Utilizadas:** | SZCONFIGCARTEIRACONV |
| **Sistema(s) Operacional(is):** | Windows*®* |

## Descrição

Esta implementação possibilita que o sistema realize a leitura dos cartões magnéticos dos usuários de planos de saúde, conforme as regras estabelecidas através do TOTVS Gestão Hospitalar.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No menu**Opções/Parâmetros/Parâmetros Gerais**, acesse a aba **Registro e Controle IV**.
2. Configure os parâmetros:

   1. **Lê Carteira no Reg. Atend. Interno**: Faz a leitura da carteira do convênio no registro de atendimento interno.
   2. **Lê Carteira no Reg. Atend. Extern**o: Faz a leitura da carteira do convênio no registro de atendimento externo.

## Procedimento para Utilização

IMPORTANTE

Esta rotina é diretamente dependente da configuração da carteira do convênio disponível no seguinte documento técnico: [Leitura da Carteirinha do Convênio do Paciente: Cadastro](http://tdn.totvs.com/pages/viewpage.action?pageId=286025313).

**Leitura da Carteira do Convênio**

* Após clicar que em novo atendimento, caso o parâmetro de Lê Carteira Convênio, da respectiva tela (Interno e/ou Externo) esteja marcado a seguinte tela é apresentada:
* Exemplo de leitura (Convênio TOTVS VIDA).
  + Supondo que ao realizar a leitura da carteira, a informação contida seja igual ao exemplo abaixo  

    **%Paciente Saudável?**  
    **;01020304050607080=090293=000000000000?**

    Levando em consideração que a configuração da carteira do convênio exemplo (TOTVS VIDA) informou que não primeira trilha há o Nome do Paciente (**Paciente Saudável**) e na segunda trilha há o Número da Carteira (**01020304050607080**) e a Data de Nascimento (**090293**).
  + Selecionar o convênio / Posicionar o cursor no campo Número da Carteira / Realizar a leitura / Receber os dados.

**Leitura da Carteira do Convênio no Registro de Atendimento Interno / Externo**

Esta rotina é valida para as seguintes rotinas:

* Atendimento / Internação / Registros de Internações.
* Atendimento / Pronto Atendimento/Ambulatório / Registro de Atendimento Externos.

1. Clique em **Novo Atendimento**.
2. Posicione o cursor no campo **Número da Carteira**.
3. Realize a Leitura e clique em **OK**.

* Caso um registro do paciente seja encontrado, as informações deste paciente serão replicadas para o **Novo Registro de Atendimento**.
* Caso o paciente não seja encontrado pelo número da carteira, a seguinte mensagem é apresentada e a tela de **Pesquisa de Clientes e Atendimento** é apresentada.
* Após selecionar um registro pela tela de **Pesquisa de Clientes e Atendimento**, o campo **Cód. Usuário no Convênio** é atualizado automaticamente.

divs
