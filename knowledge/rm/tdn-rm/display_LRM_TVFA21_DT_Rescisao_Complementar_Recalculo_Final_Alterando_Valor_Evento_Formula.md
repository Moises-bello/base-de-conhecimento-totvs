---
content_hash: 6495e26b77d9cff3f0702c1fcef72478c9fde83d181a486ff0e0b1a05f7fde1d
fetched_at: '2026-06-29T00:08:16.148570+00:00'
page_id: '244927033'
product: rm
source: tdn-rm
title: TVFA21_DT_Rescisao_Complementar_Recalculo_Final_Alterando_Valor_Evento_Formula
type: documentation
url: https://tdn.totvs.com/display/LRM/TVFA21_DT_Rescisao_Complementar_Recalculo_Final_Alterando_Valor_Evento_Formula
version: 112
---

# RESCISÃO COMPLEMENTAR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão Complementar* |
| **Situação/Requisito:** | Tenho um funcionário que teve uma rescisão complementar em Fevereiro/2016, pois ele deveria receber os eventos 0127 - COMISSÃO e 3279 - DSR S/COMISSÃO, porém, ao calcular está rescisão complementar, verificamos que no LOG de médias, o sistema está considerando o valor atual do evento 4120 que é R$ 624,91 e na rescisão complementar o valor do evento é R$ 599,91  Gostaria de saber o motivo do sistema não considerar o valor que foi informado no LOG de média (624,91) |
| **Solução/Implementação:** | *Ajustado o recálculo final da rescisão complementar para não considerar os eventos informados.*  *No recálculo final o sistema considera a competência atual, fazendo com que a função de fórmula F busque o valor da competência atual, sendo o correto a competência da época.* |
| **Chamados relacionados:** | *TVFA21* |

divs
