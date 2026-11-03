---
article_id: 20295371685783
category: TAF - REINF
content_hash: 205e859c046780e49fed6734a5e96483b1452ede8d79640623ce69ca3e5856df
fetched_at: '2026-06-28T22:41:34.700054+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - IR e PCC na DCTF-WEB
  a partir de 01/2024
type: support-article
updated_at: '2024-01-03T18:56:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20295371685783-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-IR-e-PCC-na-DCTF-WEB-a-partir-de-01-2024
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20295371666583) Tempo aproximado para leitura: **00:02:00min****Dúvida**

Haverá alguma alteração para envio do **IR** e **PCC** para a **DCTF-WEB** a partir de janeiro de 2024?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal - Todas as versões  
  
**Solução**

A integração entre **EFD-REINF** e **DCTFWeb** é sempre feita de forma **automática**.

Desta forma, se for necessário retificar alguma informação na **EFD-REINF** (ou **eSocial**) já encerrada, o contribuinte deverá **reabrir o movimento da escrituração,** providenciar a retificação do evento transmitido com erro e **encerrar novamente o movimento**.

Ao fazer isto, a **DCTFWeb** será **automaticamente** sensibilizada pela nova apuração, **substituindo** a apuração anterior.

Dessa forma, ao **transmitir** a apuração da **Reinf**, contendo as retenções de **IR** e **PCC** (**Bloco 40**), elas serão demonstradas na **DCTF-WEB** de forma automática, seguindo o mesmo procedimento quanto ao **INSS** (**Bloco 20**).

Para mais informações:

Perguntas Frequentes **DCTF-WEB**:   
<https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dctfweb/perguntas-e-respostas-dctfweb.pdf>

Manual de orientação **DCTF-WEB**:   
<https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/DCTFWeb/arquivos/manual-dctfweb-fevereiro-2023.pdf>
