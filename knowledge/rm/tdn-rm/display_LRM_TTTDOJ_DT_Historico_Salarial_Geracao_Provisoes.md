---
content_hash: 7d4e9e7a38dc2e9282a9fb8d59bd0684dcfbaed93de190960a7ea5498533dcbd
fetched_at: '2026-06-29T00:06:21.143550+00:00'
page_id: '223162246'
product: rm
source: tdn-rm
title: TTTDOJ_DT_Historico_Salarial_Geracao_Provisoes
type: documentation
url: https://tdn.totvs.com/display/LRM/TTTDOJ_DT_Historico_Salarial_Geracao_Provisoes
version: 1
---

# HISTÓRICO SALARIAL UTILIZADO NA GERAÇÃO DAS PROVISÕES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração de Provisões* |
| **Situação/Requisito:** | *Pesquisa do histórico salarial na geração das provisões está considerando apenas a data da modificação, fazendo com que, ao ter duas alterações no mesmo dia com diferença de minutos, seja considerado o valor mais antigo.* |
| **Solução/Implementação:** | *Ajuste na pesquisa do histórico salarial a ser utilizado no cálculo da média na geração das provisões, para considerar também a hora / minutos da alteração.*  *E assim, pegar o salário correto da época de vigência.* |
| **Chamados   relacionados:** | *TTTDOJ* |
| **Versões/Release:** | *11.82.43* |
