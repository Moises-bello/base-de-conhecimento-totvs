---
content_hash: c1482fd01f73d66658cffe221bfac24c0bbbc87fd1389487e745d9abacc66689
fetched_at: '2026-06-29T00:06:09.273893+00:00'
page_id: '203751658'
product: rm
source: tdn-rm
title: TTGPVW_DT_Gerar_Requisicao_De_Substituicao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGPVW_DT_Gerar_Requisicao_De_Substituicao
version: 1
---

# GERAR REQUISIÇÃO DE SUBSTITUIÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Função:** | *Gerar Requisição de Substituição* |
| **Situação/Requisito:** | *Quando o sistema gera uma Requisição de Substituição para um Funcionário Horista que está vinculado a uma Tabela Salarial Horista, o salário considerado esta sendo o mensal quando deveria ser o salário hora.* |
| **Solução/Implementação:** | *Ao gerar uma requisição de Substituição que está vinculada a uma tabela salarial horista, o sistema irá considerar o salário hora para nova requisição. Ao abrir a edição da Requisição de Substituição o sistema apresentará a descrição como "salário hora" ao invés de "salário". O mesmo se aplica tanto para aplicação (RM.exe) quanto para o Portal.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTGPVW* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
