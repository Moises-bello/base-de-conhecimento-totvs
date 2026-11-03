---
content_hash: 2b5f3eb648e361a22b2f288298cc428b6f108cbc837dc307463010e864a243c0
fetched_at: '2026-06-29T00:06:30.272260+00:00'
page_id: '235318155'
product: rm
source: tdn-rm
title: TTXZB4_DT_Arredondamento_Alteracao_Salario_Composto
type: documentation
url: https://tdn.totvs.com/display/LRM/TTXZB4_DT_Arredondamento_Alteracao_Salario_Composto
version: 2
---

# ARREDONDAMENTO INCORRETO NA ALTERAÇÃO SALARIAL DE SALÁRIO COMPOSTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Alteração Salarial* |
| **Situação/Requisito:** | *No processamento da alteração salarial de funcionário horista, utilizando salário composto, ocorre diferença de centavos devido a arredondamento para 2 casas decimais. E quando é acessado o campo de salário hora no cadastro do salário composto, o valor do salário do funcionário é alterado novamente.*  *Por exemplo: Salário de 2601,00 com uma jornada de 112,5 horas, resultando em um salário hora de 23,12.*  *Se for aplicado um aumento salarial de 0,5%, passa-se o salário para 2614,00, resultando em um salário hora de 23,2356. Quando arredondado para 2 casas decimais, o salário hora passa a ser de 23,24.*  *Ao acessar o campo no cadastro do salário composto, é executada a conta reversa, de 23,24 \* 112,5, e assim altera o salário do funcionário para 2614,50.* |
| **Solução/Implementação:** | *Ajuste na alteração salarial de funcionário horista, para efetuar a conta reversa com o salário hora já arredondado para duas casas decimais, antes de gravar o salário mensal do funcionário.* |
| **Chamados   relacionados:** | *TTXZB4, TUOKN1* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
