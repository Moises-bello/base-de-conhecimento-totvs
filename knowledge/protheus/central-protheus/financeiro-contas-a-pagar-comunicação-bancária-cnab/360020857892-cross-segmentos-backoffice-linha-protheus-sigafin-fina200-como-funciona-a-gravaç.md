---
article_id: 360020857892
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 7912c7e48bf3680ca4d79f6b9da16729aa2332b40ee8b59bb32d23c1218e88c8
fetched_at: '2026-06-28T22:37:55.056979+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA200 - Como funciona
  a gravação de registro na FI0 e FI1
type: support-article
updated_at: '2025-10-24T12:25:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020857892-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA200-Como-funciona-a-grava%C3%A7%C3%A3o-de-registro-na-FI0-e-FI1
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35853921612695)**Tempo aproximado para leitura:**00:03:00min**

**Dúvida**Como funciona a gravação de registro na FI0 e FI1?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – FINA200 - Versão 12.  
  
  
**Solução**As tabelas: FI0 e FI1 são tabelas de rastreabilidade. Ou seja, assim que executar a rotina Retorno de Cobrança (FINA200), serão gravados nas tabelas citadas registros correspondentes a títulos baixados.

Qual a funcionalidade desta gravação? Para que o sistema não gere um movimento bancário indevido, impedindo a geração de movimentação em duplicidade em títulos que já foram baixados.  
As ocorrências do tipo 02 (Entrada Confirmada) não baixam os títulos. Neste caso, não serão gravados registros nas tabelas: FI0 e FI1.  
  
Existe o ponto de entrada: **F200GLOG**, caso esteja. T. será gravado log para todos os títulos processados, independentemente de serem títulos baixados ou processados.  
   
**F200GLOG gravação de log no momento de recebimento do CNAB**[DT\_F200GLOG\_gravacao\_de\_log\_recebimento\_CNAB](http://tdn.totvs.com/display/public/PROT/DT_F200GLOG_gravacao_de_log_recebimento_CNAB)
