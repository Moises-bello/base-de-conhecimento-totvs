---
content_hash: 77a5406f4383335ba69c072fff1ec951c783a8b974c3ebd7386f65d7c6f7d426
fetched_at: '2026-06-29T00:06:09.292459+00:00'
page_id: '203752382'
product: rm
source: tdn-rm
title: TTGTKA_Funcao_De_Formula_DUTEISMES
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGTKA_Funcao_De_Formula_DUTEISMES
version: 3
---

# FUNÇÃO DE FÓRMULA- DUTEISMES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Função de fórmula - DUTEISMES* |
| **Situação/Requisito:** | *Ao utilizar a função de fórmula do TOTVS Folha de Pagamento "DUTEISMES" o sistema retorna a seguinte mensagem, somente para uma coligada, as demais que utiliza a função de fórmula retorna o valor da função de fórmula com sucesso, abaixo segue mensagem:*  *ERRO no cálculo do evento "VerbaVTTotalEntregue" para funcionario 000067:*  *System.NullReferenceException: Referência de objeto não definida para uma instância de um objeto.*  *em RM.Fop.Facade.FopUtilsPto.GetBatidaHorario(Int16 CodColigada, String Chapa, DateTime DataInicio, DateTime DataFim, String CodUsuario)*  *em RM.Fop.UtilsMC.FopUtilsMC.GetBatidaHorario(Int16 codColigada, String chapa, DateTime dataInicio, DateTime dataFim, String codUsuario)*  *em RM.Fop.CalculosBase.FuncionarioBase.DiasTrabalhadosUteis(DateTime primeiroDia, DateTime ultimoDia, List`1 tiposConsiderar)*  *em RM.Fop.CalculosBase.VerbaVTTotalCalculado.DoCalcula()*  *em RM.Fop.CalculosBase.VerbaVTTotalEntregue.DoCalcula()*  *em RM.Fop.CalculosBase.VerbaBase.Calcula()* |
| **Solução/Implementação:** | *Foi realizado o ajuste para que a função de fórmula DUTEISMES não retorne jornadas nulas para o cálculo.* |
| **Chamados relacionados:** | *TTGTKA* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
