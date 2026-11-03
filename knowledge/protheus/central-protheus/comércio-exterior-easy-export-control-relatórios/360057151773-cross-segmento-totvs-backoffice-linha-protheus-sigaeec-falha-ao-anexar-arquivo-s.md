---
article_id: 360057151773
category: Comércio Exterior - Easy Export Control - Relatórios
content_hash: 045ea3cc33f4232fe08200b9324f2db1a2a5e6a04f1e1a8187bec861459c2850
fetched_at: '2026-06-28T22:36:59.887296+00:00'
product: protheus
section_id: 1500001538161
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Falha ao Anexar
  Arquivo: ''\SYSTEM\REL13.PDF'' no E-Mail: Operantion Completed Successfully.'
type: support-article
updated_at: '2021-08-19T12:41:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057151773-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Falha-ao-Anexar-Arquivo-SYSTEM-REL13-PDF-no-E-Mail-Operantion-Completed-Successfully
---

**Dúvida**

Como corrigir  a Falha ao Anexar Arquivo: '\SYSTEM\REL13.PDF' no E-Mail: Operantion Completed Successfully?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095931173/mceclip0.png)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**

No pacote da expedição contínua tem os arquivos dentro da pasta *config\crystallDLLs*. Nesta pasta tem o arquivo *leiame.txt* com as orientações a pasta *install* com os arquivos que devem ser copiados para a pasta SmartClient.

Os registros das ***DLLs*** consistem, basicamente, em acessar o ***CMD*** como administrador e executar os comandos:

regsvr32 C:\caminho do SmartClient\crtslv.dll  
regsvr32 C:\caminho do SmartClient\ExportModeller.dll

As orientações também podem ser encontradas em: [<https://tdn.totvs.com/pages/releaseview.action?pageId=271413885>.]

Pacote Acumulado Comex

[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Pacote Acumulado Comex](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047332793-MP-SIGAEIC-Pacote-acumulado-do-Comex-no-Portal-de-Cliente)
