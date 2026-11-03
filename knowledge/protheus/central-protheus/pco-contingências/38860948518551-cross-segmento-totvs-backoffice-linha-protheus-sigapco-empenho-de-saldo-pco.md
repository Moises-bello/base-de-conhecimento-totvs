---
article_id: 38860948518551
category: PCO - Contingências
content_hash: 251bb62f94ce071c187be86f628d64683e813d7b43931fccb5e9ee7bafa9027f
fetched_at: '2026-06-28T22:37:12.179144+00:00'
product: protheus
section_id: 1500001539761
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPCO - Empenho de saldo
  PCO
type: support-article
updated_at: '2026-03-09T11:52:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38860948518551-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAPCO-Empenho-de-saldo-PCO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38860925058583) Tempo aproximado para leitura: 00:10 min  
  
**Dúvida**  
Como configurar e utilizar o processo de empenho de saldo (contingência) no módulo de Planejamento e Controle Orçamentário (SIGAPCO)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPCO - A partir da versão 12  
  
**Solução**  
O empenho de saldo no PCO tem a finalidade de reservar (bloquear) um valor do orçamento disponível no momento em que uma solicitação de contingência é gerada por falta de saldo, impedindo que outros processos utilizem esse mesmo limite enquanto a contingência aguarda aprovação.

Para que o sistema realize esse controle corretamente, é necessário configurar os tipos de saldo, os pontos de lançamento do processo de contingência (Processo 356) e os totalizadores nos Cubos Gerenciais.

**Configurações no SIGAPCO**

1. Acesse Atualizações > Cadastros > Tipos de Saldo.
2. Verifique se o tipo de saldo para Empenho (exemplo: Código `EM`, Descrição `EMPENHO`) está devidamente cadastrado.
3. Acesse Atualizações > Lançamentos > Por Processos.
4. Localize e altere o processo 356 (Liberação de Solicitação de Contingência).
5. Selecione o Item 2 (que trata do lançamento de contingência) e acesse a Configuração do Lançamento.
6. Marque a flag indicando que o ponto de lançamento está em uso.
7. Configure as informações dos campos, baseando-se na tabela de itens da contingência (`ALJ`). Para o valor do empenho, referencie o campo específico da tabela (ex: `EMPIVAL`), além de configurar os campos de Conta e Centro de Custo.
8. Salve as configurações do processo e acesse Atualizações > Cubos > Cubos Gerenciais.
9. Posicione no cubo utilizado para a verificação (ex: Cubo 1, com níveis de Conta e Centro de Custo) e edite suas configurações.
10. Na amarração dos Tipos de Saldo, configure para que a apuração do bloqueio considere o empenho. Exemplo prático de configuração de soma:

    * Orçado: Somar o saldo Orçado + Contingência (`OR` + `CT`).
    * Realizado: Somar o saldo Realizado + Empenho (`RE` + `EM`).
11. Salve as configurações do cubo.

    |  |
    | --- |
    |  |

**Validação e Utilização do Empenho**

12. No **SIGAPCO**, acesse Atualizações > Planilhas > Lançamentos e inclua um saldo inicial orçado. *Exemplo: Inclusão de um lançamento a crédito, tipo de saldo Orçado (OR), no valor de R$ 1.000,00 para uma conta e centro de custo específicos.*
13. Acesse o módulo integrado (ex: SIGACOM - Compras) e gere um movimento que estoure o orçamento, como a inclusão de um Pedido de Compra (`MATA121`) no valor de R$ 1.500,00 para a mesma amarração gerencial.
14. Ao tentar salvar o pedido, o sistema apresentará a tela de bloqueio por **Saldo Insuficiente**, demonstrando o **Orçamento** (R$ 1.000,00), o **Realizado** (R$ 1.500,00) e a necessidade de contingência (R$ 500,00).
15. Clique no botão Contingência para solicitar a aprovação. O sistema irá gerar a solicitação e empenhar (reservar) os R$ 1.000,00 disponíveis.
16. Validação do Empenho: Se você tentar incluir um novo Pedido de Compra de R$ 500,00 para a mesma conta/centro de custo, o sistema bloqueará novamente. Desta vez, exigirá uma contingência do valor total (R$ 500,00), pois os R$ 1.000,00 orçados inicialmente já foram bloqueados/empenhados pelo processo anterior que aguarda liberação.

    |  |
    | --- |
    |  |

**Saiba Mais**

[SIGAPCO Utilização de Contingência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018523352-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Utiliza%C3%A7%C3%A3o-de-Conting%C3%AAncia)  
[SIGAPCO Como Vincular a Contingência ao Processo Solicitante](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38860632078231-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAPCO-Como-Vincular-a-Conting%C3%AAncia-ao-Processo-Solicitante)
