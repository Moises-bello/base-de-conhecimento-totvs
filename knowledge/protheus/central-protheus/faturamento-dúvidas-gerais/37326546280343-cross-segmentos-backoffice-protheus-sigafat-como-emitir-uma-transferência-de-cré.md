---
article_id: 37326546280343
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 1747c0aa773d8e3dee6458242b42f36a51d6081651dff72a849d33d247f9a5d4
fetched_at: '2026-06-28T22:38:29.764021+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como emitir uma Transferência
  de crédito na sucessão (tpNFDebito = 05)
type: support-article
updated_at: '2025-12-29T21:21:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37326546280343-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-emitir-uma-Transfer%C3%AAncia-de-cr%C3%A9dito-na-sucess%C3%A3o-tpNFDebito-05
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37326546256535) Tempo aproximado para leitura:**00:03:00 min**  
  
**Dúvida**  
Como emitir uma Transferência de crédito na sucessão (**tpNFDebito = 05**)?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da versão 12.1.2210  
  
**Solução**  
A Nota Fiscal de Débito "**Transferência de Crédito de Sucessão**" é emitida pela empresa sucedida (fundida, cindida ou incorporada) para transferir seus créditos de IBS não utilizados para a empresa sucessora, conforme o Art. 55 da LC nº 214/2025. O Emitente deve ser a empresa sucedida e o Destinatário, a sucessora. Se houver múltiplas sucessoras, notas distintas devem ser geradas para cada uma.

**Processo**:

* Ao incluir o documento de débito deve ser informado no campo de tipo "**Tipo Compl.**" como “**5 - Transferência de Crédito de Sucessão**”;

(A numeração e série não são editáveis, pois serão geradas na confirmação.)

* Informe o **Cliente**e **Loja**, este deve ser a empresa sucessora;
* Informe uma **Condição de Pagamento**(meramente informativa, pois não haverá geração de financeiro);
* Informe na grid:

  **Produto**;

  **Quantidade -** Para este tipo de documento não deve ser informada quantidade.
* Informe o **Valor**. Será sobre este valor que haverá incidência do calculo de tributos;
* Informe uma **TES** que **não movimenta estoque** e **não gera financeiro**;
* Clique na opção **Vincular**;
  + Na parte superior, em **Filtros**, informe os dados para a busca do documento a ser referenciado nesta nota;
    - Como estamos tratando da origem do Crédito a ser transferido, informe o **Fornecedor**que gerou a nota deste Crédito;
  + Clique em **Buscar**. Serão listados até 300 documentos de entrada de acordo com os filtros na seção **Resultado do filtro**;
  + **Marque**o documento que deu origem ao crédito. O registro marcado será listado na seção **Documentos Selecionados**;
  + Clique em **Confirmar**;
* Clique em **Confirmar**;
* Selecione a **Série** e **Numeração**para geração do documento.

**Saiba mais:**

* [Notas de Débito (NF-e: finNFe = 6 - NT 2025.002)](https://tdn.totvs.com/pages/viewpage.action?pageId=1013620273)
