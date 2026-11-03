---
article_id: 23969091155479
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 6b3462b5f3290e485bf906903b83c629531970db9d6abed40d8e21f88c226a5c
fetched_at: '2026-06-28T22:37:24.033089+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Possibilidade de alteração
  do campo "Valor Unitário" (CNE_VLUNIT) na Medição em Contratos Fixos
type: support-article
updated_at: '2024-07-26T15:41:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23969091155479-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Possibilidade-de-altera%C3%A7%C3%A3o-do-campo-Valor-Unit%C3%A1rio-CNE-VLUNIT-na-Medi%C3%A7%C3%A3o-em-Contratos-Fixos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23969084330903) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Qual a possibilidade de alteração do campo "Valor Unitário" (CNE\_VLUNIT) na Medição em Contratos Fixos ?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões]  
  
**Solução**

Referente a possibilidade ou restrição de se alterar o campo de Valor Unitário ***CNE\_VLUNIT*** na medição de contratos fixos, no padrão do sistema, quando o contrato é cadastrado com um Tipo de Planilha/Contrato do Tipo Fixo (***CN1\_CTRFIX=Sim / CNL\_CTRFIX=Sim***), a possibilidade existente deste campo ser permitida a alteração é apenas quando ele também tenha no Tipo de Planilha e/ou Tipo de Contrato utilizados no cadastro do contrato, o campo de valor Limite de Medição (no Tipo de Contrato (***CN1\_LMTMED***) e no Tipo de Planilha (***CNL\_LMTMED***) diferente de zero, ou seja, contenha algum valor de percentual nesses campos.

Caso o campo de limite mencionados esteja diferente de zero a rotina de medição permite alterar o conteúdo do campo ***CNE\_VLUNIT*** nessa situação.  
  
Esta é a possibilidade no padrão do sistema e a forma como ele trabalha.

Caso no processo da empresa, seja necessário a informação neste campo referente ao Limite do Tipo de Contrato/Planilha, porém não se deseja que permita a alteração do Valor Unitário na Medição, a possibilidade neste caso é através de uma customização na rotina ou validação customizada no campo.

Abaixo o artigo com pontos de entrada na rotina de medição em caso de necessidade de utilização:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o?source=search)

***Obs:***

Outros tipos possiveis que permitem a alteração do campo de Valor Unitário no momento da medição são os *Tipo de Contrato/Planilha Flexível*, sendo que neste o cadastro do contrato não possui item e todas as informações do Item são inseridas no momento da medição, e o *Tipo de Contrato/Planilha de Serviço*, cujas informações constam nos artigos abaixo:

* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar a inclusão de um Contrato Flexível ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037640253-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-a-inclus%C3%A3o-de-um-Contrato-Flex%C3%ADvel-?source=search)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais as configurações para utilização de Contrato / Planilha de Serviço no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053570234-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-as-configura%C3%A7%C3%B5es-para-utiliza%C3%A7%C3%A3o-de-Contrato-Planilha-de-Servi%C3%A7o-no-Gest%C3%A3o-de-Contratos-?source=search)

***Saiba Mais:***

[17764762 DTEXPRO-1943 DT Impedia alteração do valor unitário de contratos fixos](https://tdn.totvs.com/x/fwsBLw)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o?source=search)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar a inclusão de um Contrato Flexível ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037640253-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-a-inclus%C3%A3o-de-um-Contrato-Flex%C3%ADvel-?source=search)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais as configurações para utilização de Contrato / Planilha de Serviço no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053570234-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-as-configura%C3%A7%C3%B5es-para-utiliza%C3%A7%C3%A3o-de-Contrato-Planilha-de-Servi%C3%A7o-no-Gest%C3%A3o-de-Contratos-?source=search)

[Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
