---
content_hash: a51475529ecc940aaf3c6930dadc76a660d23626df84b2c1527228ac9694d236
fetched_at: '2026-06-29T00:06:03.427114+00:00'
page_id: '198954131'
product: rm
source: tdn-rm
title: TSZKI7_DT_Faturamento_de_Movimento_com_Formula_Visual
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZKI7_DT_Faturamento_de_Movimento_com_Formula_Visual
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque Compras e Faturamento* |
| **Função:** | *Faturamento de Movimentos* |
| **Situação/Requisito:** | Inconsistência ao faturar movimento utilizando fórmula visual responsável por definir default o campo OPERACAOCONSUMIDORFINAL da tabela TMOVFISCAL, quando no movimento de origem não existia registro na tabela TMOVFISCAL. |
| **Solução/Implementação:** | Ajuste no método responsável para execução da atividade de formula visual responsável por definir default o campo OPERACAOCONSUMIDORFINAL da tabela TMOVFISCAL. Definido como obrigatoriedade o tipo de movimento de destino estar parametrizado para Gerar Escrituração(Etapa Fis – Escrituração 1/2) |
| **Conversores e Parâmetros:** | *Não se aplica* |
| **Chamados relacionados:** | Não se aplica |
| **Requisito (ISSUE):** | Não se aplica |
| **Versões/Release:** | *12.1.7* |
