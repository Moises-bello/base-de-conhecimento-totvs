---
article_id: 7866755741975
category: RH - Soluções para error.log
content_hash: eadad20d1a6dc7fc46e210d2c714631a827a4d768204738cb33f3a70eb6d8310
fetched_at: '2026-06-28T22:44:08.910791+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Error Log ao tentar gerar o arquivo de Líquido:
  argument #0 error, expected D->C,  function dtos on SAVEPARAM(MSLIB.PRW)'
type: support-article
updated_at: '2025-07-29T20:54:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7866755741975-RH-Linha-Protheus-GPE-Error-Log-ao-tentar-gerar-o-arquivo-de-L%C3%ADquido-argument-0-error-expected-D-C-function-dtos-on-SAVEPARAM-MSLIB-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33804906818071) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao tentar gerar o **arquivo de Líquido** através da rotina GPEM080, é gerado o *error log* ***argument* #0 *error, expected* D->C, *function* dtos *on* SAVEPARAM(MSLIB.PRW)**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O erro ocorre por inconsistência no **Grupo de Perguntas GPEM080R2.**  
  
**Solução**Para correção do erro será necessário atualizar o ambiente com o último pacote de **[Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)** e executar o **UPDDISTR.**  
  
O Grupo de Perguntas **GPEM080R2** deve possuir a estrutura abaixo:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33804922246807)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33804922249239)  
  
  
**Saiba Mais:**  
[DT Correção Grupo de Perguntas GPEM080R2 da rotina GPEM080](https://tdn.totvs.com/pages/viewpage.action?pageId=694106764)  
[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
