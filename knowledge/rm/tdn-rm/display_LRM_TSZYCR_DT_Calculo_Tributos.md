---
content_hash: 27ab25c861088119c86a7eb475d140ff9e8cad967eeb903284479c869fcc1b89
fetched_at: '2026-06-29T00:06:03.940822+00:00'
page_id: '200902817'
product: rm
source: tdn-rm
title: TSZYCR_DT_Calculo_Tributos
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZYCR_DT_Calculo_Tributos
version: 2
---

# Cálculo de Tributos

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Estoque, Compras e Faturamento* |
| **Função:** | *Cálculo de Tributos* |
| **Situação/Requisito:** | Ao incluir um movimento a alíquota de alguns tributos não está sendo preenchida no campo Tributos Valores (Tributos) do Item de Movimento. |
| **Solução/Implementação:** | Ajustamos a regra responsável por buscar a alíquota dos tributos quando o tipo de movimento está parametrizado para utilizar TOTVS Colaboração, caso seja feita uma inclusão  Manual, o sistema busca os defaults do produto normalmente, caso seja feita uma inclusão a partir de XML, serão mantidas as tributações da nota em questão. |
| **Conversores e Parâmetros:** | *Não se Aplica* |
| **Chamados relacionados:** | *Não se Aplica* |
| **Requisito (ISSUE):** | *Não se Aplica* |
| **Versões/Release:** | *12.1.7* |
