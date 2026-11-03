---
content_hash: 4e9faaf6f1186f2f096dd7b2048071506981ed4b8001f1c0e92802d8898b806f
fetched_at: '2026-06-29T00:06:17.506050+00:00'
page_id: '213976399'
product: rm
source: tdn-rm
title: TTQMWR_DT_Alteracao_Global_Salarios
type: documentation
url: https://tdn.totvs.com/display/LRM/TTQMWR_DT_Alteracao_Global_Salarios
version: 1
---

# ALTERAÇÃO GLOBAL DE SALÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Alteração global de salários* |
| **Situação/Requisito:** | Ao rodar a alteração salarial (salário composto), o sistema não alterou o salário de uma determinada funcionária. Alterou apenas o histórico salarial |
| **Solução/Implementação:** | A solução tem 2 partes diferentes. Uma é o acerto do histórico salarial do funcionário para que a alteração global de salários funcione.  A outra é a manutenção realizada na reprogramação salarial para que não volte a apresentar o mesmo problema.  Identificamos que a alteração do salário não funcionou devido o histórico salarial estar inconsistente.  Essa inconsistência se deve ao fato da reprogramação salarial não manter fidelidade ao histórico e mudar constantemente o número do salário do funcionário.  Para resolver o problema será necessário executar um programa a parte (desenvolvido pelo Jorge) para acertar o histórico salarial antes de executar a alteração global de salários.  Evitando novas inconsistências relacionadas ao número de salário, foi realizada uma manutenção na reprogramação salarial, para que a reprogramação mantenha fidelidade ao histórico salarial, mantendo os números de salários ao seus respectivos códigos de eventos. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTQMWR |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
