---
content_hash: e7bb58e7ea4e211772e617cdf9ce6b1b86ad3c8394213a2a956aa15f50c70330
fetched_at: '2026-06-29T00:08:51.899286+00:00'
page_id: '338368295'
product: rm
source: tdn-rm
title: 2284864 FISCAL01-3639 DT EFD Contribuições 0200
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338368295
version: 1
---

# EFD Contribuições

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração do Arquivo EFD Contribuições |
| **Situação/Requisito:** | Na geração da rotina EFD Contribuições (SPED PIS/Cofins) ocorre a inconsistência:  “System.FormatException   Erro: A cadeia de caracteres de entrada não estava em um formato incorreto. ”.    Mensagem de erro completa:    “...  [15:16:07] F525 - Indicador da composição da receita recebida no período : 1  [15:16:07] ======================================================  [15:16:33] ======================================================  [15:16:33] Ocorreu um erro inesperado na geração.  [15:16:33]   [15:16:33] System.FormatException  [15:16:33] Erro: A cadeia de caracteres de entrada não estava em um formato incorreto.  [15:16:33] ======================================================  [15:16:33] em System.Number.StringToNumber(String str, NumberStyles options, NumberBuffer& number, NumberFormatInfo info, Boolean parseDecimal)  em System.Number.ParseInt32(String s, NumberStyles style, NumberFormatInfo info)  em RM.Lib.RMSConvert.ToInt32(Object value, Int32 nullValue)  em RM.Lib.RMSConvert.ToInt32(Object value)  em RM.Gen.Runtime.GenRuntimeModule.InsereRegistro0200\_ListaItem(Registro0140Record Registro0140, FisItemLancamentoCxt ListaItemItem, FisLancamentoFiscalCxt GetTodosLancamentosItem)  em RM.Gen.Runtime.GenRuntimeModule.InsereRegistro0140\_GetTodosLancamentos(FisLancamentoFiscalCxt GetTodosLancamentosItem)  em RM.Gen.Runtime.GenRuntimeModule.OnExecute(List`1 files)  em TNF.Gen.Runtime.RuntimeModule.Execute()  [15:16:33] ======================================================  [15:16:33] Geração concluída com erros. Duração: 0:0:26,35”. |
| **Solução/Implementação:** | Gerar o campo (08)COD\_NCM  do registro 0200 sem a conversão para inteiro. o mesmo continuara gerando apenas o código do NCM sem mascara ignorando caracteres especiais. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | Não se Aplica |
| **Requisito:** | FIS000385 |
| **Documento de Referência:** | Não se Aplica |
