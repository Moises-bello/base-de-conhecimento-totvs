---
article_id: 26567901386007
category: SIGAEST - RELATORIOS
content_hash: debc90593ef7361b42859d11361d49e89c349738c1b12ffdd3febb461000370d
fetched_at: '2026-06-28T22:39:06.210947+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR910 não imprime
  dados.
type: support-article
updated_at: '2024-09-23T19:07:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26567901386007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR910-n%C3%A3o-imprime-dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26567949328535) Tempo aproximado para leitura: **00:01:12min****Ocorrência**

Ao realizar a impressão do MATR910 não está sendo apresentado as movimentações, mesmo o produto tendo movimentações no período parametrizado.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**Temos mapeado esse problema relacionado ao parâmetro MV\_VEICULO ativo no ambiente, porém o campo B1\_CODITE está em branco.   
  
**Solução**Quando temos o parâmetro MV\_VEICULO habilitado no ambiente o campo B1\_CODITE passa a ser um campo validado como obrigatório para impressão do relatório, dessa maneira para que retorne a trazer informações se faz necessário preencher o campo B1\_CODITE.

[Clique aqui](https://tdn.totvs.com/x/hCzQF) para maiores informações sobre o campo.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Relatórios do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)*
