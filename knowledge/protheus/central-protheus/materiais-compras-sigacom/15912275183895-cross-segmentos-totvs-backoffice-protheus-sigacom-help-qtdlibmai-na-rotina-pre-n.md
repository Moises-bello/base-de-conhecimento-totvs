---
article_id: 15912275183895
category: Materiais - Compras (SIGACOM)
content_hash: 17051f31e3a881b918ebc1f8eaa6966b817379dedd1e62bcb72262356577b943
fetched_at: '2026-06-28T22:41:18.959954+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help QTDLIBMAI na rotina
  Pre-Nota MATA140
type: support-article
updated_at: '2023-08-03T13:03:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15912275183895-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-QTDLIBMAI-na-rotina-Pre-Nota-MATA140
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15912285742615) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Em que momento sistema apresentará Help **QTDLIBMAI** na rotina na Pre-Nota?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
**Solução**

Possibilidades para que o sistema apresente o help **QTDLIBMAI**, são:

* MV\_PCTOLER = 0 , **para Permitir a Quantidade digitada na Pré-Nota maior que a do Pedido de Compras configure o parâmetro MV\_PCTOLER.**
* MV\_TOLENEG = .F.
* MV\_RESTCLA = 2
* Se o Pedido foi eliminado por resíduo - **C7\_RESIDUO ( S )**
* Se o Pedido estiver encerrado - **C7\_ENCER - ( E )**

***Obs:***

Em alguma situações existem validações/verificações diferentes entre Pré-Nota e Documento de entrada. Com isso, na Pre-Nota deve-se avaliar a configuração dos parâmetros MV\_PCTOLER, MV\_TOLENEG e MV\_RESTCLA.

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help QTDLIBMAI do Documento de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012330951-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-QTDLIBMAI-do-Documento-de-Entrada?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
