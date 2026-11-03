---
article_id: 37327439906967
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 4e4c81c884474bd8a6006bfa9554455d688aee2e92c8d56c2eaea1814a23ab25
fetched_at: '2026-06-28T22:38:29.716785+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como emitir uma Nota de Débito
  de Perda em Estoque (tpNFDebito = 07)
type: support-article
updated_at: '2026-05-18T13:46:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37327439906967-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-emitir-uma-Nota-de-D%C3%A9bito-de-Perda-em-Estoque-tpNFDebito-07
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37327439894039) Tempo aproximado para leitura:**00:03:00 min**  
  
**Dúvida**  
Como emitir uma Nota de Débito de Perda em Estoque (**tpNFDebito = 07**)?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**  
A Nota Fiscal de Débito Tipo "**Perda em Estoque**" deve ser emitida para estornar (cancelar) os créditos de IBS previamente recebidos sobre bens que sofreram perda material no estoque, incluindo os créditos dos bens e dos serviços a eles relacionados, conforme o Art. 47 da LC nº 214/2025.

Para bens adquiridos de terceiros, é obrigatório que a nota referencie o documento fiscal original de aquisição do bem e o de serviços vinculados. A emissão desta nota formaliza o Débito na apuração.

**Obs.: Este procedimento não se aplica a perdas que ocorrem durante o transporte dos bens**.

**Processo**:

* Ao incluir o documento de débito deve ser informado no campo de tipo "**Tipo Compl.**" como “**7 - Perda em Estoque**";

(A numeração e série não são editáveis, pois serão geradas na confirmação.)

* Informe o **Fornecedor**e **Loja**, este deve ser o próprio emitente, pois este Débito é sobre sua própria perda de estoque;
* Informe uma **Condição de Pagamento**(meramente informativa, pois não haverá geração de financeiro);
* Informe na grid:

  **Produto**;

  **Quantidade**perdida;

  Informe o **Valor**. Será sobre este valor que haverá incidência do calculo de tributos;

  Informe uma **TES**que **não gera financeiro**; (Movimentação de Estoque - Caso informe uma TES que movimenta estoque, o saldo será baixado automaticamente)
* Clique na opção **Vincular**;

  + Na parte superior, em **Filtros**, informe os dados para a busca do documento a ser referenciado nesta nota, ou seja, os documentos de origem dos materiais perdidos;
  + Na seção **Itens**, serão listados os produtos informados no documento. A busca será feita com base nos dados da seção **Filtros**e do produto posicionado nesta seção.
  + Clique em **Buscar**. Serão listados até 300 linhas de itens de entrada de acordo com os filtros na seção **Resultado do filtro**;
  + **Marque**o item que deu origem ao crédito. O registro marcado será listado na seção **Documentos Selecionados**;
  + Clique em **Confirmar**;
* Clique em **Confirmar**;
* Selecione a **Série**e **Numeração**para geração do documento.

**Sobre produtos industrializados:**

Se você comprou matéria-prima e aproveitou crédito de IBS/CBS, mas o produto final gerado foi perdido, **é necessário estornar esse crédito emitindo uma Nota de Débito**. Nesta Nota de Débito, você deve vincular a Nota Fiscal de compra da matéria-prima utilizada para fabricar o produto final.

O estorno é obrigatório quando o item (ou o que foi produzido com ele) **tenha sido**:

* furtado ou roubado;
* inutilizado ou deteriorado;
* destruído ou envolvido em sinistro;
* empregado em outros produtos que tenham tido a mesma destinação;
* objeto de saída com suspensão do pagamento dessas contribuições.

**Saiba Mais:**

* [Notas de Débito (NF-e: finNFe = 6 - NT 2025.002)](https://tdn.totvs.com/pages/viewpage.action?pageId=1013620273)
* [Orientações Consultoria de Segmentos - PSCONSEG-18561 - Reforma Tributária - Novas Finalidades de Emissão da NF-e](https://tdn.totvs.com/pages/releaseview.action?pageId=982919844#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosPSCONSEG18561ReformaTribut%C3%A1riaNovasFinalidadesdeEmiss%C3%A3odaNFe-3.1.2NotadeD%C3%A9bito-PerdaemEstoque)
