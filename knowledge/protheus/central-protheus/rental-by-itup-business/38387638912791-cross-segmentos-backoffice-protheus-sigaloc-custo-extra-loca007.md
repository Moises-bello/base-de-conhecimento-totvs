---
article_id: 38387638912791
category: Rental by ItUp Business
content_hash: 1fb122085562c80d4aae6aa7aa33ac9c14a698e0fa89dab93b01be10fd66cd63
fetched_at: '2026-06-28T22:36:20.604565+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Custo Extra (LOCA007)
type: support-article
updated_at: '2026-02-13T20:43:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38387638912791-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Custo-Extra-LOCA007
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38387630189207) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como criar e faturar um custo extra referente a um projeto no sistema SIGALOC?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões.  
  
**Solução**  
Para realizar esse processo, siga os passos abaixo:

**Etapa 1: Lançamento do Custo Extra**

1. Acesse o módulo **Rental (94)** > Atualizações > Comercial > **Orçamento (LOCA001)**;
2. Selecione o orçamento desejado, clique em **Outras Ações** e escolha a opção **Custos Extras (LOCA007)**;
3. Clique em **Incluir** e preencha os campos essenciais:

   * **Projeto (FPG\_PROJET):** Número do contrato/projeto vinculado.
   * **Nr. AS (FPG\_NRAS):** Número da Autorização de Serviço vinculada.
   * **Produto (FPG\_PRODUT):** Código do produto que originou o custo.
   * **Quantidade (FPG\_QUANT):** Quantidade do item.
   * **Vl. Unitário (FPG\_VLUNIT):** Valor unitário do custo.
   * **Cobrar (FPG\_COBRAR):** Defina como **S - Sim** para que o valor seja enviado ao cliente.
   * **Junto (FPG\_JUNTO):** \* **S - Sim:** O faturamento ocorrerá junto com a medição da locação, **N - Não:** O custo será faturado de forma isolada.
   * **Natureza (FPG\_NATURE):** Informe a natureza financeira para integração com o Financeiro.
4. Confirme a gravação do registro.

**Etapa 2: Faturamento do Custo Extra**

1. Acesse **Outras Ações** > **Faturamento Automático (LOCA021)**;
2. Nas perguntas (parâmetros) da rotina, altere o campo **Tipo de Projeto** para **Custo Extra**;
3. Selecione o projeto e clique em **OK** para processar e gerar o Pedido de Venda/Nota Fiscal.

**Saiba mais:** [***Custos Extras***](https://tdn.totvs.com/display/public/PROT/Custos+Extras)
