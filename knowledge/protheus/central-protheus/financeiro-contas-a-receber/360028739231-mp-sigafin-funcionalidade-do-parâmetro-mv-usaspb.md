---
article_id: 360028739231
category: Financeiro - Contas a Receber
content_hash: b662ea8adac4ccb0f73dda7fbc5734602781f2409c509a81560f3fa1fc0fa1d9
fetched_at: '2026-06-28T22:38:15.096728+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - Funcionalidade do parâmetro MV_USASPB
type: support-article
updated_at: '2021-04-28T15:17:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028739231-MP-SIGAFIN-Funcionalidade-do-par%C3%A2metro-MV-USASPB
---

**Dúvida**Funcionalidade do parâmetro **MV\_USASPB**?  
   
 **Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12  
  
**Solução**Através do parâmetro: **MV\_USASPB** (Indica a utilização ou não do controle de SPB - Sistema de Pagamentos Brasileiro) preenchido no conteúdo : **S**, é possível habilitar o campo: **Modalidade (E2\_MODSPD)** na tela da baixa do título e selecione qual será modalidade definida. Segue as opções no padrão que podem ser escolhido no campo Modalidade:

**Utilização:**

1=TED;  
2=CIP;  
3=COMP **Campos envolvidos:****1-Contas a Receber - SE1->E1\_MODSPB**"Modalidade de recebimento prevista (SPB)" **2-Contas a Pagar - SE2->E2\_MODSPB**"Modalidade de pagamento prevista (SPB)" **3-Movimento Bancário - SE5->E5\_MODSPB**"Modalidade da operação financeira (SPB)"
