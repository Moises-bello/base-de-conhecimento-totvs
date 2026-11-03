---
article_id: 4415929027223
category: RH - Soluções para error.log
content_hash: 6bf357d8b7a5edd634f9e3253688efb10e967662b63ef628ceb6b72ab58444a9
fetched_at: '2026-06-28T22:44:08.915282+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Error log ao tentar gerar opções do Relatório
  de Rescisão - InterFunctionCall: cannot find function GPER994'
type: support-article
updated_at: '2025-09-11T17:50:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415929027223-RH-Linha-Protheus-GPE-Error-log-ao-tentar-gerar-op%C3%A7%C3%B5es-do-Relat%C3%B3rio-de-Rescis%C3%A3o-InterFunctionCall-cannot-find-function-GPER994
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34873895100823) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao tentar utilizar as opções de Impressão do Relatório de Rescisão, através da rotina **GPER140**, é gerado ***error log***: "***InterFunctionCall: cannot find function*** **GPER994** ***in AppMap on*** **IMPFUNC(GPER140.PRX)**".  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Causa**Este erro ocorre devido à falta de compilação dos RDMakes **IMPRESZ**, **IMPRESG**, **IMPRESC**, **IMPRESH** e/ou **IMPGRFC.**  
Cada falta de RDMake gera um error log, conforme abaixo:  
   -> InterFunctionCall: cannot find function **GPER994**: RDMake **IMPGRFC**  
   -> InterFunctionCall: cannot find function **GPER999**: RDMake **IMPRESC**  
   -> InterFunctionCall: cannot find function **GPER1000**: RDMake **IMPRESG**  
   -> InterFunctionCall: cannot find function **GPER1001**: RDMake **IMPRESH**  
   -> InterFunctionCall: cannot find function **GPER1002**: RDMake **IMPRESZ**  
  
**Solução  
1.**Compilar os RDMakes **IMPRESZ**, **IMPRESG**, **IMPRESC**, **IMPRESH** e **IMPGRFC** disponibilizados no diretório "RDMakes" do pacote de Expedição Contínua do RH:  
Pacote de Expedição Contínua do RH:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>   
 **Saiba Mais:**  
Documentação técnica sobre a implementação: <https://tdn.totvs.com/pages/releaseview.action?pageId=644718698>   
Como compilar fontes: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019132991>
