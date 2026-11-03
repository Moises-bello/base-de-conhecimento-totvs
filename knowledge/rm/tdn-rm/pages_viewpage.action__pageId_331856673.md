---
content_hash: 6b99927480660169c2d00649d22756c1f4c35378ac26064006027bc756759465
fetched_at: '2026-06-29T00:08:49.711779+00:00'
page_id: '331856673'
product: rm
source: tdn-rm
title: 2068311 FISCAL01-3227 DT Geração DIRF 2018
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331856673
version: 4
---

# Rotina Federal DIRF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração de Arquivo para rotina Federal DIRF |
| **Situação/Requisito:** | Inconsistência ao gerar o arquivo da DIRF em base oracle.  Erro: ORA-03114: not connected to ORACLE  Ao executar a rotina DIRF está ocorrendo falha de conexão no banco de dados Oracle. |
| **Solução/Implementação:** | Foi removido e ajustado um subselect redundante da query que carrega as retenções  do Liber IRRF PF, IRRF PPJ ou COSIRF da rotina DIRF. |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Tickets relacionados:** | Não se Aplica |
| **Requisito:** | FIS000307 |
| **Documento de Referência:** | <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.DIRF.aspx> |
