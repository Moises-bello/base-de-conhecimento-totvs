---
content_hash: 69404321de4de7aa60356f4fb970da39372b51bc77d3aa7de851d22de184739d
fetched_at: '2026-06-29T00:06:04.093779+00:00'
page_id: '200905444'
product: rm
source: tdn-rm
title: TTAIYL_DT_Funcao_BASEFGTS_Afastado
type: documentation
url: https://tdn.totvs.com/display/LRM/TTAIYL_DT_Funcao_BASEFGTS_Afastado
version: 2
---

# FUNÇÃO FÓRMULA BASEFGTS AFASTADO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Função de Fórmula* |
| **Situação/Requisito:** | *Função de fórmula BASEFGTS está duplicando o valor no primeiro cálculo, quando funcionário está afastado o mês inteiro e existe o evento de CC 315 no período.*  *Com o recálculo do envelope, o valor da função passa a ficar correto.* |
| **Solução/Implementação:** | *Ajustar o cálculo da função de fórmula BASEFGTS para não duplicar a base de funcionário afastado o mês inteiro, quando já existe o evento de CC 315 no envelope.*  *Na primeira vez que eram lançados o evento de CC 315 e o evento utilizando a função BASEFGTS, o cálculo da base de afastados procurava pelo CC 315 no mês. Como o evento ainda não estava inserido na tabela do banco, a base de FGTS de afastados era calculada novamente.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTAIYL* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
