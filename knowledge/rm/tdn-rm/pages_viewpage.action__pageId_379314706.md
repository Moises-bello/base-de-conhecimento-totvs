---
content_hash: 87ddc9a876df4c3259c307317d61ed931d0fc3e611fbd108603605481a07afc2
fetched_at: '2026-06-29T00:09:02.488495+00:00'
page_id: '379314706'
product: rm
source: tdn-rm
title: 3145942 FISCAL01-5195 DT Cálculo do ICMS-ST
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379314706
version: 3
---

# Cálculo do ICMS-ST quando utilizado o parâmetro "Calcula ICMS-ST de saída com CST 60 com base na última entrada do produto"

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Cálculo de Tributação |
| **Situação/Requisito:** | Ajuste no cálculo do ICMS-ST quando utilizado o parâmetro \*Calcula ICMS-ST de saída com CST 60 com base na última entrada do produto\*, disponível na etapa Fis - Dados dos parâmetros do tipo de movimento.  Quando o CST do ICMS for igual à “60 - ICMS cobrado anteriormente por substituição tributária” será realizado o cálculo do valor unitário da Base de Cálculo e do Valor do Imposto do ICMS-ST referente ao último movimento de entrada que tenha ICMS ST e que controle saldo de estoque. |
| **Solução/Implementação:** | Alteração no cálculo do ICMS-ST quando utilizado o parametro "Calcula ICMS-ST de saída com CST 60 com base na última entrada do produto" disponível na etapa Fis - Dados dos parâmetros do tipo de movimento. Alterando o cálculo considerando o fator de conversão, pois quando temos divergências entre a unidade da entrada e da saída, o calculo deve considerar o fator de conversão da unidade de medida.    Tabela para conferência do Cálculo:     |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | ENTRADA | | | |  | SAÍDA | | | | | Unidade | A | Cálculo | CX (12 unid) |  | UNIDADE | G | Cálculo | Unidade | |  |  |  |  |  | Fator Conv | H |  | 12 | | Quantidade Entrada | B |  | 50 |  | Quantidade Saída | I |  | 4 | | Base ST Entrada | C |  | 300 |  | Base ST Unit Saída | J | (E/H) | 0,5 | | Valor ST Entrada | D |  | 15 |  | Valor ST Unit Saída | K | (F/H) | 0,025 | |  |  |  |  |  |  |  |  |  | | Base ST Unitária | E | (C/B) | 6 |  | Base ST Saída | L | (I\*J) | 2 | | Valor ST Unitário | F | (D/B) | 0,3 |  | Valor ST Saída | M | (I\*K) | 0,1 | |
|  |  |
