---
article_id: 360003145391
category: Rescisão
content_hash: 465465b5c111b7b9bbda6c64410000f87b20539849e163d09ff82fb4bf3e0cbc
fetched_at: '2026-06-28T22:46:55.441264+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Seguro Desemprego: Fórmulas para cálculo'
type: support-article
updated_at: '2025-02-27T18:03:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003145391-RH-RM-FOP-Seguro-Desemprego-F%C3%B3rmulas-para-c%C3%A1lculo
---

**Dúvida**Caso seja necessário parametrizar fórmulas para o cálculo da remuneração do Seguro Desemprego, é possível informar fórmulas de cálculo para que na geração o cálculo seja realizado conforme o desejo dos usuários. Quais seriam as fórmulas base para esta parametrização?  
  
**Ambiente**RM - Totvs Folha de Pagamento - A partir da versão 11.80  
  
**Solução**Nos casos em que for necessário calcular as remunerações de forma diferente do calculado pelo sistema, deve-se parametrizar uma fórmula e informá-la no cálculo do Seguro Desemprego.   
  
Segue abaixo **EXEMPLO** de fórmulas que podem ser usadas e alteradas, conforme necessidade:  
  
**Fórmula para Remuneração - Último mês:**se RC > 0 entao  
RC + (MV (MESDT (DTD), ANODT(DTD), 'CODIGO\_DO\_EVENTO') + MV (MESDT(DTD), ANODT (DTD), 'CODIGO\_DO\_EVENTO') + MV (MESDT(DTD), ANODT(DTD), 'CODIGO\_DO\_EVENTO'))  
senao  
ACUMFF (MESDT (DTD), ANODT (DTD), 'CODIGO\_DO\_ACUMULADOR')  
FIMSE  
  
-----------------------------------------------  
  
**Fórmula para Remuneração - Penúltimo mês**  
  
DECL AA, MM;  
SETVAR (MM, DECMES (MES, 1));  
SETVAR (AA, DECANO (MES, ANO, 1));  
se RC > 0  
entao RANT (MTDATA (01,MM,AA)) + (MV (MM, AA, 'CODIGO\_DO\_EVENTO') + MV (MM, AA, 'CODIGO\_DO\_EVENTO') + MV (MM, AA, 'CODIGO\_DO\_EVENTO'))  
senao ACUMFF (MM, AA, 'CODIGO\_DO\_ACUMULADOR')  
FIMSE  
  
-----------------------------------------------  
  
**Fórmula para Remuneração - Antepenúltimo Mês**DECL AA, MM;  
SETVAR (MM, DECMES (MESDT (DTD), 2));  
SETVAR (AA, DECANO (MESDT (DTD), ANODT (DTD), 2));  
se RC > 0   
entao RANT (MTDATA (01, MM, AA)) + (MV (MM, AA, 'CODIGO\_DO\_EVENTO') + MV (MM, AA, 'CODIGO\_DO\_EVENTO') + MV (MM, AA, 'CODIGO\_DO\_EVENTO'))  
senao ACUMFF (MM, AA, 'CODIGO\_DO\_ACUMULADOR')  
FIMSE  
  
  
**Legenda:**  
CODIGO\_DO\_EVENTO: Alterar o texto pelo código do evento utilizado, se houver.  
CODIGO\_DO\_ACUMULADOR: Alterar o texto pelo código do acumulador utilizado, se houver.  
  
  
**Importante**  
Caso seja necessário realizar alguma alteração nas fórmulas para atender a realidade da sua empresa e você necessite de suporte, será necessário entrar em contato com a consultoria telefônica da Totvs, por se tratar de uma customização do produto padrão.
