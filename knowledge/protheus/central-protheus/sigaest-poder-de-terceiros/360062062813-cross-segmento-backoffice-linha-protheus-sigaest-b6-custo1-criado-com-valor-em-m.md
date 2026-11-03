---
article_id: 360062062813
category: SIGAEST - PODER DE TERCEIROS
content_hash: 7f30bb1052baab2bb1fc459aca176e6f72cfc430c23e89509702c63e008d1e55
fetched_at: '2026-06-28T22:39:03.135473+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - B6_CUSTO1 criado com
  valor em Movimentação de TES que não atualiza estoque. O que fazer?
type: support-article
updated_at: '2022-07-07T20:31:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062062813-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-B6-CUSTO1-criado-com-valor-em-Movimenta%C3%A7%C3%A3o-de-TES-que-n%C3%A3o-atualiza-estoque-O-que-fazer
---

**Dúvida**

Fiz uma movimentação com TES que não atualiza estoque e controla poder de terceiros, porém na tabela SB6 - B6\_CUSTO1 alimentou valor. O que fazer para corrigir?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Sabemos que TES que não movimenta estoque automaticamente não gera Kardex, porém numa situação de ter havido movimento de/em terceiros com TES que não atualiza estoque mas que gera B6\_CUSTO1, pode-se tomar as seguintes ações:

**1. Dificilmente será diagnosticado o porquê gerou B6\_CUSTO com valor**

Este tipo de movimento normalmente não é notado no momento de efetuar o movimento, então muitas vezes ocorrem questionamentos de como ocorreu. Este problema pode ocorrer normalmente por dois motivos:

- Manipulação no campo via Base de Dados;

- No momento da movimentação, a TES atualizava estoque (F4\_ESTOQUE = S);

**Observação:** Quaisquer motivos que indiquem não conformidade sistêmica, deve-se imediatamente contatar o Suporte Técnico com evidências da criação indevida do campo nesta condição.

**2. Avaliar se realmente o campo D1\_CUSTO/D2\_CUSTO1 foi alimentado com valor**

Quando falamos de controle de poder de terceiros, a tabela SB6 irá fazer checagem no campo D1\_CUSTO (quando trata-se de Documento de Entrada) e D2\_CUSTO1 (quando se trata de Pedido de Venda). Se o campo foi alimentado com Custo, ele irá replicar para o campo B6\_CUSTO1 (SB6).

**3. Resolvendo o problema**

Como a orientação e solução, recomendamos que toda manipulação seja primeiramente realizado em base de homologação, por um especialista de Estoque/Custos in loco. O custo da tabela SD1/SD2 precisa estar zerado para, no momento de executar a rotina Refaz Poder de Terceiros (MATA216), o campo B6\_CUSTO1 seja recriado com valor zerado.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)*
