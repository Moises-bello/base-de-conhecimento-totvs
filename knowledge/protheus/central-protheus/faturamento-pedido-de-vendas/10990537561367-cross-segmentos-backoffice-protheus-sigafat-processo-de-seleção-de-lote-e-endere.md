---
article_id: 10990537561367
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: cd46c24aff2475f7a956eabcf16445daa1f82a81f3ec5a83d23118e87600f7fe
fetched_at: '2026-06-28T22:38:40.001644+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Processo de seleção de Lote
  e Endereçamento no Faturamento
type: support-article
updated_at: '2026-05-07T21:41:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10990537561367-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Processo-de-sele%C3%A7%C3%A3o-de-Lote-e-Endere%C3%A7amento-no-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40314099441431) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Como utilizar Lotes e Endereçamento no módulo de Faturamento (SIGAFAT)  
  
**Ambiente**  
Cross Segmentos - BackOffice Protheus - SIGAFAT - Todas as versões.  
  
**Solução**

Para utilizar o controle de Lote (Rastreabilidade) e Endereçamento (Localização) no Faturamento, verifique as configurações e processos abaixo:

### 1. Requisitos Prévios

* **Para Lote:** Parâmetro MV\_RASTRO = S e campo Rastro (B1\_RASTRO) no Cadastro de Produtos (MATA010) preenchido como "L" ou "S".
* **Para Endereço:** Parâmetro MV\_LOCALIZ = S e campo Contr.Endere (B1\_LOCALIZ) no Cadastro de Produtos (MATA010) como "S".

---

### 2. Processo de Lote (Rastreabilidade)

O número do lote pode ser definido de duas formas:

* **Seleção Manual:** No Pedido de Venda (MATA410), posicione no campo Lote (C6\_LOTECTL) e pressione F4 para escolher o lote disponível.
* **Seleção Automática:** Caso o campo no pedido fique em branco, o sistema selecionará o lote automaticamente no momento da Liberação do Pedido, utilizando o conceito *FIFO* (primeiro que vence, sai primeiro). O número do lote será gravado diretamente nas tabelas SC9 (Pedidos Liberados) e SD2 (Itens da NF).

**Observação 1:** Após o faturamento da nota, não é possível alterar o lote. Caso precise trocar, será necessário excluir a nota fiscal.

---

### 3. Processo de Endereçamento (Localização)

* **Seleção Manual:** No Pedido de Venda (MATA410), posicione no campo Endereço (C6\_LOCALIZ) e pressione F4 para selecionar o saldo por endereço.
* **Seleção Automática:** Se não informado manualmente, o sistema fará a seleção automática conforme o saldo em estoque.

**Observação 2****:** O endereçamento é um controle interno de estoque e essa informação não é levada para a nota fiscal.

**Saiba mais**:

* [Uso de Lote e Endereçamento no Faturamento (SIGAFAT)](https://tdn.totvs.com/x/DpNvI)
* [Cross Segmentos - Backoffice Protheus - SIGAFAT - Como habilitar o botão "Lote e endereços" na opção "Nova Liberação" da rotina de Liberação de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044388894-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-habilitar-o-bot%C3%A3o-Lote-e-endere%C3%A7os-na-op%C3%A7%C3%A3o-Nova-Libera%C3%A7%C3%A3o-da-rotina-de-Libera%C3%A7%C3%A3o-de-Estoque)
