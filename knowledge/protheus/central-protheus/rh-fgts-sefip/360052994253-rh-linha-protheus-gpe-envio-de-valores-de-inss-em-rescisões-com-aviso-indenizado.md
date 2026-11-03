---
article_id: 360052994253
category: RH - FGTS / SEFIP
content_hash: dcde80819f46ff4b9ce9d1e91ce3ef494fa9cc82c0a4670c3ac42d2f03fdf1b8
fetched_at: '2026-06-28T22:43:41.235858+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Envio de valores de INSS em rescisões com aviso
  indenizado (MV_SOMAVIS)
type: support-article
updated_at: '2025-08-14T17:49:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052994253-RH-Linha-Protheus-GPE-Envio-de-valores-de-INSS-em-rescis%C3%B5es-com-aviso-indenizado-MV-SOMAVIS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34185845982487)** Tempo aproximado para leitura: **00:03:00 min**  
**Dúvida**Envio de valores de INSS em rescisões com aviso indenizado (MV\_SOMAVIS)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**

Conceito sistêmico e de negocio em relação ao envio da SEFIP com rescisões que possuem aviso prévio indenizado e seus reflexos em férias e 13º salário  
  
Guia passo a passo:

1. Cálculo de rescisão
2. Geração da GRRF
3. Geração da SEFIP
4. Orientações da consultoria de segmentos

O parâmetro **MV\_SOMAVIS** foi criado com intuito de flexibilização no envio dos valores de previdência social em relação ao aviso prévio indenizado, algumas empresas entendem que o sistema deve declarar/recolher o INSS sobre os valores de aviso indenizado e outras entendem que por tratar-se de valores indenizatórios não é devido o recolhimento do imposto sobre elas.

Quando o parâmetro esta com **.T.** (Verdadeiro) ele **considera** todas as verbas de aviso para a base de cálculo do INSS (Aviso prévio, 13º sobre aviso, férias sobre aviso e 1/3 de férias sobre aviso). Quando esta com **.F.** (Falso) ele **despreza** as verbas de aviso levando apenas a informação de saldo de salário e demais pagamentos com incidência para o INSS.

Independente do conteúdo do parâmetro, a GRRF continuará realizando o recolhimento dos valores de FGTS das rescisões sem justa causa. Quando há casos em que o recolhimento é feito pela GRRF, na SEFIP é enviada uma informação no arquivo indicando que o FGTS já foi recolhido sobre o valor daquela base.

OBS: Em casos de complementares por DISSÍDIO, os valores obrigatoriamente são levados na SEFIP 650, fazendo que aconteça uma possível duplicidade por um GAP existente no próprio validador da SEFIP, que não reconhece o recolhimento via GRRF.

Exemplo:

a) Cálculo de rescisão

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_11-19-57.png?version=1&modificationDate=1584023674903&api=v2)

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_11-21-12.png?version=1&modificationDate=1584023674863&api=v2)

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_11-21-39.png?version=1&modificationDate=1584023674833&api=v2)

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_11-22-11.png?version=1&modificationDate=1584023674797&api=v2)

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_11-22-43.png?version=1&modificationDate=1584023674763&api=v2)

b) Geração da GRRF

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_11-30-51.png?version=1&modificationDate=1584023674730&api=v2)  
![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_11-31-14.png?version=1&modificationDate=1584023674697&api=v2)  
![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_11-31-41.png?version=1&modificationDate=1584023674663&api=v2)

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_11-32-23.png?version=1&modificationDate=1584023674587&api=v2)

Coluna **Rem. Mês Resc.** traz o valor calculado na verba 126 - Saldo de salário = 322,58

Coluna **Av. Prévio** traz o valor da soma das verbas 160 +164 = 12.833,33

c) Geração da SEFIP

Parâmetro MV\_SOMAVIS:

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-33-44.png?version=1&modificationDate=1584034424603&api=v2)

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-28-15.png?version=1&modificationDate=1584034095533&api=v2)  
![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-29-7.png?version=1&modificationDate=1584034147183&api=v2)  
![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-29-28.png?version=1&modificationDate=1584034168887&api=v2)

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-29-54.png?version=1&modificationDate=1584034194780&api=v2)  
![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-30-37.png?version=1&modificationDate=1584034237857&api=v2)  
![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-31-18.png?version=1&modificationDate=1584034278883&api=v2)

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-31-49.png?version=1&modificationDate=1584034309240&api=v2)  
![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-32-19.png?version=1&modificationDate=1584034339930&api=v2)

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-34-8.png?version=1&modificationDate=1584034448497&api=v2)

Validação feita na SEFIP:

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-34-45.png?version=1&modificationDate=1584034485267&api=v2)

O valor levado para SEFIP são as somas das verbas com SIM para INSS excluindo as verbas de aviso. Conforme preenchimento do MV\_SOMAVIS. E não apura nenhum valor de FGTS, pois os mesmos foram enviados a GRRF.

Parâmetro MV\_SOMAVIS= .T.

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-54-47.png?version=1&modificationDate=1584035687297&api=v2)

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-55-4.png?version=1&modificationDate=1584035704373&api=v2)

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-55-21.png?version=1&modificationDate=1584035721940&api=v2)

O sistema levou todos os valores de INSS conforme configuração do MV\_SOMAVIS, e não apurou nenhum valor de FGTS.

Quando existem códigos de saque que representam movimentações definitivas na conta do FGTS do trabalhador, automaticamente o sistema envia para a SEFIP a base do INSS, pois entende que os valores do FGTS foram recolhidos na GRRF por terem caráter indenizatório.

O validador da SEFIP por si não esta preparado para receber DUAS bases de cálculo (INSS e FGTS), portanto se o parâmetro esta com .T. ele enviará a base de cálculo do INSS com todas as verbas de aviso para SEFIP dando a entender que existe uma duplicidade de recolhimento.

Por isso a consultoria de segmentos orienta que os valores de INSS sobre aviso sejam apurados na GPS do próprio sistema ou manualmente, pois da GPS da SEFIP esta defasada a anos.

O parâmetro com .F. ignora todas as verbas de aviso prévio e seus reflexos para SEFIP. Pois entende que os recolhimentos devem ser feitos especificamente pela GRRF e GPS (dentro do software).

TODOS os valores referentes ao aviso indenizado foram levados e recolhidos na GRRF. No próprio log da SEFIP é informado que em casos de alguns códigos de saque (que caracterizam recolhimento pela GRRF) automaticamente a base enviada é a de INSS. Fica a critério do cliente recolher ou não o INSS.

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-58-57.png?version=1&modificationDate=1584035937443&api=v2)

Orientações da nossa consultoria de segmentos:

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_15-0-51.png?version=1&modificationDate=1584036051230&api=v2)

![](https://tdn.totvs.com/download/attachments/543083114/image2020-3-12_14-59-58.png?version=1&modificationDate=1584035998817&api=v2)

Link referência: [Orientações Consultoria de Segmentos - TPGWBX - Como fazer a SEFIP-GFIP quando houver aviso prévio indenizado](https://tdn.totvs.com/pages/viewpage.action?pageId=146966501)

**Saiba mais:**

[RH \_ FGTS/SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
