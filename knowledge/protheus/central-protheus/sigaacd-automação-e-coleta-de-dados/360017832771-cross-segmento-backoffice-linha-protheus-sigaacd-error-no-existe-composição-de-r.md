---
article_id: 360017832771
category: SIGAACD - Automação e Coleta de Dados
content_hash: 4fbc8c9058c515248334c12568fe474cd1f88d3adbb053e4c0cd62938aaab8db
fetched_at: '2026-06-28T22:39:11.011498+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Error "No existe composição
  de reserva (SDC)"
type: support-article
updated_at: '2025-07-29T20:16:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017832771-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Error-No-existe-composi%C3%A7%C3%A3o-de-reserva-SDC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33797818977303)  Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Error "No existe composicao de reserva (SDC)"

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Durante o processo de geração de uma **Ordem de Separação (OS)**, pode ser apresentado o seguinte erro:

```
Pedido 000333 - Cliente: 000001-01 - Lugar: 01  
Orden de Separacion: NO GENERADA  
Motivo:  
Item 01 - Producto: BAN 34X62 ECON - Lugar: 01  
--> No existe composicion de reserva (SDC)
```

Este erro indica que o sistema não encontrou a **composição de reserva de estoque (registro na tabela SDC)** para o item e local informados.

### **Causas Prováveis e Soluções**

#### **1. Origem: Pedido de Venda**

**Causa**:  
Ao gerar uma OS com origem em **Pedido de Venda**, o erro pode ocorrer quando o item possui controle por **endereço logístico**, mas a **TES (Tipo de Entrada/Saída)** vinculada ao pedido está parametrizada para **não atualizar o estoque**.  
Consequentemente, não há saldo reservado na **tabela SDC**, que é utilizada pelo módulo de separação.

**Solução**:

* Acesse o cadastro da **TES** utilizada no pedido.
* Verifique se o campo **Atualiza Estoque** está **ativado (Sim)**.
* Caso contrário, ajuste a TES ou utilize uma TES que efetivamente atualize o estoque.
* Gere o pedido novamente e refaça o processo de geração da Ordem de Separação.

#### **2. Origem: Ordem de Produção**

**Causa**:  
Na geração de uma OS a partir de uma **Ordem de Produção (OP)**, este erro ocorre quando o(s) produto(s) controlado(s) por endereço não são corretamente **empenhados**. Isso normalmente acontece quando o **Tipo de Movimento (TM)** definido no parâmetro `MV_CBREQD3` está configurado para **não atualizar o empenho**.

**Solução**:

* Acesse o cadastro do **Tipo de Movimento (TM)** definido no parâmetro `MV_CBREQD3`.
* Certifique-se de que o TM está configurado para **atualizar o empenho**.
* Caso necessário, ajuste a configuração do TM para garantir a correta reserva dos produtos na tabela SDC.
* Após a correção, reprocessar a geração da Ordem de Separação.

### **Informações Técnicas Adicionais**

* **Tabela SDC**: Responsável por armazenar as **reservas de estoque por endereço**, utilizadas pelo módulo de **Automação e Coleta de Dados (ACD)** nas operações de separação.
* **Controle por endereço**: Produtos com controle logístico exigem movimentações que atualizem corretamente saldo e reservas por endereço.
* **Empenho**: A reserva de estoque com finalidade de separação depende da correta geração de empenhos vinculados ao pedido ou OP.

**Saiba mais**

[Acesse artigos complementares sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas#:~:text=Saiba%20Mais%3A,Coleta%20de%20Dados)
