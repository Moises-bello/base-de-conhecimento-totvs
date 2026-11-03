---
content_hash: 3987a831c04f01611139d73d992d333ef9f7be00a6477de21827220c3ea76390
fetched_at: '2026-06-29T00:09:00.180071+00:00'
page_id: '364923540'
product: rm
source: tdn-rm
title: 2881635 FISCAL01-4828 REINF - Registro T001AB - Erro na geração do código do
  município
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364923540
version: 2
---

# Integração RM X TAF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Integração RM X TAF |
| **Situação/Requisito:** | Ao processar a integração com o TAF é apresentado a seguinte mensagem:  Erro 1 - Linha: 1 O valor 'MG' informado na coluna 14 para o campo Id. da UF da Vara ( C1G\_UFVARA ) somado ao valor '10620' informado na coluna 15 para o campo Id. Município Vara ( C1G\_CODMUN ) não existe na base de dados. |
| **Solução/Implementação:** | No campo 15 (CODMUNIC) do registro T001AB a expressão que antes era:  ListaProcessoItem.CodMunicipio !**=** null && ListaProcessoItem.CodMunicipio.Length **==** 7 ? ListaProcessoItem.CodMunicipio.Substring(1,5): ListaProcessoItem.CodMunicipio  Foi alterada para:  ListaProcessoItem.CodMunicipio !**=** null && ListaProcessoItem.CodMunicipio.Length **==** 7 ? **ListaProcessoItem.CodMunicipio.Substring(2,5)**: ListaProcessoItem.CodMunicipio |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Tickets relacionados:** | 2881635 |
| **Requisito:** | Não se Aplica |
| **Documento de Referência:** | Não se Aplica |
