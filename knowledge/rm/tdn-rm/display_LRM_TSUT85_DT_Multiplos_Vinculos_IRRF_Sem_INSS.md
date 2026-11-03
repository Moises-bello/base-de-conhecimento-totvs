---
content_hash: 6d2d17f93ded59991c240642b05345e00117c6aef89ff182ac49b9cf7bcb71c2
fetched_at: '2026-06-29T00:06:02.113549+00:00'
page_id: '198943551'
product: rm
source: tdn-rm
title: TSUT85_DT_Multiplos_Vinculos_IRRF_Sem_INSS
type: documentation
url: https://tdn.totvs.com/display/LRM/TSUT85_DT_Multiplos_Vinculos_IRRF_Sem_INSS
version: 2
---

# MULTIPLOS VINCULOS DE IRRF SEM DESCONTO DE INSS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cálculo de IRRF com Múltiplos Vínculos* |
| **Situação/Requisito:** | *Quando no cadastro da chapa centralizadora de funcionário com múltiplos vínculos está informado que não possui desconto de INSS, pasta "Parâmetros", no cálculo da movimentação não está lançando o evento de CC 302 (BASE DE IRRF FOLHA OUTROS VÍNCULOS) e não considera as bases de IRRF das chapas dos outros vínculos.*  *No caso de haver desconto de INSS o cálculo fica correto.* |
| **Solução/Implementação:** | *A carga das chapas de múltiplos vínculos de INSS e IRRF passou a ser feita ao mesmo tempo, e sob demanda, no momento do cálculo do desconto de INSS, que ocorre antes do cálculo do IRRF.*  *Deverá ser alterado para que esta carga ocorra separadamente, e as chapas de IRRF sejam carregadas no cálculo do desconto de IRRF. Assim, a não ocorrência do desconto de INSS não irá afetar o cálculo de múltiplos de vínculos de IRRF.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSUT85* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
