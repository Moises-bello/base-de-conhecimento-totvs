---
content_hash: 63a03a2ad6072948cb01ed49c23f89332326c88cc4f9e3a58c80fbf1c78eea12
fetched_at: '2026-06-29T00:08:10.878049+00:00'
page_id: '241698925'
product: rm
source: tdn-rm
title: TVCBQ6_DT_Media_Salario_Maternidade_Calculo_Somente_Bases
type: documentation
url: https://tdn.totvs.com/display/LRM/TVCBQ6_DT_Media_Salario_Maternidade_Calculo_Somente_Bases
version: 2
---

# MEDIA DE SALÁRIO MATERNIDADE É RECALCULADA QUANDO CALCULA SOMENTE BASES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Salário Maternidade* |
| **Situação/Requisito:** | *Quando, após lançar Salário Maternidade pelo Grupo de Eventos, é marcado o flag "Forçar valores do Envelope" e executa o recálculo de somente Bases / Rateio C.Custo, está dobrando o valor da média na movimentação por centro de custo e no cadastro do funcionário, pasta Parâmetros, no campo Média Sal. Maternidade.* |
| **Solução/Implementação:** | *Ajuste no recálculo de somente Bases / Rateio C.Custo, quando existem valores de média no envelope marcado com o flag "Forçar valores do Envelope". Neste caso não deve haver recálculo das médias.* |
| **Chamados   relacionados:** | *TVCBQ6, TVDE10* |
| **Versões/Release:** | *12.1.12, 11.82.45* |
