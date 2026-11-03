---
content_hash: 5d97e0e80e9b07fecda90170dc0d776c77b881ddc98c847d2a18cdcd01ae0262
fetched_at: '2026-06-29T00:06:04.077059+00:00'
page_id: '200905284'
product: rm
source: tdn-rm
title: TT4204_DT_Funcao_BASEFGTS_Afastado
type: documentation
url: https://tdn.totvs.com/display/LRM/TT4204_DT_Funcao_BASEFGTS_Afastado
version: 3
---

# FUNÇÃO FÓRMULA BASEFGTS AFASTADO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Fórmula* |
| **Situação/Requisito:** | *Função de fórmula BASEFGTS está duplicando o valor no primeiro cálculo, quando funcionário está afastado o mês inteiro e existe o evento de CC 315 no período.*  *Com o recálculo do envelope, o valor da função passa a ficar correto.* |
| **Solução/Implementação:** | *Ajuste no cálculo da função de fórmula BASEFGTS para não duplicar a base de funcionário afastado o mês inteiro, quando já existe o evento de CC 315 no envelope.*  *Na primeira vez que eram lançados o evento de CC 315 e o evento utilizando a função BASEFGTS, o cálculo da base de afastados procurava pelo CC 315 no mês. Como o evento ainda não estava inserido na tabela do banco, a base de FGTS de afastados era calculada novamente.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TT4204* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
