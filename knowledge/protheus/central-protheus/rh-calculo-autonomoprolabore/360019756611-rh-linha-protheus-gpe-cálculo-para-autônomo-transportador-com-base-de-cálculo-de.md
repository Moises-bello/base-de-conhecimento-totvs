---
article_id: 360019756611
category: RH - Calculo Autonomo/Prolabore
content_hash: 2afbae6458cfc885ba45ed70f0811a8f29f07e1b6d22a6da198a99b4d9ddf207
fetched_at: '2026-06-28T22:43:15.117012+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo para autônomo transportador com base de
  cálculo de encargos reduzida
type: support-article
updated_at: '2025-05-07T14:25:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019756611-RH-Linha-Protheus-GPE-C%C3%A1lculo-para-aut%C3%B4nomo-transportador-com-base-de-c%C3%A1lculo-de-encargos-reduzida
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25082188997655)*** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**No módulo Gestão de Pessoal, como efetuar o cálculo para autônomo transportador com base de cálculo do encargos reduzida?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Versão 12.1.17  
  
**Solução**Cadastre os identificadores de cálculo 1563, 1564 e 1565 conforme documentação a seguir: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016300812>   
  
![](http://tdn.totvs.com/download/attachments/435101370/image2018-11-8_19-33-35.png?version=1&modificationDate=1541714102963&api=v2)  
  
No cadastro do Autônomo, informe no campo Categoria sefip o conteúdo 15  
  
![](http://tdn.totvs.com/download/attachments/435101370/image2018-11-8_19-40-18.png?version=1&modificationDate=1541714102873&api=v2)

Ajuste os mnemônicos P\_PERBCIR1 e P\_PERBCIR2 em **Atualizações > Definições de Cálculos > Mnemônicos (GPEA300)**:

Base reduzida a 10%  
  
![](http://tdn.totvs.com/download/attachments/435101370/image2018-11-8_19-42-25.png?version=1&modificationDate=1541714102817&api=v2)  
  
Base reduzida a 60%  
  
![](http://tdn.totvs.com/download/attachments/435101370/image2018-11-8_19-43-14.png?version=1&modificationDate=1541714102760&api=v2)  
  
Para considerar a base de 60%, informe a verba com id 0218 no mnemônico P\_TRANSPAP:  
  
![](http://tdn.totvs.com/download/attachments/435101370/image2018-11-8_19-50-5.png?version=1&modificationDate=1541714102600&api=v2)  
  
Em lançamentos > Por Funcionário, faça o lançamento da verba com id 0218 com o valor total da prestação de serviços:  
  
![](http://tdn.totvs.com/download/attachments/435101370/image2018-11-8_19-46-34.png?version=1&modificationDate=1541714102680&api=v2)  
  
Faça o Cálculo do roteiro AUT:  
  
![](http://tdn.totvs.com/download/attachments/435101370/image2018-11-8_19-51-56.png?version=1&modificationDate=1541714102497&api=v2)  
  
Para considerar a base de 10%, é necessário apenas ter o autônomo cadastrado na categoria 15 e o mnemônico sem a verba informada:  
  
![](http://tdn.totvs.com/download/attachments/435101370/image2018-11-8_19-53-50.png?version=1&modificationDate=1541714102467&api=v2)  
  
Cálculo da folha:  
![](http://tdn.totvs.com/download/attachments/435101370/image2018-11-8_19-54-54.png?version=1&modificationDate=1541714102427&api=v2)

**Saiba Mais**

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
