---
article_id: 4402126343447
category: Materiais - Compras (SIGACOM)
content_hash: 72d83d5b6a92e1f0b7019e2469fa6acd445e7575f8f3b35ebb33c033380fe222
fetched_at: '2026-06-28T22:41:17.417734+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É Possível Acrescentar
  o Valor do Frete ao Valor do Ativo Imobilizado, quando há vinculo com a Nota de
  Entrada do Bem ?
type: support-article
updated_at: '2022-05-16T22:53:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402126343447-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-Poss%C3%ADvel-Acrescentar-o-Valor-do-Frete-ao-Valor-do-Ativo-Imobilizado-quando-h%C3%A1-vinculo-com-a-Nota-de-Entrada-do-Bem
---

**Dúvida**

É Possível Acrescentar o Valor do Frete ao Valor do Ativo Imobilizado, quando há vinculo com a Nota de Entrada do Bem ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões  
  
**Solução**

**Pelo módulo de compras** mesmo que a nota de **conhecimento de frete, incluída** pela rotina de documento de entrada (**MATA103**) ou pela rotina Nt. Conhec. frete (**MATA116**), seja vinculada a nota de entrada da compra do ativo, **não há a junção** do valor do frete no valor do ativo imobilizado no cadastro de ativos (módulo Ativo - rotina ATFA012).

Porém, dentro do módulo de ativo, temos uma rotina padrão, Aquisição por transferência (**ATFA251**),onde ao executá-la o sistema conseguirá efetuar a junção do valor do frete ao valor do ativo, para isso, é necessário que, o TES de compra do frete também esteja configurado para atualizar o ativo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402125389079/mceclip0.png)

Para saber mais sobre a rotina do módulo de ativo, veja abaixo :

[ATFA251 - Agregar-Aglutinar-Desmembrar-bens-do-ativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006767052-MP-SIGAATF-ATFA251-Agregar-Aglutinar-Desmembrar-bens-do-ativo?source=search)

Caso tenha alguma dúvida em como executar a rotina ATFA251, por favor abrir um ticket para a equipe de suporte do ativo.

Para os casos onde o valor do frete esteja lançado na mesma nota de compras do ativo imobilizado, temos o parâmetro **MV\_VLRATF**, conforme documento abaixo :

[MP - SIGAATF - Ativo Fixo x Frete / IPTU /Seguros / Licença de Uso](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016120672-MP-SIGAATF-Ativo-Fixo-x-Frete-IPTU-Seguros-Licen%C3%A7a-de-Uso?source=search)

***Saíba Mais :***

[ATFA251 - Agregar-Aglutinar-Desmembrar-bens-do-ativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006767052-MP-SIGAATF-ATFA251-Agregar-Aglutinar-Desmembrar-bens-do-ativo?source=search)

[MP - SIGAATF - Ativo Fixo x Frete / IPTU /Seguros / Licença de Uso](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016120672-MP-SIGAATF-Ativo-Fixo-x-Frete-IPTU-Seguros-Licen%C3%A7a-de-Uso?source=search)

*[PÁGINA](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)* *[CENTRALIZADORA DO COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)*

*[MAIS ARTIGOS MATERIAIS - COMPRAS -](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)*  [SIGACOM](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
