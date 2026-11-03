---
article_id: 360027509452
category: Financeiro - Contas a Receber
content_hash: d75228307d5d2b9e66126c2b4bd44b10e75e52961db06ee4c9769cb60a409ed0
fetched_at: '2026-06-28T22:38:15.057865+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'MP - SIGAFIN - FINA460 - AJUDA:REGBLOQ    Este registro está bloqueado para
  uso. SA6-Bancos '
type: support-article
updated_at: '2021-04-28T15:17:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027509452-MP-SIGAFIN-FINA460-AJUDA-REGBLOQ-Este-registro-est%C3%A1-bloqueado-para-uso-SA6-Bancos
---

**Ocorrência**  
 No módulo **Financeiro**, ao tentar realizar a **Liquidação** (**FINA460**) é apresentada o help/mensagem  AJUDA:REGBLOQ Este registro está bloqueado para uso. SA6-Bancos  e AJUDA:FALHATUDOK   
Falha na execução dos processos de validação da rotina de geração de títulos (FINA040).   
   
 **Ambiente**  
Microsiga Protheus– Financeiro – A partir da versão 11.80  
   
 **Causa**Essa mensagem é exibida, pois o banco cadastrado no parâmetro **MV\_CXFIN** está bloqueado no cadastro de Bancos (**SA6**).  
  
 **Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Visualizar o conteúdo do parâmetro **MV\_CXFIN.**  
 2. Realizar o desbloqueio do registro em questão, através da rotina de **Cadastros Bancos.**  
 3. Efetuar novamente o processo de **Liquidação** (**FINA460**).
