---
content_hash: 50c55868b07b3448ec19a9de20f0166ef091f77b4cbb488c28e83cadf786bd79
fetched_at: '2026-06-29T00:06:19.494082+00:00'
page_id: '219698353'
product: rm
source: tdn-rm
title: CLB_0004_Informações_Técnicas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219698353
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Colaboração 2.00 |
| **Versões:** | 12.1 e superiores |
| **Ocorrência:** | Informações Técnicas |
| **Ambiente:** | Banco de dados |
| **Passo a passo:** | Alterações Estruturais no Banco de Dados Para que o ERP TOTVS Linha RM utilize a integração “TOTVS Colaboração 2.00” foi necessário incluir campos no banco de dados na tabela “TPAR”:     |  |  |  |  | | --- | --- | --- | --- | | **Novos Campos TPAR** | **Descrição/Conteúdo** | **Tipo** | **Tamanho** | | DIRETORIOTOTVSCOLAB | Diretório de XML - TOTVS Colaboração versão 2.00 | Varchar | 255 | | VERSAOTOTVSCOLAB | Versão TOTVS Colaboração | Varchar | 10 |     Foi criada a tabela “TXMLCOLAB – XML de Integração com o NeoGrid Client” para armazenamento provisório dos XMLs lidos pelo ERP através da execução de JOB de modo a serem processados e atualizados os respectivos dados no ERP, objetivando melhor performance para o processamento dos documentos.     |  |  |  |  |  | | --- | --- | --- | --- | --- | | **Campos TXMLCOLAB** | **Descrição/Conteúdo** | **Tipo** | **Tamanho** | **Chave** | | IDXMLCOLAB | Identificador | Int | 4 | Sim | | CODCOLIGADA | Código da Coligada | Int | 4 | Sim | | NOMEARQUIVO | Nome do arquivo retornado pela NeoGrid | Varchar | 100 |  | | MODELOARQUIVO | Modelo do arquivo | Int | 4 |  | | SEQUENCIAL | Sequencial do arquivo retornado pela NeoGrid | Int | 4 |  | | XML | XML retornado pela NeoGrid | Varchar | -1 |  | | LOG | Log de Erro do XML | Varchar | 2000 |  | | STATUS | Status do XML | Varchar | 1 |  |        Houve adequação também na tabela “TPARFILIAL” para informar Versão de Evento de documentos CT-e e MD-e:     |  |  |  |  | | --- | --- | --- | --- | | **Novos Campos TPARFILIAL** | **Descrição/Conteúdo** | **Tipo** | **Tamanho** | | VERSAOEVENTOCTE | Versão do Evento do CT-e | Varchar | 10 | | VERSAOEVENTOMDE | Versão do Evento do MD-e | Varchar | 10 |      Tabelas Envolvidas       * GCOLIGADA – Coligadas * GFILIAL – Filiais * TPAR – Parâmetros Gerais * TPARFILIAL – Parâmetros por Filial * FCFO – Clientes/Fornecedores * TTMV – Tipos de Movimento * TCTEMOV – Tabela Base do CT-e      **Observação:** Coluna Tipo: “C” = CT-e; “M” = MDF-e      * TMOV – Movimentos * TCTE – Conhecimento de Transporte Eletrônico CT-e * TCTEHISTORICO – Histórico de CT-e * TCTRC – Notas Fiscais Conhec.Transporte * TCTESEGURO – Dados do Seguro do CT-e * TCTEEMISSOR – Dados do Emissor de Docs Anteriores CT-e * TCTEDOC – Dados dos Documentos Anteriores CT-e * TVEICULOS – Veículos * TXMLCOLAB – XML de Integração com o NeoGrid Client * TMOVTRANSP – Dados de Transporte * TVAGAO – Cadastro de Vagões * TCTEINUT – Inutilização do CT-e * DNATUREZA – Naturezas Fiscais * TNFEESTADUAL – Nota fiscal eletrônica * TNFEESTADUALHIST – Histórico da NF-e * TNFEMUNICIPAL – Nota Fiscal de Serviço eletrônica * TNFEMUNICIPALHIST – Histórico da NFS-e * TNFEESTADUALEVENT – Eventos da NF-e   TNFEESTADUALEVENTHIST – Histórico de Eventos da NF-e |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |

divs
