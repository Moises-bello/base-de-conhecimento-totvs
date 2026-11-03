---
article_id: 360059471093
category: PONTO ELETRÔNICO
content_hash: 2b1621ddf55ba541c2fc421b55c29e9c5c643d2083264ab6b247dbcb152ef9d2
fetched_at: '2026-06-28T22:44:36.738022+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - MEU RH - É possível impedir que o sistema registre marcações
  em duplicidade e impor intervalo mínimo entre as marcações
type: support-article
updated_at: '2026-06-22T18:21:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059471093-RH-Linha-Protheus-MEU-RH-%C3%89-poss%C3%ADvel-impedir-que-o-sistema-registre-marca%C3%A7%C3%B5es-em-duplicidade-e-impor-intervalo-m%C3%ADnimo-entre-as-marca%C3%A7%C3%B5es
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24769574295575)**Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**É possível impedir que o sistema registre marcações remotas em duplicidade e definir intervalo mínimo entre duas marcações?  
  
**Ambiente**TOTVS RH (Linha Protheus) - MEU RH - todas as versões  
  
**Solução**

Foram implementadas melhorias no processo de batida remota por geolocalização, para impedir que o sistema registre batidas em duplicidade, ou dentro de um intervalo mínimo entre duas ou mais batidas.  
  
Para que seja possível fazer esse controle, o sistema irá validar o conteúdo os parâmetros **MV\_MCIGUAL** e **MV\_DESPMIN** na inclusão de batidas remotas. Esses parâmetros já são avaliados durante o processo de leitura de marcações pelo módulo Ponto Eletrônico do Protheus (SIGAPON), e agora passam a ser avaliados também pelo Meu RH.  
  
**Informações sobre os parâmetros:****MV\_MCIGUAL** - Define se o sistema irá aceitar marcações duplicadas. Valores aceitos: **S** (sim) ou **N** (não).  
  
Exemplo: o parâmetro configurado com valor N indica que o sistema não aceitará batidas iguais Caso o funcionário registre duas batidas às 08:00 a segunda batida será ignorada e não será exibida em seu espelho de ponto.

**MV\_DESPMIN** - Define o intervalo de minutos que deve existir entre duas marcações.   
Valores aceitos: **0****1** a **10**Exemplo: o parâmetro configurado com valor 05 indica que o intervalo mínimo entre duas batidas deverá ser de 5 minutos. Caso o funcionário registre uma batida às 08:00 e outra às 08:03, a marcação feita às 08:03 será ignorada e não será exibida em seu espelho de ponto.

Documento de referência: [Melhorias na batida remota do ponto - Portaria 373/2011](https://tdn.totvs.com/pages/viewpage.action?pageId=562482900)  
  
Exemplo da utilização dos parâmetros:  
  
**MV\_DESPMIN = 05 -** Definido intervalo de 5 minutos entre duas marcações  
**MV\_MCIGUAL = N -** Definido para não aceitar marcações duplicadas  
  
O usuário acessa o MEU RH e registra mais de uma batida no mesmo minuto: **11:40hs**  
  
![HvrIPZduq6.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4417470162711)  
  
Neste exemplo o usuário registra outra batida dentro do intervalo estabelecido de 5 minutos, onde já havia efetuado uma batida às **11:40hs** e registrou outra às **11:43hs.**A segunda batida então é desconsiderada e não é apresentada em seu espelho de ponto  
  
![IbkvmUqL7M.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4417462643863)  
  
**Observações:**

As batidas que foram ignoradas automaticamente ficarão registradas no sistema, e serão geradas no relatório AFDT com algum dos motivos abaixo, conforme a origem da exclusão:

*Exclusão automática APP MEURH: batida duplicada*

*Exclusão automática APP MEURH: batida abaixo do intervalo mínimo entre duas ou mais batidas*

**Saiba Mais  
[RH - Linha Protheus - MEU RH - Como registrar a marcação de Ponto através da rotina Relógio (Geolocalização)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050355093)  
[RH - Linha Protheus - MEU RH - Marcações realizadas pela Geolocalização precisa de aprovação pelo Gestor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044750674)**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
