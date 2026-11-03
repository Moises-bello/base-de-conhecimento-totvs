---
content_hash: 697d50582ca560803a224d2e5f8139d08155f6d8ada0244cd15fa023e113ee60
fetched_at: '2026-06-29T00:06:04.910123+00:00'
page_id: '200912706'
product: rm
source: tdn-rm
title: TSVPAW_DT_Copia_De_Movimento_Por_Referencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVPAW_DT_Copia_De_Movimento_Por_Referencia
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
| **Versões/Release:** | *11.82.41* |
