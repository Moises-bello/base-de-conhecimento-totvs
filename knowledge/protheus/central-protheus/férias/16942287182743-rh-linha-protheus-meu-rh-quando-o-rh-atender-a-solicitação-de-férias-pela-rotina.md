---
article_id: 16942287182743
category: FÉRIAS
content_hash: d0ec14742679242dade90cba19d7460a323a732144b6670364205d50da11f8b3
fetched_at: '2026-06-28T22:44:34.523708+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - Meu RH - Quando o RH atender a solicitação de férias
  pela rotina de Efetivação Portal, o Controle Dias de Direito, será aberto para complemente
  dos dados
type: support-article
updated_at: '2025-11-05T21:13:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16942287182743-RH-Linha-Protheus-Meu-RH-Quando-o-RH-atender-a-solicita%C3%A7%C3%A3o-de-f%C3%A9rias-pela-rotina-de-Efetiva%C3%A7%C3%A3o-Portal-o-Controle-Dias-de-Direito-ser%C3%A1-aberto-para-complemente-dos-dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16942269249559) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quando o RH atender a solicitação de férias pela rotina de Efetivação Portal, o Controle Dias de Direito, será aberto para complemento dos dados  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Meu RH – Todas às versões  
  
**Solução**Quando o funcionário realiza uma **solicitação de férias, pelo App Meu RH**, se houve hierarquia de aprovação, essa requisição irá ao seu Gestor para aprovação. Após essa aprovação, **seguirá para a Equipe de RH atender via módulo 07 - SIGAGPE**, na rotina **Efetivar Solicitação Portal - TCFA040**.  
  
Funcionário **solicita 20 dias de férias**, com a venda de **10 dias em abono pecuniário** e **solicitação de 1ª parcela do 13º salário:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16941243126551)  
  
Gestor aprova:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16941272283799)  
  
Após o Gestor aprovar, seguirá para a **Equipe de RH atender**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16941331348631)  
  
Nesse momento, ao clicar em Atender, **o Protheus abrirá essa tela**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16941382771351)  
  
No quadrante abaixo, **as informações da solicitação feita**:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16941377624983)**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16941404029591)  
  
A opção **1ª Parcela de 13º Salário está ativa**, ou seja, **o funcionário solicitou essa antecipação**.  
Nesse momento, ao clicar em Outras Ações -> Aprovar, **será aberta a tela da rotina de controle de Dias de Direito deste funcionário:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16941447485335)  
  
Cabe ressaltar que, **sempre quando um funcionário solicitar férias via App Meu RH**, este **período de gozo escolhido**, assim como **os dias que ele irá vender como abono pecuniário**, serão composto nos **campos abaixo, da rotina Controle Dias de Direito:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16941511071255)  
  
Mas, como o funcionário **solicitou a antecipação da 1ª parcela do 13º salário**, o Protheus abrirá a **rotina de Controle Dias de Direito,** para que o RH preencha a **porcentagem de adiantamento a ser paga ao funcionário:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16941565895063)  
  
Preenchendo esse campo e salvando, a rotina Controle de Dias de Direito irá gravar a solicitação de férias, sendo referenciada como Férias Programadas e, com isso, a Equipe do RH poderá realizar o cálculo efetivamente, pela rotina de **Férias Programadas no menu Miscelânea -> Cálculos -> Férias Programadas - GPEM060.**  
  
Essa necessidade de preenchimento da **porcentagem da 1ª parcela do 13º salário**, ocorre pois, o **parâmetro MV\_PERC13S está em branco, ou com o conteúdo 0**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16941645002903)  
  
O parâmetro **MV\_PERC13S**, permite informar um **valor padrão de porcentagem** do **Adiantamento da 1ª parcela do 13º Salário na Programação de Férias**, que é lançado **automaticamente ao aprovar Solicitações de Férias** advindas do Meu RH, cuja opção "Adiantamento de 13º" foi selecionada.  
  
Se o parâmetro em questão, no momento da solicitação das férias e aprovação da Equipe do RH, **já estiver preenchido com algum percentual**, ao atender a requisição de férias, **a rotina Controle de Dias de Direito, não será aberta e a programação efetivada por completo.**  
  
**Saiba Mais**[**Funcionalidade do parâmetro MV\_PERC13S**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10005428982679-RH-Linha-Protheus-Meu-RH-Funcionalidade-do-par%C3%A2metro-MV-PERC13S)[**Como calcular férias programadas**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004091821-RH-Linha-Protheus-GPE-Como-calcular-f%C3%A9rias-programadas)**[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)[para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/%20https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)**  
**[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)[para acessar a documentação de referência sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)[Artigos sobre Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-Meu-RH)**
