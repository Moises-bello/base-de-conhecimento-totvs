---
article_id: 23533525764375
category: PONTO ELETRÔNICO
content_hash: c60208801cb39bd18ea7668a590a0ac1bbbce122c2a809c0195dfd6d02726994
fetched_at: '2026-06-28T22:44:36.496882+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - Por que a marcação feita no horário noturno,
  foi alocada para o dia seguinte de forma incorreta
type: support-article
updated_at: '2026-06-22T17:33:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23533525764375-RH-Linha-Protheus-Meu-RH-Por-que-a-marca%C3%A7%C3%A3o-feita-no-hor%C3%A1rio-noturno-foi-alocada-para-o-dia-seguinte-de-forma-incorreta
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23533552326679) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Por que a marcação feita no horário noturno, foi alocada para o dia seguinte de forma incorreta?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**  
Para um funcionário com horário comercial diurno, **a Tabela de Horário Padrão vinculada ao seu Turno de Trabalho**, terá uma configuração semelhante a esta do exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23533525726231)  
  
É importante também ter os **dias não trabalhados**, no caso Sábado e Domingo, **com os horários preenchidos**, pois o funcionário poderá ser convocado para realizar uma Hora Extra nestes dias, com isso, **o App Meu RH e o Ponto Eletrônico (módulo SIGAPON)** terão a referência **para gerar a alocação da marcação e, consequentemente, os apontamentos.**  
  
Porém, no caso de realização de **Hora Extra num dia de trabalho**, e o funcionário realizar a marcação **em horário noturno, ou seja, após as 22:00**, essa marcação precisará ser alocada **para o mesmo dia da jornada inicial no App Meu RH.**  
  
Neste caso, simulando que este funcionário no dia 24/05/2024 recebeu uma solicitação de Hora Extra, para que ele finde o dia de jornada apenas as 23:30.   
Neste dia, o funcionário terá essas marcações:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23533525727895)  
  
Quando for realizar **via Geolocalização, ou até por inclusão manual**, a marcação das 23:30 do dia 24/05, o Meu RH poderá alocar para o dia seguinte, dessa forma:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23533552333719)  
  
Este cenário ocorreu por causa do **preenchimento incorreto do campo Limite Superior da Tabela de Horário Padrão do funcionário.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23533525734423)  
  
Neste exemplo, a jornada padrão do funcionário **finda às 18:00**, porém como o **Limite Superior** está cadastrado **como 4 horas**, somente irão ser processadas corretamente, as **marcações incluídas até as 22:00** daquele dia, **pois 18:00 + 4:00 = 22:00.**  
  
No caso, o funcionário realizou a marcação **após esse horário limite**, **sendo as 23:30,** por isso, essa alocação para o dia seguinte.  
  
Efetivamente, um dia acaba as 23:59, por isso, nesse exemplo, a **quantidade correta para o campo Limite Superior seria: 23:59 - 18:00 = 05:59:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23533552337303)  
  
Com esta configuração, o dia como um todo, ficará coberto **pelos limites e pela jornada de trabalho**, assim se o funcionário realizar a **marcação as 23:30 esta será alocada como 2ª saída do mesmo dia da 1ª entrada.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23533552338967)  
  
**IMPORTANTE:**  
Esta mesma premissa e orientação, vale para uma **Tabela de Horário Padrão quando o funcionário trabalha efetivamente num horário noturno**, onde a 1ª Entrada é num dia e, as demais no dia seguinte.  
  
Exemplo de uma Tabela de Horário Padrão em **horário noturno**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23533552340375)  
  
**Limite Inferior**, irá compreender das 12:00 as 22:00, pois temos 10 horas de limite inferior.  
**Limite Superior**, irá compreender das 05:00 as 11:59, pois temos 06:59 horas de limite superior.  
  
Basicamente, se somarmos os montantes teremos exatamente:  
10:00 horas **(limite inferior)** + 07:00 horas **(jornada total)** + 06:59 horas **(limite superior)**  
**TOTALIZANDO: 23:59 horas**  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
