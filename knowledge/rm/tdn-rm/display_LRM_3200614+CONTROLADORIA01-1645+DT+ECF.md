---
content_hash: 1a3e9a4f37435ab5129c747933236c138b0e1c7303824919f208ce1461a342fe
fetched_at: '2026-06-29T00:09:02.533105+00:00'
page_id: '379319302'
product: rm
source: tdn-rm
title: 3200614 CONTROLADORIA01-1645 DT ECF
type: documentation
url: https://tdn.totvs.com/display/LRM/3200614+CONTROLADORIA01-1645+DT+ECF
version: 4
---

# ECF registro K155

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Contábil. |
| **Função:** | ECF registro K155. |
| **Situação/Requisito:** | A apuração remove a informação do centro de custo / rateio gerencial da conta patrimonial quando a mesma não tem rateio. Mesmo que não esteja parametrizado para utilizar conta gerencial. |
| **Solução/Implementação:** | Implementar a verificação do parâmetro que retorna o tipo de informação para Centro de Custo no SPED contábil para que, ao ser validado na Apuração Virtual para a ECF a conta de patrimônio líquido que não possui distribuição gerencial, e deve ter o seu centro de custo gerencial removido, não efetue esta operação caso o tipo de informação esteja utilizado o próprio centro de custo e não a conta gerencial. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 3257022 |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
