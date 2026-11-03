---
article_id: 33027344116119
category: SIGAEST - RELATORIOS
content_hash: 13e28cd881123c5277a7355abd3dbfc03d015fcecd835006c5dbf656cf8dc8e6
fetched_at: '2026-06-28T22:39:06.223561+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Qual relatorio para
  listar o CM do produto mes a mes?
type: support-article
updated_at: '2025-06-24T20:07:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33027344116119-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Qual-relatorio-para-listar-o-CM-do-produto-mes-a-mes
---

A geração de um relatório com o Custo Médio por períodos, de forma consolidada e sem movimentações, dependerá de uma customização, e pode ser implementada conforme a necessidade específica de sua operação, contatando seu ESN(Gerente de contas) ou solicitação ao seu analista desenvolvedor.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33027344078871) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
O módulo de Estoque e Custos possui um relatório que demonstre o Custo Médio (CM) do produto, período a período?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Atualmente, o relatório mais utilizado para validação de custos por movimentação é o [**Relatório KARDEX (MATR900)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es). Este relatório apresenta todas as movimentações do item no período consultado, incluindo uma coluna com o **Custo Médio (CM)** aplicado em cada movimentação. A última linha do relatório representa o custo consolidado, que será considerado como **custo médio final do período**, utilizado no processo de fechamento de estoque.   
  
No entanto, **não existe um relatório padrão no sistema que apresente exclusivamente o Custo Médio por produto, período a período**, sem considerar as movimentações.

Caso haja essa necessidade específica, é possível desenvolver um relatorio **\*customizado\*** com essa finalidade, utilizando como base a tabela **SB9** – que é a tabela de controle de fechamento do estoque.   
  
**Nesta tabela, pode-se considerar:**

O campo B9\_DATA para identificar o período de fechamento.

O campo B9\_CM1 para obter o custo médio apurado daquele período para o item

E demais que sejam necessarios.

É importante atentar-se ao uso e interpretação do parâmetro [**MV\_CUSFIL**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011068802-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CUSFIL), que influencia o comportamento do seu custo por periodo.

**Saiba mais:**

[*MP - SIGAEST - Como fazer uma análise de Custos no Protheus?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
