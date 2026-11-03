---
article_id: 37400900437911
category: Gestão de Distribuição (SIGAOMS)
content_hash: f43eb103612300bb814257ca332cf10dae462ebc7014695505071070e32ee72f
fetched_at: '2026-06-28T22:45:49.786917+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Data Prevista de Entrega no Faturamento
  por Carga e Retorno no OMS
type: support-article
updated_at: '2026-01-02T20:19:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37400900437911-Log%C3%ADstica-Linha-Protheus-OMS-Data-Prevista-de-Entrega-no-Faturamento-por-Carga-e-Retorno-no-OMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37400953570839) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como informar a **Data Prevista de Entrega** no **faturamento por carga** e no **retorno da carga pelo OMS**?  
  
**Ambiente**  
TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**  
Com as alterações da **Reforma Tributária (Nota Técnica "NT 2025.002")**, foi incluida a nova tag **<dPrevEntrega>** que representa a data prevista de entrega no cabeçalho da Nota Fiscal Eletrônica, o Sistema passou a validar a data de entrega para a geração do documento de saída quando o campo **Tipo Frete - C5\_TPFRETE** no Pedido de Vendas está preenchido como:

**C - CIF**  
**T - Por conta terceiros**  
**R - Por conta remetente**

Com o **Módulo OMS**, ao gerar a carga por meio da rotina **OMSA200 – Montagem de Carga**, o faturamento é realizado pela rotina **MATA460B – Preparação de Documentos por Carga**.

O preenchimento da data prevista de entrega (tag dPrevEntrega) deve ser informada durante o processo de faturamento de uma das seguintes formas:

* **Modulo OMS/Atualizações/Cargas/Documento de Saida - Carga - MATA460B**: informar a data de entrega pelo pergunte novo, chamado de **Data de Entrega? - SX1 - MT460A28**;
* Diretamente no campo **C5\_FECENT**, localizado no cabeçalho do **Pedido de Venda - MATA410**.

Com o correto preenchimento dessa data, a informação será gravada automaticamente no campo **F2\_DTENTR** da Nota Fiscal.  
  
Para mais detalhes sobre o tratamento da data prevista de entrega, consulte os artigos abaixo:  
  
[Data prevista de entrega](https://tdn.totvs.com/display/public/PROT/Data+prevista+de+entrega)  
[Cross Segmentos – Backoffice Protheus – SIGAFAT – Pedido gerando várias notas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37036636655767-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pedido-gerando-v%C3%A1rias-notas)  
[Cross Segmentos – Backoffice Protheus – SIGAFAT – Help SEMDATA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37027164084503-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-SEMDATA)  
  
**Importante**  
O pergunte **SX1 – MT460A28** permite informar uma **data inferior à data de emissão da Nota Fiscal**. Dessa forma, ao realizar o retorno da Nota Fiscal pela rotina **OMSA320 – Retorno da Carga**, essa data já é apresentada preenchida.

No entanto, o comportamento correto é que a data informada seja posterior ou igual à data de emissão da Nota Fiscal. Caso contrário, o sistema apresentará o help:

**OMS32001 – “A data de entrega informada é menor do que a data de emissão da nota fiscal.”**  
**“Informe uma data de entrega maior ou igual à data de emissão da nota fiscal.”**

Ainda assim, a rotina OMSA320 permite o ajuste manual da data informada.

Este comportamento foi submetido à avaliação do time de **Produto Protheus Faturamento**, responsável por essa alteração. Assim que tivermos o parecer do time responsável, este artigo será devidamente atualizado.  
  
**Saiba mais**  
Mais informações poderão ser acessadas os *links*:   
[Logística - Linha Protheus - OMS - Quando o help OMS32001 será apresentado na rotina OMSA320](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37399639448599-Log%C3%ADstica-Linha-Protheus-OMS-Quando-o-help-OMS32001-ser%C3%A1-apresentado-na-rotina-OMSA320)
