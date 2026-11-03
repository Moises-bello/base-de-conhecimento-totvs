---
article_id: 36573314419351
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 13d6313cc75225e0774d32e9c6ba89971b9da2bef84993886d8c490241019808
fetched_at: '2026-06-28T22:38:29.781227+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Configuração do fluxo de
  Alçadas no Pedido de Venda
type: support-article
updated_at: '2026-05-18T12:15:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36573314419351-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-do-fluxo-de-Al%C3%A7adas-no-Pedido-de-Venda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36573314380055) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**

Como configurar e qual o comportamento do fluxo de alçadas no módulo Faturamento para controle de aprovação de Pedidos de Venda?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

[**How To | SIGAFAT - Configurar Alçadas no Pedido de Vendas**](https://www.youtube.com/watch?v=sMEDYnCvx9Y)

O fluxo de Alçadas para o Pedido de Venda (MATA410) restringe a manutenção e exige a aprovação de pedidos com base em regras de valor, visando o controle e a redução de erros.

Para que o processo funcione, são necessários os seguintes cadastros e configurações:

1. **Pré-requisitos:**

   * Ter Aprovadores (MATA095) e Perfis de Aprovação (COMA210) cadastrados.
2. **Configuração da Alçada:**

   * Cadastrar o Grupo de Aprovação (MATA114) com as regras desejadas (por valor de pedido ou por valor de desconto).
3. **Configuração de Parâmetros:**

   * Preencher o parâmetro **MV\_PVAPROV** com o código do Grupo de Aprovação criado no passo anterior.
   * Preencher o parâmetro **MV\_TALCFAT** para definir o tipo de alçada que será considerada:

     + 1 - Pedido de Venda: A alçada é validada pelo valor total do pedido.
     + 2 - Desconto de Venda: A alçada é validada pelo valor total de desconto no pedido.

O controle de alçadas gerará as seguintes informações para Bloquear, Rejeitar ou Liberar um pedido de vendas no campo "Controle de Aprovação" (C5\_CONAPRO) - Status:**L - Liberado**, **B - Bloqueado** (No aguardo pelo responsável para sua validação) e **R - Rejeitado** (Rejeitado pelo responsável).

A liberação é feita na rotina **Liberação de Documentos (MATA094).**

**Observação 1**: A validação da alçada de aprovação ocorresempre antes dos bloqueios de Regra/Verba, Crédito e Estoque.

**Observação 2:** Estorno de Liberação **-** só é possível antes da liberação de crédito ou crédito/estoque. Após isso, deve-se estornar o pedido pelo fluxo de faturamento, para que o aprovador possa atuar novamente na MATA094.

**Observação 3:** O processo de Alçadas só é executado via preenchimento do parâmetro **MV\_PVAPROV** e não considera a aba "Entidades Contábeis" na configuração do Grupo de Aprovação.

**Saiba mais:**

* [Alçada de Aprovação - Pedido de Venda (MATA094 - SIGAFAT)](https://tdn.totvs.com/x/n1D4Lw)
