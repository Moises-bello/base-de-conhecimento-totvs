---
content_hash: ffde097ba8079833fcd9d1202a94800efe4c753a2746cce5cd3fed26e502b6ec
fetched_at: '2026-06-29T00:08:09.159247+00:00'
page_id: '239026259'
product: rm
source: tdn-rm
title: TUZVJ0_DT_DIASTRAB_Relatorio_Delphi_Chamar_Calculo_Net
type: documentation
url: https://tdn.totvs.com/display/LRM/TUZVJ0_DT_DIASTRAB_Relatorio_Delphi_Chamar_Calculo_Net
version: 1
---

# FUNÇÃO DIASTRAB UTILIZADA NO GERADOR DE RELATÓRIOS DELPHI DEVE CHAMAR CÁLCULO .NET

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Fórmula* |
| **Situação/Requisito:** | *A formula DIASTRAB só existe em .Net, por isso deve ser criado um método em .Net que possa ser acionado pelo Delphi.*  *Será passado pela MDI Delphi a Coligada, Chapa, Data de Início, Data Fim, Inicio do Intervalo, Fim do Intervalo, Situação e Parametros Gerais.* |
| **Solução/Implementação:** | *Feito tratamento para que, q**uando for utilizada a função DIASTRAB em relatórios do Gerador Delphi, seja desviada a execução para o cálculo .Net.* |
| **Chamados   relacionados:** | *TUZVJ0, TVARB9* |
| **Versões/Release:** | *11.82.44, 12.1.12* |
