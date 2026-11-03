---
article_id: 360036654194
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 51ef4d3c6a86cf4111ed765108ae76a0b008d77b477a37957e7b2441a6c5feba
fetched_at: '2026-06-28T22:38:28.620297+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Nota sobre tratamento
  de fatjobnfe no documento de entrada
type: support-article
updated_at: '2023-02-03T18:15:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036654194-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-sobre-tratamento-de-fatjobnfe-no-documento-de-entrada
---

**Dúvida**

Verificado que o Job para cancelamento de NF-e ([https://tdn.totvs.com/x/UoBdCg)](https://tdn.totvs.com/x/UoBdCg) não funciona no módulo de compras, para as notas fiscais de entrada. Ele só funciona para a exclusão de documentos de saída. 

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

A função **Fatjobnfe** foi criada na rotina **MATA521**, Exclusão da Nota de Saída, especificamente para tratar as notas geradas pela rotina **MATA461**, preparação de notas de saída.

As notas de entrada (**MATA103**) não passam pela exclusão do **MATA521**, por isso, que o job não trata as notas de entrada.

O JOB também não é uma parte da rotina **NFeSefaz**, onde tanto notas de entrada quanto notas de saídas são transmitidas ou canceladas, podendo passar a ideia de que deveria funcionar ao cancelar a NFe de entrada. 

A função do job é mandar alertas para o monitor Nfe verificando se a nota pode ser excluída, trabalhando com uma parceira da rotina **NfeSefaz**.

Enquanto não tiver a resposta positiva do Sefaz, o job fica aguardando o retorno do TSS  até que seja enviada a resposta e repassada para a rotina **mata521**, que por sua vez validará o campo **F2\_FIMP** e alimentará o campo  **F2\_STATUS** com o código que permitirá ou não o cancelamento da nota  de saída  do browse.

Saiba mais:  **[FAT0191\_FATJOBNFE\_para\_Exclusão\_documento\_de\_Saída\_MATA521](https://tdn.totvs.com/pages/releaseview.action?pageId=272154294)**

No caso das notas geradas via **MATA103** deverá ser desenvolvido um tratamento próprio para validar se pode ou não ser excluída, dúvidas neste processo acione a equipe de atendimento de Compras para auxilio.
