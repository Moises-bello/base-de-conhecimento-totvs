---
article_id: 360017748031
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 1190699722cce5402cb7dcf08f2b54e98c855383e9fce383f3fdc2a139f72805
fetched_at: '2026-06-28T22:38:39.753619+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Configurações para Bloqueio
  de Crédito
type: support-article
updated_at: '2024-12-04T12:17:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017748031-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Configura%C3%A7%C3%B5es-para-Bloqueio-de-Cr%C3%A9dito
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21457053395735) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**

Orientações para configuração de Bloqueio de Crédito do Pedido de Vendas (MATA410)

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

Para que o Bloqueio de Crédito seja respeitado no módulo Faturamento (SIGAFAT), devem ser realizadas as configurações e análises abaixo. É importante reforçar que a liberação "Automática" leva em consideração as configurações inseridas, já a liberação "Manual" ignora as configurações e força a Liberação de Crédito.

**Sobre o Bloqueio/Análise Automática de Crédito:**

**Conceito**: A Análise automática de crédito abate, do saldo de Crédito do Cliente (**A1\_LC**), o valor de Pedidos já liberados por crédito (**A1\_SALPEDL**) e o valor dos títulos em aberto (**A1\_SALDUP**).

**Obsrvação**: Títulos de NCC e RA (ainda que com data de vencimento ultrapassado) não impedem liberação automática; pois caracterizam crédito do Cliente e não débito, eles também alimentam o campo títulos em aberto (**A1\_SALDUP**) porém, com negativo para que contabilize o valor como crédito.

**Configurações básicas:**

* Configuração do parâmetro **MV\_BLOQUEI** como .T.:  Ele habilita a Análise de Crédito no Protheus, caso esteja desativado, apenas a análise de Estoque será realizada;
* Informe a moeda de análise de crédito do Cliente (**A1\_MOEDALC**), exemplo Moeda 1, caso o cliente possua Crédito em Moeda 1 e for informada a Moeda 2 no pedido, ocorrerá Bloqueio de Crédito;
* Configure o **MV\_MCUSTO** que deve ser compatível com a moeda do cadastro do cliente para a análise automática;
* Limite de crédito (**A1\_LC**): Valor de Limite que este Cliente tem de crédito com sua empresa, se estiver zerado, irá bloquear por falta de crédito;
* Risco: No cadastro de cliente, informe o risco que este cliente terá podendo ser **A,B,C,D ou E**, sendo que **risco A sempre irá liberar o crédito** e **risco E sempre irá bloquear o crédito** (Para maiores detalhes consulte: [Configurações para Análise / Bloqueio de Crédito](https://tdn.totvs.com/x/Trl3DQ);
* **Importante**: *Caso preencha o campo “**Risco**” (**A1\_RISCO**) como “**A – Risco A**”, **não** preencha o campo “**Venc.Lim.Cre**” (**A1\_VENCLC**) ou o sistema pode realizar o **Bloqueio** pelo **Vencimento do Limite de Crédito**.*
* Configure o parâmetro **MV\_CREDCLI:**
  + Se = C (Cliente) - Irá validar os dados de todas as Lojas para bloqueio do Cliente;
  + Se = L (Loja) - A análise será individual por cada Loja do Cliente (Bloqueio por loja).

Este parâmetro tem o objetivo especificamente de indicar se deve ser consultada a situação de outras Filiais antes de liberar o Pedido, de modo a permitir o bloqueio com base na inadimplência de outra Filial do mesmo Cliente!

Se **MV\_CREDCLI** = C então todas as lojas deverão conter conteúdo no campo **A1\_RISCO** (detalhes acima). Caso contrário, não será possível a avaliação de situação financeira das demais lojas para a liberação do Pedido, de modo que é exibida a mensagem: "***Atenção É necessário que o cliente e loja estejam com configurações de risco conforme outras lojas***"

**Saiba mais**:**[Configurações para bloqueio de crédito](http://tdn.totvs.com/pages/viewpage.action?pageId=225950030)**
