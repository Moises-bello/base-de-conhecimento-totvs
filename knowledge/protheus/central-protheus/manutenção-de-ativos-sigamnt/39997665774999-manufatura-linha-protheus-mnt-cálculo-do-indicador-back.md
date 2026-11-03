---
article_id: 39997665774999
category: Manutenção de Ativos (SIGAMNT)
content_hash: 978afe86c227b4fac4573a2e282ae599c7f720b2d69032968299b5bb4f0ad1ea
fetched_at: '2026-06-28T22:42:32.864089+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Cálculo do indicador BACK
type: support-article
updated_at: '2026-04-27T12:21:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39997665774999-Manufatura-Linha-Protheus-MNT-C%C3%A1lculo-do-indicador-BACK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39997657822615) Tempo aproximado para leitura: **00:01:20 min**  
  
**Dúvida**  
Como é realizado o cálculo do indicador **BACK - Tempo para Atendimento de Serviço da Manutenção**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**  
O indicador **BACK** representa o percentual da capacidade de mão de obra que está comprometida com ordens de serviço em um determinado período.  
  
Para a realização do cálculo é utilizada a fórmula abaixo:  
  
**BACK = (MNTV10 / MNTV11) \* 100**  
  
Onde:  
**MNTV10 - Horas Previstas**: Corresponde à **somatória das horas de mão de obra previstas** nas Ordens de Serviço (OS) dentro do período informado.  
**MNTV11 - Disponibilidade de Mão de Obra**: Corresponde à **somatória da capacidade total** de trabalho dos funcionários no período.  
  
**Cálculo do MNTV11**:  
Para cada funcionário, o Sistema calcula a quantidade de horas disponíveis no período, utilizando seu turno no **Calendário**.  
  
**Exemplo**:  
Se o calendário for:  
- Segunda a sexta: 08:00  
- Sábado/domingo: 00:00  
  
E o período for:  
- 06/04/2026 a 10/04/2026 (segunda à sexta)  
  
8 + 8 + 8 + 8 + 8 = 40 horas  
  
**Exemplo completo do cálculo do BACK**:  
- Horas previstas (**MNTV10**): 4 horas  
- Disponibilidade total (**MNTV11**): 40 horas  
- **BACK** = (4 / 40) \* 100 = **10%**
