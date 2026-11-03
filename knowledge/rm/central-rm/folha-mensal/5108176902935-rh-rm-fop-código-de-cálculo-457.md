---
article_id: 5108176902935
category: Folha Mensal
content_hash: 81fe3069815ebc6bc6d9d47538ee79993ec4705b616523162d90286002fc8823
fetched_at: '2026-06-28T22:46:59.224689+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Código de cálculo 457
type: support-article
updated_at: '2025-01-20T21:42:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5108176902935-RH-RM-FOP-C%C3%B3digo-de-c%C3%A1lculo-457
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:21 min** **Dúvida**Qual o cálculo e funcionalidade do código de cálculo 457?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, segue abaixo orientações quanto a funcionalidade do código de cálculo 457. Este evento deverá ter a parametrização como Base de cálculo do tipo valor. Será utilizado para o cálculo de diferença de 13º salário referente a dissídio. Este evento será o somatório da diferença calculada dos eventos pagos, que tenham incidência em INSS 13º Salário por dissídio e Incidência Exclusiva do Segurado. Ele deve incidir em Incidência exclusiva do empregador. Não deve incidir em INSS 13º Salário em hipótese alguma.  
  
**Exemplo Base INSS 13º Dissídio Exclusiva Empresa e Base INSS Dissídio 13º Rescisão Exclusiva Empresa**- Para funcionário que teve um evento com incidência exclusiva do segurado, ao lançar a folha foi calculado apenas o valor descontado do segurado.  
- Ao calcular a diferença 13º salário por Dissídio é lançado o evento de [Código de Cálculo 115 - Estorno Base INSS Dissídio Ret. 13º](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718646) com o valor total dos eventos que incidem em INSS 13º.  
- Ao lançar o evento de salário mensal do mês atual o valor do evento tem a dedução do valor do código de cálculo 115, ou seja, deduz o valor de diferença do evento que era com incidência exclusiva do segurado da base de cálculo empresa.  
- Para que o cálculo do valor empresa fique com o valor total é necessário lançar o [Código de Cálculo 457 - Base INSS Dissidio 13º salário Exclusiva Empresa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=628375538), sendo esse lançamento automático pelo cálculo da diferença de 13º Salário Por Dissidio.  
- O mesmo ocorre para o lançamento da rescisão complementar com o [Código de Cálculo 458 - Base INSS Dissidio 13º Rescis. Exclusiva Empresa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=628375549).  
Para uma melhor compreensão da funcionalidade deste código de cálculo, veja a simulação nos prints abaixo:  
  
Valores da diferença de 13º por dissídio e rescisão complementar sem os códigos de cálculo.  
  
![](https://tdn.totvs.com.br/download/attachments/642960341/image2021-7-9_14-44-42.png?version=1&modificationDate=1633350801420&api=v2&effects=border-simple,shadow-kn "Linha RM > Exemplo Base INSS 13º Dissídio Exclusiva Empresa e Base INSS Dissídio 13º Rescisão Exclusiva Empresa > image2021-7-9_14-44-42.png")  
  
![](https://tdn.totvs.com.br/download/attachments/642960341/image2021-7-9_14-45-18.png?version=1&modificationDate=1633350801377&api=v2&effects=border-simple,shadow-kn)  
  
![](https://tdn.totvs.com.br/download/attachments/642960341/image2021-7-9_14-46-7.png?version=1&modificationDate=1633350801343&api=v2&effects=border-simple,shadow-kn)  
  
Valor da guia de INSS - 3677,42 + 800 + 250(13º sal) + 42,61Média HE 13º sal) = 4770,03.  
  
![](https://tdn.totvs.com.br/download/attachments/642960341/image2021-7-9_14-47-6.png?version=1&modificationDate=1633350801307&api=v2&effects=border-simple,shadow-kn)

Encargos INSS empresa, Folha 5000 – 1322,58 = 3677,42.  
  
![](https://tdn.totvs.com.br/download/attachments/642960341/image2021-7-9_14-47-53.png?version=1&modificationDate=1633350801257&api=v2&effects=border-simple,shadow-kn)  
  
Rescisão 1000 – 200 = 800  
  
![](https://tdn.totvs.com.br/download/attachments/642960341/image2021-7-9_14-48-36.png?version=1&modificationDate=1633350801227&api=v2&effects=border-simple,shadow-kn)

Valores da diferença salarial e rescisão complementar com os códigos de cálculo.  
  
![](https://tdn.totvs.com.br/download/attachments/642960341/image2021-7-9_14-49-22.png?version=1&modificationDate=1633350801193&api=v2&effects=border-simple,shadow-kn)

![](https://tdn.totvs.com.br/download/attachments/642960341/image2021-7-9_14-49-55.png?version=1&modificationDate=1633350801163&api=v2&effects=border-simple,shadow-kn)  
  
![](https://tdn.totvs.com.br/download/attachments/642960341/image2021-7-9_14-50-27.png?version=1&modificationDate=1633350801130&api=v2&effects=border-simple,shadow-kn)  
  
Valor da guia de INSS - 5000 + 1000 + 250(13º sal) + 42,61Média HE 13º sal) = 6292,61.  
  
![](https://tdn.totvs.com.br/download/attachments/642960341/image2021-7-9_14-51-56.png?version=1&modificationDate=1633350801103&api=v2&effects=border-simple,shadow-kn)  
  
Encargos INSS empresa - Folha 5000.  
  
![](https://tdn.totvs.com.br/download/attachments/642960341/image2021-7-9_14-53-0.png?version=1&modificationDate=1633350801073&api=v2&effects=border-simple,shadow-kn)  
  
Rescisão - 1000  
  
![](https://tdn.totvs.com.br/download/attachments/642960341/image2021-7-9_14-53-32.png?version=1&modificationDate=1633350801037&api=v2&effects=border-simple,shadow-kn)  
  
**Saiba Mais**  
[RH - RM - FOP - Códigos de Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412890806807-RH-RM-FOP-C%C3%B3digos-de-C%C3%A1lculo)
