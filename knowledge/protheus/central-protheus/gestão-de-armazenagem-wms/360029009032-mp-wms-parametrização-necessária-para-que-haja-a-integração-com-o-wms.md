---
article_id: 360029009032
category: Gestão de Armazenagem (WMS)
content_hash: 16c1965983e6f91b351d1d548a74bf922b61ee906a9ad69ebccc2886744f78fa
fetched_at: '2026-06-28T22:45:48.213730+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: MP - WMS - Parametrização necessária para que haja a integração com o WMS
type: support-article
updated_at: '2021-01-19T17:01:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029009032-MP-WMS-Parametriza%C3%A7%C3%A3o-necess%C3%A1ria-para-que-haja-a-integra%C3%A7%C3%A3o-com-o-WMS
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)***Tempo aproximado para leitura:**00:01:36 min****Dúvida**Qual é a parametrização necessária para que haja a integração com o **WMS *-* Warehouse Management System**?  
  
**Ambiente**Microsiga Protheus – Gestão de Armazenagem – A partir da versão 12  
  
**Solução**Para que ocorra a integração com o **WMS** a partir dos diversos processos existentes no sistema, sejam entradas, saídas ou movimentos internos, são avaliados três elementos principais:  
  
1. Se o parâmetro que indica a integração dos módulos de logística está ativo - **MV\_INTDL - Identifica se os Módulos do Pacote de Distribuição e Logistica (WMS, OMS e TMS) estão integrados aos outros Módulos**.   
2. Se o produto utilizado na movimentação possui **Controle de endereçamento** - **B1\_LOCALIZ**.  
3. Se foi informado um serviço de **WMS** para os itens do documento.  
  
Sempre que um processo atender a estas três condições haverá integração com o **WMS** por meio da geração de uma ordem de serviço, que poderá ser executada de forma manual ou automática, de acordo com a configuração do serviço a ser executado.  
  
Assim como condição para integração, estes três elementos são avaliados na realização de todas as validações e consistências necessárias para o correto funcionamento do módulo Gestão de Armazenagem.  
  
Além disto, foi identificada a necessidade de criar um parâmetro exclusivo para indicar a integração com o módulo **WMS**, que é o **MV\_INTWMS - Indica integração com o módulo WMS**.  
  
**Saiba mais**  
Mais informações na documentação: [Parametrização Necessária Para Que Haja Integração Com o WMS](http://tdn.totvs.com/pages/viewpage.action?pageId=244724422)
