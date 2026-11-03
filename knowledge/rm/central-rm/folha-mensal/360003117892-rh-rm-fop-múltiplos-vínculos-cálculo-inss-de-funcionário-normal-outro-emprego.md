---
article_id: 360003117892
category: Folha Mensal
content_hash: c131dd170525c61527f14f4ccbe22c45328387358a1e94f9149af78a064701a3
fetched_at: '2026-06-28T22:47:00.340910+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Múltiplos Vínculos: cálculo INSS de funcionário normal outro
  emprego'
type: support-article
updated_at: '2024-10-04T18:27:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003117892-RH-RM-FOP-M%C3%BAltiplos-V%C3%ADnculos-c%C3%A1lculo-INSS-de-funcion%C3%A1rio-normal-outro-emprego
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**  
Como calcular o INSS de funcionário normal outro emprego?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Quando um colaborador possui mais de um contrato de trabalho, seja no mesmo empregador ou não, ele possui múltiplos vínculos. Nesse contexto, é importante sabermos que o cálculo da contribuição previdenciária deve ser feito considerando a soma da remuneração recebida em todas as fontes, caso contrário, o INSS será calculado incorretamente.  
  
Para solucionar essa dúvida, siga os passos abaixo:  
  
1. Para calcular o INSS conforme o ESocial será necessário marcar o parâmetro **Calcula INSS conforme eSocial** e informar a partir de quando o sistema iniciará a calcular desta forma, em **Parametrizador | Folha Normal | Geral.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405510466455/mceclip0.png)  
  
Importante**Marcando o parâmetro destacado na imagem acima em uma coligada todas deverão estar marcadas.  
  
**2.** Cadastrar os códigos de cálculo abaixo para atenderem às situações de múltiplos vínculos:  
  
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
  
**Exemplo do cálculo da Folha de funcionário normal outra empresa:**Nesse exemplo, será demonstrado o cálculo de um funcionário que possui dois vínculos em empresas distintas, que não são do mesmo grupo econômico.  
  
Funcionário coligada 1, chapa 00041, salario 2.200,00;  
Foi lançado 30 dias salario;  
Foi lançado o evento **código de calculo 181 – Base INSS outro emprego** no valor de 1.045,00;  
Foi lançado o evento **código de calculo 29 – INSS descontado outro emprego** no valor de 78,37;  
O sistema irá somar a base de INSS, refazer o calculo, conforme a tabela Progressiva.  
  
Calculo: Como já descontou a primeira faixa da tabela na outra empresa – 1.045,00 \* 7,5% = 78,37. O sistema irá começar o calculo a partir da 2 faixa da tabela.  
  
**Base de INSS Outro Emprego (Desconto Complementar):** 1.045,00

                     Total Base de INSS: 3.245,00 (2.200,00 + 1.045,00)

                     INSS: 7,5000% \* Base(1.045,00) = 78,37

                     INSS: 9,0000% \* Base(1.044,60) = 94,01

                     INSS: 12,0000% \* Base(1.044,80) = 125,37

                     INSS: 14,0000% \* Base(110,60) = 15,48

                     Valor do INSS: 313,23

                     INSS Outro Emprego: 78,37

                     Valor a ser descontado: 313,230000 - 78,370000 = 234,860000

**Valor do evento:** 234,86  
  
**Importante**O Sistema não irá trabalhar mais com chapa centralizadora, para atender o ESOCIAL. Diante disso, o sistema irá validar a base de calculo através do CPF do funcionário.  
  
**Saiba Mais**[RM - FOP - Quando utilizar os códigos de cálculo 72, 181 e 29 no cálculo de INSS Múltiplos Vínculos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063693393-RM-FOP-Quando-utilizar-os-c%C3%B3digos-de-c%C3%A1lculo-72-181-e-29-no-c%C3%A1lculo-de-INSS-M%C3%BAltiplos-V%C3%ADnculos-?source=search)[RM - FOP - Quais são os códigos de cálculo para o cálculo de múltiplos vínculos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058694713-RM-FOP-Quais-s%C3%A3o-os-c%C3%B3digos-de-c%C3%A1lculo-para-o-c%C3%A1lculo-de-m%C3%BAltiplos-v%C3%ADnculos-?source=search)  
[Cálculo de INSS múltiplos vínculos conforme o eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=440829559)
