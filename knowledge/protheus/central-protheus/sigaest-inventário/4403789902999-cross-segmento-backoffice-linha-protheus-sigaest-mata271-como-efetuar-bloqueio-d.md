---
article_id: 4403789902999
category: SIGAEST - INVENTÁRIO
content_hash: effa3fbe3ff8b76625e64cc83fb22938b80b4a11ec3f3c839553cb567d5c9bf3
fetched_at: '2026-06-28T22:38:50.349966+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA271 - Como efetuar
  bloqueio de inventário por endereço?
type: support-article
updated_at: '2025-03-12T12:23:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403789902999-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA271-Como-efetuar-bloqueio-de-invent%C3%A1rio-por-endere%C3%A7o
---

**Dúvida**É possível efetuar o Bloqueio de Inventário por Endereçamento?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Atualmente, não há no Protheus uma rotina para bloqueio de Inventário por Endereço. Isso se dá pelo fato dos perguntes utilizados estarem vinculados ao fonte da rotina, aonde o mesmo é utilizado na query de atualização das tabelas.

Algumas sugestões paliativas são:

- Checagem da viabilidade do Ponto de Entrada [**MT271FIL**](https://tdn.totvs.com/display/public/PROT/MT271FIL+-+Filtra+os+produtos) para delegação de regras que, por exemplo, considere B1\_LOCALIZ = S;

- Usuários que tem codificação padrão para produtos com controle de endereço pode-se fazer uso do campo "Máscara", onde nele pode-se definir por exemplo "produtos que começam com CE", desta forma o Protheus varre todos os produtos com essa condição pra execução do bloqueio/desbloqueio.

Caso as alternativas acima não atendam a empresa, existe a possibilidade de solicitação de melhoria do produto através da **[Central Colaborativa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466814-Funcionalidades-Dispon%C3%ADveis-na-Central-Colaborativa-TOTVS)**

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - Processo padrão para Inventariar produtos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque)*

*[Clique aqui e veja mais artigos sobre Inventário no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)*
