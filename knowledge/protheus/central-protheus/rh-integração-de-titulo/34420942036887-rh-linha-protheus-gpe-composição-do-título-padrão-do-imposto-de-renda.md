---
article_id: 34420942036887
category: RH - Integração de Titulo
content_hash: 5a9fa6a20276d47e0f8a73aebb67740cfb420ae273d6ab4d8350fe001abfaf34
fetched_at: '2026-06-28T22:43:36.287416+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Composição do Título Padrão do Imposto de Renda
type: support-article
updated_at: '2025-08-25T16:53:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34420942036887-RH-Linha-Protheus-GPE-Composi%C3%A7%C3%A3o-do-T%C3%ADtulo-Padr%C3%A3o-do-Imposto-de-Renda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34420907632151) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Quais são as verbas que compõem o Título Padrão de Imposto de Renda?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**  
Utilizando a opção Padrão de Título de Imposto de Renda, o Protheus busca os valores conforme roteiro/período nas tabelas de Movimento do Período (SRC) ou Histórico de Movimentos (SRD), para os Identificadores de Cálculo:  
  
    0009 - IR Adiantamento     
    0063 - Dedução do resíduo de IR pago maior  
    0066 - IRRF                  
    0107 - Desconto IRRF mês anterior  
    0659 - Valor de compensação de IR  
    0978 - IR RRA                
    0067 - IR Férias  
    0101 - Diferença de IR Férias  
    0071 - IRRF 13º Salário   
    0983 - IR RRA 13º Salário

Caso possua registro de rescisão (SRG) ainda não integrada, verifica nos Itens de Férias e Rescisões (SRR) se existem valores dos IDs 0066, 0067, 0101, 0071.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34421233725591)

**Saiba Mais:**  
[Composição dos Títulos Padrões](https://tdn.totvs.com/pages/releaseview.action?pageId=976128352)   
[RH - Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
