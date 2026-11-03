---
article_id: 34706468094359
category: SIGAACD - Automação e Coleta de Dados
content_hash: a601360bbcbc98e3b8c7e5a46e7d942cfe68e9cb58fcefd9b61ef2793021b1a5
fetched_at: '2026-06-28T22:39:12.863198+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Nota do Conhecimento
  de Transporte Eletrônico (CTe) em processo de conferência
type: support-article
updated_at: '2025-09-04T19:19:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34706468094359-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Nota-do-Conhecimento-de-Transporte-Eletr%C3%B4nico-CTe-em-processo-de-confer%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34706482377751) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Nota do Conhecimento de Transporte Eletrônico (CTe) em processo de conferência, como corrigir para não ficar em processo de conferência?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**  
Para que as notas da espécie CTe não sejam em  conferência, siga o passo a passo abaixo:

1. Acessar o configurador na parte de parâmetro, e buscar o parâmetro MV\_TPCONFF = 2 e o MV\_CONFFIS = S
2. No cadastro do  fornecedor na aba outros, deixar o campo A2\_CONFFIS = 3 (Não utiliza )
3. Usar uma TES que não atualiza estoque ou também que atualiza estoque, com a configuração do item acima, a nota não vai entra em conferência.
4. No cadastro do fornecedor, pode deixar  o campo A2\_CONFFIS = 0 (Parâmetro), e usar uma TES que não atualiza estoque, nesse momento também as notas da espécie CTe não vão ficar em conferência.

**Saiba Mais:**  
[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
