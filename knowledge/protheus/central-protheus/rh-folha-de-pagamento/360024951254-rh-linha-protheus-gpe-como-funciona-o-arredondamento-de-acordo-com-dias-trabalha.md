---
article_id: 360024951254
category: RH - Folha de Pagamento
content_hash: bab0fab82f585cc18e18eddb33f0ef731f4e29b3930d913372225a7e41dc7dfb
fetched_at: '2026-06-28T22:44:13.510064+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona o arredondamento de acordo com dias
  trabalhados e dsr
type: support-article
updated_at: '2024-09-10T18:59:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024951254-RH-Linha-Protheus-GPE-Como-funciona-o-arredondamento-de-acordo-com-dias-trabalhados-e-dsr
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26278238056087) Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**Como funciona o arredondamento de acordo com dias trabalhados e dsr?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões **Solução**O sistema efetua o cálculo das horas normais e DSR separadamente, multiplicando a quantidade de dias pela quantidade de horas diárias (RA\_HRSDIA), sendo assim ficaria:

No primeiro caso:  
26 \* 7,3333 = 190,6658 = 190,67 (Normal)  
5 \* 7,3333 = 36,6665 = 36,67(DSR)  
Total = 227,34  
  
No segundo caso:  
25 \* 7,3333 = 183,3325 = 183,33 (Normal)  
6 \* 7,3333 = 43,9998 = 44,00(DSR)  
Total = 227,33  
  
Importante observar que não trata-se de erro no sistema, e sim de arredondamento. Verifique que o valor final é sempre o mesmo, somente a referencia que sofre alteração.  
  
Se truncar o valor, ao invés de utilizar o arredondamento, no fim das contas, o valor ainda seria diferente, exemplo:  
26 \* 7,3333 = 190,6658 => 190,66  
5 \* 7,3333 = 36,6665 => 36,66  
A soma seria 227,32

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
