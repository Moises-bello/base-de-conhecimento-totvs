---
article_id: 4417265212183
category: Call Center - Telecobrança
content_hash: fc34843693e0df873dc8587b480abfc58a3656533789967f52181f3cc27b82db
fetched_at: '2026-06-28T22:41:28.529553+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center - Processamento
  Quitação de Cobrança
type: support-article
updated_at: '2021-12-28T10:46:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417265212183-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Call-Center-Processamento-Quita%C3%A7%C3%A3o-de-Cobran%C3%A7a
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **01:30:00 min** **Dúvida**Processamento da quitação de cobrança para encerramento do atendimento.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center - a partir da versões.  
  
**Solução**O processo para atualizar Status(ACF\_STATUS) para encerramento do atendimento:  
  
1- O sistema verifica se o titulo está como pago SE1 para deletar na SK1;  
  
2-Verifca se a SK1 deletada existe com as mesmas informações na ACG dos campos abaixo:  
  
K1\_PREFIXO = ACG->ACG\_PREFIXO  
K1\_NUM = ACG->ACG\_TITULO  
K1\_PARCELA = ACG->ACG\_PARCEL  
K1\_TIPO = ACG->ACG\_TIPO  
  
3- O sistema busca o atendimento pelo campo ACG\_CODIGO, pra depois encontrar a ACF\_CODIGO;  
  
4- Atualiza a informação do parâmetro MV\_TMKBXCO com data base;  
  
5- Verifica se todos títulos do atendimento está com a ACG\_STATUS= 1 Pago, para atualizar o para ACF\_STATUS = 3 Encerrado;

6- Caso o atendimento seja gerado pela Lista de Cobrança, o sistema vai atualizar estes campos na SU4 e SU6, com estas informações para encerrar:

SU4->U4\_STATUS="2"  
SU4->U4\_DATA=Data em que foi encerrado  
SU4->U4\_ROTINA="TK290ATU"

SU6->U6\_STATUS="3"  
SU6->U6\_DATA=Data em que foi encerrado  
SU6->U6\_ROTINA="TK290ATU"
