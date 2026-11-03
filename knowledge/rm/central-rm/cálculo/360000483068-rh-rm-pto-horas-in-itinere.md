---
article_id: 360000483068
category: Cálculo
content_hash: 4b5c0995c4f8666ce8afce65a7d87688e19300f70db1615176578fe2695a35cd
fetched_at: '2026-06-28T22:46:29.275858+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Horas In itinere
type: support-article
updated_at: '2025-02-19T15:30:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000483068-RH-RM-PTO-Horas-In-itinere
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16984264572183)**Tempo aproximado para leitura: 00:00:45 min**

**Dúvida**O RM realiza o cálculo nativo de Horas In itinere?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Solução**

O horário “in itinere” é o tempo despendido pelo empregado até o local de trabalho e para o seu retorno, tratando-se de local de difícil acesso ou não servido por transporte público, em condução fornecida pelo empregador.  
  
O sistema não possui parametrização padrão para calcular as horas In itinere.  
  
Então será necessário a criação de fórmula onde seja definido a quantidade de horas que deseja calcular e associar essa fórmula ao evento que armazenará essas horas.  
  
Obs.: Existe a possibilidade de calcular os valores de acordo com o centro de custo. Neste caso deverá ser utilizado na fórmula uma consulta SQL que retorne o centro de custo e colocar as condições para cálculo do valor.  
  
Caso precise de auxílio para criação dá fórmula, sugiro nossa equipe de consultoria telefônica. Lembrando que este é um serviço tarifado.

Importante: Considerando o que determina as ~~Portarias 1510 e 373 (SREP)~~ ***(Anuladas Pela Portaria 671/2021)***, as horas in itineres devem ser demonstradas no espelho de ponto ou em qualquer outro documento legal referente ao ponto eletrônico? Quais?

Não sendo obrigatória a demonstração das horas itineres, mesmo assim podemos informá-las nos documentos legais do ponto (como os existentes no SREP)?

**Resposta:**

*De acordo com a Sumula nº 90 do TST em seu parágrafo V – determina que, considerando que as horas "in itinere" são computáveis na jornada de trabalho, o tempo que extrapola a jornada legal é considerado como extraordinário e sobre ele deve incidir o adicional respectivo.*As horas in itinere estão dentro da jornada de trabalho, geralmente os empregados registram as batidas somente no local de trabalho, pois não existe relógio no local do transporte para que possam efetuar os registros das batidas antes de pegar o transporte para o deslocamento de ida/volta. 

**Saiba mais:**[Artigo 58 parágrafo 3 - Horas In Tinere - Remuneração revogada.](https://tdn.totvs.com/pages/viewpage.action?pageId=286222680)[Orientações Consultoria de Segmentos - Horas In Itinere](https://tdn.totvs.com/pages/releaseview.action?pageId=678591603#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosHorasInItinere-4.Conclus%C3%A3o)
