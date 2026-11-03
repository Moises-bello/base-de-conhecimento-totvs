---
article_id: 39270456065687
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 3ed1003319cf1a6450849dc001790a9745d3f64fd8b73ff07c18db5a068e855d
fetched_at: '2026-06-28T22:38:45.332985+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como realizar a emissão de
  Nota Fiscal de Complemento de Preço ou Quantidade em operações de beneficiamento
  para um Fornecedor no Protheus
type: support-article
updated_at: '2026-03-27T18:52:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39270456065687-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-realizar-a-emiss%C3%A3o-de-Nota-Fiscal-de-Complemento-de-Pre%C3%A7o-ou-Quantidade-em-opera%C3%A7%C3%B5es-de-beneficiamento-para-um-Fornecedor-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39270456048151) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como realizar a emissão de Nota Fiscal de Complemento de Preço ou Quantidade em operações de beneficiamento para um Fornecedor no Protheus?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12.  
  
**Solução**  
No módulo de Faturamento (Pedido de Venda), o sistema não permite a geração de notas de saída diretamente para uma entidade cadastrada exclusivamente como **Fornecedor**. Para complementar uma nota de saída emitida para um fornecedor (comumente utilizada em processos de beneficiamento), é obrigatório que este fornecedor possua um cadastro correspondente na rotina de **Clientes**.

**Passos**

* **Complemento de Quantidade:**

1. Acesse a rotina **Cadastro de Clientes (CRMA980)** e cadastre o fornecedor em questão como um cliente;
2. Acesse a rotina **Pedido de Venda (MATA410)** e preencha o cabeçalho:

   * **Tipo Pedido (C5\_TIPO):** C - Compl.Preco/Quantidade;
   * **Cliente (C5\_CLIENTE):** Selecione o fornecedor cadastrado como cliente;
   * **Tipo Compl. (C5\_TPCOMPL):** 2 - Quantidade.
3. Preencha os itens do pedido:

   * **Produto (C6\_PRODUTO):** Informe o mesmo código do produto da NF de origem;
   * **Quantidade (C6\_QTDVEN):** Informe a quantidade que deseja complementar;
   * **Prc Unitário (C6\_PRCVEN):** Informe o mesmo preço da NF de origem;
   * **Tipo Saída (C6\_TES):** Utilize a mesma TES da NF de origem;
   * **N.F. Original (C6\_NFORI):** Digite manualmente o número da NF de origem;
   * **Série Orig. (C6\_SERIORI):** Digite manualmente a série da NF de origem;
4. Salve o pedido, realize a liberação e o faturamento.

* **Complemento de Preço:**

1. Acesse a rotina **Cadastro de Clientes (CRMA980)** e cadastre o fornecedor em questão como um cliente;
2. Acesse a rotina **Pedido de Venda (MATA410)** e preencha o cabeçalho:

   * **Tipo Pedido (C5\_TIPO):** C - Compl.Preco/Quantidade;
   * **Cliente (C5\_CLIENTE):** Selecione o fornecedor cadastrado como cliente;
   * **Tipo Compl. (C5\_TPCOMPL):** 1 - Preço.
3. Preencha os itens do pedido:

   * **Produto (C6\_PRODUTO):** Informe o mesmo código do produto da NF de origem;
   * **Quantidade (C6\_QTDVEN):** Deixe este campo zerado;
   * **Prc Unitário (C6\_PRCVEN):** Informe apenas o valor do complemento;
   * **Vlr. Total (C6\_VALOR):** Informe o mesmo valor inserido no campo "Prc Unitário";
   * **Tipo Saída (C6\_TES):** Utilize a mesma TES da NF de origem;
   * **N.F. Original (C6\_NFORI):** Digite manualmente o número da NF de origem;
   * **Série Orig. (C6\_SERIORI):** Digite manualmente a série da NF de origem;
4. Salve o pedido e proceda com o faturamento.

**Saiba Mais**

* [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Inclusão de Pedido de Vendas do Tipo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044765573-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Inclus%C3%A3o-de-Pedido-de-Vendas-do-Tipo-Complemento-de-Quantidade)
* [Complemento de Preço / Quantidade](https://tdn.totvs.com/x/ghGWDg)
