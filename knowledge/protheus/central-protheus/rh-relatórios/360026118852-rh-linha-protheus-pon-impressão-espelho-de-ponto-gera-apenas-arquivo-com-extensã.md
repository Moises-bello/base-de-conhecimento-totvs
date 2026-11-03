---
article_id: 360026118852
category: RH - Relatórios
content_hash: ecd4faa0f31bed625bdbe888c14dc2950d4d90feed00487affb2f61a5206eba2
fetched_at: '2026-06-28T22:44:43.590092+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Impressão espelho de ponto gera apenas arquivo
  com extensão .REL no diretório
type: support-article
updated_at: '2025-10-07T14:43:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026118852-RH-Linha-Protheus-PON-Impress%C3%A3o-espelho-de-ponto-gera-apenas-arquivo-com-extens%C3%A3o-REL-no-diret%C3%B3rio
---

**Ocorrência**Impressão espelho de ponto gera apenas arquivo com extensão .REL no diretório  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**Esse incidente ocorre, por não encontrar o arquivo Printer na pasta do Appserver e do SmartClient ou encontrá-lo em duplicidade  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.** Nos diretórios **Appserver** e **SmartClient** no servidor instalado o PROTHEUS, verifique se existe o arquivo **Printer.exe** com o logo da TOTVS, conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6376828473879)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6376839529239)

**2.** Se não existir o arquivo no diretório, será necessário seguir o processo da documentação abaixo:  
[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como atualizar o Totvs Printer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020375912-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-atualizar-o-Totvs-Printer)  
  
**Saiba Mais:**[Instalação Printer](http://tdn.totvs.com/pages/viewpage.action?pageId=364910001)[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)
