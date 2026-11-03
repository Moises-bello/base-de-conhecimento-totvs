---
article_id: 40749381084439
category: Gestão de Distribuição (SIGAOMS)
content_hash: 90c0c84f6d3aececc17f3bc22979c725c744607ab68c0a3dc7c55d60ab3bc007
fetched_at: '2026-06-28T22:45:49.857738+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Help OMSA20015 – Pedido com itens que possuem
  datas de entrega diferentes não podem ser alocados na mesma carga
type: support-article
updated_at: '2026-05-29T20:21:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40749381084439-Log%C3%ADstica-Linha-Protheus-OMS-Help-OMSA20015-Pedido-com-itens-que-possuem-datas-de-entrega-diferentes-n%C3%A3o-podem-ser-alocados-na-mesma-carga
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40749386081047) Tempo aproximado para leitura: **00:02:12 min**  
  
**Dúvida**  
Por que o *Help* **OMSA20015** é apresentado ao tentar alocar pedidos com itens de diferentes datas de entrega na mesma carga?  
  
**Ambiente**  
TOTVS Logistica - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - A partir da versão 12.1.2410  
  
**Solução**  
Com as alterações implementadas no Sistema para atendimento à **Reforma Tributária**, passou a ocorrer a geração de múltiplas Notas Fiscais para um mesmo pedido de venda. No **módulo OMS**, foi identificado que a divisão da Nota Fiscal por data de entrega estava ocasionando a criação de diversos documentos para um único pedido. Esse comportamento resultava na perda do vínculo entre os itens da carga e as Notas Fiscais emitidas, comprometendo o controle do processo.  
   
Quando um pedido possui itens com datas de entrega diferentes, conforme as regras da **Reforma Tributária**, a Nota Fiscal deve ser gerada considerando a data de entrega. No processo de **Montagem de Carga - OMSA200**, foi implementado um bloqueio para evitar esse cenário.  
   
Foram realizadas as seguintes implementações na rotina de **Montagem de Carga**:

* Inclusão da coluna **“Data de Entrega”** do pedido de venda na tela de seleção;
* Bloqueio da seleção de itens de um mesmo pedido que possuam **datas de entrega diferentes**.

Caso seja identificada esse cenário, o Sistema apresentará o aviso **Help OMSA20015 – Pedido com itens que possuem datas de entrega diferentes não podem ser alocados na mesma carga.**  
  
**Importante**  
Destacamos que atualmente não possuímos ponto de entrada ou parâmetro que impeça a ocorrência desse bloqueio. O parâmetro **MV\_LDTENTR** não possui ação sobre a rotina de **Montagem de Carga**, atuando apenas no processo de **Faturamento da Carga**. Na versão atual do produto, não há recurso disponível para contornar esse bloqueio.  
  
**Saiba mais**  
Mais informações poderão ser acessadas nos *link's* abaixo:  
[DT Inconsistência pedido com várias datas de entrega na mesma carga.](https://tdn.totvs.com/pages/viewpage.action?pageId=1034808104)  
[Cross Segmentos - Backoffice Protheus - SIGAFAT - Pedido gerando várias notas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37036634978711-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pedido-gerando-v%C3%A1rias-notas)
