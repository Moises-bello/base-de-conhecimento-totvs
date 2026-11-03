---
article_id: 7220807496471
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 807936fe13d09ea9fe60dddec823bed610bb91381e14fef88143135518d6becd
fetched_at: '2026-06-28T22:39:41.178228+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Impressão da
  purchase order '
type: support-article
updated_at: '2024-05-07T14:01:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7220807496471-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Impress%C3%A3o-da-purchase-order
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Ao gerar a impressão em "**Linguagem = Inglesa**" na rotina  Impressão de Purchase Order **(EICPO150)**, o modo de entrega *(mode of delivery)* esta saindo com as informações em português. Como corrigir esta informação uma vez que a rotina esta atualizada e encontra na função protheus?  
![MODE_OF_DELIVERY.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7218084206231/MODE_OF_DELIVERY.PNG)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**A informação da descrição em inglês da via de Transporte vem da SX5 (tabela genérica) filtrado pela tabela Y3, onde será exibido as vias de transporte  e as suas descrições em espanhol e em inglês.  O que pode acontecer é que todas as descrições estão em português. Isso pode acontecer em informações de releases anteriores que já estavam incorretas. Por isso que ao gerar o relatório a informações estão vindo em português.  
O correto é que as informações estejam da seguinte forma:  
![Y3_DESCENG.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7219121312151/Y3_DESCENG.png)  
É possível fazer o ajuste das descrições pelo configurador.  
  
1. Acesse o Configurador.  
2. Menu Base de Dados -> Dicionário -> Base de Dados:

![CONFIGURADOR_BASE_DE_DADOS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7220534287895/CONFIGURADOR_BASE_DE_DADOS.png)  
3. Clique na opção Tabela Genéricas -> Clique no botão Pesquisar -> Procurar por : Y3

![Y3_CONFIGURADOR.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7220603639447/Y3_CONFIGURADOR.png)

Faça o ajuste das descrições em inglês das vias de transporte.  
  
Segue abaixo as descrições em inglês e espanhol:

|  |  |  |  |
| --- | --- | --- | --- |
| X5\_CHAVE | X5\_DESC | X5\_DESCESPA | X5\_DESCENG |
| 1 | Maritimo | Maritimo | By Sea |
| 2 | Fluvial | Fluvial | By River |
| 3 | Lacustre | Lacustre | By Water (Lake) |
| 4 | Aerea | Aerea | By Airmail |
| 5 | Postal | Postal | By Mail |
| 6 | Ferroviaria | FERROVIA | By Railroad |
| 7 | Rodoviaria | CARRETERA | By Road |
| 8 | Tubo Conduto | TUBO CONDUCTO | Duct Tube |
| 9 | Meios Proprios | Medios Propios | Own means |
| A | Entrada/Saida FICTA | Entrada/Salida FICTA | FICTA Inflow/Outflow |

**Saiba mais**[DTRADE-4877 - Migração dos rdmakes para programa padrão SIGAEIC](https://tdn.totvs.com/pages/releaseview.action?pageId=559287068)
