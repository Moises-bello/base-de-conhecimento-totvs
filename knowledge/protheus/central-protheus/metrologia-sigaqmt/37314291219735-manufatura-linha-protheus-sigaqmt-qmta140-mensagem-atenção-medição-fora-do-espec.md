---
article_id: 37314291219735
category: Metrologia (SIGAQMT)
content_hash: 2c181a14f7858e4c485975ac7fd7bbe11d99310870c380463542d6e1840825de
fetched_at: '2026-06-28T22:42:24.847693+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - QMTA140 - Mensagem Atenção - Medição
  fora do Especificado
type: support-article
updated_at: '2025-12-29T13:27:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37314291219735-Manufatura-Linha-Protheus-SIGAQMT-QMTA140-Mensagem-Aten%C3%A7%C3%A3o-Medi%C3%A7%C3%A3o-fora-do-Especificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37314279697431) Tempo aproximado para leitura: **00:00:40 min**  
  
**Ocorrência**  
No módulo **SIGAQMT - Metrologia**, ao incluir um valor de medição inicial ou final na rotina **QMTA140 - Medições** ocorre a mensagem **Atenção - Medição fora do especificado.**  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**  
Essa mensagem ocorre na rotina **QMTA140** quando o valor inserido na medição **não é o valor igual** ao especificado no **padrão do instrumento**. É uma **mensagem de alerta** e pode ser **habilitada/desabilitada** pelo parâmetro **MV\_QVLINIF - Liga/Desliga alerta se valores iniciais de medicao estao fora do especificado** e pelo parâmetro **MV\_QVLFIMF - Liga/Desliga alerta se valores finais de medicao estao fora do especificado**.                 
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Insira na medição inicial / final o **valor exato ao especificado** no padrão do instrumento;  
2. Ou altere o conteúdo dos parâmetros **MV\_QVLINIF** e **MV\_QVLFIMF** para **N - Não.**
