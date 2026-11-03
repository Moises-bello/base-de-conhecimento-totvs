---
content_hash: dc610b62784e0c2838e8d4e4206ce9ecd52f3e1098f4ca56c34bf1a55ad32aa6
fetched_at: '2026-06-29T00:09:03.516029+00:00'
page_id: '381046543'
product: rm
source: tdn-rm
title: 930735 MATESTCNTFTOF01-947 DT Recalculo de Custo da Ordem de Produção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=381046543
version: 2
---

# Recalculo de Custo - Ordem de Produção

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão Planejamento e Controle da Produção. |
| **Função:** | Recalculo de Custo. |
| **Situação/Requisito:** | O recalculo de custo da ordem de produção apresentou divergência dos valores calculado entre o recalculo antigo (RMFactor.exe) e o novo Recalculo de Custo (RM.exe).    A divergência deve-se a consideração do histórico de custo e o prazo considerado, conforme documentação, deve-se considerar quando não existir cadastro de custo da entidade no mês em que ocorre o apontamento, o custo mais recente no período de vinte e quatro meses antes e após apontamento.    Verificado também a necessidade de ajustar o sumarizador de custos (equipamento e mão de obra) no novo recalculo, em situação especifica adicionava valor a mais que o calculado. |
| **Solução/Implementação:** | - Ajuste no somatório de custo de entidade (equipamento e mão de obra) com múltiplos intervalos de trabalho.    - Adequação no limite do histórico de custo a ser avaliado quando o mês em que o apontamento foi realizado não tem custo definido, está garantido a verificação de 24 meses antes e após apontamento e utilização do do custo mais recente do histórico, obs (somente quando não tem custo cadastrado no mês em que ocorre apontamento).  Observação :  - As melhorias e ajustes foram aplicados somente ao novo recalculo de custo acessado via RM.exe, o antigo recalculo de custo vai ser descontinuado na versão 12.1.21 e não sofre nenhum tipo de ajuste ou melhoria.  - Toda verificação de custeio deve ser realizada somente sob a ótica do novo recalculo de custo. |
| **Conversores e Parâmetros:** | Desnecessário. |
| **Tickets relacionados:** | 930735 |
| **Documento de Referência:** |  |
