---
article_id: 4479141016983
category: Evento S-2240
content_hash: dab15b34e9c3555bb9025e0b2030033568384f159e8853c92f74082cf2ca537b
fetched_at: '2026-06-28T22:45:23.574388+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Como gerar a Carga de Risco
  de uma filial específica
type: support-article
updated_at: '2025-03-12T18:34:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4479141016983-RH-Linha-Protheus-MDT-eSocial-S-2240-Como-gerar-a-Carga-de-Risco-de-uma-filial-espec%C3%ADfica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25674319277463) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como gerar a Carga de Risco (S-2240) de uma filial específica?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Para gerar a Carga de Risco por filial (**Miscelânea - Implantação - Gerar Risco eSocial**), é necessário que deixe os parâmetros abaixo Exclusivos por Filial:  
  
**\*** MV\_NG2BLEV  
\* MV\_MID  
**\*** MV\_NG2ESOC  
**\*** MV\_NG2DTES  
**\*** MV\_NG2AVIS  
**\*** MV\_NG2NENV  
**\*** MV\_NG2TDES  
**\*** MV\_NG2RIST   
**\*** MV\_NG2VLAU  
**\*** MV\_NG2EPIR  
**\*** MV\_NG2REST  
\* MV\_NG2EAMB  
\* MV\_NG2TPAG  
\* MV\_NG2RAMB  
\* MV\_NG2VEVP  
\* MV\_NG2DENO  
  
No módulo Configurador, acesse o menu **Ambiente - Cadastros - Parâmetros**, localize os parâmetros informados acima e preencha o campo Filial (**X6\_FIL**).  
  
**Obs.:** Para gerar os Riscos apenas da Filial logada, os parâmetros citados acima devem estar com o campo filial preenchido. Se um dos parâmetros ficar com o campo Filial em branco, o sistema irá validar todas as filiais, mesmo que os demais parâmetros estejam com o campo **X6\_FIL** preenchido.  
          Para efetuar a carga para todas filiais, os parâmetros devem ficar com o campo Filial (**X6\_FIL**) em branco.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4479133106327)  
  
Para mais informações, consulte a documentação: [Orientação para gerar a Carga de Riscos por Filial](https://tdn.totvs.com/pages/releaseview.action?pageId=644292746)  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
