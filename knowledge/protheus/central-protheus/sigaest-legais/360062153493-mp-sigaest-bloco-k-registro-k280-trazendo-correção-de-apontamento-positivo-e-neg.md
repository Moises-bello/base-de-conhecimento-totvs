---
article_id: 360062153493
category: SIGAEST - LEGAIS
content_hash: 3c014e7d060a92c4161922cbfd1130d55aae32c6d724c4c8ea918688db0eb86c
fetched_at: '2026-06-28T22:38:51.918284+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: MP - SIGAEST - Bloco K - Registro K280 trazendo correção de apontamento positivo
  e negativo
type: support-article
updated_at: '2021-06-24T10:40:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062153493-MP-SIGAEST-Bloco-K-Registro-K280-trazendo-corre%C3%A7%C3%A3o-de-apontamento-positivo-e-negativo
---

**Dúvida**Ao gerar o SPED Fiscal com Bloco K, o registro K280 está sendo alimentado com várias linhas trazendo saldo positivo e negativo. Como corrigir este problema?

**Ambiente**Microsiga Protheus - Estoque - A partir da versão 12.1.17

**Solução**Para solucionar este problema, siga o procedimento abaixo:

1. Aplique o pacote Acumulado do módulo de Livros Fiscais e Estoque Custos.

***Pacotes acumulados Estoque/Custos:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/960571) **|** 12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/826640) **|** 12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/748747)

***Pacotes acumulados Livros Fiscais:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/956585) **|**12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/805589) **|**12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/770598)

**Observação:** Aplicar a atualização primeiramente em ambiente de homologação. Em caso de sucesso, aplique-o em ambiente de produção.

Com o ambiente atualizado com os fontes mais atuais responsáveis pela correta geração dos registros do Bloco K, basta executar novamente o SPED Fiscal para que o problema seja devidamente corrigido.

**Saiba mais:**

*[MP - SIGAEST - Bloco K - Conceito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014906651)*

*[Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
