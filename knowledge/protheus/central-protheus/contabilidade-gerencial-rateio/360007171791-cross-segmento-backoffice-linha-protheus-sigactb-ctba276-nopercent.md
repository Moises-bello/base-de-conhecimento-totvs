---
article_id: 360007171791
category: Contabilidade Gerencial - Rateio
content_hash: cf18531f82e2f6ecf7d9c53ed62046319942bafde8d80964820bcd5796823599
fetched_at: '2026-06-28T22:40:35.580773+00:00'
product: protheus
section_id: 1500001548962
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus- SIGACTB - CTBA276: NOPERCENT'
type: support-article
updated_at: '2024-01-31T18:08:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007171791-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA276-NOPERCENT
---

**Ocorrência:**Na inclusão de um Grupo de Rateio, é apresentado o Help abaixo:  
"NOPERCENT: O percentual não pode ficar zerado"  
  
**Ambiente:**Microsiga Protheus - Versão 12  
  
**Causa:**Campo CW1\_PERCEN com percentual igual a zero.  
  
**Solução:**Para que este Help não seja apresentado, é necessário seguir as orientações abaixo:  
1- Configurar o parâmetro MV\_CTQFTZR com ".T.";  
2- O Grupo de Rateio deve ser de tipo 2 (Destino);  
3- Deve ser informada fórmula no campo CW1\_FORMUL.  
  
Segue link com informações:  
<http://tdn.totvs.com.br/display/public/PROT/Ferramentas+para+o+cadastro+de+rateios+off-line+--+110589>
