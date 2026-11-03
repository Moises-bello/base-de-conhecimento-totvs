---
content_hash: 04c65bb2d270ffb35a4594022e68811bbc0785b0a2923c7e2785b36d9e10bd15
fetched_at: '2026-06-29T00:09:51.762248+00:00'
page_id: '437261489'
product: rm
source: tdn-rm
title: 3904817 FISCAL01-7056 DT - Escrituração Fiscal - Referência de objeto não definida
  para uma instância de um objeto.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=437261489
version: 3
---

# Escrituração Fiscal

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Escrituração de Lançamentos Fiscais |
| **Situação/Requisito:** | Ao realizar o processo de Escrituração migrado, foi apresentado erro:  Início do Processo  ================================================================================= Escrituração Total de Movimentos Selecionados: 1 Total de Lançamentos Gerados: 0 Total de Erros Encontrados: 1 Valor Total de Lançamentos Escriturados: 0,00 =================================================================================  --------------------------------------------------------------------------------- Erros ao Validar Movimentos Movimento: 000000121056 Erro: Referência de objeto não definida para uma instância de um objeto. |
| **Solução/Implementação:** | Foi identificado que o erro era apresentado quando o campo complementar DTCOMPETENCIASERVICO na TMOVCOMPL estava ativo , porém não visível no tipo de movimento, desta forma o campo estava nulo.  Foi efetuado uma correção para que quando o campo complementar esteja nulo não dispare o erro de "Referência de objeto não definida para uma instância de um objeto". |
