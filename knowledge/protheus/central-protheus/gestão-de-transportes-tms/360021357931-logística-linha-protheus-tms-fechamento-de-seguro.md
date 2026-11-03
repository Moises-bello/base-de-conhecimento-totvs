---
article_id: 360021357931
category: Gestão de Transportes (TMS)
content_hash: 95da29f787dc6bfbc49aa23aa31aee85cd5e07bdbe9f029e8e75653cdcd15cf3
fetched_at: '2026-06-28T22:45:29.176860+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Fechamento de Seguro
type: support-article
updated_at: '2022-01-06T20:16:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021357931-Log%C3%ADstica-Linha-Protheus-TMS-Fechamento-de-Seguro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)**Tempo aproximado para leitura: **00:01:40 min  
  
Dúvida**Como executar o processo de **Fechamento de Seguro**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
Para executar o processo de fechamento de seguro é preciso realizar o seguinte procedimento:

1. É necessário que o **CT-e** **- Conhecimento de Transporte Eletrônico** esteja autorizado na **SEFAZ** **- Secretaria de Estado da Fazenda** para iniciar o processo;
2. A Seguradora cadastrada no parâmetro **MV\_FORSEG** deve estar cadastrada na rotina **Seguradoras** - **TMSA295;**
3. Ter os componentes de Seguro cadastrados na rotina **Componentes** - **TMSA290;**
4. Ter cadastrada as Tabelas de Seguro na rotina **Tabela - TMSA300**, onde:  
   4.1. Definir Modal do tipo da tabela de Seguro - **DU4\_TPTSEG**.  
   4.2. Definir Vigência da tabela - **DU4\_DATDE** e **DU4\_DATATE**.  
   4.3. Nos componentes, informar o produto do cliente - Produto informado no campo **DTC\_CODPRO** em **TMSA050** ou o produto genérico informado no parâmetro **MV\_PROGEN**, valor e fração do seguro e por fim, Origem e Destino da Prestação do serviço de transporte ou deixar em branco caso os valores forem abranger todas as regiões.
5. Na rotina **Serviços x Tarefas -** **DLGA070**, relacionar a tabela de seguro ao serviço da nota no campo **Tab. Seguro - DC5\_TABSEG**. É por meio deste campo que iremos relacionar a tabela que utilizaremos para determinar os valores do seguro para este serviço.
6. Com o processo feito, basta acessar a rotina **Fechamento de Seguro** - **TMSA330** e executar o comando Fechar.
7. Esse processo grava a numeração no campo **DT6\_DOCSEG**, podendo ser consultado posteriormente para a geração do**MDF-e - Manifesto Eletrônico de Documentos Fiscais**.

**Importante**Quando o Cliente é o responsável pelo Seguro da Carga, o Sistema busca o número da averbação informado no cadastro de **Averbação do Cliente -** **TMSA650** no campo **DV6\_NUMAVB**.
