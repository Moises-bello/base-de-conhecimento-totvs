---
content_hash: 1c3eecf82e781d2eceb432e9850982eb88cdb6f225cba0b4f906531f7ef4f80d
fetched_at: '2026-06-29T00:08:20.040942+00:00'
page_id: '267809715'
product: rm
source: tdn-rm
title: TVVMXP_DT_Tratar_Data_Nascimento_Nao_Preenchida
type: documentation
url: https://tdn.totvs.com/display/LRM/TVVMXP_DT_Tratar_Data_Nascimento_Nao_Preenchida
version: 110
---

# CADASTRO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de funcionário* |
| **Situação/Requisito:** | Ao cadastrar um funcionário sem preencher a data de nascimento é apresentado a mensagem de aviso '' A data de nascimento que foi cadastrada para este funcionário, o deixa com mais de 80 anos''. Porém nenhuma data de nascimento foi cadastrada, desta forma a mensagem a ser apresentada deveria ser outra. |
| **Solução/Implementação:** | *Foi ajustado o sistema para que no momento em que for cadastrado um funcionário e a data de nascimento não for preenchida, o sistema emita uma mensagem informando que a data não está preenchida e deveria ser preenchida.* |
| **Chamados relacionados:** | TVVMXP |

divs
