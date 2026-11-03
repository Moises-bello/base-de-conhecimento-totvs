---
content_hash: a45ec16fbfaa946cee1e7a8a1c6db6cba3eadfa8841a4051f1027ab7541a2f59
fetched_at: '2026-06-29T00:06:25.752830+00:00'
page_id: '224444701'
product: rm
source: tdn-rm
title: TUEPIK_DT_Mensagem_Referente_Compensação_Em_Competências_Anteriores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224444701
version: 124
---

# DIRF/INFORME DE RENDIMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | Ao gerar a DIRF/Informe de Rendimentos para funcionário que em algum mês tiveram valores  de Restituição de INSS maior do que o valor de desconto de INSS, o sistema apresenta a seguinte mensagem:  Avisos encontrados para a Chapa: 00020 - CARLOS VICENTINO MORAES Compensação do Cálculo 'INSS: Rendimentos Recebidos Acumuladamente' de valor negativo em  competências anteriores. Valor -505,53  Essa mensagem não é coerente com a situação, pois, nesse caso não há nenhuma relação com RRA(Rendimentos Recebidos Acumuladamente). Sendo assim é necessário que essa mensagem seja ajustada para que fique mais clara para o cliente e também para o suporte. |
| **Solução/Implementação:** | *Ajustado mensagem quando tem INSS negativo em alguma competência. O sistema tenta compensar em competências anteriores, por isso é feito este log para explicar o cálculo.* |
| **Chamados relacionados:** | *TUEPIK,TUFRDB* |

divs
