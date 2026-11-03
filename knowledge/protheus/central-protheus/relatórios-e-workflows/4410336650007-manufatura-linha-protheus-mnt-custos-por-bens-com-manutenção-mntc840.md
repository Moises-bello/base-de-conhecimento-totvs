---
article_id: 4410336650007
category: Relatórios e Workflows
content_hash: 6feb17c7663dba8b6d7024ea2b30ebd363805613e73d6ff685691a959bc636a7
fetched_at: '2026-06-28T22:42:31.671963+00:00'
product: protheus
section_id: 360010992394
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Custos por Bens com Manutenção - MNTC840
type: support-article
updated_at: '2021-10-11T11:37:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410336650007-Manufatura-Linha-Protheus-MNT-Custos-por-Bens-com-Manuten%C3%A7%C3%A3o-MNTC840
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Para que serve a consulta de **Custos por Bens com Manutenção - MNTC840**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Relatórios e Workflows - Todas as versões  
  
**Solução**Essa rotina tem por objetivo a visualização e detalhamento dos custos previstos e realizados agrupado por bem com manutenção, ou seja, bens que possuem ordens de serviço **Liberada** e **Terminada**.  
Permite ampliar ou reduzir o nível de detalhamento para proporcionar diferentes visões sobre os custos.  
Desta forma, além de considerar as definições feitas por meio dos parâmetros para apresentação dos custos, existem algumas regras implícitas pelo sistema que devem ser consideradas:

* O **Histórico de Manutenção - STS** também será considerado para a formação dos custos.
* Somente serão consideradas ordens de serviço onde o campo **Finalizadas -** **TJ\_TERMINO** seja igual a **S - Sim** ou o campo **Finalizadas Histórico - TS\_TERMINO** seja igual a **S**.
* O filtro de data verifica se a **Data real fim -** **TJ\_DTMRFIM**ou o campo **Data real fim histórico- TS\_DTMRFIM** de uma ordem de serviço encontra-se contida nos parâmetros **De/Até Data**.
* O cálculo responsável pela geração dos custos apresentados, segue a regra estabelecida pelo **custo médio**. Sendo que o mesmo custo pode ser verificado no campo **Custo - TL\_CUSTO**ou **Custo histórico - TT\_CUSTO** de cada insumo pertencente a ordem de serviço.

**Saiba mais**Acesse a documentação completa: [Custos por Bens com Manutenção - MNTC840](https://tdn.totvs.com/pages/releaseview.action?pageId=543075862).
