---
article_id: 4403501623703
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 600f05ae4be07d87fa5845480fe9e6cad66041323cd00441e6b546e3e9ae5972
fetched_at: '2026-06-28T22:38:58.449734+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação do Help
  MA265CAPAC '
type: support-article
updated_at: '2021-06-30T20:00:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403501623703-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-do-Help-MA265CAPAC
---

**Dúvida**Em Movimentos Internos (MATA240/MATA241), Transferências Internas (MATA260/MATA261) ou no Endereçamento (MATA265) ocorre o Help MA265CAPAC. Como validar este erro?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Este Help é apresentado quando o Protheus começa a fazer checagem na Capacidade do Endereço Físico (MATA015 - Tabela SBE) por meio dos campos BE\_CAPACID (capacidade), BE\_ALTURLC (altura), BE\_LARGLC (largura) e BE\_COMPRLC (comprimento) comparando-os com os Dados Adicionais do Produto (MATA010 - Tabela SB5) por meio dos campos B5\_COMPRLC (comprimento), B5\_LARGLC (largura)  e B5\_ALTURLC (altura).

Neste caso, a primeira coisa é validar se o tamanho de dígitos do campo BE\_CAPACID (capacidade) do Endereço Físico (SBE) está sendo ultrapassada pela quantidade endereçada (MATA265 - campo DB\_QUANT), ou a quantidade em qualquer movimento interno irá ultrapassar a capacidade do Endereço.

Outro cenário é quando existem os dois cadastros de cubagem, tanto de Capacidade no Endereço  quanto no Cadastro do Produto porém o do Cadastro do Produto é maior do que o do Endereço, então pode ocasionar o Help.

Caso o usuário não queira que o Protheus valide a Capacidade do Endereço Físico, basta deixar o parâmetro MV\_CAPLOCA = .F.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
