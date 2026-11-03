---
article_id: 32579961782167
category: eConsignado (Crédito do Trabalhador)
content_hash: 3306abc18edd27fe187b9fd67afcd687885dada3eb77a224372f8ca65f5c6490
fetched_at: '2026-06-28T22:43:07.184172+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Arquivo não encontrado na Importação do arquivo
  Credito Trabalhador Econsignado (MP1.292/2025)
type: support-article
updated_at: '2025-07-24T14:50:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32579961782167-RH-Linha-Protheus-GPE-Arquivo-n%C3%A3o-encontrado-na-Importa%C3%A7%C3%A3o-do-arquivo-Credito-Trabalhador-Econsignado-MP1-292-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32579957664919) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Arquivo não encontrado na Importação do arquivo Credito Trabalhador Econsignado (MP1.292/2025)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32579957666199)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois o caminho para selecionar o arquivo de importação baixado do Portal Emprega Brasil tem mais de 100 caracteres. Pode ocorrer também, porque o arquivo selecionado não tem a extensão .CSV ou .JSON.  
  
**Solução**  
Certifique-se que o arquivo baixado no Portal Emprega Brasil, é de extensão .CSV e .JSON. Depois altere a pasta onde está gravado o arquivo, deixando o caminho inferior a 100 caracteres. Orientamos que seja gravado em uma pasta dentro do disco C:.

**1.** Altere a pasta do arquivo, de preferencia dentro do disco C:;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32579961764119)  
  
**2.** Acesse novamente a rotina de Importação Credito trabalhador em **Miscelânea > Importação > Crédito do Trabalhador (GPEM944) >** preencha os **parâmetros >** **selecione o arquivo de forma que apareça a extensão completa**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33375494919575)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32579961765143)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32579961765527)

**Para maior conhecimento assista os videos How to abaixo:**

**Saiba mais:**

[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)
