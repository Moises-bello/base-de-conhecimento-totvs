---
article_id: 37325211963031
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 30ba1ad679273a45a5c57407b174c59e7fd905cd12c2aec5a1853ff3dec7914c
fetched_at: '2026-06-28T22:38:33.036400+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como emitir uma Transferência
  de créditos para Cooperativas (tpNFDebito = 01)
type: support-article
updated_at: '2025-12-29T19:18:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37325211963031-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-emitir-uma-Transfer%C3%AAncia-de-cr%C3%A9ditos-para-Cooperativas-tpNFDebito-01
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37325200145687) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como emitir uma Transferência de créditos para Cooperativas (**tpNFDebito = 01**)?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da versão 12.1.2210  
  
**Solução**  
A Nota Fiscal de débito do tipo “**Transferência de Créditos para Cooperativas**” é emitida por umAssociado (Regime Regular) para transferir à Cooperativa (Regime Específico) os créditos decorrentes de aquisições de bens e serviços fornecidos com redução de 100% da alíquota.

O sistema deve processar o valor destacado como Débito para o Associado e Crédito para a Cooperativa.

O valor transferido é limitado ao saldo de créditos de IBS não utilizados pelo Associado. Se o valor da nota exceder esse saldo, o excesso deve ser desconsiderado pelo sistema de apuração, produzindo efeito de crédito na Cooperativa apenas até o limite disponível do Emitente.

**Processo**:

* Ao incluir o documento de débito deve ser informado no campo de tipo "**Tipo Compl.**" como “**1 - Transferência de Créditos para Cooperativas**”;

(A numeração e série não são editáveis, pois serão geradas na confirmação.)

* Informe o **Cliente**e **Loja**, este deve ser a Cooperativa que receberá o Crédito proveniente desta nota de Débito;
* Informe uma **Condição de Pagamento** (meramente informativa, pois não haverá geração de financeiro);
* Informe na grid:
  + **Produto**;
  + **Quantidade** - Para este tipo de documento não deve ser informada quantidade.
* Informe o **Valor**. Será sobre este valor que haverá incidência do cálculo de tributos;
* Informe uma **TES**que **não movimenta estoque** e **não** **gera financeiro**;
* Clique na opção **Vincular**;
  + Na parte superior, em **Filtros**, informe os dados para a busca do documento a ser referenciado nesta nota;
    - Como estamos tratando da origem do Crédito a ser transferido, informe o **Fornecedor** que gerou a nota deste Crédito;
  + Clique em **Buscar**. Serão listados até 300 documentos de entrada de acordo com os filtros na seção
  + **Marque**o(s) documento(s) que deram origem ao crédito. O(s) registro(s) marcados serão listados na seção **Documentos Selecionados**;
  + Clique em **Confirmar**;
* Clique em Confirmar;
* Selecione a **Série** e **Numeração**para geração do documento.

**Saiba mais:**

* [Notas de Débito (NF-e: finNFe = 6 - NT 2025.002)](https://tdn.totvs.com/pages/viewpage.action?pageId=1013620273)
