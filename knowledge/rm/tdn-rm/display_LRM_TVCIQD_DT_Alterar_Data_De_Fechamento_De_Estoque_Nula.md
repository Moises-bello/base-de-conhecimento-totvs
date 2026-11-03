---
content_hash: b48900e70425a5f260c4ce8b8fa13b7dee4fa29a2ea655ce8f84df1ab4e3dec1
fetched_at: '2026-06-29T00:08:11.951698+00:00'
page_id: '243631712'
product: rm
source: tdn-rm
title: TVCIQD_DT_Alterar_Data_De_Fechamento_De_Estoque_Nula
type: documentation
url: https://tdn.totvs.com/display/LRM/TVCIQD_DT_Alterar_Data_De_Fechamento_De_Estoque_Nula
version: 2
---

# Alterar Data De Fechamento De Estoque Nula

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Função:** | Alterar data de fechamento de estoque |
| **Situação/Requisito:** | Alteração na consistência da parametrização de data de fechamento de estoque. |
| **Solução/Implementação:** | Quando a data de fechamento é nula (30/12/1899) e o sistema possui produtos não regerados o sistema não permitia alterar essa data.  A nova consistência permite alterar essa data para uma data menor ou igual à data da primeira movimentação no sistema. |
| **Conversores e Parâmetros:** | *NA.* |
| **Chamados relacionados:** | TVEBIU |
| **Requisito (ISSUE):** | *NA.* |
