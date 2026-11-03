---
article_id: 360026659294
category: Financeiro - Contas a Pagar
content_hash: f485b4b2007f54df192f92d40b093be8caa45e477d4f80ea571bd08eef455a07
fetched_at: '2026-06-28T22:38:09.572465+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA080 - Cancelamento
  baixa HELP NODELETA
type: support-article
updated_at: '2023-07-06T21:24:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026659294-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA080-Cancelamento-baixa-HELP-NODELETA
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**  
No módulo Financeiro FINA080, ao tentar realizar o cancelamento de baixa é informado que o título possui impostos. Como podemos proceder para o cancelamento?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**   
Esse incidente ocorre, pois a parametrização do sistema está ajustada por padrão para bloqueio do estorno de baixa com impostos.  
  
**Solução**A retenção dos impostos de **PIS**/**COFINS**/**CSLL** está definido na emissão, conforme exemplo abaixo possuo os títulos **TX** correspondente a cada imposto e **NF** baixados:

![](http://tdn.totvs.com.br/download/attachments/356814285/image2018-4-25_15-19-33.png?version=1&modificationDate=1524680787000&api=v2)

No momento do cancelamento da baixa do título **NF** apresenta help: **NODELETA**

![](http://tdn.totvs.com.br/download/attachments/356814285/image2018-4-25_15-20-52.png?version=1&modificationDate=1524680787000&api=v2)

1. Diante deste cenário, será necessário cancelar primeiro as baixas dos títulos **TX** para depois realizar o cancelamento da baixa da **NF**. Ajustado o parâmetro **MV\_CB10925**=**1**, poderá realizar mais uma tentativa de cancelamento da baixa da mesma **NF** e apresentará um novo help:

![](http://tdn.totvs.com.br/download/attachments/356814285/image2018-4-25_15-24-35.png?version=1&modificationDate=1524680787000&api=v2)

2. Selecione a opção: **Sim**, o sistema permitirá cancelar a baixa apenas da **NF** e os títulos **TX** permanecerão baixado:

![](http://tdn.totvs.com.br/download/attachments/356814285/image2018-4-25_15-26-15.png?version=1&modificationDate=1524680787000&api=v2)
