---
article_id: 360015983071
category: Cálculo
content_hash: 53d1a50e18ced8654c7c07a5aa5733483afc99f893e26ef7199f531bdb470ed7
fetched_at: '2026-06-28T22:46:29.255457+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Calcular as extras de refeição em um evento do Automação de
  Ponto
type: support-article
updated_at: '2026-05-22T20:10:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015983071-RH-RM-PTO-Calcular-as-extras-de-refei%C3%A7%C3%A3o-em-um-evento-do-Automa%C3%A7%C3%A3o-de-Ponto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19409056172055) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Como calcular as extras de refeição em um evento do Automação de Ponto?  
  
**Ambiente**  
RH - RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 11.80  
  
**Solução**  
  
Para calcular as extras de refeição do funcionário em um evento do Automação de Ponto, siga os passos abaixo:

* **Parametrização**  
  1- Acesse no módulo de **Automação de Ponto,** o menu **Configurações | Parametrizador** ao abrir o assistente clique em avançar e selecione o processo **08.02 - Sindicato** e edite o sindicato que terá a diferenciação das extras referente ao intervalo de ausência planejada. ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13638813391127)  
    
  2- Ao abrir o novo assistente, avance até a etapa **2 - Extras** e marque o parametro **Considera extras de refeição dentro do intervalo de ausência planejada,** e avance as demais etapas até concluir.  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13638893568023)
* **Ajustes horários:**  
  1- Para horários do tipo **flexível**e **rígido**, deve ser cadastrado o intervalo de ausência planejada.   
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29748256655255)  
    
  2- Para horários do tipo **semi-flexível**, inclua a ausência planejada/e ou limite de refeição, porém não deve ser cadastrado **tempo mínimo**, pois as extras do funcionário não serão calculadas.  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29748264099351)
* **Eventos**  
  1- Acesse no módulo de **Automação de Ponto,** o menu **Configurações | Evetnos:**  
  **![](https://centraldeatendimento.totvs.com/hc/article_attachments/13639108768535)**  
  2 - Selecione o botão **Incluir** e cadastre um novo evento de **Extra de Refeição Autorizado** com o código de cálculo **0043 - Tipo Ocorrência**.  
  ![2018-09-14_12_17_13-.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011091712)  
    
  3- Após salvar o evento, selecione o menu **Anexos** e a opção **Evento por tipo de ocorrência**.  
  ![2018-09-14_12_17_37-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011123291)  
    
  4-Insira a ocorrência do tipo **ERA - Extra Refeição Autorizado** e salve o evento.  
  ![2018-09-14_12_18_22-.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011123311)  
  ![2018-09-14_12_18_36-.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011123331)  
    
  5- Acesse no módulo de **Automação de Ponto,** o menu **Configurações | Parametrizador a**o abrir o assistente clique em avançar e selecione o processo **08.02 - Sindicato** e edite o sindicato desejao.  
    
  6- Ao abrir o novo assistente, avance até a etapa **18 - Eventos** e realize a inserção do evento cadastrado com o evento desejado do **Labore.**  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29748264101911)  
  ![2018-09-14_12_20_09-.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011123371)  
    
  **Importante:**  
  - Efetuar o recálculo do espelho do funcionário e conferir na aba do espelho do funcionário, Ocorrências os registros existentes com a ocorrência ERA (Extra de Refeição Autorizada);

  **- O funcionário deverá ter batidas lançadas no período para o intervalo de ausência de planejada (intervalo de refeição) e estas batidas deverão compreender um número de horas menor  do que o cadastrado para este intervalo, sendo assim calculadas horas extras referente a este intervalo;**  
    
  Para que gere a extra de refeição, quando não houver a intercessão entre as batidas realizada e intervalo de refeição planejado é necessário executar o processo de ignorar ausência planejada para o dia/e ou periodo que o funcionário trabalhou no periodo integral da refeição. Nos links abaixo segue as orientações de como realizar o processo para ignorar a ausência:  
    
  [RH - RM - PTO - Ignorar ausência planejada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007455371-TOTVS-RH-Linha-RM-PTO-Ignorar-aus%C3%AAncia-planejada?source=search)  
  [RH - RM - PTO - Ignorar ausência planejada de forma global](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5622637670039-TOTVS-RH-Linha-RM-PTO-Como-ignorar-aus%C3%AAncia-planejada-de-forma-global?source=search)

**Saiba Mais**  
[Considera extras de refeição dentro do intervalo de ausência planejada](https://tdn.totvs.com/pages/viewpage.action?pageId=241698141)  
[Sindicato - Considera extra de refeição no Feriado](https://tdn.totvs.com/pages/viewpage.action?pageId=640531249)

[Extra](https://tdn.totvs.com/display/public/LRM/Extra)  
[Artigo 59-A - Acordo Individual Doze Horas Seguidas por Trinta e Seis](https://tdn.totvs.com/display/LRM/Artigo+59-A+-+Acordo+Individual+Doze+Horas+Seguidas+por+Trinta+e+Seis)
