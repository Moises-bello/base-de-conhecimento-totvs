---
content_hash: 47d1cc6567a4981a33e4f38070b5a982e805297278122ddb717948ae1db6c048
fetched_at: '2026-06-29T00:09:02.931326+00:00'
page_id: '381029394'
product: rm
source: tdn-rm
title: 3009142 FOPROTINAS01-4768 DT - Erro ao Carregar Perfis de Geração de Folha
  Analítica Antigos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=381029394
version: 1
---

# ERRO AO CARREGAR PERFIL DE PROCESSO DE GERAÇÃO DE FOLHA ANALÍTICA ANTIGO COM FÓRMULA DE RESUMO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Recursos Humanos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Folha Analítica |
| **Situação/Requisito:** | Ao abrir o assistente de geração de Folha Analítica com um perfil antigo que contém fórmula(s) de resumo de funcionário(s), é emitido o erro "<target>.CODCOLIGADA e <source>.CODCOLIGADA têm propriedades conflitantes: propriedade DataType incompatível". |
| **Solução/Implementação:** | Foi alterada a sobrecarga do método que realiza o merge dos conjuntos de dados que contêm as fórmulas, utilizando a opção de ignorar diferenças nos schemas. |
| **Tickets relacionados:** | [3009142](https://totvssuporte.zendesk.com/agent/tickets/3009142 "Open ticket in Zendesk Support") |
