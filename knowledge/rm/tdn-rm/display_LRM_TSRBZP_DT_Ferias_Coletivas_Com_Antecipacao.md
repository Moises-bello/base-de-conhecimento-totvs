---
content_hash: bec64b7a0d10d5a6bb748340d2f0aee5bf9e718b4d85dfa3f755ecae0515c48c
fetched_at: '2026-06-29T00:06:02.232224+00:00'
page_id: '198944921'
product: rm
source: tdn-rm
title: TSRBZP_DT_Ferias_Coletivas_Com_Antecipacao
type: documentation
url: https://tdn.totvs.com/display/LRM/TSRBZP_DT_Ferias_Coletivas_Com_Antecipacao
version: 1
---

# FÉRIAS COLETIVAS ANTECIPANDO DIAS DO PERIODO AQUISITIVO SEGUINTE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Férias Coletivas* |
| **Situação/Requisito:** | *Quando está marcado o parâmetro "Permite antecipação de dias de férias do próximo período aquisitivo" no Sindicato, ao lançar férias coletivas para funcionário com mais de 1 ano de casa, que não possui férias vencidas, está sendo antecipado número de dias incorreto do período aquisitivo seguinte.* |
| **Solução/Implementação:** | *Ajustar o cadastro de férias coletivas, no tratamento do parâmetro "Permite antecipação de dias de férias do próximo período aquisitivo" do Sindicato, para fazer a correta antecipação dos número de dias de férias o período aquisitivo posterior ao período em aberto.*  *Quando o funcionário com mais de 1 ano de casa, ainda não possui férias vencidas, irá ocorrer um adiantamento do saldo do período.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSRBZP* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
