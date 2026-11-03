---
article_id: 360026650711
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: e6ebcf235034ac694e7014f3b02ea746bfc37ade473cd2dac25cf7602319d36c
fetched_at: '2026-06-28T22:37:20.051344+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Há possibilidade de
  efetuar Controle de Documentos no módulo Gestão de Contratos ?
type: support-article
updated_at: '2024-11-01T12:15:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026650711-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-H%C3%A1-possibilidade-de-efetuar-Controle-de-Documentos-no-m%C3%B3dulo-Gest%C3%A3o-de-Contratos
---

**Dúvida**Há possibilidade de efetuar Controle de Documentos no módulo Gestão de Contratos ?

**Ambiente**Microsiga Protheus – SIGAGCT – A partir da versão 11.80  
  
**Solução**Existe a funcionalidade de controle de data de Documentos, onde possibilita que a rotina padrão de controle de documentos exigidos nos contratos passe a controlar também a data de validade dos documentos entregues, para que estes fiquem aptos a seguirem o processo contratual padrão.

Um contrato não poderá mudar de situação (Ex.: de Em Elaboração para Emitido) sem que os documentos necessários para etapa sejam apresentados e vinculados ao contrato, como já é feito pela rotina padrão de Contratos. Além dos documentos apresentados, o sistema verifica se a data de validade de cada documento solicitado em sua respectiva etapa está vencida. Nessa situação, o sistema informa que o processo contratual padrão não pode prosseguir, até que a data de validade seja ajustada.

Para viabilizar esse controle, há o campo ***Ctr. Dt.Doc. (CN1\_CTRDOC)*** para definir se o sistema efetua o controle da data de validade dos documentos do contrato pertencentes a um determinado tipo.

Para cada tipo de documento informado na rotina **Documentos (*CNTA171*)**, o sistema efetua o controle da data de validade do documento na mudança de situação do contrato, através da rotina **Contratos (*CNTA300*)**. O sistema permite o fornecimento de mais de um documento para o mesmo tipo informado na rotina Documentos

Na rotina de **Contratos (*CNTA300*)**, se num determinado cenário dois ou mais documentos do mesmo tipo forem entregues para possibilitar a mudança da situação do contrato para a respectiva situação informada na rotina ***Docs x Situação*** **(*CNTA210*)**, o sistema verifica a data de validade de cada documento fornecido. Aquele documento cuja data de validade estiver vencida, o sistema bloqueia a mudança de situação do contrato e exibe um alerta sobre o documento vencido, inclusive o código de sequência do registro. A alteração da situação é permitida somente após a mudança da data de validade do documento na rotina ***Documentos (CNTA171)***.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
