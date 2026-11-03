---
article_id: 360019948211
category: RH - Rescisão
content_hash: 449960620ce55aca9d9b0bfcb53d1c2c9b17408a6910cdca294ef1cb64014a00
fetched_at: '2026-06-28T22:43:51.049629+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE -  Rescisão complementar não calcula a diferença
  do dissídio para as verbas informadas na rescisão original
type: support-article
updated_at: '2025-06-16T18:46:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019948211-RH-Linha-Protheus-GPE-Rescis%C3%A3o-complementar-n%C3%A3o-calcula-a-diferen%C3%A7a-do-diss%C3%ADdio-para-as-verbas-informadas-na-rescis%C3%A3o-original
---

**Dúvida**Complementar não calcula a diferença do dissídio para as verbas informadas na rescisão original  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
**Solução**O sistema **Protheus** realmente não realizará o **cálculo da diferença do dissídio** para verbas que foram informadas (Origem I) no cálculo da **rescisão original**.  
  
O sistema apenas carregará na complementar, as verbas Informadas na rescisão Original e estas devem ser ajustadas manualmente pelo usuário, para que no cálculo da complementar o sistema apresente o valor a ser pago.  
  
Ou seja, exemplo, foi pago na rescisão original a **verba X**, no valor de R$230,64; porém, na complementar, esta verba está sendo apresentada com o mesmo valor, mas, queremos que a **verba X** sofra um ajuste de 10% para ser paga.  
  
Com isto, faremos o seguinte lançamento na **verba X**= R$230,64 X 10%= R$23,06. Com isto, **verba X** 230,64 + 23,06 diferença dissídio= 253,70, o qual iremos alterar.  
  
Quando o cálculo da complementar for realizado, observe que o sistema apresentará a **verba X** no valor total de R$23,06.  
  
**- Rescisão Original:**  
Observe que a verba 018 - Periculosidade foi Informada, por isto apresenta na coluna Origem o conteúdo I.

**![](http://tdn.totvs.com/download/attachments/286494702/image2017-8-23%2016%3A32%3A22.png?version=1&modificationDate=1503517244000&api=v2)**

**- Rescisão complementar:**

![](http://tdn.totvs.com/download/attachments/286494702/image2017-8-23%2016%3A24%3A37.png?version=1&modificationDate=1503517244000&api=v2)

Observe que as verbas que foram informadas na rescisão original, estão sendo apresentadas na rescisão complementar.  
**- Verba 018- Periculosidade = R$230,64**

![](http://tdn.totvs.com/download/attachments/286494702/image2017-8-23%2016%3A29%3A50.png?version=1&modificationDate=1503517244000&api=v2)

Visto que a diferença do dissídio é de 10%= 230,64+10%=253,70 que é o valor que iremos alterar para a verba 018.

![](http://tdn.totvs.com/download/attachments/286494702/image2017-8-23%2016%3A36%3A34.png?version=1&modificationDate=1503517244000&api=v2)

Ao efetuar o cálculo da complementar após alterar o valor da verba, veja que o sistema efetua o pagamento apenas da diferença, no valor de R$23,06.

![](http://tdn.totvs.com/download/attachments/286494702/image2017-8-23%2016%3A34%3A50.png?version=1&modificationDate=1503517244000&api=v2)

**Importante:**Se as verbas foram lançadas manualmente na rescisão original, o sistema não acatará estas para realizar automaticamente o valor da diferença do dissídio na complementar.  
  
Neste caso, quando a rescisão original foi realizada, o procedimento correto seria o usuário ajustar o sistema para que o mesmo fizesse o cálculo corretamente utilizando o seu processo padrão, diante disto, uma vez o valor manipulado na original, na rescisão complementar deverá ser efetuado o mesmo processo.  
  
**Saiba Mais**  
Para adquirir mais informações acesse o *link*: [MP - GPE0781 - Rescisão complementar não calcula a diferença do dissídio para as verbas Informadas na rescisão Original.](http://tdn.totvs.com/pages/viewpage.action?pageId=286494702)
