---
article_id: 4459571056535
category: FÉRIAS
content_hash: c72294f8f2260a995cbf62ea21c05deee071d028730409a16478e66bdeb6b89f
fetched_at: '2026-06-28T22:44:34.555975+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - MEU RH - Existe a possibilidade de filtrar os funcionários
  conforme o risco de vencimento do período concessivo das férias
type: support-article
updated_at: '2026-06-22T18:16:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4459571056535-RH-Linha-Protheus-MEU-RH-Existe-a-possibilidade-de-filtrar-os-funcion%C3%A1rios-conforme-o-risco-de-vencimento-do-per%C3%ADodo-concessivo-das-f%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30647517295895)Tempo aproximado para leitura: 00:04:00 min  
  
Dúvida**Existe a possibilidade de filtrar os funcionários conforme o risco de vencimento do período concessivo das férias? **Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões **Solução**Realizada a implementação de uma nova funcionalidade chamada **Risco de Vencimento**, onde esta se encontra disponível nos filtros avançados da tela de Gestão de Férias.  
  
O objetivo deste novo filtro é permitir que o Gestor consiga ter uma visão daqueles funcionários que estão com risco de dobrar as férias.  
  
Dentro dos filtros avançados da tela de Gestão de Férias, foi disponibilizado a opção "Risco de Vencimento".  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4459613350295)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4459424593431)

Esta opção possui alguns valores padrões que vão de 1 ao 10.  
Esses valores são referentes à meses  
  
**Não é possível mudar esses valores ou acrescentar novos valores.**Ao escolher qualquer valor dentro dos disponíveis, o filtro funcionará da seguinte forma.  
  
Tomando por exemplo que foi escolhido o valor 3 (Meses).  
  
1 - O valor escolhido **sempre será multiplicado por 30** para a computação de dias. Logo, se foi escolhido 3, serão 90 dias.  
2 - Serão filtrados os **subordinados do gestor**que tem o vencimento do período concessivo dentro dos próximos 90 dias.  
2.1 - Supondo que um funcionário possua um período concessivo que vencerá em **01/04/2022**, caso a busca seja feita no dia **13/01/2022**, este funcionário **será** apresentado na lista (13/01 + 90 dias = 12/04)  
2.2 - Caso seja escolhida a opção 2 ( 60 Dias), este mesmo funcionário **não** será apresentado ( 13/01 + 60 dias = 13/03)  
  
Abaixo exemplo ao escolher no filtro o **Risco de vencimento = 2**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4459555569815)

3 - Funcionários que possuem **apenas férias a vencer não serão listados**, pois não há risco de dobro de férias.  
4 - Funcionários que possuem férias vencidas, **porém já programadas** no Controle de Dias de Direito (SRF), **não** serão listados.  
5 - Funcionários que **já possuem férias calculadas** **não** serão listados.  
6 - Funcionários que possuem solicitações **ainda não aprovadas**(RH3\_STATUS = 1 ou 4) (Seja pelo Gestor ou pelo RH), **serão** apresentados, desde que estas férias não sejam a vencer.  
7 - Funcionários com férias que já **constam em dobro** **não** serão apresentados, pois as férias já dobraram.  
  
**Documento de referência: [Gestão de Férias - Risco de Vencimento](https://tdn.totvs.com/pages/viewpage.action?pageId=660096701)****Saiba Mais  
[RH - Linha Protheus - MEU RH - É possível o Gestor saber quando um ou mais funcionários da equipe estarão de férias simultaneamente durante o período de gozo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4424988643735)  
[RH - Linha Protheus - MEU RH - O gestor pode solicitar as férias do funcionário pelo MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402719334551)  
[RH - Linha Protheus - MEU RH - É possível o gestor informar o motivo da rejeição na solicitação de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421278138391)  
[RH - Linha Protheus - MEU RH - É possível o Gestor ter maiores informações das férias dos funcionários na rotina Gestão de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4424781949079)  
  
[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)[para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)[para acessar a documentação de referência sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
