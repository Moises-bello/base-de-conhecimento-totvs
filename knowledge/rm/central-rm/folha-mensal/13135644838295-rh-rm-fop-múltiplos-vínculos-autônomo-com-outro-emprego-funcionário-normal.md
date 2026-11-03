---
article_id: 13135644838295
category: Folha Mensal
content_hash: 5dffe56c90fb7c4a76a3c6c64131a7714ff918e6043bc93c5afbc15c6a3df25d
fetched_at: '2026-06-28T22:46:58.258683+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Múltiplos Vínculos: autônomo com outro emprego funcionário
  normal'
type: support-article
updated_at: '2024-10-04T18:25:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13135644838295-RH-RM-FOP-M%C3%BAltiplos-V%C3%ADnculos-aut%C3%B4nomo-com-outro-emprego-funcion%C3%A1rio-normal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26844162740375)Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**  
Como calcular o INSS de autônomo outro emprego funcionário normal?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Quando um colaborador possui mais de um contrato de trabalho, seja no mesmo empregador ou não, ele possui múltiplos vínculos. Nesse contexto, é importante sabermos que o cálculo da contribuição previdenciária deve ser feito considerando a soma da remuneração recebida em todas as fontes, caso contrário, o INSS será calculado incorretamente.  
  
Para solucionar essa dúvida, siga os passos abaixo:  
  
1. Para calcular o INSS conforme o ESocial será necessário marcar o parâmetro **Calcula INSS conforme eSocial** e informar a partir de quando o sistema iniciará a calcular desta forma, em **Parametrizador | Folha Normal | Geral.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26844132594199)  
  
Importante**Marcando o parâmetro destacado na imagem acima em uma coligada todas deverão estar marcadas.  
  
**2.** Cadastrar os códigos de cálculo abaixo para atenderem às situações de múltiplos vínculos:  
  
[29 - I.N.S.S. Outro Emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452719905)  
[72 - Base de I.N.S.S. de outro emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452718956)  
[417 - Base Tributada de INSS Autônomos Múltiplos Vínculo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=492700190)  
[418 - Base de INSS Autônomo outro Emprego](http://tdn.totvs.com/pages/viewpage.action?pageId=510508458)  
[428 - Base Tributada De Inss Folha Primeira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857540)  
[429 - Base Tributada De Inss Folha Segunda Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857547)  
[430 - Base Tributada De Inss Folha Terceira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857555)  
[431 - Base Tributada De Inss Folha Quarta Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857562)  
[432 - Base Tributada De Inss 13º Primeira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857570)  
[433 - Base Tributada De Inss 13º Segunda Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857577)  
[434 - Base Tributada De Inss 13º Terceira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857583)  
[435 - Base Tributada De Inss 13º Quarta Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857591)  
  
Os códigos de cálculo abaixo deixaram de ser utilizados:  
  
[387 - Base tributada de INSS folha Múltiplos vínculos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857591)  
[388 - Base tributada de INSS 13º Múltiplos vínculos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857591)

Para maiores informações quanto a parametrização e funcionalidades dos códigos de cálculos acima, [CLIQUE AQUI.](https://tdn.totvs.com/pages/releaseview.action?pageId=452719279)  
  
**3.** Validar a Base de Calculo do INSS e o valor descontado no outro emprego. Informe dentro do grupo de eventos ou código fixo (como desejar). Informar os seguinte código de calculo: [72 - Base de I.N.S.S. de outro emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452718956) e o [29 - I.N.S.S. Outro Emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452719905).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13135360707223)  
  
Após realizar o lançamento veja como é feito o calculo:  
  
Sistema realiza o calculo de 11% sobre o autônomo e abate o INSS descontado outro emprego normal.  
  
Formula utiliza no evento de INSS Autônomo:  
[RH - RM - FOP - INSS Autônomo Outro Emprego](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5150487252887-RH-RM-FOP-INSS-Aut%C3%B4nomo-Outro-Emprego)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13135389280535)  
  
Envelope:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13135264673303)  
  
**Saiba Mais**  
[RH - RM - FOP - Múltiplos Vínculos: Quando utilizar os códigos de cálculo 72, 181 e 29 no cálculo de INSS Múltiplos Vínculos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063693393-RM-FOP-Quando-utilizar-os-c%C3%B3digos-de-c%C3%A1lculo-72-181-e-29-no-c%C3%A1lculo-de-INSS-M%C3%BAltiplos-V%C3%ADnculos-?source=search)  
[RH - RM - FOP - Cálculo INSS e IRRF para Autônomos e Diretores](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412995898519-RH-RM-FOP-C%C3%A1lculo-INSS-e-IRRF-para-Aut%C3%B4nomos-e-Diretores)  
[RH - RM - FOP - Fórmulas e Funções](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061764374-RM-FOP-Fun%C3%A7%C3%B5es-de-Formula-de-calculo-Folha-de-Pagamento-RM-Labore-?source=search)
