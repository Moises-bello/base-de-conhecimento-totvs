---
content_hash: 996975fb27bd0cf43b9c0dae8bd231c6f7840862dc238ed48b1a290bc46bfe7c
fetched_at: '2026-06-29T00:09:12.281732+00:00'
page_id: '416848412'
product: rm
source: tdn-rm
title: 3947532 DEDUINTEGRACOES-3403 DT Filtro de contratos no processo de criação
  de parcelas de contratos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=416848412
version: 79
---

# FILTRO DE CONTRATOS NO PROCESSO DE CRIAÇÃO DE PARCELAS DE CONTRATOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Criação de parcelas de contratos* |
| **Situação/Requisito:** | *O filtro de contratos está retornando o erro abaixo:*  Foi definido um filtro não suportado por este processo. O filtro deve fazer referência apenas a colunas existentes nas tabelas:  [SALUNO] [PPESSOA] [SCONTRATO] [SHABILITACAOFILIAL]  [SHABILITACAO] [SGRADE] [STURNO] [SCURSO]  Filtro definido:  SCONTRATO.IDPERLET = :IDPERLET AND SCONTRATO.TIPOCONTRATO <> 'A' AND (SCONTRATO.STATUS = 'N' OR SCONTRATO.STATUS IS NULL) AND SPLETIVO.CODPERLET = :F1 AND  SMATRICPL.CODTURMA = :F2  The multi-part identifier "SPLETIVO.CODPERLET" could not be bound.  The multi-part identifier "SMATRICPL.CODTURMA" could not be bound. |
| **Solução/Implementação:** | - Acréscimo das tabelas abaixo na consulta de contratos por filtro do corpore:      - SMATRICPL  (Para buscar o campo Código da turma)     - SPLETIVO   (Para buscar o código do período letivo)     - SPLANOPGTO (Para buscar a descrição do plano de pagamento)  - Tratamento dos campos: CODCURSO, CODHABILITACAO, CODGRADE e CONSIDERADESCANTECIPACAO no props de contratos que não exibiam a descrição do campo e sim o campo puro da base de dados. |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *DEDUINTEGRACOES-3403* |

divs
