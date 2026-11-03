---
article_id: 360050452713
category: RH - Cadastros
content_hash: ccf9cf3af8de854ada05473a593967cd8c1c876640a41b351c2f82fb7402cfb3
fetched_at: '2026-06-28T22:44:52.952481+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Configuração de Tolerância para Horas Não Realizadas
  por Marcação e Período
type: support-article
updated_at: '2026-02-03T17:51:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050452713-RH-Linha-Protheus-PON-Configura%C3%A7%C3%A3o-de-Toler%C3%A2ncia-para-Horas-N%C3%A3o-Realizadas-por-Marca%C3%A7%C3%A3o-e-Per%C3%ADodo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28676921013655)** Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como configurar a Tolerância para Horas não realizadas por Marcação e Período?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para os exemplos abaixo, foi considerado um funcionário com horário 08:00 - 12:00 - 13:00 - 17:00, tolerância de 5 minutos por marcação e 10 minutos diários.

Em **Atualizações - Cadastros Ponto - Regra de Apontamento**, filtre a regra do funcionário e, com a opção **Alterar**, na **aba Tolerâncias**, defina as tolerâncias de 00:05 por marcação e 00:10 por período apenas para os campos correspondentes às horas não realizadas (Tol. Hr. NReal), conforme exemplo da tela abaixo:

![Capturar9.PNG](https://tdn.totvs.com/download/attachments/496398394/Capturar9.PNG?version=1&modificationDate=1579780332823&api=v2)

**- Horas Não Realizadas**  
Acesse em **Atualizações - Lançamentos - Integrados**, filtre a matrícula do funcionário e siga o cenário:

Para o dia 01/01/2020, o sistema irá gerar o evento de atraso com 00:06, pois apenas a tolerância por marcação não foi respeitada.

Para o dia 02/01/2020, o sistema irá gerar 00:06 de atraso e 00:05 de saída antecipada. Neste caso, a tolerância por período não foi respeitada.

Para o dia 03/01/2020, o sistema não irá gerar evento de atraso e saída antecipada, pois as duas tolerâncias foram respeitadas.

![Capturar10.PNG](https://tdn.totvs.com/download/attachments/496398394/Capturar10.PNG?version=3&modificationDate=1579781470593&api=v2)

**Observação:**Quando apenas a tolerância de horas não realizadas estiver preenchida, os eventos de atraso e saída antecipada serão somados e o resultado será validado com a tolerância de horas não realizadas.  
  
É possível também cadastrar a tolerância de horas não realizadas apenas por período, por exemplo, de 10 minutos diários. Para isso, deixe o cadastro da Regra de Apontamento desta forma:  
![Capturar5.PNG](https://tdn.totvs.com/download/attachments/496398394/Capturar5.PNG?version=1&modificationDate=1579725730167&api=v2)  
  
**Observação:** Não será possível preencher o campo Tol. Hr. NReal, caso o campo Tol. S. A. Per. ou o Tol. Atr. Per. estiverem preenchidos com algum valor.  
No apontamento, o sistema irá somar atrasos e saída antecipada, como se fossem um único evento negativo do dia e verificar se ultrapassaram a tolerância cadastrada.  
As marcações que geraram descontos estão destacadas com vermelho, pois somadas ultrapassam a tolerância de 00:10.  
  
Para o dia 08/01/2020, o sistema somou os dois eventos (Atrasos e Saída Antecipada) e, como o resultado, ultrapassou a tolerância de 10 minutos. Ambos os eventos foram apontados:  
![Capturar6.PNG](https://tdn.totvs.com/download/attachments/496398394/Capturar6.PNG?version=1&modificationDate=1579726287457&api=v2)

**Importante:** O sistema não irá aplicar as tolerâncias para os eventos com ID 001A, 005A, 026A e 027N.  
  
  
**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como parametrizar a tolerância por marcação e por período corretamente?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406537073687-RH-Linha-Protheus-PON-Como-parametrizar-a-toler%C3%A2ncia-por-marca%C3%A7%C3%A3o-e-por-per%C3%ADodo-corretamente)
