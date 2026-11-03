---
article_id: 360025029132
category: Gestão de Transportes (TMS)
content_hash: 11e278d1910b59bd725c588aea58e52ffb05f631bceeb9f3c892d7cedeceadb9
fetched_at: '2026-06-28T22:45:32.600097+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição 531 na Emissão de CTE
type: support-article
updated_at: '2022-04-27T11:45:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025029132-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-531-na-Emiss%C3%A3o-de-CTE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:30 min****Dúvida**Como resolver a **rejeição 531** na transmissão do **CT-e - Conhecimento de Transporte eletrônico** ?  
  
**Ambiente**

TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões   
  
**Solução**Quando ocorrer a **Rejeição 531 - Valor a receber vRec deve ser menor ou igual ao Valor da Prestação do Serviço vtPrest**, deverá analisar os parâmetros **MV\_CTEVPRE** e **MV\_CTEVFRE**.  
  
Os parâmetro devem ser ajustado conforme a necessidade da empresa. Segue abaixo as opções para configuração:

* **MV\_CTEVFRE - Determina valor a ser utilizado do componente de frete.**No **CT-e**, *tag***vComp.**
  + **T - Verdadeiro:** Valor dos componentes do frete **sem impostos**;
  + **F - Falso:** Valor dos componentes do frete **com impostos**.
* **MV\_CTEVPRE - Determina valor a ser utilizado do Total da Prestaçao.** No **CT-e**, *tag***vTPRest.**
  + **T - Verdadeiro:**Valor total da prestação **sem impostos;**
  + **F - Falso:** Valor total da prestação **com impostos**.

Se mesmo assim o crédito presumido estiver somando ao titulo à receber, verifique a **TES - Tipos de Entrada e Saída** utilizada no cálculo, no campo **F4\_AGREGCP - Agreg CrdPre**no cadastro **Atualizações/Cadastros/Tipos de Entrada e Saída - MATA080**na aba **Outros**.  
  
Para agregar o **Crédito Presumido** ao valor **Total** da nota, informar **1 - Sim.** Caso contrário, informe **2 - Não.**
