---
content_hash: 3c64a1dc47610b76398ce15429b9af96a7f38fd08859fd396faa81d172c0eba6
fetched_at: '2026-06-29T00:08:57.173604+00:00'
page_id: '353277953'
product: rm
source: tdn-rm
title: FISCAL01-4333 DT Geração de Registro TAF - Notas inutilizadas na integração
  com TAF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353277953
version: 1
---

# Geração de Registro TAF - Notas inutilizadas na integração com TAF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração de Registro TAF |
| **Situação/Requisito:** | Ao tentar gerar os registro para integração com o TAF o sistema apresenta a seguinte mensagem de erro:  [09:54:08] ======================================================  [09:54:08] Ocorreu um erro inesperado na geração.  [09:54:08]  [09:54:08] System.NullReferenceException  [09:54:08] Erro: Referência de objeto não definida para uma instância de um objeto.  [09:54:08] ======================================================  [09:54:08]    em RM.Fis.Sped.FisNaturezaOperacaoCxt.get\_TresUltimosCodigoNaturezaSintetica()     em RM.Gen.Runtime.GenRuntimeModule.InsereT072\_Agrup\_GetTodosLancamentos(FisLancamentoFiscalCxt GetTodosLancamentosItem)     em RM.Gen.Runtime.GenRuntimeModule.OnExecute(List`1 files)     em TNF.Gen.Runtime.RuntimeModule.Execute() |
| **Solução/Implementação:** | Foi modificado o filtro do registro T072 para não ser gerado para as notas inutilizadas.  É necessário atualizar o Layout de integração com o TAF disponível na pasta objetos gerenciais no diretório de instalação do TAF |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Documento de Referência:** | Não se Aplica |
