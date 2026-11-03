---
article_id: 360061854034
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: b9df19e3ecc4da0dd2937ed17e5f434f1566d2ecbaacf27050edadffc3247c43
fetched_at: '2026-06-28T22:39:09.506538+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Houve uma
  alteração de grupo do produto
type: support-article
updated_at: '2025-03-12T12:22:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061854034-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Houve-uma-altera%C3%A7%C3%A3o-de-grupo-do-produto
---

**Dúvida**Ao efetuar, via MATA010 - Cadastro de Produtos, a alteração do Grupo de Produto (B1\_GRUPO), ocorre a seguinte mensagem "*Houve uma alteração de grupo do produto, o mesmo requer acesso exclusivo ao sistema em modo SIGAADV."*Como resolver este problema?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003486281/mceclip0.png)  
**Ambiente**Microsiga Protheus - Estoque/Custos - A partir da versão 11.80

**Solução**

Este erro normalmente ocorre quando o parâmetro MV\_VEICULO está ativado (quando ocorre ativação do módulo de veículos integrado). Desta forma, basta desabilitar o parâmetro, deixando-o como **MV\_VEICULO = N**para que essa inconsistência não volte a ocorrer.

Caso mesmo assim persista, avalie se outro usuário está fazendo alteração no grupo de produtos, pois essa alteração ocorre em modo exclusivo. Caso contrário, o sistema bloqueia para evitar falha de integridade de dados.

**Saiba mais:**

*[MP - SIGAEST- MATA010 - Erro THREAD ERROR: Nome de coluna 'CDV\_PRODUT' inválido.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021428711-MP-SIGAEST-MATA010-Erro-THREAD-ERROR-Nome-de-coluna-CDV-PRODUT-inv%C3%A1lido-)*

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais para o Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033382-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
