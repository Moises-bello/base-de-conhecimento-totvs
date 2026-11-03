---
content_hash: 6ccd2c321e271f2eb6d205abe5dc1fee2da4bea75a2b4312e4a283c2d1b0bce4
fetched_at: '2026-06-29T00:08:05.130371+00:00'
page_id: '235584487'
product: rm
source: tdn-rm
title: TURRYN_DT_Nivel_Ensino
type: documentation
url: https://tdn.totvs.com/display/LRM/TURRYN_DT_Nivel_Ensino
version: 117
---

# NÍVEL DE ENSINO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Nível de Ensino* |
| **Situação/Requisito:** | *Em Gestão fiscal >> Cadastros >> Filiais >> Anexos >> Dados educacionais >> Anexos >> Níveis de ensino por filial. Após criar uma nova filial e tentar associá-la a um nível de ensino, o sistema exibe a seguinte mensagem de erro e não permite salvar.* |
| **Solução/Implementação:** | *Ajuste no método que efetua a propagação de parâmetros entre contextos, o mesmo estava com uma não conformidade, de duplicidade de chaves, que não possibilitava vincular um nível de ensino a uma filial.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
