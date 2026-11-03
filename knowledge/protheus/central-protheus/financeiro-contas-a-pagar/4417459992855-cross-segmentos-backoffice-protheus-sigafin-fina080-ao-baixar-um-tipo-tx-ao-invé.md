---
article_id: 4417459992855
category: Financeiro - Contas a Pagar
content_hash: b3ede294dc4ed0c0e96b156d30d64c1438a2a6e36fa52268039df84aae6caee3
fetched_at: '2026-06-28T22:38:09.830607+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGAFIN - FINA080 - Ao baixar um tipo:
  TX ao invés de gerar movimento a pagar, gera um movimento a receber.'
type: support-article
updated_at: '2022-03-23T02:45:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417459992855-Cross-Segmentos-Backoffice-Protheus-SIGAFIN-FINA080-Ao-baixar-um-tipo-TX-ao-inv%C3%A9s-de-gerar-movimento-a-pagar-gera-um-movimento-a-receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**No módulo Financeiro, ao baixar um tipo: TX ao invés de gerar movimento a pagar, gera um movimento a receber.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro  - Todas as versões  
  
**Causa**Um dos motivos que ocorre este erro é referente a rotina **Tipos de títulos (FINA015 - SIGAFIN),** podendo ter registros na tabela **SES** para tratamento dos tipos de títulos de Mercado Internacional (Outros países) com carteira a receber.   
  
**Solução**Realize o processo primeiramente base de homologação.  
Identificar se na **ES\_TIPORIG** contém o tipo **TX** inserido, desabilite o registro e efetue novamente a baixa do **TX** no **Contas a Pagar**. 

Ao incluir dados na rotina "**Tipos de títulos - FINA015**" que alimenta a tabela **SES**  
Não é possível prever os impactos de inclusão de tipos de títulos na rotina **FINA015.**  
  
Uma das inconsistências imprevisíveis é fazer com que ao baixar um título de **impostos a pagar do** **tipo:TX** no **Contas a Pagar,** gere uma movimentação a receber, ao invés de gerar uma movimentação a pagar  
  
Onde é possível identificar que é gravado na tabela o conteúdo **E5\_RECPAG=R** ao invés de gravar o conteúdo **E5\_RECPAG=P**

**Importante**  
A utilização desta rotina ou inclusão manual diretamente na tabela **SX5**, em ambientes do Brasil "**BRA**" poderá ocasionar problemas imensuráveis em diversas rotinas do sistema, sendo expressamente não recomendada.  
  
**Saiba mais**  
<https://tdn.totvs.com/display/public/PROT/FIN0004_Utilizacao_rotina_tipos_de_titulos_FINA015>
