---
content_hash: ca8efc05e1db2a6a30a24abb78d1db03d3c15a5fd8d22a058c3e0df586e95879
fetched_at: '2026-06-29T00:08:58.921654+00:00'
page_id: '361452410'
product: rm
source: tdn-rm
title: 2783387 FISCAL01-4650 DT Geração de Registro TAF - REINF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=361452410
version: 2
---

# Geração de Registro TAF - REINF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração de Registro TAF |
| **Situação/Requisito:** | 1 - Ao gerar os registros para integração com o TAF, o sistema apresenta uma mensagem de inconsistência:  Consulta uma cadeia de caracteres localizada semelhante a não há nenhum registro para ser salvo. [12:40:42] System.NullReferenceException [12:40:42] Erro: Referência de objeto não definida para uma instância de um objeto. [12:40:42] ====================================================== [12:40:42] em RM.Gen.Runtime.GenRuntimeModule.InsereT013AO\_GetTodosLancamentos(T013Record T013,  FisLancamentoFiscalCxt GetTodosLancamentosItem) em RM.Gen.Runtime.GenRuntimeModule.InsereT013\_GetTodosLancamentos(FisLancamentoFiscalCxt  GetTodosLancamentosItem) em RM.Gen.Runtime.GenRuntimeModule.OnExecute(List`1 files) em TNF.Gen.Runtime.RuntimeModule.Execute()  2 - Cliente entrou em contato informando que ao integrar o registro T007 com o TAF, está sendo apresentado erro no código da ANP. informando o seguinte erro:  Erro 1 - Linha: 1 O valor '820' informado na coluna 20 para o campo ( C1L\_IDCFQ ) não existe na base de dados.  O mesmo informa que conforma a tabela, o campo deve ser preenchido com 9 dígitos, e somente esta levando para o TAF 3 dígitos. Dessa forma ao tentar integrar está sendo apresentada a mensagem de erro. |
| **Solução/Implementação:** | 1 - Foi implementada uma validação para que ao gerar o Registro T013AO o sistema não apresente este erro.  Obs.: O Erro ocorre por existir na Base Lançamentos Fiscais sem dados de Transporte, como  alguns campos deste registro são obrigatórios e originados destes dados o sistema só ira  gerar este registro se tiver dados de Transporte no Lançamento Fiscal  2 - Foi retirada a ligação do campo 20-COD\_CFQ do Registro T007 |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Documento de Referência:** | Não se Aplica |
| **Issues Relacionadas:** | FISCAL01-4650 FISCAL01-4596 FISCAL01-4664 |
