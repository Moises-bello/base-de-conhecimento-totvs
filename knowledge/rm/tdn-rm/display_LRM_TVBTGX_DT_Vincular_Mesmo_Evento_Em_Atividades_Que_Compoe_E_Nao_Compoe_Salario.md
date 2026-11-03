---
content_hash: fcf5f4d4d17ac7458340debec3e660666a4ecc30fd53477887418d3018e10830
fetched_at: '2026-06-29T00:08:11.997971+00:00'
page_id: '243633408'
product: rm
source: tdn-rm
title: TVBTGX_DT_Vincular_Mesmo_Evento_Em_Atividades_Que_Compoe_E_Nao_Compoe_Salario
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBTGX_DT_Vincular_Mesmo_Evento_Em_Atividades_Que_Compoe_E_Nao_Compoe_Salario
version: 112
---

# REPROGRAMAÇÃO SALARIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Reprogramação Salarial* |
| **Situação/Requisito:** | Ao cadastrar o evento de Atividade remunerada o sistema não valida se o evento já está cadastrado como salario composto e ao realizar o lançamento do salário composto o sistema sobrescreve o evento do salário composto gerando o valor e referencia incorretos no envelope do funcionário. |
| **Solução/Implementação:** | *Ao executar a reprogramação salarial foi adicionado uma validação que verifica se o usuário vinculou o mesmo evento em atividades que compõe e não compõe salário.* |
| **Chamados relacionados:** | *TVBTGX* |

divs
