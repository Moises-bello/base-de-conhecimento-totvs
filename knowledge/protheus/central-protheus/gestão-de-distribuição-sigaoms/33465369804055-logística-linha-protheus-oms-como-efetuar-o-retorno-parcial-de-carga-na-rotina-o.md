---
article_id: 33465369804055
category: Gestão de Distribuição (SIGAOMS)
content_hash: 8d16084c657b1c4310561a44f161b01fc0665396dcf988d77c3813b09fc10f2c
fetched_at: '2026-06-28T22:45:49.681729+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como efetuar o retorno parcial de carga
  na rotina OMSA320 -  Retorno de Cargas
type: support-article
updated_at: '2026-01-02T20:20:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33465369804055-Log%C3%ADstica-Linha-Protheus-OMS-Como-efetuar-o-retorno-parcial-de-carga-na-rotina-OMSA320-Retorno-de-Cargas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33465369791127) Tempo aproximado para leitura: **00:02:24 min**  
  
**Dúvida**  
Como efetuar o retorno parcial de carga na rotina **OMSA320 -  Retorno de Cargas?**  
  
**Ambiente**  
TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**  
A rotina **OMSA320 – Retorno de Cargas** possibilita a formalização do retorno de uma carga, permitindo a conclusão das entregas vinculadas a ela. O retorno pode ser realizado de forma total ou parcial, de acordo com a necessidade operacional.  
  
O controle dessa funcionalidade é feito por meio do parâmetro **MV\_OMSRETP**, que define se o retorno parcial das cargas será permitido, considerando as datas de entrega das Notas Fiscais.

* Por padrão, o parâmetro vem configurado como **Falso (.F.)**, permitindo apenas o retorno total da carga. Nesse cenário, será necessário formalizar o *Status* de entrega de todas as Notas Fiscais da carga de uma só vez. Após concluir o retorno, o *Status* do Retorno da Carga ficará igual a **Efetuado - Legenda Vermelha**. O preenchimento do campo **F2\_DTENTR** não é obrigatório.
* Quando o parâmetro estiver definido como **Verdadeiro (.T.)**, o Sistema permite o **retorno parcial**, possibilitando registrar as entregas conforme ocorrem. Nesse caso, no campo **F2\_DTENTR** será necessário o preenchimento da data de entrega de cada Nota Fiscal. 

  ![3.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/33477473981719)
* Ao salvar o retorno da carga, caso exista alguma Nota Fiscal sem a data de entrega informada, o sistema exibirá a seguinte mensagem de alerta:  
  **OMS32002 – O status da carga não será alterado, pois existem notas sem data de entrega informada.**

**Importante**  
Mesmo com o parâmetro ativado, enquanto houver Notas Fiscais sem a data de entrega preenchida, o status da carga permanecerá em aberto. A conclusão do retorno financeiro na rotina OMSA341 somente será permitida após o preenchimento do campo F2\_DTENTR para todas as Notas Fiscais vinculadas à carga.  
  
**Saiba mais**  
Mais informações poderão ser acessadas no *link*:   
[Logística - Linha Protheus - OMS - Quando o help OMS32001 será apresentado na rotina OMSA320](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37399639448599-Log%C3%ADstica-Linha-Protheus-OMS-Quando-o-help-OMS32001-ser%C3%A1-apresentado-na-rotina-OMSA320)  
[Logística - Linha Protheus - OMS - Quais funcionalidades compreende a rotina de Retorno de Cargas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063841253-Log%C3%ADstica-Linha-Protheus-OMS-Quais-funcionalidades-compreende-a-rotina-de-Retorno-de-Cargas)  
[Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na rotina Retorno de Cargas - OMSA320](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411608756631-Log%C3%ADstica-Linha-Protheus-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-Retorno-de-Cargas-OMSA320)  
[Retorno de Cargas - OMSA320](https://tdn.totvs.com/pages/releaseview.action?pageId=559505011)
