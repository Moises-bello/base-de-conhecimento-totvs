---
content_hash: 335583afaba3c5ebfdfb83d4fc3006767603c4a3d63a8edf423a20efe7f827e2
fetched_at: '2026-06-29T00:08:03.935324+00:00'
page_id: '235330038'
product: rm
source: tdn-rm
title: TUMFPL_DT_Envelope
type: documentation
url: https://tdn.totvs.com/display/LRM/TUMFPL_DT_Envelope
version: 114
---

# ENVELOPE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Envelope* |
| **Situação/Requisito:** | Salario inconsistente na visualização do envelope de pagamento.  Na visualização do Envelope de Pagamento do mês corrente do funcionário o sistema mostra na parte superior do lado direito da chapa/nome do funcionário, a soma do salário composto e do lado o valor por hora, onde é dividido o total de salário composto pela soma das horas para chegar no valor de 1 hora.  No exemplo da funcionária 10072 - Ana Carolina Piragine Contador ela tem os seguintes salários compostos:  0298 / R$ 41,49 / 1:00Hs  0360 / R$ 3.994,95 / 112:30Hs  0377 / R$ 35,34 / 1:00Hs  A soma é R$ 4.071,78  E o valor Hora é 4.071,78 / 114:30 = R$ 35,56.  O problema é que nos envelopes anteriores a competência atual, o valor da soma dos salários compostos é de R$ 11.759,58 e o valor de 1 hora é de R$ 221,60 e a funcionária não tem esse salário |
| **Solução/Implementação:** | Ajuste na rotina que retorna o valor do salário do funcionário, de forma que a rotina não some valores de  salários duplicados. O sistema estava somando mais de uma vez o valor para cada número de salário  *.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUMFPL |
| **Requisito (ISSUE):** |  |

divs
