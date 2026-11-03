---
content_hash: 3b4a077efcacac6a923f6dfbaba5bb9e341ec85d1e53ec9569530a6876db9499
fetched_at: '2026-06-29T00:08:20.721205+00:00'
page_id: '268585513'
product: rm
source: tdn-rm
title: TVZVJP_DT_Notas_Avaliacao_Casas_Decimais
type: documentation
url: https://tdn.totvs.com/display/LRM/TVZVJP_DT_Notas_Avaliacao_Casas_Decimais
version: 112
---

# NOTAS DE AVALIAÇÃO - CASAS DECIMAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Notas de Avaliação - Casas Decimais* |
| **Situação/Requisito:** | *O Campo de casas decimais não está sendo respeitado, quando coloco 5 ou mais casas decimais, no Portal e no RM arredonda para 4 casas sempre nas notas de avaliação do aluno.* |
| **Solução/Implementação:** | *Ajuste no cadastro da disciplina (contexto ensino superior) e no cadastro da disciplina da matriz (contexto ensino básico) para que não seja possível cadastrar um valor maior que 4 no campo de casas decimais, pois este valor é definido na base de dados. Caso informe um valor maior que 4 o sistema ecoará a seguinte mensagem: "O número máximo de casas decimais definida na base de dados é 4.".* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
