---
article_id: 360018569672
category: PCO - Movimentos
content_hash: 295d9c355af71ab6182b9da8ceb0a553b1c4f1b98b303866abd5b98c14847e95
fetched_at: '2026-06-28T22:37:09.556035+00:00'
product: protheus
section_id: 1500001550962
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - Procedures Dinamicas
  SIGAPCO (Planejamento e Controle Orçamentário)
type: support-article
updated_at: '2023-11-21T13:39:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018569672-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Procedures-Dinamicas-SIGAPCO-Planejamento-e-Controle-Or%C3%A7ament%C3%A1rio
---

**Dúvida**Procedures Dinamicas SIGAPCO (Planejamento e Controle Orçamentário)

**Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
   
**Solução**

***PCOA122 - Query para obter recnos da tabela AK2 ou AK3 da nova versao***

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Função** | **Descrição** | **Postgre** |
| **PCOA122.PRW** | **CallXFilial** | Função xFilial para uso dentro do corpo das procedures dinâmicas do PCO, recebe como parâmetro as strings das variáveis da procedure a serem utilizadas | CREATE FUNCTION - Query returned successfully in 103 msec. |
| **PCOA122.PRW** | **Popula\_AK2** | Chama as funções que fazem a criação e instalação de procedures que geram níveis superiores para as entidades | CREATE FUNCTION - Query returned successfully in 582 msec. |
| **PCOA122.PRW** | **Popula\_AK3** | Chama as funções que fazem a criação e instalação de procedures que geram níveis superiores para as entidades | CREATE FUNCTION - Query returned successfully in 58 msec. |
| **PCOA122.PRW** | **PcoCriaPai** | Chama as funções que fazem a criação e instalação de procedures que geram níveis superiores para as entidades | CREATE FUNCTION - Query returned successfully in 93 msec. |
| **PCOA122.PRW** | **A122LastDay** | Cria procedure que retorna o último dia do mês | CREATE FUNCTION - Query returned successfully in 125 msec. |
| **PCOA122.PRW** | **PCOA122B** | Cria as procedures de atualização do AKT | CREATE FUNCTION - Query returned successfully in 78 msec. |
| **PCOA122.PRW** | **PCOA122A** | Cria procedures para atualização do AKT para os níveis superiores (sintéticas) do Cubo | CREATE FUNCTION - Query returned successfully in 258 msec. |
| **PCOA122.PRW** | **PCOA122Proc** | Cria procedures pai | CREATE FUNCTION - Query returned successfully in 82 msec. |
| **PCOA122.PRW** | **PCOA122\_Del** | Cria procedure de exclusão do AKD | CREATE FUNCTION - Query returned successfully in 603 msec. |

Rotinas que precisam ser alteradas

| **Rotina** | **Função** | **DESCRIÇÃO** |
| --- | --- | --- |
| **PCOA120.PRW** | **Pco120Frv** | Validação para o banco Postgre |
| **PCOXDIV.PRW** | **AuxRevisa** | Validação para o banco Postgre |

***PCOA300 - Rotina de reprocessamento de cubos***

| Rotina | Função | Descrição | Postgre |
| --- | --- | --- | --- |
| **PCOA300.PRW** | **A300LastDay** | Cria  procedure que retorna o ultimo dia do mês | CREATE FUNCTION - Query returned successfully in 603 msec. |
| **PCOA300.PRW** | **PCOA300B** | Cria as procedures de atualizacao do AKT | CREATE FUNCTION - Query returned successfully in 216 msec. |
| **PCOA300.PRW** | **PCOA300F** | Cria procedure Exclusao de AKT do periodo | CREATE FUNCTION - Query returned successfully in 109 msec. |
| **PCOA300.PRW** | **PCOA300A** | Cria procedures pa atualizacao do AKT para todos os niveis do cubo | CREATE FUNCTION - Query returned successfully in 237 msec. |
| **PCOA300.PRW** | **PCOA300Proc** | Cria procedures Pai | CREATE FUNCTION - Query returned successfully in 136 msec. |
| **PCOA300.PRW** | **CallXFilial** | Funcao xFilial para uso dentro do corpo das procedures dinamicas do PCO, recebe como parametro as strings das variaveis da procedure a serem utilizadas | CREATE FUNCTION - Query returned successfully in 300 msec. |

***PCOA310 - Programa para reprocessamento dos pontos de lançamento***

| Rotina | Função | Descrição | Postgre |
| --- | --- | --- | --- |
| **PCOA310.PRW** | **A310ProcDel** | Procedure para excluir registros da AKD do processo | CREATE FUNCTION - Query returned successfully in 68 msec. |
| **PCOA310.PRW** | **A310LOTAKD** | Funcao para lockar o proximo lote da AKD | CREATE FUNCTION - Query returned successfully in 72 msec. |
| **PCOA310.PRW** | **A310LoteId** | Funcao para gerar proximo id do lote | CREATE FUNCTION - Query returned successfully in 72 msec. |
| **PCOA310.PRW** | **A310Proced** | Criar procedure principal do reprocessamento de lancamentos | CREATE FUNCTION - Query returned successfully in 220 msec. |

***PCOC361-Programa de Consulta a visao por cubos em periodos***

| Rotina | Função | Descrição | Postgre |
| --- | --- | --- | --- |
| **PCOC361.PRW** | **Pco\_360Sld** | Retorna o array aProcessa quando chamada pela funcao PcoCub\_Vis() | CREATE FUNCTION - Query returned successfully in 598 msec. |

**Obs: A rotina é chamada pela rotina PCOC360.PRW ("Consulta Saldos por Periodo")**

Rotina que de ver alterado

| **Rotina** | **Função** | **DESCRIÇÃO** |
| --- | --- | --- |
| **PCOA361.PRW** | **Pco\_360Sld** | Validação para o banco Postgre |

***PCOXINC- Programa de montagem da tela de planilha orcamentaria***

| Rotina | Função | Descrição | PgAdmin |
| --- | --- | --- | --- |
| **PCOXINC.PRW** | **PcoCC\_User** | Funcao que verifica os direitos do Usuario x Centro Custo. | CREATE FUNCTION - Query returned successfully in 598 msec. |
| **PCOXINC.PRW** | **PcoIC\_User** | Funcao que verifica os direitos do Usuario x Item Contabil. | CREATE FUNCTION - Query returned successfully in 598 msec. |
| **PCOXINC.PRW** | **PcoSPAK5Sup** | Cria as procedures para popular a tabela de superiores | CREATE FUNCTION - Query returned successfully in 598 msec. |
| **PCOXINC.PRW** | **PcoSPCTTSup** | Cria as procedures para popular a tabela de superiores | CREATE FUNCTION - Query returned successfully in 598 msec. |
| **PCOXINC.PRW** | **PcoSPCTDSup** | Cria as procedures para popular a tabela de superiores - CTD Item Contábil | CREATE FUNCTION - Query returned successfully in 598 msec. |
| **PCOXINC.PRW** | **PcoSPCTHSup** | Cria as procedures para popular a tabela de superiores - CTH Classe de Valor | CREATE FUNCTION - Query returned successfully in 598 msec. |
| **PCOXINC.PRW** | **PcoSPCV0Sup** | Cria as procedures para popular a tabela de superiores - CV0 | CREATE FUNCTION - Query returned successfully in 598 msec. |
