---
content_hash: f30f7ab8124025251a3c221acb75823677ef2162c97e3ea73dc45ecb47de4e71
fetched_at: '2026-06-29T00:08:18.836611+00:00'
page_id: '266970722'
product: rm
source: tdn-rm
title: TVGFV3_DT_DiasTrab_Admissao_Demissao_Dias_Totais_Mes
type: documentation
url: https://tdn.totvs.com/display/LRM/TVGFV3_DT_DiasTrab_Admissao_Demissao_Dias_Totais_Mes
version: 1
---

# DIAS TRABALHADOS NA ADMISSÃO E DEMISSÃO CONSIDERAR DIAS TOTAIS DO MÊS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Folha Mensal* | *Cálculo da Folha Mensal* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Folha Mensal** | *Cálculo da Folha Mensal* | | *Rescisão* | *Cálculo de Rescisão* | |
| **Cadastros Iniciais:** | *Parametrizador* |
| **Parâmetro(s):** | *Considera divisor pelo número de dias do mês na remuneração da Admissão e Demissão* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *TVGFV3, TVQVAP* |
| **Requisito (ISSUE):** | *Folha* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server, Oracle* |
| **Tabelas Utilizadas:** | *PPARAMADICIONAIS* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Cliente solicita que seja efetuado o cálculo de dias trabalhados de mensalista nos meses de admissão e rescisão, conforme a quantidade de dias do mês, conforme Artigo 64 da CLT.

Já existe no sistema o parâmetro "Usa mês comercial na admissão". Este parâmetro modifica a parte do multiplicador do cálculo, sendo que a divisão é sempre por 30.

A solicitação do cliente é que a divisão nos meses de admissão e demissão seja pelo total de dias do mês.

Foi criado um novo parâmetro no Parametrizador, pasta Folha Mensal/Cálculo, "Considera divisor pelo número de dias do mês na remuneração da Admissão e Demissão".

Este novo recurso não poderá ser utilizado junto com o parâmetro "Usa mês comercial na admissão", ou seja, para marcar um o outro tem que estar desmarcado. Isto, porque se o multiplicador for limitado a 30 dias, não podemos utilizar no divisor o total de dias do mês.

O novo parâmetro não será considerado para funcionários Horistas e Tarefeiros.
