---
article_id: 37327614990359
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 7e53fbf470048b76331f7282ab35f97d2169a77d970db6ba4db161d9e3403df6
fetched_at: '2026-06-28T22:38:29.727959+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como emitir uma nota de Desenquadramento
  do Simples Nacional (tpNFDebito = 08)
type: support-article
updated_at: '2025-12-29T21:11:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37327614990359-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-emitir-uma-nota-de-Desenquadramento-do-Simples-Nacional-tpNFDebito-08
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37327644958999) Tempo aproximado para leitura:**00:03:00 min**  
  
**Dúvida**  
Como emitir uma nota de Desenquadramento do Simples Nacional (tpNFDebito = 08)?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da versão 12.1.2210  
  
**Solução**  
A Nota Fiscal de Débito Tipo "**Desenquadramento do Simples Nacional**" é  é utilizada para registrar o débito de tributos devido em razão da saída do contribuinte do regime do Simples Nacional, quando o desenquadramento implica ajuste ou recolhimento complementar dos tributos sob o novo regime. Essa nota serve como um documento de transição, marcando o início da incidência dos novos tributos a partir da data de efeito do desenquadramento, garantindo que o contribuinte registre o débito complementar na apuração assistida.

**Processo**:

* Ao incluir o documento de débito deve ser informado no campo de tipo "**Tipo Compl.**" como “**8 - Desenquadramento do SN**”;

(A numeração e série não são editáveis, pois serão geradas na confirmação.)

* Informe o **Cliente**e **Loja**dos documentos a serem referenciados;
* Informe uma **Condição de Pagamento**(meramente informativa, pois não haverá geração de financeiro);
* Informe na grid:

  **Produto**;

  **Quantidade -** Para este tipo de documento não deve ser informada quantidade.

  Informe o **Valor**. Será sobre este valor que haverá incidência do calculo de tributos;

  Informe uma **TES**que **não movimenta estoque** e **não gera financeiro**;
* Clique na opção **Vincular**;
  + Na parte superior, em **Filtros**, informe os dados para a busca do documento a ser referenciado nesta nota;
  + Clique em **Buscar**. Serão listados até 300 documentos de saída de acordo com os filtros na seção **Resultado do filtro**;
  + **Marque**o documento para referência. O registro marcado será listado na seção **Documentos Selecionados**;
  + Clique em **Confirmar**;
* Clique em **Confirmar**;
* Selecione a **Série**e **Numeração**para geração do documento.

**Saiba mais:**

* [Notas de Débito (NF-e: finNFe = 6 - NT 2025.002)](https://tdn.totvs.com/pages/viewpage.action?pageId=1013620273)
