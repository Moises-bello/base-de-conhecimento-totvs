---
article_id: 22047732107671
category: Evento S-2220
content_hash: cb19e6adcc1515ba99ef83eda687084f0bda17bf4e38fcd1f1189fb4a79a0ece
fetched_at: '2026-06-28T22:45:25.509570+00:00'
product: protheus
section_id: 8260535758103
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2220 - Como integrar o evento S-2220
  para o TAF após atualização do Acumulado MDT de Fevereiro
type: support-article
updated_at: '2025-03-12T21:13:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22047732107671-RH-Linha-Protheus-MDT-eSocial-S-2220-Como-integrar-o-evento-S-2220-para-o-TAF-ap%C3%B3s-atualiza%C3%A7%C3%A3o-do-Acumulado-MDT-de-Fevereiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22047726024471) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como integrar o evento S-2220 para o TAF após atualização do Acumulado MDT de Fevereiro/2024?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Com ajuste no envio do evento S-2220, a integração passou a ter três formas de realizar:   
  
**1-** Ao incluir um aso com **"Data Emissão" preenchida** e houver um **exame Ocupacional** vinculado, o sistema irá fazer o envio do evento.   
  
Na rotina Exames do Funcionário, precisa ter um exame com **"Data de Resultado"**, **"Origem = Ocupacional"** e **"Natureza"** de acordo com o ASO a ser gerado:  
  
Atualizações - PCMSO - Exames do Funcionário:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22047732085783)   
Incluir o Atestado ASO (Atualizações - Atendimento Médico - Atestado ASO), **preencher** o campo **"Data Emissão"** e **"Natureza"** conforme natureza do exame e confirmar se o exame esta vinculado (Outras Ações - Exames):   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22047882336663)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22047882348311)  
  
Após confirmar os cadastros, clique em **Salvar** que o registro será integrado e apresentará a mensagem de integração do S-2220:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22049184775447)  
  
**2-** Incluir um ASO com **"Data Emissão" em branco**, e salvar o registro, porém, **não ocorre a integração**.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22049184786839)  
  
Para que seja integrado, o usuário poderá efetuar os processos:   
  
\* **Alterar** o ASO **incluindo uma "Data Emissão"** e **vincular um exame ocupacional**:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22049173804183)  
  
Ao salvar, será apresentado a **mensagem de alteração**, porém, o registro **será integrado ao TAF**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22049173814679)  
  
**3-** Na inclusão do ASO, se optar por deixar o campo **"Data Emissão"** em **branco**, será necessário **imprimir o ASO** para integração com o TAF:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22049184818327)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22049184825751)  
  
Consulte documentação técnica: <https://tdn.totvs.com/pages/releaseview.action?pageId=825924378>  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-BR/sections/9198712823575-Assistente-Virtual-Carolina)
