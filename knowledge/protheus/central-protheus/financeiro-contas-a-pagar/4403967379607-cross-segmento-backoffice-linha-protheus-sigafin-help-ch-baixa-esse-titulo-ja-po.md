---
article_id: 4403967379607
category: Financeiro - Contas a Pagar
content_hash: 5cdb1ff42d35fe2f41341818869520bbd33a096bfd68cd32913097baea1e774f
fetched_at: '2026-06-28T22:38:07.005342+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - BackOffice Linha Protheus - SIGAFIN - HELP: CH_BAIXA Esse
  titulo ja possui cheque gerado na rotina de Cheque S/Tit.'
type: support-article
updated_at: '2026-02-03T14:11:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403967379607-Cross-Segmento-BackOffice-Linha-Protheus-SIGAFIN-HELP-CH-BAIXA-Esse-titulo-ja-possui-cheque-gerado-na-rotina-de-Cheque-S-Tit
---

**Ocorrência**  
No módulo Financeiro, ao tentar realizar baixa de titulo com cheque vinculado é apresentada o HELP CH\_BAIXA

![CH_BAIXA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403967223703)  
  
**Ambiente**  
Cross Segmento - BackOffice Linha Protheus – Financeiro – A partir da versão 12.1.17  
  
**Causa**  
Esse incidente ocorre, pois o motivo de baixa utilizado não aceita movimentação bancária e cheques.  
  
**Solução**  
Ajustar o motivo de baixa utilizado para permitir a movimentação bancária e de cheques, por meio da rotina FINA490 – Tabela de Motivos de Baixa.

**Saiba mais**

[Cadastro de Motivo de Baixa - FINA490](https://tdn.totvs.com/display/public/PROT/Cadastro+de+Motivo+de+Baixa+-+FINA490)  
[Baixas Pagar Manual - FINA080](https://tdn.totvs.com/display/public/PROT/Baixas+Pagar+Manual+-+FINA080+-+Financeiro+-+P12)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Descrições dos tipos de movimentações do campo E5\_TIPODOC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022538171-MP-SIGAFIN-Descri%C3%A7%C3%B5es-dos-tipos-de-movimenta%C3%A7%C3%B5es-do-campo-E5-TIPODOC-)
