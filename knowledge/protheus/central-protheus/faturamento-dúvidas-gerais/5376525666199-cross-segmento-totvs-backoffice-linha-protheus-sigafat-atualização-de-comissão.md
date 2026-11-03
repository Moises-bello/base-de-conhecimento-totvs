---
article_id: 5376525666199
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 4d14971d7af9e0290e0336cc26694dbc294e54b3e4f4040bcc121a1c69623ebe
fetched_at: '2026-06-28T22:38:28.509012+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Atualização
  de Comissão
type: support-article
updated_at: '2022-04-11T17:55:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5376525666199-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Atualiza%C3%A7%C3%A3o-de-Comiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:04:00** **min** **Dúvida**Como gerar o titulo a pagar da comissão gerada na SE3?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões  
  
**Solução**

A atualização de comissão (**MATA530**) é a rotina gera a integração entre as **Comissões** e as rotinas de **Folha de Pagamento** e/ou **Contas a Pagar**. É responsável também por processar e gravar as datas das baixas de pagamento das comissões na tabela **SE3**.

Para que haja a geração de um titulo a pagar ao rodar a atualização de comissão é necessário:

* Informar o conteúdo "**S – Contas a Pagar**" no campo “**Forma Pgto**” (**A3\_GERASE2**);
* Vincular um fornecedor ao cadastro do Vendedor pelo campo “**Fornecedor**” (**A3\_FORNECE**);

**Observação**: O título a pagar será gerado com o Prefixo “**COM**”, em nome do Fornecedor vinculado ao vendedor e somando todos os valores de comissões do período.

**Parâmetros da Rotina**:

* **Gera pela**: Processa as comissões geradas pela Emissão, pela Baixa, Todas ou Manual (Incluídas manualmente);
* **Considera Data / Até a Data**: Filtra as comissões, a serem processadas, pela data de emissão (E3\_EMISSAO);
* **Do Vendedor / Até o Vendedor**: Filtra o processamento das comissões pelo vendedor (E3\_VEND);
* **Data de Pagamento**: Data do Pagamento da Comissão a ser registrada (E3\_DATA);
* **Habilita interface de Pagamento**: Habilita/Desabilita a integração das comissões com o Contas a Pagar ou Folha de pagamento;
* **Contabiliza On-line / Mostra Lct.Contabil**: Habilita/Desabilita Contabilização dos Títulos gerados;
* **Do Vencimento / Até o Vencimento**: Filtra o processamento das comissões pelo vencimento da Comissão (E3\_VENCTO):
  + O vencimento (E3\_VENCTO) é determinado pelo “**Dia Pgto Com**” (**A3\_DIA**), no cadastro do vendedor;

* **Considera Data**: Considera a data de vencimento dos títulos a partir do Vencimento da Comissão (**E3\_VENCTO**) ou a data de pagamento preenchida na pergunta “**Data de Pagamento**”;
* **Seleciona Filiais / Filial De / Filial Até**: Seleciona os registros por filial.

Ao acessar rotina mata530, defina os parâmetros , levando em consideração a informação acima e processo a rotina.

Ao finalizar, o sistema baixa o registro na SE3 e gera o título a pagar na sE2.

Em anexo, tem a visão do processo de atualização.
