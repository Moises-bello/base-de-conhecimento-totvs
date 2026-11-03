---
content_hash: 73067059e55ccd5f353f4f61643282ed33fd63b23150bf5bf034dd4098863fcb
fetched_at: '2026-06-29T00:08:17.232350+00:00'
page_id: '254609754'
product: rm
source: tdn-rm
title: TVLYSI_DT_CalculoVT_Linha_Iniciando_Meio_Mes_Corrente
type: documentation
url: https://tdn.totvs.com/display/LRM/TVLYSI_DT_CalculoVT_Linha_Iniciando_Meio_Mes_Corrente
version: 2
---

# CÁLCULO DE VT QUANDO A LINHA TEM DATA DE INÍCIO NO MEIO DO MÊS CORRENTE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Vale Transporte* |
| **Situação/Requisito:** | *Quando a data de início da utilização de uma Linha de VT é no meio do mês corrente, é calculado o número de dias úteis a serem trabalhados pelo funcionário à partir desta data, considerando dados de férias, afastamento, admissão, feriados e escala de horário.*  *Caso este número seja menor que os dias úteis informado no cadastro do funcionário, ele passa a ser utilizado no cálculo do CC 32, Total entregue de VT.*  *O problema ocorria quando o funcionário não tinha uma escala de horário válida, e este cálculo retornava zero. Ai não estava sendo calculado o evento de CC 32.* |
| **Solução/Implementação:** | *Foi tratado para fazer o comparativo dos dias úteis calculado com o dias úteis cadastrado somente se o calculado retornar maior que zero.* |
| **Chamados   relacionados:** | *TVLYSI, TVTPFN* |
| **Versões/Release:** | *11.82.46, 12.1.14* |
