---
content_hash: b21533c28f0fa6bc383d8933fff4821298173d410e28cfb13e6b66f611683ab7
fetched_at: '2026-06-29T00:08:03.837167+00:00'
page_id: '235326316'
product: rm
source: tdn-rm
title: TUOMOU_DT_Hora_Diferenca_Salarial_Varios_Meses
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOMOU_DT_Hora_Diferenca_Salarial_Varios_Meses
version: 2
---

# CAMPO HORA NO EVENTO DE DIFERENÇA DE VARIOS MESES SÓ DEMONSTRA VALOR DO ÚLTIMO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença Salarial* |
| **Situação/Requisito:** | *No cálculo da diferença salarial de um evento do tipo hora, quando o evento de diferença acumula valores de vários meses, o conteúdo do campo hora só demonstra a quantidade do último mês.*  *Por exemplo, no envelope do primeiro mes o evento de hora extra está com 10 horas, no segundo está com 20 horas.*  *Ao calcular a diferença retroativa aos dois meses, o evento de diferença de hora extra demonstra 20 horas.* |
| **Solução/Implementação:** | *Não podemos acumular a quantidade de horas dos eventos de todos os meses, porque este número não iria demonstrar o que foi calculado.*  *Será tratado no processo da diferença salarial para demonstrar o conteúdo do campo hora no evento de diferença, somente se neste evento constar o valor de um único evento original.*  *Se forem acumulados mais de um valor de diferença em um mesmo evento, o campo hora ficará vazio. A mesma regra será utilizada para o campo referência.* |
| **Chamados   relacionados:** | *TUOMOU, TUPF28* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
