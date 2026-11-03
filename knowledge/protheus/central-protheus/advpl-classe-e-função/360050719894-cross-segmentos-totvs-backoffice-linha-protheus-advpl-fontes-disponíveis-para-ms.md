---
article_id: 360050719894
category: ADVPL - Classe e Função
content_hash: 4174069d0c1a9910d9c172879ca04f12526e3c5d4231e616150288eba8ec892f
fetched_at: '2026-06-28T22:40:19.315939+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Fontes disponíveis
  para MSCBSAY '
type: support-article
updated_at: '2022-01-10T19:17:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050719894-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fontes-dispon%C3%ADveis-para-MSCBSAY
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Quais tipos de fontes posso utilizar no comando **MSCBSAY**?  
  
**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**

Como pode ser visto na documentação do comando MSCBSAY(**saiba mais**), o quinto parâmetro é onde se indica o fonte a ser usado, porem esta fonte não são os fontes do **windows** ou qualquer outro sistema operacional, e sim os fontes residentes na impressora usada e é limitado, ou seja , o nome das fontes são identificados por letras ou números dependendo do hardware usado :

**String com os tipos de Fonte**

|  |  |
| --- | --- |
| **Zebra** | (A,B,C,D,E,F,G,H,0) 0(zero)- fonte escalar |
| **Datamax** | (0,1,2,3,4,5,6,7,8,9) 9 – fonte escalar |
| **Eltron** | (0,1,2,3,4,5) |
| **Intermec** | (0,1,7,20,21,22,27) |

Portanto não é possível determinar um fonte windows na impressora, a não ser que a fonte seja adquirida com o fabricante da impressora e seja carregado na memoria para uso endereçando seu posicionamento, neste caso é necessário entrar em contato com o fabricante para orientações.  
  
**Saiba mais**  
[MSCBSAY](https://tdn.totvs.com/display/public/mp/MSCBSay+-+Imprime+uma+String+--+30801)
