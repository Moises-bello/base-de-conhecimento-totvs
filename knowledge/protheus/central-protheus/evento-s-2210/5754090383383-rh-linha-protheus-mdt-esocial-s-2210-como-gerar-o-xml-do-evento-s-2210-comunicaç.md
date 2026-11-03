---
article_id: 5754090383383
category: Evento S-2210
content_hash: 080ee17c3270e9a37e0df0b865a8cdd1c3c05de2f4529578f0888518adc8bc5e
fetched_at: '2026-06-28T22:45:24.447612+00:00'
product: protheus
section_id: 8260521640983
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2210 - Como gerar o XML do evento S-2210
  (Comunicação de Acidente de Trabalho) no modulo MDT e TAF para analise do suporte
  técnico
type: support-article
updated_at: '2024-07-31T17:08:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5754090383383-RH-Linha-Protheus-MDT-eSocial-S-2210-Como-gerar-o-XML-do-evento-S-2210-Comunica%C3%A7%C3%A3o-de-Acidente-de-Trabalho-no-modulo-MDT-e-TAF-para-analise-do-suporte-t%C3%A9cnico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25311257627799) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como gerar o XML do evento **S-2210** (Comunicação de Acidente de Trabalho) no modulo **MDT** (Medicina e Segurança do Trabalho) e **TAF** (TOTVS Automação Fiscal) para analise do suporte técnico?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Para gerar o XML do evento S-2210, realize os seguintes passos:  
1. Primeiro é necessário efetuar a integração do evento S-2210 com o TAF. Deve efetuar o cadastro na rotina de Acidentes (Atualização - Acidente Trabalho - Acidentes) e vincular com o **Atestado Médico** (Atualizações - Atendimento Médico - Atestado Médico) ou **Diagnóstico Médico** (Atualizações - Atendimento Médico - Diagnóstico Médico).  
Veja o link com orientação para integração do evento: [Como emitir uma CAT evento S-2210 no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409360161047)  
  
2. Após o evento integrado, na rotina de Acidentes (Atualização - Acidente Trabalho - Acidentes), posicione no registro desejado e entre na opção Outras Ações - Gerar XML eSocial.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5753843529239)  
  
Será aberto a tela para gravar o arquivo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5753870991127)  
  
3. No módulo SIGATAF (84) o menu **Atualizações - Eventos eSocial - Não Periódicos - CAT Comun. Acid. Trab**. (TAFA257).  
Posicione no funcionário que deseja gerar o XML, clique em Outras Ações > **Gerar XML eSocial**, selecione o tipo XML TAF e confirme o local onde será gravado o arquivo.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5753995702167)  
  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5754040026135)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5754023814423)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
