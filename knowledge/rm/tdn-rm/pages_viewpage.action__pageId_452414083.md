---
content_hash: 6cc379e4511667a27aa6e54e44645e9a0a03da92df19a232f6fe804a44437cd2
fetched_at: '2026-06-29T00:09:58.294524+00:00'
page_id: '452414083'
product: rm
source: tdn-rm
title: 4331486 FISCAL01-7721 DT EFD Contribuições - Registro 1900 e F500
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452414083
version: 2
---

# EFD Contribuições

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração do Arquivo EFD Contribuições |
| **Situação/Requisito:** | Ao gerar o EFD Contribuições foi apresentado a seguinte mensagem:  [15:20:19] ====================================================== [15:20:19] Devart.Data.Oracle.OracleException [15:20:19] Erro: ORA-03114: not connected to ORACLE [15:20:19] ====================================================== [15:20:19] em RM.Lib.Data.DbServices.OLCOPDMNHFAPPAGKCDHABAILNKHPECIMGDPO(DataSet , String , String , Int32 , Int32 , Object[] parameters) em RM.Lib.Data.DbServices.QueryFill(DataSet dataSet, String tableName, String sqlText, Object[] parameters) em RM.Lib.Data.DbServices.QueryFillUnSec(DataSet dataSet, String tableName, String sqlText, Object[] parameters) em RM.Fis.Sped.FisSpedContextGeradorLoader.CarregaDadosF500FiscaleMovimento(FisSpedParams parametros, DataSet dataSet, RMSStringList listaFiltrosF500, List`1 listaFiltroTipoDoc) [15:20:19] ====================================================== [15:20:19] Geração concluída com erros. Duração: 0:0:5,406 |
| **Solução/Implementação:** | EFD Contribuições  Ajuste nas consultas SQL que carregam os registros F500 e 1900, para que evite inconsistências com o banco de dados oracle. |
| **Requisito:** | FIS000385 |
