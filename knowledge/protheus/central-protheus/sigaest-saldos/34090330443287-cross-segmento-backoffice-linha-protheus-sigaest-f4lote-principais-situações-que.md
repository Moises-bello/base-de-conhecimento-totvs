---
article_id: 34090330443287
category: SIGAEST - SALDOS
content_hash: 822d415d4d27f98b05ab3d5fd10671b6e07a68688a568a63d5960d4f2474d167
fetched_at: '2026-06-28T22:39:14.857159+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - F4LOTE - Principais
  situações que podem apresentar esse HELP
type: support-article
updated_at: '2025-08-11T12:05:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34090330443287-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-F4LOTE-Principais-situa%C3%A7%C3%B5es-que-podem-apresentar-esse-HELP
---

O artigo aborda um problema ao tentar movimentar produtos com controle de lote no TOTVS Backoffice (Linha Protheus), onde o sistema apresenta o HELP F4LOTE. Isso ocorre quando não há saldo de lote disponível para a movimentação. A solução envolve verificar o saldo atual do produto, confirmar a ativação do parâmetro MV\_RASTRO, garantir que não há desbalanceamento de saldos, checar se o produto pertence a terceiros e se o lote está vencido. Caso o problema persista, recomenda-se testar em um ambiente atualizado e desativar customizações.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34090287599383) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao tentar efetuar uma movimentação de saida/requisição de um produto que tem controle de lote, o HELP F4LOTE é apresentado em tela.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34090330439959)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**  
Quando o HELP é acionado, significa que o sistema não achou relação do saldo do lote do produto para a movimentação. Assim, ao tentar requisitar saldo do produto em algumas rotinas o sistema apresenta o help **F4LOTE**.

**Solução**

### **Verifique as possibilidades de solução dependendo do seu cenário:**

1. Verifique se o Saldo ATUAL do Produto, existe de fato no local o qual voce quer requisitar a quantia de movimentação ([Como descobrir a origem dos saldos na consulta com comando [F4]](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-MP-SIGAEST-Consulta-F4-cadastro-de-produtos));

2. Confira de fato se o parametro **MV\_RASTRO** esteja ativo no ambiente, bem como no cadastro do produto, o campo "Rastro **B1\_RASTRO**" esteja configurado para o controle devido de L = Lote.

3. Certifique que o produto **não possua algum desbalanceamento** de saldos, apartir da geração do relaotiro MATR282 [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR282 - Parametrização para validar divergência de saldos SB2 x SB8 x SBF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-para-validar-diverg%C3%AAncia-de-saldos-SB2-x-SB8-x-SBF)

4. Valide de fato, **se não foi efetuada alguma "Manutenção no banco"** para os registros de movimentação desse item, como **SD3/SD5/SB8**.

5. Verifique se o saldo do produto pertence a Terceiros ([É possível requisitar ou consumir Saldo de Terceiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052767993-MP-SIGAEST-Requisitar-ou-consumir-Saldo-de-Terceiro-no-Estoque))

6. Verifique se o lote esteja vencido ([Movimentar produto com Lote Vencido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025875571-MP-SIGAEST-MATA275-Faturar-ou-Inventariar-produto-com-Lote-Vencido-que-esta-bloqueado-para-movimenta%C3%A7%C3%A3o?source=search))

### **Caso após as verificações o problema persista, avalie:**

1. Interferência de incompatibilidade de fontes (necessário testar em ambiente atualizado)

2. Interferência de customizações (necessário testar desativando as customizações do ambiente através dos [3 métodos indicados nesta documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292), impreterivelmente)*.*

**Sobre o controle de lotes no FATURAMENTO:**  
[Uso de Lote, Endereçamento e Serie no Faturamento (SIGAFAT)](https://tdn.totvs.com/x/DpNvI)

**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
