---
article_id: 10533626636311
category: Originação de Grãos (OG)
content_hash: 48b6a963f8e2bd81b2cf6de076ab692686f7dfd9733dc5bdc22d4338a4c455d0
fetched_at: '2026-06-28T22:45:41.031867+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Moeda Estrangeira no Contrato de Venda - Exemplo
  de Utilização
type: support-article
updated_at: '2025-04-10T13:48:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10533626636311-Agro-Linha-Protheus-AGR-Moeda-Estrangeira-no-Contrato-de-Venda-Exemplo-de-Utiliza%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20417319331095)*** Tempo aproximado para leitura: **00:01:20 min****Dúvida**  
Como incluir um **contrato de venda fixo em moeda estrangeira**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**1.** Realize os parâmetros **MV\_AGRO001**, **MV\_AGRA002** e **MV\_AGRO040**habilitados, pois todos parâmetros devem ser alterados no módulo **Configurador**;

**2.** Analise em **Gestão de Agronegócio - SIGAAGR** acessando em **Atualizações > Comercialização > Negociação > Contrato de Venda > Contrato de Venda**;

**3.** Clique em **Incluir**;

**4.** Informe os campos obrigatórios;

* Na pasta Principal: **Entidade, Safra, Produto, TES**;
* Na pasta Previsão de Entrega: **Quantidade, Filial de Origem**;
* Na pasta Financeiro: **Contrato, Tipo Valor, Quantidade/Percentual**.
* Na pasta Dados Negócio/Financeiro: O campo ***Tipo Fix*. para 1 - Fixo**.
* Para caracterizar o contrato de venda como moeda estrangeira informe os dados abaixo:
* Na pasta Principal do campo: **Tipo de Mercado** deve ser 1 - Interno;
* Na pasta Dados Negócio/Financeiro campo: **Moeda** deve ser diferente de 1.

**5.** Informe os dados e clique em **Confirmar**;

**6.** Acesse **Outras Ações > Fixação de Preço** e realize a fixação de preço;

**7.** Informe os valores nos componentes e clique em **Confirmar**. Observar que o preço de venda que foi fixado está na moeda do contrato;

* Acesse **Outras Ações > Gerar Previsão Financeira** para gerar os valores financeiros.
* Acesse **Outras Ações > Confirmar** para efetivar o contrato de venda.

**8.** Observe na imagem a seguir é exibido um exemplo de fixação de preço. Quando o contrato de venda é fixo, a fixação será sempre de preço. Portanto, não é permitido fixar apenas o componente. Sendo moeda estrangeira, a fixação é na moeda do contrato;

![EXEM.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10535065243415)

**9.** Realize os parâmetros **MV\_AGRO001**, **MV\_AGRA002** e **MV\_AGRO040** habilitados, pois todos parâmetros devem ser alterados no módulo **Configurador**;

**10.** Analise em **Gestão de Agronegócio - SIGAAGR** acessando em **Atualizações > Comercialização > Negociação > Contrato de Venda > Contrato de Venda**;

**11.** Clique em **Incluir**;

**12.** Informe os campos obrigatórios;

* Na pasta Principal: **Entidade, Safra, Produto, TES**;
* Na pasta Previsão de Entrega*:***Quantidade, Filial de Origem, Data Limite de Fixação, Mês Bolsa,  Negócio**;
* Na pasta Financeiro: **Contrato, Tipo Valor, Quantidade/Percentual**.
* Na pasta Dados Negócio/Financeiro**:** O campo **Tipo Fix**. **para 2 - A Fixar**.
* Para caracterizar o contrato de venda como moeda estrangeira informe os dados abaixo;
* Na pasta Principal: O campo **Tipo de Mercado deve ser 1 - Interno**;
* Na pasta Dados Negócio/Financeiro: O campo **Moeda deve ser diferente de 1**.

**13.** Clique em **Confirmar** e informe os dados;

**14.** Realize a fixação de componente, acessando em **Outras Ações > Fixação de Preço**;

**15.** Informe os valores nos componentes e clique em **Confirmar**. Em contratos a fixar somente é possível fixar os componentes. Para fechar o valor, a fixação de preço deve ocorrer pelo **Painel de Fixações**;

**16.** Acesse **Outras Ações > Gerar Previsão Financeira** para gerar os valores financeiros. Nesse momento, como não há fixação de preço os valores são calculados em base ao índice informado;

**17.** Acesse **Outras Ações > Confirmar** para efetivar o contrato de venda;

**18.** Verifique em **Gestão de Agronegócio - SIGAAGR** acessando **Atualizações > Comercialização > Negociação > Contrato de Venda > Contrato de Venda**;

**19.** Posicione no contrato de venda que deseja consultar;

**20.** Clique em **Visualizar**;

**21.** Clique na pasta **Financeiro**;

**22.** Verifique na parte inferior, pois são apresentadas as previsões financeiras que foram geradas na data de vencimento e valor;

**23.** Realize a gestão dos títulos utilize o **Painel Financeiro**;

**24.** Realize a consulta dos valores financeiros, de faturamento e fixados em **Gestão de Agronegócio -  SIGAAGR** acessando **Atualizações > Comercialização > Negociação > Contrato de Venda > Contrato de Venda***;*

**25.** Posicione no contrato de venda que deseja consultar;

**26.** Clique em **Visualizar**;

**27.** Clique na pasta **Previsão de Entrega**;

**28.** Verifique na tabela superior da pasta **Previsão de Entrega** selecione a cadência que deseja consultar os valores;

**29.** Verifique na tabela inferior da pasta Previsão de Entrega são exibidas regras fiscais. Para cada regra fiscal é possível ter acessos aos valores do contrato nos campos **Tot. Fin**, **Vlr. Tot. Fate** **Vlr. Tot. Fix;**

**30.** Analise na nova comercialização se existe o conceito de regra fiscal que é similar a um pedido. Uma previsão de entrega pode ter uma ou mais regras fiscais;

**31.** Gere um relatório com os dados financeiro faturamento e fixação;

**32.** Verifique em **Gestão de Agronegócio - SIGAAGR** acessando **Atualizações > Comercialização > Negociação > Contrato de Venda > Contrato de Venda***;*

**33.** Posicione no contrato de venda que deseja gerar o relatório;

**34.** Clique em **Outras Ações > Mais Ações > Extrato Contrato**.
