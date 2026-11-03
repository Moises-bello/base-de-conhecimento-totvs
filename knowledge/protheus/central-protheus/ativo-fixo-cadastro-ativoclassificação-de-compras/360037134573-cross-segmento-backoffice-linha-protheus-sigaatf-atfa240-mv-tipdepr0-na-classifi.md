---
article_id: 360037134573
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 36c985cd253eb89c70e0966f084ae67ffa61d899ed7efe93a7bd67a99d9dfb90
fetched_at: '2026-06-28T22:41:48.314918+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF -  ATFA240 :MV_TIPDEPR=0,
  NA CLASSIFICAÇÃO O SISTEMA CONSIDERA A DATA BASE OU DATA DE AQUISIÇÃO?
type: support-article
updated_at: '2022-11-07T18:57:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037134573-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-MV-TIPDEPR-0-NA-CLASSIFICA%C3%87%C3%83O-O-SISTEMA-CONSIDERA-A-DATA-BASE-OU-DATA-DE-AQUISI%C3%87%C3%83O
---

**Dúvida**MV\_TIPDEPR=0, NA CLASSIFICAÇÃO DO BEM (ATFA240) O SISTEMA CONSIDERA A DATA BASE OU DATA DE AQUISIÇÃO?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Ativo Fixo - Todas as versões  
  
**Solução**

Criação de pergunta via **F12** para parametrizar se é desejado utilizar a **data da nota fiscal** de entrada ou a **data base** do sistema (pergunta criada ***Utiliza Dt Aquis. ou Dt Base?***).

Quando se optar em classificar o bem utilizando o **grupo de bens**, a rotina de classificação poderá atualizar a **data de início de depreciação** da seguinte forma, conforme a resposta a pergunta:

1. **Data Base:** o campo referente a data do início de depreciação**(N3\_DINDEPR)** será atualizado com a **data base do sistema**.
2. **Data de Aquisição:** o campo referente a data do início de depreciação**(N3\_DINDEPR)** será atualizado de acordo com a **data da nota fiscal de entrada (N1\_AQUISIC).**

**![image2019-7-19_14-37-8.png](https://tdn.totvs.com/download/attachments/501466158/image2019-7-19_14-37-8.png?version=1&modificationDate=1563557828303&api=v2)**

* Importante! Releases inferiores a 12.1.28

*Importante: Para os releases inferiores a versão 12.1.28, deve-se incluir a nova pergunta via SIGACFG conforme documentação:*

*<https://tdn.totvs.com/pages/releaseview.action?pageId=501466158>*
