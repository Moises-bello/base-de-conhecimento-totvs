---
content_hash: 99fe22ceffe8200f849c4b93313c0513aa02495da565601451b92a64d0635891
fetched_at: '2026-06-29T00:08:16.181496+00:00'
page_id: '244928194'
product: rm
source: tdn-rm
title: TVDNNR_DT_Salario_Maternidade_Evento_Incide_Salario
type: documentation
url: https://tdn.totvs.com/display/LRM/TVDNNR_DT_Salario_Maternidade_Evento_Incide_Salario
version: 111
---

# SALÁRIO MATERNIDADE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Salário Maternidade* |
| **Situação/Requisito:** | Ao incluir evento com incidência em salário no mesmo envelope em que a funcionária recebeu salário maternidade (CC 17), sistema soma o valor do evento que incide em salário ao valor do salário base do funcionário, alterando assim o valor do evento.   Para outras rotinas como 13º, aviso prévio e férias existe um parâmetro para ignorar essa incidência. |
| **Solução/Implementação:** | Criado parâmetro para que o cliente tenha opção se para o cálculo do salário maternidade deve considerar ou não os eventos que incidem em salário. Parâmetro: Ignora eventos que incide em salário - Marcando este parâmetro o sistema irá desconsiderar os eventos que incidem em salário para o cálculo do salário maternidade. |
| **Chamados relacionados:** | *TVDNNR* |

divs
