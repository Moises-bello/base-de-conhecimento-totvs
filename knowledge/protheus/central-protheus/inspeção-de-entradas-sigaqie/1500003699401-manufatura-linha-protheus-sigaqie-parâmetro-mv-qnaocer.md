---
article_id: 1500003699401
category: Inspeção de Entradas (SIGAQIE)
content_hash: 28d73574c983527e7a2b253f4eed570f1bdd373c6171a922e3fa10d9e5d4f7a6
fetched_at: '2026-06-28T22:42:27.122776+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Parâmetro MV_QNAOCER
type: support-article
updated_at: '2021-08-09T12:46:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003699401-Manufatura-Linha-Protheus-SIGAQIE-Par%C3%A2metro-MV-QNAOCER
---

***![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:45 min**  
**Dúvida**Como e em qual rotina é utilizado o parâmetro **MV\_QNAOCER - Indica se as Entradas Certificadas em Regime de Skip-Lote, não serão consideradas no Calculo do IQF Mensal**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**Este parâmetro é validado pela rotina **QIEA230 - Geração do Índice de Qualidade**, na geração dos índices.  
Quando o parâmetro **MV\_QNAOCER** estiver com conteúdo igual à **T- True**, indica que durante o processamento da rotina **QIEA230**, não serão consideradas as entradas certificadas pelo *skip-lote*, ou seja, irá desconsiderar todos os registros onde o campo **QEK\_VERIFI - Inspec/Cert.** seja igual a **2 - Certifica**.
