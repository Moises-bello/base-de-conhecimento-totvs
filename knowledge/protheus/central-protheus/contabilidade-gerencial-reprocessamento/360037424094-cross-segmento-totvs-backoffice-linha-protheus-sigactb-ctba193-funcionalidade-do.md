---
article_id: 360037424094
category: Contabilidade Gerencial - Reprocessamento
content_hash: 5ed206567d1cfb388d3bce5bb7a818c633170cff4ea4ac1ff047091ee97d087d
fetched_at: '2026-06-28T22:40:42.022556+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - CTBA193 - Funcionalidade
  do Processamento em Fila
type: support-article
updated_at: '2026-06-15T11:32:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037424094-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-CTBA193-Funcionalidade-do-Processamento-em-Fila
---

A rotina CTBA193 no TOTVS Protheus permite o processamento de saldos sem concorrência de usuários, melhorando a performance. Requer atualização online (MV\_ATUSAL = "S") e configuração do schedule CTBA193. Os saldos são armazenados na tabela CQA e processados via JOB agendado. Recomenda-se compartilhar a tabela CQA e centralizar o agendamento para otimizar recursos e desempenho.

**Dúvida**  
Qual a funcionalidade e vantagem do Processamento em Fila (CTBA193)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial (SIGACTB) - a partir da versão 12  
  
  
**Solução**  
O maior diferencial desta rotina (**CTBA193**) é o processamento de saldos sem concorrência de usuários e a melhora na performance. Para o processamento, a atualização de saldos precisa ser online e será necessária a configuração do schedule **CTBA193**.

* **MV\_ATUSAL** = S (atualização de saldo online)
* Configuração do Schedule **CTBA193** (SIGACFG)

![](https://totvssuporte.zendesk.com/attachments/token/xO06lvXgToVZ4rxGgivqTCWIf/?name=inline-1748029171.png)

Após a configuração do ***JOB***, todo novo lançamento terá seus saldos armazenados na tabela **CQA**. As tabelas de saldos só serão preenchidas após a execução do ***JOB*** (processamento) conforme o tempo estipulado na configuração.  
  
  
**Importante:**

* O parâmetro **MV\_ATUSAL** deve estar configurado como **"S"** (Deverá ser online sempre).
* O arquivo **SX2** da tabela **CQA** deve seguir o mesmo compartilhamento das tabelas **CQ0**, **CQ1**, **CQ2**, etc.

**Recomendação:**  
  
Para otimizar o processamento e resolver a sobrecarga, a arquitetura correta é utilizar o agendamento de forma centralizada. Siga as orientações abaixo:

* **Alterar o modo de compartilhamento:** configure a tabela **CQA** como Compartilhada.
* **Entenda o funcionamento:** A tabela **CQA** já possui o campo **CQA\_FILCT2**. Este campo é o responsável por definir e separar de qual filial de origem é o registro.
* **Ajustar o** **agendamento****:** Com a tabela compartilhada, crie o agendamento da rotina **CTBA193** para apenas uma empresa e filial. Essa única thread será capaz de ler e processar os registros de todas as filiais mapeadas pelo campo **CQA\_FILCT2**, garantindo um enorme ganho de performance e alívio nos servidores.

**Saiba mais:**  
[Documentação JOB CTBA193](https://tdn.totvs.com/display/PROT/CTBA193+Gerenciador+de+Saldos+On-Line+-+P12)  
[CTBA193 - em ambiente com múltiplos slaves](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007379271-MP-SIGACTB-Saldos-em-Fila-CTBA193-em-ambiente-com-m%C3%BAltiplos-slaves-?source=search)  
[CTBA193 - Reprocessamento de Saldos em Fila](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006706472-MP-SIGACTB-Reprocessamento-de-Saldos-em-Fila-CTBA193-?source=search&auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo4ODgxMTAsInVzZXJfaWQiOjM2MjE3MDM1OTY4OCwidGlja2V0X2lkIjo0MTAxMzc0LCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTU0MTYxNTg4NH0.jrYeb8rt-JC0V_x0wCCZ2Z7VfpjqsTxbJ1T2Xr1r3SY)  
[Schedule - Como agendar a execução de rotinas](https://tdn.totvs.com/pages/releaseview.action?pageId=271167961)
