---
article_id: 360057431273
category: SIGAEST - CUSTOS
content_hash: 810d1f5da532f7d8005f2334c9fa54ff8c742eecb2c99cc42f7387255ca1777b
fetched_at: '2026-06-28T22:39:00.938775+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP A650NOP durante
  custo medio
type: support-article
updated_at: '2025-03-12T11:43:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057431273-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-A650NOP-durante-custo-medio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28807702836887)**Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**

No módulo de estoque ao Executar o Custo Médio apresenta a seguinte mensagem:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8399567974679)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**

A mensagem  em questão indica existência de movimentação nas **tabelas SD1, SD2 ou SD3 onde o campo D1\_OP, D2\_OP ou D3\_OP** **possui número de Ordem de Produção** que não consta na tabela SC2, no caso parece ter excluído na tabela esse OS este número pode ser proveniente de projeto(PMS) ou manutenção de ativos (MNT)  
  
Durante o processamento, a rotina busca pela 00003301001 (um exemplo) na tabela SC2, apresentando o assistente **A650NOP** caso não localize.  
  
**Isso é um validador padrão do sistema,**vai ter que localizar nas tabelas SD1, SD2 e SD3 o número dessa OP ao localizar, estornar essa movimentação e executar o Custo Médio.  
  
Para corrigir o help, será necessário validar se o item em questão, consta como deletado na tabela SC2. Mesmo possuindo movimentações nas tabelas **SD1, SD2 ou SD3**.

**Solução**  
Para "validar essa ocorrência", onde pode estar relacionado a registros incorretos em base, realize os seguintes passos, **em acompanhamento de uma analista consultor in loco.**

**Fazer um filtro nas tabelas SD1, SD2  e SD3 para localizar essa Ordem de Produção.**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8399802554263)**

**Caso seja localizado o movimento PR0 (Produção) ou qualquer movimento de Requisição/Devolução no campo D3\_CF, é necessário avaliar se a Ordem de Produção em questão, consta como deletada, conforme print abaixo:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8399948925079)

Caso item esteja realmente deletado, será necessário recuperar o registro. Após isso, realizar o estorno do apontamento dessa OP pela rotina Apontamento de Produção (MATA250),  em seguida, excluir esse item na rotina Ordem de Produção (MATA650).

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
