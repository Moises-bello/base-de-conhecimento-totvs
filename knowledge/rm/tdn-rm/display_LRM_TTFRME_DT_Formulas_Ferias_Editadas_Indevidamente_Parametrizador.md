---
content_hash: 55e15778b4014f9bcdf5773c59d35618c170bbd5e2ff8e1542e83745c7840780
fetched_at: '2026-06-29T00:06:10.361348+00:00'
page_id: '203762442'
product: rm
source: tdn-rm
title: TTFRME_DT_Formulas_Ferias_Editadas_Indevidamente_Parametrizador
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFRME_DT_Formulas_Ferias_Editadas_Indevidamente_Parametrizador
version: 1
---

# FÓRMULAS DE FÉRIAS EDITADAS INDEVIDAMENTE NO PARAMETRIZADOR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Parametrizador* |
| **Situação/Requisito:** | *As fórmulas para "Número de dias de direito a férias" e "Dias de férias x faltas" estão sendo editadas no Parametrizador, pasta Férias/Fórmulas, como opção de preenchimento para o cálculo das férias.*  *Entretanto esses campos foram descontinuados, e o sistema nunca realizou tratamento algum para estas fórmulas no cálculo .Net.* |
| **Solução/Implementação:** | *Remover a edição das fórmulas para "Número de dias de direito a férias" e "Dias de férias x faltas" do Parametrizador, pasta Férias/Fórmulas.*  *Obs.: No parametrizador Delphi (Opções> Parâmetros> RM Labore) os campos já foram removidos.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTFRME* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
