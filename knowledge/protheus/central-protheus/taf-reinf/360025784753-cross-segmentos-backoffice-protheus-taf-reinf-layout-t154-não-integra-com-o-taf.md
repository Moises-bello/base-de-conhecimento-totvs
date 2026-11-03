---
article_id: 360025784753
category: TAF - REINF
content_hash: 6d01cc2d8f68e40a5f21722cfb00367da289ad55238b30f3853e9aaccc46253f
fetched_at: '2026-06-28T22:41:33.574562+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Layout T154 Não Integra
  com o TAF
type: support-article
updated_at: '2023-03-31T16:47:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025784753-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Layout-T154-N%C3%A3o-Integra-com-o-TAF
---

**Dúvida**

REINF- Layout T154 Não Integra com o TAF  
  
**Ambiente**

Protheus – FIN – A partir da versão 12.1.17  
  
**Solução**

Para que o título a pagar ou a receber seja enviado ao REINF, é necessário obrigatoriamente informar em "Complemento do Título", o campo Tipo de Serviço (FKF\_TPSERV) ou Tipo de Repasse (FKF\_TPREPA).

Foi criado o botão "Complemento de Título" no browse (tela principal) das rotinas Contas a Receber (FINA040), Contas a Pagar (FINA050), Funções Contas a Receber (FINA740) e Funções Contas a Pagar (FINA750).

Essa opção permite o preenchimento dos campos de complemento do título (tabela FKF), independente do status do título, para possibilitar o envio do título avulso para o REINF.

![Slide1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360040699513/Slide1.JPG)

![Slide1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360039875314/Slide1.JPG)

![Slide2.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360039874414/Slide2.JPG)

Também são premissas para que o Layout T154 seja integrado ao TAF com sucesso na tabela (LEM) rotina TAFA448:

O cadastro do fornecedor deve estar configurado para reter o INSS (A2\_RECINSS = S).

O cadastro de cliente deve estar configurado para reter o INSS (A1\_RECINSS = S).

O cadastro de natureza deve estar configurado para reter o INSS (ED\_CALCINS = S).

**Assuntos relacionados:**

<http://tdn.totvs.com/display/public/PROT/EFD-REINF>

<https://tdn.totvs.com/display/public/PROT/DT+Extrator+Financeiro+para+o+TAF+-+REINF>
