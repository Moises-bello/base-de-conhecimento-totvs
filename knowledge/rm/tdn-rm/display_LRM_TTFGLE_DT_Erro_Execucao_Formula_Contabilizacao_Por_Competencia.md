---
content_hash: 07f46673d146f179f883076f0158fbe2c43555022ef8515b50c69a3303242e1b
fetched_at: '2026-06-29T00:06:08.622505+00:00'
page_id: '201750900'
product: rm
source: tdn-rm
title: TTFGLE_DT_Erro_Execucao_Formula_Contabilizacao_Por_Competencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFGLE_DT_Erro_Execucao_Formula_Contabilizacao_Por_Competencia
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Contabilização por competência* |
| **Situação/Requisito:** | *Ao gerar o processo de contabilização do contrato educacional (Contabil/Estorno) o sistema me retorna o seguinte erro:*  *\*\*\* ERROS \*\*\**  *Não foi possível gerar a contabilização para o contrato 4161. O Evento Contábil 1-5 possui uma fórmula (CONT002) que não pode ser executada.*  *Verifique o item de Evento e as fórmulas correspondentes.*  *------------------------------------------------------------------------------*  *Detalhes*  *------------------------------------------------------------------------------*  *Erro:*  *There is no row at position 0.* |
| **Solução/Implementação:** | *Tratamento do código de integração com o Protheus que somente será chamado quando o parâmetro estiver marcado e antes da exclusão das tabelas SCONTRATOBOLSA e SCONTRATOSERVICO* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11\_83\_55* |
