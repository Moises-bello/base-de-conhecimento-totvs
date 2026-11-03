---
article_id: 9560690789527
category: Controle de Documentos (SIGAQDO)
content_hash: b69cb80957e1a8258c18c33d285a90cc11e041e1507aa5470d09375a8fcf1b16
fetched_at: '2026-06-28T22:42:29.916153+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Revalidação de Documentos
type: support-article
updated_at: '2025-03-06T12:08:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9560690789527-Manufatura-Linha-Protheus-SIGAQDO-Revalida%C3%A7%C3%A3o-de-Documentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18401789323927) Tempo aproximado para leitura: **00:01:40 min** **Dúvida**É possível alterar a **Data de validade** de um **Documento**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**É possível alterar a **Data de validade** do **Documento**, utilizando o conceito de **Revalidação de Documentos**. Para utilizar este conceito, o parâmetro **MV\_QDREVAL - Define o Uso da Rotina de Revalidação** deve ter conteúdo igual à **1-Sim**, e na rotina **QDOA050 - Documentos**, ao gerar uma nova revisão do documento, por meio da opção **Outras Ações/Gera Revisão**, onde a data base do **Protheus** seja maior ou igual à **QDH\_DTLIM - Data Limite**, será exibida a mensagem **Documento está com a data de validade vencida! Gera revalidação?**.  
Confirmando, será possível informar a quantidade de dias de validade no campo **Dias Validade**, para que então, a data no campo **Dt Revalidação** seja calculada automaticamente, levando em consideração a quantidade de dias de validade informada e data de validade atual do documento. E após, informar um motivo justificando a revalidação deste documento.  
  
**Observação**Se o campo **QDH\_DTLIM - Data Limite** não tiver conteúdo, ou seja, se no momento da distribuição na rotina **QDOA110 - Distribuição de Documento** não for preenchido a data de vencimento, o documento não se torna elegível para aplicação da **Revalidação de Documentos**.   
  
**Importante**  
A rotina permite que seja informado a **Quantidade de dias** com no máximo 9999 dias.  
Após este processo é possível consultar tanto o motivo informado para a revalidação quanto a **Data de validade** anterior como a atual do documento, na visualização do documento por meio da opção **Outras Ações/Revalid** da rotina **QDOA050**.  
Somente os **usuários responsáveis** pelo documento (**Elaborador, Revisor, Aprovador, Homologador**) com permissão de **Gerar revisão** igual a **Sim** marcada no **Tipo de Documento** na rotina **QDOA020 - Tipos de Documento** poderão **Gerar Revisão** e **Revalidar** o documento.
