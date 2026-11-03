---
content_hash: b6f7b99ecfb99b7ca2df0564d68c339ab99dc10ec565312e8fb417650aad6885
fetched_at: '2026-06-29T00:06:07.858854+00:00'
page_id: '201739214'
product: rm
source: tdn-rm
title: TTBMJR_DT_Copia_De_Movimento_Por_Referencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBMJR_DT_Copia_De_Movimento_Por_Referencia
version: 2
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque Compras e Faturamento* |
| **Função:** | *Assistente de Cópia de Movimento Por Referência* |
| **Situação/Requisito:** | Inconsistência ao criar um movimento através do assistente de cópia de movimento por referência. Estava apresentando a mensagem:  "Tentativa de Divisão por Zero " |
| **Solução/Implementação:** | Ajuste no processo do Assistente de Cópia de movimento por referência.    A inconsistência apresentava quando o tipo de movimento destino utiliza rateio por centro de custo,  valor do campo VALORLIQUIDOORIG da tabela TMOV igual a zero (0) e Parâmetros de Rateio de Centro de Custo e Departamento de Tipo de Movimento igual a Percentual |
| **Conversores e Parâmetros:** | *Não se Aplica* |
| **Chamados relacionados:** | *Não se Aplica* |
| **Requisito (ISSUE):** | *Não se Aplica* |
| **Versões/Release:** | *12.1.8* |
