---
article_id: 360046488713
category: Competências
content_hash: 15f831f20b2120f9dde1137b137811ff07fa48d4c4b1b09751ca1f51f78484a0
fetched_at: '2026-06-28T22:47:20.254510+00:00'
product: rm
section_id: 1500000861322
source: central-rm
title: RH - RM - RHU - Cálculo interno da Gestão por Quadrantes
type: support-article
updated_at: '2025-09-25T14:50:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046488713-RH-RM-RHU-C%C3%A1lculo-interno-da-Gest%C3%A3o-por-Quadrantes
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16034801242263) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como é realizado o cálculo interno para distribuição dos funcionários, na Gestão por Quadrantes?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - Todas as versões  
  
**Solução**O cálculo para distribuição dos funcionários dentro do quadrantes, leva em conta a nota da avaliação de desempenho. O ponto de corte definido no momento da configuração da avaliação de desempenho é a média calculada com base na meta utilizada no cadastrado da gestão por quadrantes.

* Cálculo da nota obtida em cada Competência da avaliação de desempenho:  
     
  Peso do Item de Performance x Valor da Nota obtida na Avaliação / Soma dos pesos dos itens de performance

|  |
| --- |
| Fórmula: **NC = (pIP1 \* VN1) + (pIP2 \* VN2) + ...(pIPn \* VNn)+** |
| **(pIP1 + pIP2 + ...+pIPn)** |

Onde,  
NC = Nota da Competência  
pIP = Peso do Item de Performance  
VN = Valor da Nota Obtida na Avaliação

* Verificação da alocação do funcionário nos quadrantes:   
    
  Percentual potencial = Soma das notas das competências \* 100 / Nota máxima obtida nas competências.

**Saiba mais**

Para maiores informações, acesse:

- [Exemplo de cálculo da Gestão por Quadrantes](https://tdn.totvs.com/pages/viewpage.action?pageId=452719371)

- [Cadastro do quadrante](https://tdn.totvs.com/display/LRM/Quadrante)

- [Gestão por Quadrantes](https://tdn.totvs.com/pages/viewpage.action?pageId=452719224)
