---
content_hash: da6863947c0e826cad3c6928751a58742d3f99e4e1b0082a8e76e06a472e667b
fetched_at: '2026-06-29T00:06:10.670708+00:00'
page_id: '203766025'
product: rm
source: tdn-rm
title: ER_PCREQ-7763_Conversor_Integracao_Educacional_Protheus
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-7763_Conversor_Integracao_Educacional_Protheus
version: 7
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Gestão Educacional |
| **Segmento Executor** | Educacional | | |
| **Projeto** | R\_EDU\_CTB004 | **IRM** | PCREQ-7762 |
| **Requisito** | PCREQ-7763 | **Subtarefa** | PDR\_EDU\_CTB003-555 |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** | Não |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

## Objetivo

Ajustar a base de dados do RM para o correto funcionamento da integração do Educacional x BackOffice Protheus via mensagem única, devido a integração antiga (via stored procudure) fazer inserts, updates, etc direto no banco de dados. 

## Definição da Regra de Negócio

O conversor deverá executar os seguintes passos:

* Validar o saldo da conta corrente dos alunos. Caso existem alunos com saldo na conta corrente, exibir uma mensagem informando a necessidade de executar o assistente para "Aproveitar valores em conta corrente". Ou seja, é uma premissa para executar o conversor que não exista saldo em conta corrente dos alunos.
* Alterar o campo GERANUMDOC (Gera número do documento) da tabela FTDO (Tipo de Documento) para o valor 0 (zero) dos registros que estiverem com o valor nulo.
* Alterar o campo TIPOCONTABILLAN (Tipo Contábil) para o valor 0 (zero) e o campo CODAPLICAO (Aplicação de Origem) para o valor 'F' da tabela FLAN (Lançamento) dos registros com o CODAPLICACAO = 'PR'.
* Atualizar o campo IDCONVENIO (Id. do Convênio) da FLAN (Lançamento) de acordo com o convênio referente a conta caixa dos lançamentos dos registros que estiverem com o valor nulo.
* Executar o processo de Conversão para Boletos do TOTVS Gestão Financeira.
* Efetuar a carga nas tabelas SCLASSEVALORPROTHEUS (Classe de Valor) e SITEMCONTABILPROTHEUS(Item Contábil) de acordo com parametrizações existentes nas tabelas SHABILITACAOFILIALINTPROTHEUS, SPSPROCSELINTPROTHEUS e LUNIDADEPARAMPROTHEUS.
* Converter os lançamentos financeiros de origem do Educacional, Processo Seletivo e Biblioteca registrados no RM para obedecer a regra de negócio do novo modelo de baixa. Para os lançamentos do Educacional acertar as baixas referentes as bolsas, caso existem.
* Atualizar o campo SERIEDOCUMENTO (Série do Documento) da tabela FLAN (Lançamento) com o valor do campo PREFIXO da tabela INT\_TITULO da base de dados do Protheus, do ultimo registro referente ao lançamento.
* Limpar os parâmetros, da etapa 4 (cobrança retroativa), de integração financeira do Educacional, pois os mesmos não serão mais utilizados na integração do Totvs Educacional com o BackOffice Protheus.

Deverá ser implementado uma classe, descendente da classe RM.Upg.Server.UpgBaseServer, para que o conversor seja executado pelo RM.Atualizador.exe.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
