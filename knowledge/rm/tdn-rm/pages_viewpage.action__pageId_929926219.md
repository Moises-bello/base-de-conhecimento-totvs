---
content_hash: 91aa0502aaa0a2d70dbefef3cddda51220c15b0e9899e4eaa2cb5cc20ecc206f
fetched_at: '2026-06-29T00:12:08.204491+00:00'
page_id: '929926219'
product: rm
source: tdn-rm
title: Cadastro do eventos S-2501 - Leiaute 1.3 - NT 03/2025
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=929926219
version: 14
---

Evento S-2500 - Leiaute 1.2NovidadesO que está diferente?

* **Alteração da condição do campo {perRef}**

**DE:**

**PARA:**

**Alteração na Regra de Validação do Período de Referência**

A regra de validação do campo de período de referência foi ajustada para considerar a existência do campo **{ideSeqTrab}** no evento S-2500.

**Antes:** O período informado deveria existir em um evento S-2500 para o trabalhador indicado em **{cpfTrab}** e ser igual ou posterior a **[2008-12]**.

**Agora:** Além da exigência de que o período informado exista em um evento S-2500 para o trabalhador indicado em **{cpfTrab}**, a validação também passa a considerar o campo **{ideSeqTrab}**, caso esteja presente no evento S-2500 correspondente.

Essa mudança garante que a referência ao período esteja corretamente vinculada ao conjunto de dados específico de um processo trabalhista, respeitando a estrutura definida pelo eSocial.

NovidadesEntenda o evento S-2501

* **Diagramação de exemplo do S-2501**

**S-2501 sem sequencial:**

**S-2501 com sequencial:**

**Importante entender**

A definição de existir ou não um sequencial fica a cargo do cliente dada a volumetria de informações que necessitem ser enviadas ao governo.

**Observação:**   
  A chave do evento S-2501 é composta por Número do Processo + Período de Apuração de Pagamento + Sequencial (caso exista)
