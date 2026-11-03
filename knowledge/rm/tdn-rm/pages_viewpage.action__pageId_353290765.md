---
content_hash: 8b46f55b93c3c87ccb4670029aa1129cbabc2000bbc426b4c5c4d83a55167746
fetched_at: '2026-06-29T00:08:57.301592+00:00'
page_id: '353290765'
product: rm
source: tdn-rm
title: 2352453 RMSAU-3166 DT Colunas de Controle no Registro de Atendimento Interno/Externo
  e Elaboração de Contas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353290765
version: 1
---

# olunas de Controle no Registro de Atendimento Interno/Externo e Elaboração de Contas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Registro de Internações | PSARC001 |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Registro de Internações | PSARC001 | | Registro de Atendimentos Externos | PSARC023 | |
| **Tickets relacionados** | [#2352453](https://totvssuporte.zendesk.com/agent/tickets/2352453) |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | RMSAU-3166 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server |
| **Tabelas Utilizadas:** | SZATENDIMENTO, SZPARCIALATEND |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Este procedimento tem como objetivo alimentar as colunas de controle RECCREATEDON, RECCREATEDBY, RECMODIFIEDON e RECMODIFIEDBY, as operações de inclusão/alteração de um registro de atendimento (interno e externo), bem como suas parciais relacionadas, para fins de controle de logs e emissão de relatórios gerenciais.

## Procedimento para Utilização

1atendExtRegistro de Atendimentos Externos

# **Inclusão:**

1. Acesse o RM Saúde > Atendimentro >  Pronto Atendimento/Ambulatório > Registro de Atendimentos Externos.
2. Clique em "Novo Atendimento" para a inclusão
3. Preencha os campos necessários
4. Clique em "Registra"
5. A data atual do servidor será gravada nas colunas RECCREATEDON e RECMODIFIEDON, do atendimento incluído, na tabela SZATENDIMENTO, assim como o nome do usuário logado será gravado nas colunas RECCREATEDBY e RECMODIFIEDBY.
6. A data atual do servidor será gravada nas colunas RECCREATEDON e RECMODIFIEDON, da parcial 1 relacionada ao atendimento acima, na tabela SZPARCIALATEND, assim como o nome do usuário logado será gravado nas colunas RECCREATEDBY e RECMODIFIEDBY.

# **Alteração:**

1. Clique em "Altera Informações" para a alteração
2. Modifique o conteúdo de algum campo e clique em "Registra"
3. A data atual do servidor será gravada na coluna RECMODIFIEDON do atendimento alterado, assim como o nome do usuário logado será gravado na coluna RECMODIFIEDBY
atendIntRegistro de Internações

# **Inclusão:**

1. Acesse o RM Saúde > Atendimento > Internação > Registro de Internações
2. Clique em "Novo Atendimento" para a inclusão
3. Preencha os campos necessários
4. Clique em "Gravar"
5. A data atual do servidor será gravada nas colunas RECCREATEDON e RECMODIFIEDON, do atendimento incluído, na tabela SZATENDIMENTO, assim como o nome do usuário logado será gravado nas colunas RECCREATEDBY e RECMODIFIEDBY.
6. A data atual do servidor será gravada nas colunas RECCREATEDON e RECMODIFIEDON, da parcial 1 relacionada ao atendimento acima, na tabela SZPARCIALATEND, assim como o nome do usuário logado será gravado nas colunas RECCREATEDBY e RECMODIFIEDBY.

# **Alteração:**

1. Clique em "Altera Informações" para a alteração
2. Modifique o conteúdo de algum campo e clique em "Registra"
3. A data atual do servidor será gravada na coluna RECMODIFIEDON do atendimento alterado, assim como o nome do usuário logado será gravado na coluna RECMODIFIEDBY
elaborCtasElaboração de Contas

# **Inclusão:**

1. Acesse o RM Saúde > Faturamento > Lançamentos na Conta do Paciente
2. Clique em "Pesquisa Atend."
3. Busque um atendimento e clique em "OK"
4. Clique em "Incluir Parcial" e "Salvar"
5. A data atual do servidor será gravada nas colunas RECCREATEDON e RECMODIFIEDON, da parcial incluída na tabela SZPARCIALATEND, assim como o nome do usuário logado será gravado nas colunas RECCREATEDBY e RECMODIFIEDBY.

# **Alteração:**

1. Selecione uma parcial com situação "Em elaboração" e clique em "Alterar início parcial" ou "Cancelar parcial",
2. A data atual do servidor será gravada na coluna RECMODIFIEDON da parcial alterada, assim como o nome do usuário logado será gravado na coluna RECMODIFIEDBY.
