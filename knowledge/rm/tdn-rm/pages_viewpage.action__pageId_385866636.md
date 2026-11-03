---
content_hash: a159114865dc7bc0b9f931eacb1d3374ea448cc203fc9439bc7cdf86cfbfe143
fetched_at: '2026-06-29T00:09:08.303281+00:00'
page_id: '385866636'
product: rm
source: tdn-rm
title: 3286947 FISCAL01-5956 DT Escrituração - Erro de divisão por zero
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385866636
version: 2
---

# Fator de redução de base de cálculo do tributo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Escrituração Fiscal |
| **Situação/Requisito:** | Ao tentar fazer a escrituração de um movimento é apresentado o seguinte erro: "Erro: Tentativa de divisão por zero." |
| **Solução/Implementação:** | Ajuste no sistema para que apresente uma mensagem informativa ao usuário:  "O fator de redução da base de cálculo do tributo não pode ser maior ou igual a 100%. Favor verificar a parametrização e executar o processo novamente". |
