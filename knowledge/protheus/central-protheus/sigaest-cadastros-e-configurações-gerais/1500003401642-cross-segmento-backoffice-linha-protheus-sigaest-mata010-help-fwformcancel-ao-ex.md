---
article_id: 1500003401642
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: ea91ab12a0ffd5b3fb2cf975d6df0870e75959d063174835e0f645943ce41303
fetched_at: '2026-06-28T22:39:09.493273+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - HELP FWFORMCANCEL
  ao excluir produto no Protheus
type: support-article
updated_at: '2025-03-12T12:22:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003401642-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-HELP-FWFORMCANCEL-ao-excluir-produto-no-Protheus
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29413826620311)** Tempo aproximado para leitura: **00:04:00 min**

**Ocorrência**Ao excluir, via MATA010 - Cadastro de Produtos, um produto é apresentado o HELP "*FWFORMCANCEL - Violação de Integridade: Foi encontrada referência de Codigo (B1\_COD) na tabela SB2 / SB6 / SB9".*

**Ambiente**Microsiga Protheus - Estoque/Custos - A partir da versão 11.80

**Causa**

**Validação de Existência do Produto em Outras Tabelas**

Este problema ocorre quando o sistema Protheus identifica a existência do produto em outras tabelas além da **SB1**. Isso significa que o produto já foi utilizado em registros distintos no banco de dados, impedindo sua exclusão para garantir a integridade das informações.

A validação verifica a presença do produto em tabelas relacionadas a saldos e movimentações, como **SB2, SB6 e SB9**, ou em registros que possam conter informações de estoque e transações, tais como:

* Empenho
* Quantidade de Entrada Prevista
* Saldo em Poder de Terceiros
* Quantidade em Pedido de Vendas

Mesmo que o produto não possua registros na tabela **SB2**, sua presença em qualquer outra tabela de movimentação – por exemplo, um **Pedido de Compras** que gere uma "Quantidade de Entrada Prevista" – impedirá a exclusão. **Essa restrição é necessária para evitar inconsistências e falhas na integridade dos dados.**

**Solução**

**Em qual caso posso deletar o produto?**  
A exclusão do produto é permitida apenas quando não há vínculo com nenhuma outra tabela além da SB1 e das tabelas de saldos e movimentações.

**Tenho um produto que não consigo excluir. Existe alguma forma de bloqueá-lo para ele não ser utilizado?**

Caso um produto não possa ser excluído, é possível bloqueá-lo para impedir seu uso em novas movimentações.

Antes de realizar o bloqueio, recomenda-se verificar se há saldos empenhados, quantidades de entrada previstas ou outros vínculos. Para isso, utilize o comando **[F4]** na consulta do produto. **O ideal é que esses saldos sejam regularizados antes do bloqueio.**

Para bloquear o produto, siga os passos abaixo:

***(Esse campo é disponivel somente para o usuario ADM)***

1. Acesse a rotina **MATA010**.
2. Localize o produto desejado e clique em **Alterar**.
3. Encontre o campo **Blq. de Tela (B1\_MSBLQL)**.
4. Defina o valor como **"Sim"** para impedir qualquer tipo de movimentação.

Com essa configuração, o produto permanecerá cadastrado, porém não poderá ser utilizado em novos processos dentro do sistema.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104487113)

Com isso, qualquer rotina que o usuário tentar selecionar o produto bloqueado, ocorrerá o HELP REGBLOQ, conforme imagem abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104487173)

**Saiba mais:**

[MP - SIGAEST - Consulta com comando [F4] no Produto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-MP-SIGAEST-Consulta-F4-cadastro-de-produtos)

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033382-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
