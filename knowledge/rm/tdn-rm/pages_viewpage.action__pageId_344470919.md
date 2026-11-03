---
content_hash: aeffa4c2852e829de583613f4933f2696609c0b52db9c36e026484d5a3302203
fetched_at: '2026-06-29T00:08:53.355906+00:00'
page_id: '344470919'
product: rm
source: tdn-rm
title: 2240267 FISCAL01-3618 DT Processo de Escrituração Fiscal (.NET)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344470919
version: 1
---

# Processo de Escrituração Fiscal (.NET) - Redução Z

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Processo de Escrituração Fiscal (.NET) - Redução Z |
| **Situação/Requisito:** | Ao criar um lote de escrituração, para mais de uma Redução Z, sistema tenta escriturar todas as reduções com o  mesmo número de documento e com isso lote é escriturado parcialmente e é exibida a mensagem de erro:  ================================================================================= Escrituração  Total de Reduções Selecionadas: 2  Total de Lançamentos Gerados: 1  Total de Erros Encontrados: 1  Valor Total de Lançamentos Escriturados: 1,00  =================================================================================  Erros no Serviço de Inclusão de Lançamentos  ---------------------------------------------------------------------------------  Erro na Inclusão do Registro:  Documento 001028 - Série ... - Data 09/02/2018:  Documento já existente.  --------------------------------------------------------------------------------- |
| **Solução/Implementação:** | Implementada melhoria para sistema conseguir escriturar duas reduções Z em um mesmo lote de escrituração. |
