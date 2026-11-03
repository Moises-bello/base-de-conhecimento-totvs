---
content_hash: 7ae9424c9347bbc1aaae63aaee12198567923bb7ff9dac75500a3f241e6f0a0d
fetched_at: '2026-06-29T00:08:12.945209+00:00'
page_id: '243655261'
product: rm
source: tdn-rm
title: TVC830_DT_Comparar_Tributos_que_nao_existem_no_XML
type: documentation
url: https://tdn.totvs.com/display/LRM/TVC830_DT_Comparar_Tributos_que_nao_existem_no_XML
version: 110
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | CLB.007 | TOTVS COLAB - INCLUSAO MOVIMENTO A PARTIR DE XML | |
| **Cadastros Iniciais:** | *-* |
| **Parâmetro(s):** | *-* |
| **Ponto de Entrada:** | *-* |
| **Chamados Relacionados** | TVCBLB |
| **Requisito (ISSUE):** | MOV000161 - TOTVS Colaboração |
| **País(es):** | *Bra* |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | - |
| **Sistema(s) Operacional(is):** | *-* |

## Descrição

O Comparador de Tributos do TOTVS Colaboração 2.0 apresentará na tela os impostos com divergência quando os mesmos constam do movimento mas não constam do XML. Esse processo será feito para os tributos ICMS, ICMS ST e IPI.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.12*

## Procedimento para Utilização

 1.            Parametrize o tipo de movimento para buscar tributos no tipo de movimento.

 2.            Inclua um movimento com XML que contenha menos tributos dos que os parametrizados (por exemplo ICMS ST) e, salve o movimento gerando valores desse tributo.

 3.            O Sistema deverá gerar a comparação com a coluna "Valor XML" com valor  igual a Zero e coluna "Valor Calculado" com o valor calculado pelo movimento.

 4.            Um Exemplo do resultado descrito pode ser visto na imagem abaixo.

divs
