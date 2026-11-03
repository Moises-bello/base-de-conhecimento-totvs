---
article_id: 12040901157271
category: Financeiro
content_hash: d5e7de03471b932730929fd16272c664c94b66ee1cb266ba8d8e476341568e38
fetched_at: '2026-06-28T22:38:04.169813+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Linha BackOffice Prothes - FINA710 - Erro 412 - Sem acesso
  ao arquivo PDF
type: support-article
updated_at: '2025-06-20T14:00:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12040901157271-Cross-Segmentos-Linha-BackOffice-Prothes-FINA710-Erro-412-Sem-acesso-ao-arquivo-PDF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24450826179479) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No Gestor Financeiro, ao realizar o download do Boleto, é exibida a mensagem "412 - Sem acesso ao arquivo PDF"

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12040800942871)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33  
  
**Causa**Esse incidente ocorre, pois a ausência do arquivo **Printer.exe** na pasta do **Appserver** dentro do Servidor.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

**Release 12.1.2310**

1. Acesse a pasta do **SmartClient** e copie o arquivo **Printer.exe**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12040854676759)

2. Cole o arquivo **Printer.exe** dentro da pasta do **Appserver**

3. Realize novamente a baixa do Boleto via **FINA710 - Novo Gestor Financeiro**

**Release 12.1.2410**

Acesse o link abaixo e efetue o download do arquivo **printer.exe** conforme sistema operacional do Servidor

<https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/PRINTER>

Adicione a pasta de todos os **Appserver** da aplicação, posteriormente reinicie o serviços do Protheus ***Obs: Caso o ambiente seja CLOUD, deve abrir um chamado pontual solicitando a atualização do Printer.exe em todos os appserver (sem necessidade de efetuar o download)***

**Importante**

O executável deve estar atualizado. Caso não esteja, atualize e adicione novamente o executável atualizado na pasta do smartclient e appserver.

**Saiba mais**

[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Arquivo .REL não é convertido em PDF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041755834-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Arquivo-REL-n%C3%A3o-%C3%A9-convertido-em-PDF)

[TOTVS Printer](https://tdn.totvs.com/display/tec/TOTVS+Printer)  
[Bradesco - Configuração Boletos - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=638386427)
