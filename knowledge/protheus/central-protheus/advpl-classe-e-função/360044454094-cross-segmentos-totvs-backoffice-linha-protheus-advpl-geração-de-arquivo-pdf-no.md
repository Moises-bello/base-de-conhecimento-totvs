---
article_id: 360044454094
category: ADVPL - Classe e Função
content_hash: aa8eefe3cf48d9360911ff415b1ecee5e85fcbe388852bb57b76d8c0dbc7edb7
fetched_at: '2026-06-28T22:40:19.526978+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Geração de arquivo
  pdf no servidor
type: support-article
updated_at: '2022-01-11T17:35:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044454094-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Gera%C3%A7%C3%A3o-de-arquivo-pdf-no-servidor
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Temos uma rotina que não está fazendo a geração de arquivo .pdf no servidor  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Para que seja gerado arquivo pdf no servidor é necessário validar se os executáveis **printer.exe** e **pdfprinter** ( *quando for linux necessário os dois*) na pasta smartclient e appserver,

Outra ação que devemos realizar é a aplicação da lib mais atual, pois envolve as classes de impressão.

Caso ambiente seja linux é necessário **printer.exe** e **pdfprinter.exe** esteja com todas devidas permissões *Cmod* 777 .  
  
**Saiba Mais**[Printer](https://tdn.totvs.com/display/tec/TOTVS+Printer)
