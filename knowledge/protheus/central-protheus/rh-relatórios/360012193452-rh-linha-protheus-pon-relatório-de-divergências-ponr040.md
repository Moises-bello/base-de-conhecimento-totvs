---
article_id: 360012193452
category: RH - Relatórios
content_hash: 7e729372ac09d22a36109da12d31096418d7c4024f5d25c1d4d7dd9b484f5e1f
fetched_at: '2026-06-28T22:44:43.400798+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON -  Relatório de Divergências (PONR040)
type: support-article
updated_at: '2025-10-08T14:20:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012193452-RH-Linha-Protheus-PON-Relat%C3%B3rio-de-Diverg%C3%AAncias-PONR040
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35490047435927) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Como gerar o relatório de divergências (PONR040)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O **relatório de divergências**: **Relatórios> Diversos> Divergências,** apresenta, as divergências encontradas nas marcações do ponto, com a relação das horas trabalhadas a mais ou a menos, tomando como base a Tabela de Horário Padrão estabelecida.  
  
A fim de determinar os minutos de tolerância utilizados para a verificação da duração do intervalo, configure o **Parâmetro MV\_DIVTINT,** conforme sua necessidade. Desta forma, o relatório apresenta o controle de uma situação semelhante a este exemplo:

Observe as seguintes marcações de intervalo realizadas, sendo:  
• Horário de intervalo previsto é 12:00 às 13:00.  
• **Conteúdo do parâmetro MV\_DIVTINT** **igual a "05"**, que corresponde a cinco minutos.

|  |  |  |  |
| --- | --- | --- | --- |
| **Saída** | **Entrada** | **Duração** | **Resultado Listado** |
| 12:00 | 13:01 | Acima do Previsto | Não Lista |
| 12:00 | 13:06 | Acima do Previsto | "Intervalo maior que o programado" |
| 12:00 | 12:54 | Abaixo do Previsto | "Intervalo menor que o programado" |
| 12:00 | 12:55 | Abaixo do Previsto | Não Lista |
| 12:05 | 13:05 | Previsto | Não Lista |
| 11:55 | 12:55 | Previsto | Não Lista |

\*\*O procedimento padrão do sistema é listar todas as ocorrências de intervalo com duração diferente da prevista.  
  
Para realizar a impressão do Relatório de Divergências siga os passos abaixo:  
**1.** É necessário que o Período de Apontamento esteja **aberto** e informado corretamente no parâmetro **MV\_PONMES**, pois o **relatório não é impresso para períodos já fechados**;  
**2.** A data base do sistema deve estar no último dia do Período de Apontamento;  
**3.** É necessário já ter feito a Leitura/Apontamento das marcações e o Cálculo Mensal do Período. **4.**É necessário preencher os parâmetros conforme sua necessidade:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32613378384791)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32613378390679)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32613378393111)  
  
**Importante:** Cabe ressaltar que, em alguns casos, mesmo quando ajustamos a ocorrência que ocasionou a divergência, numa reimpressão do Relatório, esse fato continuará sendo listado.  
  
Por exemplo: quando o funcionário possui duas marcações apenas é gerado um evento de absenteísmo, com isso, é abonado o evento, porém, no relatório de Divergências ainda teremos listado essa ocorrência, pois mesmo que o abono tenha sido lançado, o evento de desconto ainda encontra-se apontado.  
  
  
  
**Saiba Mais  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)**[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)
