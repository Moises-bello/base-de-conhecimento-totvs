---
article_id: 5773217359639
category: Evento S-2220
content_hash: 21bc22bf73b4c380a6da3dfb1c5909e00b763d3157b430d29c0581c63e256526
fetched_at: '2026-06-28T22:45:25.502995+00:00'
product: protheus
section_id: 8260535758103
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2220 - Como gerar o XML do evento S-2220
  (Monitoramento da Saúde do Trabalhador) no modulo MDT e TAF para analise do suporte
  técnico
type: support-article
updated_at: '2025-03-12T21:12:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5773217359639-RH-Linha-Protheus-MDT-eSocial-S-2220-Como-gerar-o-XML-do-evento-S-2220-Monitoramento-da-Sa%C3%BAde-do-Trabalhador-no-modulo-MDT-e-TAF-para-analise-do-suporte-t%C3%A9cnico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23166257115415) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como gerar o XML do evento **S-2220** (Monitoramento da Saúde do Trabalhador) no modulo **MDT** (Medicina e Segurança do Trabalho) e **TAF** (TOTVS Automação Fiscal) para analise do suporte técnico?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Para gerar o XML do evento S-2220, realize os seguintes passos:  
1. Primeiro é necessário efetuar a integração do evento S-2220 com o TAF. Deve efetuar os cadastros de **Exames** (Atualizações - Pcmso - Exames), **Exames por Funcionário** (Atualizações - Pcmso - Exames do Funcionário), **Atestado ASO** (Atualizações - Atendimento Médico - Atestado ASO).  
Veja o link com orientação para integração do evento: [Como gerar o ASO para o eSocial evento S-2220 no SIGAMDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414503676567-RH-Linha-Protheus-MDT-eSocial-S-2220-Como-gerar-o-ASO-para-o-eSocial-evento-S-2220-no-SIGAMDT)  
  
2. Após o evento integrado, na rotina de Atestado ASO (Atualizações - Atendimento Médico - Atestado ASO), posicione no registro desejado e entre na opção Outras Ações - Gerar XML eSocial.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5772986216599)  
  
Será aberto a tela para gravar o arquivo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17295585845655)  
  
3. No módulo SIGATAF (84) o menu **Atualizações - Eventos eSocial - Não Periódicos - Monitor. Saúde Trabalhador** (TAFA258).  
Posicione no funcionário que deseja gerar o XML, clique em Outras Ações > **Gerar XML eSocial**, selecione o tipo XML TAF e confirme o local onde será gravado o arquivo.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5773069096727)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17295585856151)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17295585867671)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
