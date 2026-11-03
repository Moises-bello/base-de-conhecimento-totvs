---
content_hash: 862462bfe73de7824e7cc0ae045d402c0658d4665c510a7da84c7b6c394695be
fetched_at: '2026-06-29T00:08:13.901169+00:00'
page_id: '244430942'
product: rm
source: tdn-rm
title: TVDDVG_DT_Inss_Diferenca_Salarial_Multiplos_Vinculos
type: documentation
url: https://tdn.totvs.com/display/LRM/TVDDVG_DT_Inss_Diferenca_Salarial_Multiplos_Vinculos
version: 111
---

# DIFERENÇA SALARIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Construção e Projetos** |
| **Módulo:** | **Folha de Pagamento** |
| **Função:** | *Diferença Salarial* |
| **Situação/Requisito:** | Sistema não está considerando o INSS pago na rescisão complementar referente a outra chapa do funcionário na empresa (Múltiplos Vínculos).  Coligada 1 – Demissão em 13/05/2016 e este mesmo funcionário foi admitido no dia seguinte na coligada 2 (data admissão 14/05/2016).     O salário deste funcionário (nas duas coligadas) foi reajustado retroativo a 04/2016.     Na coligada 1 eu executo o cálculo de uma rescisão complementar. Na coligada 2 eu executo processo de diferença salarial.     Coligada 1 – Rescisão complementar     Coligada 2:     Envelope da competência 05/2016     Cálculo da diferença salarial da coligada 2     Note que o INSS abatido é no valor de R$74,66, este valor refere-se ao INSS descontado na rescisão original. Porém o sistema também tinha que abater o valor de R$ 7,47 que é o INSS da rescisão complementar. |
| **Solução/Implementação:** | *Ajustado para considerar o INSS corretamente pago em outra chapa em movimentações de diferença salarial.* |
| **Chamados relacionados:** | *TVDDVG* |
| **Versões/Release:** | 12.1.13 |

divs
