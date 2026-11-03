---
article_id: 5532405502103
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 97e61df9999eda08c78f17df81d5f9e41fec355f64ea1afd8d047d6a58b96970
fetched_at: '2026-06-28T22:42:10.359074+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar os
  Registros R20, R21, R30 e R31 referente à Quotas na DCTF?
type: support-article
updated_at: '2022-11-11T14:37:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5532405502103-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-os-Registros-R20-R21-R30-e-R31-referente-%C3%A0-Quotas-na-DCTF
---

**Dúvida**  
Como gerar os registros **R20, R21, R30** e **R31** referente à **Quotas** na **DCTF**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

Para gerar os registros em questão referente à **Quotas**, é preciso seguir os seguintes passos:

1. Preencha o parâmetro **MV\_RECTRIM** com um código de **R****etenção Trimestral** conforme a tabela de **Códigos da DCTF.**

**Exemplo:** 0220  
  
2. Crie uma **Condição de** **Pagamento** utilizando o **TIPO 8**.

**Exemplo:** [0,30,60,90], [10,30,30,30].  
  
3. No último dia do trimestre gere o **Título** no módulo **06- Financeiro** com seguinte configuração:

* **Parcela (E2\_PARCELA**) = 0 (zero)
* **Tipo (E2\_TIPO)** = TX
* **(E2\_DESDOBR)** = Sim
* **Gera DIRF (E2\_DIRF)** = Sim
* **Cd.Retenção (E2\_CODRET)** = Um código de **Retenção Trimestral** conforme a tabela de **Códigos da DCTF.** **Exemplo:** 0220

4. Na geração do título, informe a **Condição de Pagamento Tipo 8**, preencha o **Histórico** se desejar e **Confirme**. Dessa forma, o **Título** será Desdobrado conforme a **Condição de Pagamento**.  
  
5. Gere a **DCTF** no **Trimestre** posterior ao da inclusão do título.
