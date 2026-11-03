---
content_hash: 3e903cb20b86be41f0410247bd2de16cae85663beed2b9761e0d1831c2895b27
fetched_at: '2026-06-29T00:08:29.040467+00:00'
page_id: '272142528'
product: rm
source: tdn-rm
title: MRH-7628 DT Historico Chapa Centralizadora
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-7628+DT+Historico+Chapa+Centralizadora
version: 118
---

# CRIAÇÃO DO HISTÓRICO DE CHAPA CENTRALIZADORA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Funcionário* |
| **Situação/Requisito:** | Quando existem múltiplos vínculos para uma mesma pessoa, e é utilizada uma Chapa Centralizadora para o desconto dos encargos, deverá ser guardado o histórico de alteração desta Chapa.  Isto é necessário para possibilitar a verificação de informações para a DIRF Anual, como o cadastro de Dependentes de IRRF, que estará vinculado à Chapa Centralizadora.. |
| **Solução/Implementação:** | No processo "Definição da(s) chapa(s) e coligada centralizadora(s) de IRRF/INSS" do cadastro do funcionário, sempre que for informada uma Chapa Centralizadora, será gerado um registro de histórico na tabela PPESHSTCHAPACENTRAL. |
| **Tickets relacionados:** | MRH-7628 |

divs
