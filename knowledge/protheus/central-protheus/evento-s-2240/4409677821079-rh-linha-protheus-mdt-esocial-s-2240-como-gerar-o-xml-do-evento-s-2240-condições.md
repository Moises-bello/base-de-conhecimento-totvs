---
article_id: 4409677821079
category: Evento S-2240
content_hash: 0ce87fd30da9f382fdc83e1614ede90d34d1aa88936118df1db732bcaa2b1413
fetched_at: '2026-06-28T22:45:23.461376+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Como gerar o XML do evento S-2240
  (Condições Ambientais do Trabalho) no modulo MDT e TAF para analise do suporte técnico
type: support-article
updated_at: '2025-03-03T18:03:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409677821079-RH-Linha-Protheus-MDT-eSocial-S-2240-Como-gerar-o-XML-do-evento-S-2240-Condi%C3%A7%C3%B5es-Ambientais-do-Trabalho-no-modulo-MDT-e-TAF-para-analise-do-suporte-t%C3%A9cnico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23797674058775)**Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como gerar o **XML** do evento **S-2240** (Condições Ambientais do Trabalho) no modulo **MDT** (Medicina e Segurança do Trabalho) e **TAF** (Totvs Automação Fiscal) para analise do suporte técnico?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**  
Para gerar o XML do evento S-2240, realize os seguintes passos:  
1. Primeiro é necessario efetuar a integração do evento S-2240 com o TAF. Caso já tenha integrado pule para o passo 2;  
Exemplo de geração através do cadastro de risco (MDTA180).  
  
![s-2240_geracao.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4409677503639)  
  
**Observação**   
A geração do evento S-2240 pode ocorrer de diversas rotinas, **o gif acima é apenas um exemplo** de uma geração ocorrendo através do cadastro de risco (MDTA180). Em caso de duvidas sobre como gerar o S-2240 consulte a documentação técnica no link: **[S-2240 – Condições Ambientais do Trabalho - Fatores de Risco.](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais+-+S-2240)**  
  
2. Após o evento enviado acesse no modulo SIGAMDT (35) o caminho: **atualizações > cadastros gerais > funcionários** (GPEA010).  
Posicione no funcionário que deseja gerar o **XML** e clicar em Outras Ações > **Gerar XML Riscos**. O XML será gravado no local definido.  
  
![xml_mdt.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4409677559191)  
  
3. No modulo SIGATAF (84) o caminho: **atualizações > eventos eSocial > não periódicos > cond. amb. trabalho funcionários** (TAFA264).  
Posicione no funcionário que deseja gerar o XML e clicar em Outras Ações > **Gerar XML eSocial**, selecione o tipo XML TAF e confirme o local onde será gravado o arquivo.  
  
![xml_taf.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4409682908311)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
