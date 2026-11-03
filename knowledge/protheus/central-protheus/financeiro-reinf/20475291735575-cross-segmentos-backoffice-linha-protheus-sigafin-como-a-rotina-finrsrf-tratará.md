---
article_id: 20475291735575
category: Financeiro - Reinf
content_hash: 2fd5021628ae88d6f9eb6ebc83e93227ac100f653c2d3dc8cc9b3fdca2d41073
fetched_at: '2026-06-28T22:37:51.745598+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como a rotina FINRSRF
  tratará a apuração dos tributos com a entrada do DARF numerado
type: support-article
updated_at: '2024-01-11T14:53:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20475291735575-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-a-rotina-FINRSRF-tratar%C3%A1-a-apura%C3%A7%C3%A3o-dos-tributos-com-a-entrada-do-DARF-numerado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20475291706007) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Com a entrada do Reinf, o reconhecimento dos tributos, à partir de JAN/2024, passará a ser realizados através do DARF numerado, que deverá ser emitido pelo sistema eCAC, via DCTFWeb, como o sistema tratará o período de apuração para esses tributos, sendo que não será mais usada a rotina de geração de DARF?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33  
  
**Solução**O Protheus possui no padrão a emissão da **guia de pagamento** (**DARF**) através da rotina **FINRSRF** (**impressão no Protheus**), mas com a **DCTFWeb**, o próprio portal da Receita Federal irá disponibilizar a guia de pagamento de forma online, com isso não sendo necessário imprimir a DARF pelo sistema.  
  
Quando os eventos da serie **R-4000** (**REINF**) for enviado será alimentado a base de dados da **DCTFWeb**  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/e5jd7hsgP9au4Z5vYZwAUcZ5D/?name=image.png)

Ou seja, com as informações do **REINF + eSocial** que o módulo **TAF** envia, serão gerados os dados na **DCTF-Web** para assim gerar o pagamento dos tributos

**Saiba Mais**[Fique por dentro das atualizações Reinf Protheus](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro#Eventos--839875140)  
[How To - Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19775578473751)
