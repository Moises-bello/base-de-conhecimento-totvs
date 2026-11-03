---
article_id: 37325464416791
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 928c3d6c626191070e18a2e842e10e891688fe3d046d6cc7b0c99904cc049fdb
fetched_at: '2026-06-28T22:38:33.030994+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como emitir uma Anulação
  de Crédito por Saídas Imunes/Isentas (tpNFDebito = 02)
type: support-article
updated_at: '2025-12-29T19:27:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37325464416791-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-emitir-uma-Anula%C3%A7%C3%A3o-de-Cr%C3%A9dito-por-Sa%C3%ADdas-Imunes-Isentas-tpNFDebito-02
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37325450638615) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como emitir uma Anulação de Crédito por Saídas Imunes/Isentas (tpNFDebito = 02)  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da versão 12.1.2210  
  
**Solução**  
A nota de débito tipo "**Anulação de Crédito por Saídas Imunes/Isentas**" deve ser emitida pelo contribuinte para anular créditos de IBS de forma proporcional aos insumos/aquisições utilizados em suas operações de saída imunes ou isentas de imposto (conforme Art. 51 da LC nº 214/2025), contendo o grupo "Ajuste de Competência". A emissão desta NF-e é a condição obrigatória para que o valor seja lançado como débito na apuração assistida, ajustando o saldo de créditos do contribuinte.

O Cálculo (Sistema de Apuração): O sistema deve calcular e sugerir o valor de anulação ao final do período, baseado nos dados de saída ($<cClassTrib>$ e valores) do Contribuinte.

A emissão da nota é condição para que o valor seja lançado como débito na apuração, promovendo a regularização do saldo de créditos do contribuinte conforme previsto na legislação.

**Processo**:

* Ao incluir o documento de débito deve ser informado no campo de tipo "**Tipo Compl.**" como “**2 - Anulação de Crédito por Saídas Imunes/Isentas**”;

(A numeração e série não são editáveis, pois serão geradas na confirmação.)

* Informe o **Cliente**e **Loja**, este deve ser o próprio emitente, pois este Débito visa "corrigir créditos recebidos";
* Informe uma **Condição de Pagamento**(meramente informativa, pois não haverá geração de financeiro);
* Informe na grid:

**Produto**;

**Quantidade**- Para este tipo de documento não deve ser informada quantidade.

* Informe o **Valor**. Será sobre este valor que haverá incidência do calculo de tributos;
* Informe uma **TES**que **não movimenta estoque** e **não gera financeiro**;
* Clique na opção **Vincular**;
  + Na parte superior, em **Filtros**, informe os dados para a busca do documento a ser referenciado nesta nota;
    - Como estamos tratando da origem do Crédito a ser corrigido, informe o **Fornecedor**que gerou a nota deste Crédito;
  + Clique em **Buscar**. Serão listados até 300 documentos de entrada de acordo com os filtros na seção
  + **Marque**o(s) documento(s) que deram origem ao crédito. O registro marcado será listado na seção **Documentos Selecionados**;
  + Clique em **Confirmar**;
* Clique em **Confirmar**;
* Selecione a **Série** e **Numeração**para geração do documento.

**Saiba mais:**

* [Notas de Débito (NF-e: finNFe = 6 - NT 2025.002)](https://tdn.totvs.com/pages/viewpage.action?pageId=1013620273)
