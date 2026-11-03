---
content_hash: a197ef503a48cb4eedc12526346fc027b740a65175eaecd0bcab2315bbca6599
fetched_at: '2026-06-29T00:06:09.279178+00:00'
page_id: '203751774'
product: rm
source: tdn-rm
title: TTGGVL_Funcao_De_Formula_DUTEISMES
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGGVL_Funcao_De_Formula_DUTEISMES
version: 2
---

# FUNÇÃO DE FÓRMULA - DUTEISMES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Função de fórmula - DUTEISMES* |
| **Situação/Requisito:** | *Ao utilizar a função de fórmula do TOTVS Folha de Pagamento "DUTEISMES" o sistema retorna a seguinte mensagem, somente para uma coligada, as demais que utiliza a função de fórmula retorna o valor da função de fórmula com sucesso, abaixo segue mensagem:*  *ERRO no cálculo do evento "VerbaVTTotalEntregue" para funcionario 000067:*  *System.NullReferenceException: Referência de objeto não definida para uma instância de um objeto.*  *em RM.Fop.Facade.FopUtilsPto.GetBatidaHorario(Int16 CodColigada, String Chapa, DateTime DataInicio, DateTime DataFim, String CodUsuario)*  *em RM.Fop.UtilsMC.FopUtilsMC.GetBatidaHorario(Int16 codColigada, String chapa, DateTime dataInicio, DateTime dataFim, String codUsuario)*  *em RM.Fop.CalculosBase.FuncionarioBase.DiasTrabalhadosUteis(DateTime primeiroDia, DateTime ultimoDia, List`1 tiposConsiderar)*  *em RM.Fop.CalculosBase.VerbaVTTotalCalculado.DoCalcula()*  *em RM.Fop.CalculosBase.VerbaVTTotalEntregue.DoCalcula()*  *em RM.Fop.CalculosBase.VerbaBase.Calcula()* |
| **Solução/Implementação:** | *Foi realizado o ajuste para que a função de fórmula DUTEISMES não retorne jornadas nulas para o cálculo.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTGGVL* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
