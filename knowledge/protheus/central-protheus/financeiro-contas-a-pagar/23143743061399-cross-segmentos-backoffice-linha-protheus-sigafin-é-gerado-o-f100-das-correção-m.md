---
article_id: 23143743061399
category: Financeiro - Contas a Pagar
content_hash: 85f788f25f4753df225ae604845603118f435d260722aa85921af762c66f4a63
fetched_at: '2026-06-28T22:38:08.507227+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - É gerado o F100 das
  correção monetária pela rotina FINA350, quando o registro na SE5 é gravado com o
  campo E5_TIPODOC = VM '
type: support-article
updated_at: '2024-04-30T18:26:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23143743061399-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-%C3%89-gerado-o-F100-das-corre%C3%A7%C3%A3o-monet%C3%A1ria-pela-rotina-FINA350-quando-o-registro-na-SE5-%C3%A9-gravado-com-o-campo-E5-TIPODOC-VM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23143743045783) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**É gerado o F100 da correção monetária pela rotina FINA350, quando o registro na SE5 é gravado com o campo E5\_TIPODOC = VM ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33  
  
**Solução**

O envio para o bloco F100 é apenas dos registros referente a correção monetária **E5\_TIPODOC=CM** que são gerados no momento da efetivação da baixa  
  
O registro de variação cambial **E5\_TIPODOC=VM** gerado ao processar a rotina **FINA350** realmente não são considerados.  
  
Lembrando que a variação monetária é a contabilização da variação do títulos antes de ser efetuado sua baixa  
  
**Importante**  
Existe um ponto de entrada **SPD100FIN**, onde o cliente pode alterar o array de títulos que vão ser enviados ao **F100**

[DT SPD100FIN ALTERA ARRAY BLOCO F100](https://tdn.totvs.com.br/display/public/PROT/DT_SPD100FIN_ALTERA_ARRAY_BLOCO_F100)
