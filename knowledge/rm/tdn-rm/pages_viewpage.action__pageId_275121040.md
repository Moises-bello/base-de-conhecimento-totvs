---
content_hash: 2f1e7e96d5b3c3baf5b1ef217a64070fb5faac338099ddad1f4578e1c0cc5eba
fetched_at: '2026-06-29T00:08:35.261162+00:00'
page_id: '275121040'
product: rm
source: tdn-rm
title: 731950 EDUCACIONAL01-126 DT Mudança de Turma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=275121040
version: 102
---

# MUDANÇA DE TURMA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Mudança de Turma* |
| **Situação/Requisito:** | *Quando utilizado o contexto do nível de ensino superior e o aluno possui uma turma associada ao período letivo, o sistema bloqueia a execução do processo de mudança de turma caso a turma de destino esteja em branco. Tal fato não procede, pois no ensino superior é possível efetuar troca das turmas/disciplinas.* |
| **Solução/Implementação:** | *Ajuste para que o sistema não mais obrigue o usuário informar a turma de destino quando a turma de origem estiver preenchida para execução do processo, ou seja, é possível mudar a turma sem que informe a turma de destino, apenas é selecionado as turmas/disciplinas. Além disso, foi criado um parâmetro na tela de mudança de turma chamado "Manter turma de origem", onde o mesmo apenas é habilitado e visível se a turma de origem estiver preenchida e a turma de destino estiver vazia. Caso a turma de destino estiver preenchida o parâmetro é desabilitado, porém visível. Nos demais casos o parâmetro ficará invisível. O parâmetro tem por objetivo manter a turma de origem quando não se preenche a turma de destino caso o parâmetro estiver marcado, caso contrário a turma não será mantida e será apagada ao final do processo. Tais implementações afetam apenas o nível de ensino superior.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
