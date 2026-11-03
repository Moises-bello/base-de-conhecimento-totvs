---
article_id: 20270593362583
category: Chão de Fábrica (SIGASFC)
content_hash: 510754e4c604fd61a8de3c87e07747982f5e9686e8493eef7b27577378fc50fa
fetched_at: '2026-06-28T22:42:49.794146+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: Manufatura - Linha Protheus - SIGASFC - Cálculo da disponibilidade
type: support-article
updated_at: '2024-01-03T11:42:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20270593362583-Manufatura-Linha-Protheus-SIGASFC-C%C3%A1lculo-da-disponibilidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20270577729431) Tempo aproximado para leitura: **00:01:15 min  
  
Dúvida**Na rotina **SFCC580 - Gerencial de Produção**, como é realizado o cálculo da disponibilidade?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12  
  
**Solução**A disponibilidade é um percentual do números de horas disponíveis no período , de acordo com o calendário com as paradas apontadas no intervalo subtraídas, dividido pelo número de horas disponíveis.  
São consideradas como horas improdutivas neste processo aquelas apontadas via **SFCA311** - **Apontamento de Parada** onde o motivo de parada informado não altera eficiência e também é um dos motivos de parada selecionado na aba **Parâmetros** do **SFCC580**.  
  
**Exemplo**Supondo que uma máquina opera 24 horas por dia, e no dia teve 1 hora de parada apontada no Sistema  com um motivo que não altera a eficiência e 1,5 hora de parada apontada com um motivo que altera a eficiência.  
Neste caso, a disponibilidade seria:  
(24-1)/24 =   
23/24 = 95,83%
