---
content_hash: 3367e0a2c8abd716e460c868f1f77a271eed43716ba8cb0363458863c36a4eeb
fetched_at: '2026-06-29T00:10:53.176596+00:00'
page_id: '577622133'
product: rm
source: tdn-rm
title: DT- Substituição de benefícios calculados (Consulta Movimento Integração)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=577622133
version: 2
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Cálculo de Benefícios do funcionário |
| **Situação/Requisito:** | Quando eram calculados os Benefícios em **Folha mensal | Lançamentos | Cálculo de Benefícios de Funcionários**, o sistema estava excluindo/substituindo os benefícios já calculados na aba '**Consulta Movimentação Integração**', mesmo que no momento do cálculo eu tenha selecionado apenas um benefício diferente dos que já haviam sido calculados. |
| **Solução/Implementação:** | Criado em **RH | Gestão de Pessoas | Configurações |  Parametrizador | Configurações | Benefícios**, o parâmetro '**Atualizar Benefício Selecionado**'.  Ao marcar esse parâmetro,  o sistema irá incluir ou substituir  somente o benefício selecionado, sem impactar os que já haviam sido calculados. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | [10289565](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D%20%3D%20%2210289565%22) |
| **Requisito:** | N/A |
| **Documento de Referência:** | [Cálculo de Benefícios de Funcionários](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719724)  [Benefícios - RHU](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718699) |
| **Pacote:** | N/A |
