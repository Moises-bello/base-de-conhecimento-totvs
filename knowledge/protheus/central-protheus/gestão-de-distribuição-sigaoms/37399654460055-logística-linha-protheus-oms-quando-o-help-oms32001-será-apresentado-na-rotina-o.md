---
article_id: 37399654460055
category: Gestão de Distribuição (SIGAOMS)
content_hash: 9d22031ff7c92f76c53db3a4d7445edabbcf52b031964e137a301a12cca5a3d2
fetched_at: '2026-06-28T22:45:50.118326+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Quando o help OMS32001 será apresentado
  na rotina OMSA320
type: support-article
updated_at: '2026-05-29T20:32:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37399654460055-Log%C3%ADstica-Linha-Protheus-OMS-Quando-o-help-OMS32001-ser%C3%A1-apresentado-na-rotina-OMSA320
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37399654446103) Tempo aproximado para leitura: **00:03:12 min**  
  
**Ocorrência**  
Ao realizar o retorno de cargas na rotina **OMSA320**, o sistema pode apresentar o *help* **OMS32001**, impedindo a gravação do registro quando a data de entrega informada é anterior à data de emissão da Nota Fiscal.  
  
Mensagem apresentada:   
**OMS32001**  
**“A data de entrega informada é menor do que a data de emissão da nota fiscal.**  
**Informe uma data de entrega maior ou igual à data de emissão da nota fiscal.”**  
  
**Ambiente**  
TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Causa**  
Foi identificada a possibilidade de inconsistências no processo de retorno de cargas quando o sistema permitia informar uma data de entrega inferior à data de emissão da Nota Fiscal. Para evitar esse cenário, foi implementada uma nova validação no **OMS** que compara os seguintes campos:  
  
**F2\_DTENTR – Data de Entrega**  
**F2\_EMISSAO – Data de Emissão da Nota Fiscal**  
  
Quando a data de entrega for menor que a data de emissão, o sistema bloqueia a operação e exibe o *help* **OMS32001.**  
  
**Solução**  
A correção foi aplicada para garantir a integridade das informações, impedindo o usuário de informar uma data de entrega anterior à data de emissão da Nota Fiscal. A partir dessa validação, o sistema exige que:  
A data informada no campo **F2\_DTENTR – Data de Entrega** seja maior ou igual à data do campo **F2\_EMISSAO – Data de Emissão da Nota Fiscal**.  
Caso a regra não seja atendida, o retorno da carga não será concluído.  
  
Para informar a data entrega, acesse a rotina **OMSA320**, selecione a carga desejada.  
No campo **Data de Entrega - F2\_DTENTR**, informe uma data igual ou posterior à **F2\_EMISSAO – Data de Emissão da Nota Fiscal**. Salve o retorno da carga.  
Caso a data informada seja inferior à data de emissão, o sistema exibirá o *help* **OMS32001** e impedirá a gravação.  
  
**Importante**  
Para realizar o retorno com uma data de entrega anterior à data de emissão da Nota Fiscal, disponibilizamos o parâmetro **MV\_OMDTANT**, que possibilita contornar essa validação. O detalhamento desse parâmetro pode ser consultado na seção **Saiba Mais**, logo abaixo. Entretanto, cabe a cada cliente avaliar a necessidade de utilização desse recurso, considerando que a data de entrega informada no retorno da carga atualiza o campo **F2\_DTENTR – Data de Entrega**, utilizado no preenchimento da tag da NF-e.  
  
**Saiba mais**  
Mais informações poderão ser acessadas os *links*:   
[Inclusão de Validação de Data Entrega no Retorno de Carga](https://tdn.totvs.com/pages/viewpage.action?pageId=977860145)  
[Boletim Técnico - Parâmetro MV\_OMDTANT](https://tdn.totvs.com/pages/viewpage.action?pageId=1039008717)  
[Logística - Linha Protheus - OMS - Como efetuar o retorno parcial de carga na rotina OMSA320 -  Retorno de Cargas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33465369804055-Log%C3%ADstica-Linha-Protheus-OMS-Como-efetuar-o-retorno-parcial-de-carga-na-rotina-OMSA320-Retorno-de-Cargas)  
[Logística - Linha Protheus - OMS - Quais funcionalidades compreende a rotina de Retorno de Cargas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063841253-Log%C3%ADstica-Linha-Protheus-OMS-Quais-funcionalidades-compreende-a-rotina-de-Retorno-de-Cargas)  
[Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na rotina Retorno de Cargas - OMSA320](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411608756631-Log%C3%ADstica-Linha-Protheus-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-Retorno-de-Cargas-OMSA320)
