---
content_hash: 8f981553cb921aa63cff644d636b14e93084dd551312c5d18f27552740025b83
fetched_at: '2026-06-29T00:10:13.827376+00:00'
page_id: '458760793'
product: rm
source: tdn-rm
title: 4993923 FISCAL01-8017 - Escrituração Fiscal - Redução Z de Cupom Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458760793
version: 2
---

# Escrituração Fiscal

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Escrituração Fiscal |
| **Situação/Requisito:** | Ao escriturar redução Z "Valor ICMS" fica divergente do valor esperado e apresentado na impressão da Redução Z. Isso se deve ao fato de que o campo "Valor ICMS" da aba de itens da situação tributária está preenchida com valores truncados. Se exportar a tela de itens para Excel e somar esta coluna arredondando os valores obterá o mesmo valor apresentado na redução Z. Se recalcular o lançamento fiscal o valor de ICMS passa a ser apresentado corretamente, acredito que isso ocorre, pois no recálculo, o Liber apenas aplica a alíquota do tributo á sua base e por isso consegue encontrar o valor correto. |
| **Solução/Implementação:** | No processo de escrituração fiscal, do Lote no Nucleus, o cálculo do tributo do item do cupom foi alterado a quantidade de casas decimais de 2 para 4, a fim de garantir que não haja perda na precisão da Redução Z. |
