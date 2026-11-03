---
article_id: 32419073493655
category: Financeiro - Contas a Pagar - Comunicação Bancária Online
content_hash: cef71c93b9e5a0f0cb6a216b2e73a059e7e045c012b165276fd73135d5e6ddbe
fetched_at: '2026-06-28T22:37:49.974767+00:00'
product: protheus
section_id: 26656222001687
source: central-protheus
title: Cross Segmentos - TOTVS Linha Backoffice Protheus - Financeiro - Contas a Pagar
  - FINA718 - Após baixa do título via JOB, o mesmo não é contabilizado
type: support-article
updated_at: '2025-05-28T19:38:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32419073493655-Cross-Segmentos-TOTVS-Linha-Backoffice-Protheus-Financeiro-Contas-a-Pagar-FINA718-Ap%C3%B3s-baixa-do-t%C3%ADtulo-via-JOB-o-mesmo-n%C3%A3o-%C3%A9-contabilizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32419106196119) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, após processamento da baixa via JOB FINA718, os títulos não estão sendo contabilizados de forma online.  
**Ambiente**Cross Segmentos - TOTVS Linha Backoffice Protheus - Financeiro - A partir do release 12.1.2310

**Causa**Esse incidente pode ocorrer devido a duas parametrizações incorretas;  
  
**1 -** **FINA710 - Configuração de Contas >> Opção de Contabilização Online** não está marcada para a conta bancaria utilizada   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32419073474455)

**2 -** **FINA710 - Configuração de Contas >> Motivo de baixa** está como **NORMAL**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32419106196375)  
  
**Solução**Acesse o **Novo Gestor Financeiro >> Configuração de Contas** e ajuste a opção para **"Contabilização Online" = SIM e Motivo de Baixa igual a "DEB - Debito CC"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32419106196503)

Será necessário cancelar a baixa e posteriormente baixar de novo para ser contabilizado o mesmo registro.   
  
**Saiba mais**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA718 - Baixas via API não apresentam no Extrato bancário e Conciliação Bancária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27421281374615-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA718-Baixas-via-API-n%C3%A3o-apresentam-no-Extrato-banc%C3%A1rio-e-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria)  
[Contas a pagar (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=734394071)
