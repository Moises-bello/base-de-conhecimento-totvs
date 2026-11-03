---
article_id: 36149773855127
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: e02f18fa9e605e6cef83acccc97e672ba0a499af5f81708d3447279c88766f6a
fetched_at: '2026-06-28T22:37:22.741578+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Erro na revisão de
  contratos InterFunctionCall: cannot find function CLRVCPOUSR in AppMap on CN300REV'
type: support-article
updated_at: '2026-05-20T18:19:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36149773855127-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Erro-na-revis%C3%A3o-de-contratos-InterFunctionCall-cannot-find-function-CLRVCPOUSR-in-AppMap-on-CN300REV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36149793964567) Tempo aproximado para leitura: **00:04:00 min**  
  
**Ocorrência**  
No módulo gestão de contratos ao tentar fazer uma revisão de contrato aparece a tela de erro abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40206601230103)

E também ocorre o error log: **InterFunctionCall: cannot find function CLRVCPOUSR in AppMap on CN300REV** ao tentar realizar a revisão de contratos.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS protheus Gestão de contratos - Versão 12

**Causa**

Esse incidente ocorre, devido a falta da função "CLRVCPOUSR" na rotina CNTA300R utilizada no módulo Gestão de Contratos.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Aplique a última expedição do Módulo Gestão de Contratos do link abaixo:

[- Acumulado Gestão de Contratos conforme sua versão.](https://tdn.totvs.com/pages/viewpage.action?pageId=679961416)

Neste pacote contém a função que está faltando e ao aplicar o pacote não ocorrerá mais o erro.

**Obs:**

- Se o pacote do acumulado possuir atualizaçao de dicionários (sdf), realizar também essa atualização com o UPPDDISTR.

- Realizar a atualização em ambiente de homologação, mediante a realização de backup.

***Saiba Mais:***

[**Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Documentação Gestão de Contratos do TDN**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441027145623-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Documenta%C3%A7%C3%A3o-Gest%C3%A3o-de-Contratos-do-TDN)

[**Artigos Materiais - Gestão de Contratos - (SIGAGCT)**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
