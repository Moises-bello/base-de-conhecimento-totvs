---
content_hash: 243609b0fafe203d547a186877366dd00c6f1d60547152e3382be4f13f8293f3
fetched_at: '2026-06-29T00:06:09.888425+00:00'
page_id: '203758692'
product: rm
source: tdn-rm
title: TTHLKZ_DT_Lancamento_Folha_Demitidos_Meses_Posteriores
type: documentation
url: https://tdn.totvs.com/display/LRM/TTHLKZ_DT_Lancamento_Folha_Demitidos_Meses_Posteriores
version: 2
---

# LANÇAMENTO DA FOLHA PARA DEMITIDOS EM MESES POSTERIORES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Rescisão* |
| **Situação/Requisito:** | *Ao efetuar um cadastro de rescisão posterior com 2 meses à frente da competência atual, não está sendo permitido realizar lançamentos na folha da competência atual.*  *Quando o cadastro da rescisão é na competência seguinte, os lançamentos não são bloqueados.* |
| **Solução/Implementação:** | *Ajuste no cadastro de Rescisão para não marcar o flag de rescisão calculada, no caso de data de demissão com 2 meses ou mais à frente da competência atual.*  *Para assim, permitir que haja lançamentos na folha do mês corrente.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTHLKZ* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
