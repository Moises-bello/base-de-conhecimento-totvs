---
article_id: 360058347413
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 1138bf86c7d98faee507bf8ac60f0111548be4cdc476e055135f016430ab15f3
fetched_at: '2026-06-28T22:38:54.032467+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MA240NEGAT - Principais
  situações que podem apresentar esse help
type: support-article
updated_at: '2026-04-01T20:20:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058347413-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MA240NEGAT-Principais-situa%C3%A7%C3%B5es-que-podem-apresentar-esse-help
---

As mensagens HELP MA240NEGAT e MA240NEGLT ocorrem no TOTVS Protheus quando o parâmetro MV\_ESTNEG impede movimentações que gerariam estoque negativo. Para MA240NEGAT, é necessário verificar saldos em outros armazéns, reservas, lotes vencidos e configurações de parâmetros. MA240NEGLT indica divergências entre tabelas SB2 e SB8, exigindo validação do preenchimento do lote. Caso persista, avalie incompatibilidades de fontes e customizações.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18497478014487) Tempo aproximado para leitura: **00:04:00 min**

**Ocorrência**  
Ao efetuar determinadas movimentações e transferências ocorre o **HELP MA240NEGAT/MA240NEGLT**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14183233162135)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34661107433367)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**

Quando o parâmetro **MV\_ESTNEG** está com conteúdo "N" significa que o sistema não deve deixar que movimentações que gerariam um estoque negativo sejam realizadas. Assim, ao tentar requisitar saldo do produto em algumas rotinas o sistema apresenta o help **MA240NEGAT**.

**Solução**

**MA240NEGAT**

Verifique as possibilidades de solução dependendo do seu cenário:

1. Verifique se o Saldo do Produto está em outro Armazém ([Como descobrir a origem dos saldos na consulta com comando [F4]](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-MP-SIGAEST-Consulta-F4-cadastro-de-produtos));

2. Verifique se o Saldo do Produto está empenhado em alguma Ordem de Produção;

3. Verifique se o saldo está reservado para algum Pedido de Vendas;

4. Verifique se o saldo está empenhado para alguma Solicitações ao Armazém;

5. Verifique se o saldo do produto pertence a Terceiros ([É possível requisitar ou consumir Saldo de Terceiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052767993-MP-SIGAEST-Requisitar-ou-consumir-Saldo-de-Terceiro-no-Estoque))

6. Se o parâmetro MV\_TPSALDO esta igual a S ou C, analise se a configuração deveria considerar o saldo ([Utilização do parâmetro MV\_TPSALDO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013215531-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-SX6-MV-TPSALDO))

**Se o produto controlar Lote/Endereço**:

1. Se o produto controlar Lote, verifique se o mesmo está vencido ([Movimentar produto com Lote Vencido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025875571-MP-SIGAEST-MATA275-Faturar-ou-Inventariar-produto-com-Lote-Vencido-que-esta-bloqueado-para-movimenta%C3%A7%C3%A3o?source=search))

2. Se o produto controlar Lote, verifique o saldo do Lote;

3. Se o produto controlar endereço, verifique o saldo no endereço;

4. Se o produto controlar Lote e/ou Endereço, verifique se esta desbalanceado entre as tabelas ([Identificar divergência de saldos entre tabelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-MP-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-para-identificar-diverg%C3%AAncia-de-saldos-entre-tabelas-SB2-X-SB8-X-SBF));

**Caso após as verificações o problema persista, avalie:**

1. Interferência de incompatibilidade de fontes (necessário testar em ambiente atualizo)

2. Interferência de customizações (necessário testar desativando as customizações do ambiente através dos [3 métodos indicados nesta documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292), impreterivelmente)*.*

**MA240NEGLT**

A mensagem **MA240NEGLT**pode ocorrer quando há uma divergência nas tabelas de saldo de estoque **SB2 - Saldos Físico e Financeiro** e **SB8 - Saldos por Lote.**

Validar se o conteudo do preenchimento do lote esta correto, se o tamanho de campo esteja correto, bem como se há espaçamentos indevidos pode ser a causa.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
