---
content_hash: b73e5a276591dbd1145b912225a4b61a066c8a87b2395076f6602679464771ae
fetched_at: '2026-06-29T00:06:18.275980+00:00'
page_id: '215483220'
product: rm
source: tdn-rm
title: ER_PCREQ-8789_Reajuste_de_Contrato_de_Maneira_Diferenciada_por_Tipo_de_Servico_Contratado
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8789_Reajuste_de_Contrato_de_Maneira_Diferenciada_por_Tipo_de_Servico_Contratado
version: 156
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contratos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP009 | **IRM1** | PCREQ-8788 |
| **Requisito1** | PCREQ-8789 | **Subtarefa1** | PDR\_CP\_TOP009-26 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |
| **Integração** | Não se aplica | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Criar uma nova possibilidade de reajuste de contratos a nível de item contratado.

## Definição da Regra de Negócio

Em alguns contratos, é necessário que o reajuste aconteça a nível de item contratado, como por exemplo em clientes que trabalham para o DNIT e que necessitam que esse reajuste aconteça por vários índices, sendo que cada um é aplicado para um determinado grupo de tarefas, assim como o exemplo:

Ex. Índice para reajuste de serviços de Terraplenagem, índice para reajuste de serviços de Pavimentação, etc.

Sendo assim, deverá ser criado no módulo de contratos do TOTVS Obras e Projetos, uma nova possibilidade de realizar reajustes para os itens associados aos contratos.

**1 - Edição de Contratos - Reajuste**

Deverá ser criado um novo tipo de reajuste na aba de "Reajuste" da tela de edição de contratos (), onde existirá dois tipos de reajustes: "Por Contrato" que representa o reajuste já existente e "Por Item Associado", o novo tipo de reajuste, além da opção "Sem Reajuste" que deixará de estar presente no campo "Período Reajuste" que terá apenas as opções "Anual" e "Mensal".

Ao selecionar o tipo "Por Item Associado", os índices associados, caso existam, serão excluídos, pois o reajuste por item associado dependerá de índices que deverão ser informados manualmente no processo de "Reajustar Itens Associados ao Contrato".

**2 - Processo de Reajustar Itens Associados ao Contrato**

Deverá ser desenvolvido um novo processo de reajuste de contratos, "Reajustar Itens Associados ao Contrato" (Protótipos  e ), onde algumas regras ou restrições deverão ser consideradas:

* + Tela do processo deve ser maximizada;
  + Reajuste dos itens contratados. Para aplicar em todo o contrato basta selecionar todos os itens do contrato;
  + Reajuste anual ou mensal que acontece somente a partir da "Data Base de Reajuste" definida no contrato e essas parametrizações do contrato somente estarão disponíveis para alteração se não existir reajuste para o contrato;
  + A Data Base de Reajuste poderá ser menor que a data inicial do contrato, porém não maior que a data final;
  + Ao aplicar o reajuste no item associado, deverá ser considerado duas formas de incidência, no valor inicialmente contratado, que representa o valor antes do primeiro reajuste realizado para o item, ou no valor atual, pois este pode ter sofrido reajustes anteriores. Um parâmetro na tela do processo permitirá essa flexibilidade, porém o mesmo somente estará habilitado se não existirem reajustes já realizados para o contrato, pois, caso contrário, o valor do item poderia ser diminuído em reajuste posteriores;
  + Não deverá ser utilizado índices do cadastro de cotações, pois o percentual será informado manualmente pelo usuário;
  + Deverá ser possível informar a data do reajuste, isto é, a data na qual o reajuste deverá incidir. Para definição da data, como facilitador, poderá ser selecionado o período do contrato ou o ano, sendo que este último, somente estará disponível se a periodicidade do reajuste estiver definida como "Anual". Ao selecionar o período a data definida será a data inicial do mesmo e para o ano, a data definida será a data de aniversário do reajuste:
    - Ex: Data Base: 10/02/2014 | Ano Selecionado: 2015 | Data do Reajuste: 10/02/2015
  + Possibilidade de selecionar mais de um item contratado para a aplicação de um mesmo índice;
  + Para cada item associado deverá ser exibido o índice utilizado no reajuste anterior assim como o valor antes do reajuste atual;
  + Deverá ser exibido, a partir de qual período do contrato o reajuste será considerado. Essa informação estará na tela do processo e também no log após a execução do mesmo;
  + Deverá ser exibido a data em que foi realizado o reajuste;
  + O item somente será reajustado se a data do reajuste for maior ou igual a data base de reajuste do contrato selecionado e o item estar apto para o reajuste, considerando a data de "aniversário" baseada na periodicidade do reajuste, e se não existirem reajustes realizados para o item no período em questão;
  + Itens de aditivos também deverão ser exibidos;
  + Se existir algum item de aditivo disponível para reajuste, o mesmo ocorrerá sem restrições particulares;
  + Ao aplicar o reajuste, deverá ser verificado se existem períodos medidos ou liberados dentro do intervalo subsequente ao reajuste, conforme o exemplo:
    - Ex: Reajuste em 01/01/16: Verificar se existe algum período medido ou liberado a partir dessa data de reajuste, caso exista, não deverá permitir o reajuste;
  + Os períodos que tiverem períodos complementares criados deverão considerar os valores dos itens em relação ao intervalo do reajuste, como por exemplo:
    - Contrato XYZ:  01/01/2015 à 31/12/2017 => 36 períodos;  
      Reajuste realizado a partir de 01/01/2016;  
      Períodos complementares anteriores ao 13º período (01/01/2016 à 31/01/2016) deverão considerar os valores antes do reajuste de 01/01/2016;
  + Se um contrato for paralisado, e novamente for colocado em andamento, caso os períodos não sejam reprogramados, os valores considerados na medição e liberação deverão obedecer ao período de reajuste, conforme exemplo:
    - Contrato 0001/2015 de 01/01/2015 à 31/12/2016 com 24 períodos:  
      Período 0001 - 01/01/2015 a 31/01/2015  
      Contrato paralisado em 01/02/2015  
      Contrato em andamento em 01/03/2016 no período 0015  
      Reajuste realizado em 01/01/2016  
      Valores de medição e liberação até o período 0012 deverão ser considerados antes do reajuste de 01/01/2016
  + Ao solicitar o reajuste, será verificado a pendência de algum reajuste em aniversários anteriores, no qual o usuário será avisado (). Essa validação será feita considerando a data informada para o reajuste.
  + Consistências necessárias ao processo que impedem a execução do mesmo:
    - Validar se o Tipo de Reajuste do contrato está definido como "Por Item Associado";
    - Validar se a "Data de Aniversário" corrente é maior que a Data Base de Reajuste;
    - Validar se a Data de Reajuste é maior ou igual à Data de Aniversário;
    - Validar se existem reajustes já realizados para o item;
    - Validar se existem reajustes posteriores já lançados, pois reajustes retroativos não serão permitidos;
    - Validar se existe medição no intervalo corrente, em algum período para o item;
    - Validar se o percentual informado é negativo, o que não é permitido.

****3 - Processo de Cancelar Reajuste de item Associado****

Deverá ser desenvolvido um novo processo que possibilita o cancelamento do último reajuste realizado no item associado. Este processo estará presente no menu de processos do anexo de Itens do Contrato ().

O usuário deverá selecionar os item(s) associado(s) ao contrato e executar o processo, nesse momento o último reajuste realizado para o item será excluído e os valores recalculados.

O Cancelamento acontecerá da seguinte maneira:

* + Item 001.01.01 - Escavação:  
    Valor Inicial: 500,00  
    Percentual de Reajuste: 10%  
    Valor Reajustado: 550,00  
      
    Ao cancelar o reajuste, será verificado se o valor atual do item é igual ao valor reajustado, caso positivo, o valor é alterado para o valor anterior ao reajuste, e caso contrário, o cancelamento não será processado.

Consistências necessárias ao processo que impedem a execução do mesmo:

* + Validar se o Tipo de Reajuste do contrato está definido como "Por Item Associado";
  + Validar se existem reajustes para serem cancelados;
  + Validar se existe medição no intervalo corrente, em algum período para o item;
  + Validar se o valor do item é igual ao valor reajustado.

****4 - Anexo de Reajustes de Item Associado****

Deverá ser desenvolvido no anexo de Itens do Contrato um outro anexo de "Reajustes do Item" que poderá ser visualizado na tela de edição do Item (). Nesse anexo será possível consultar todos os reajustes que foram realizados para o item em questão.

**5 - Medição de Períodos de Contrato**

No processo de medição deverá ser exibido um alerta para que o usuário saiba que o contrato necessita de um reajuste caso o mesmo não tenha sido realizado ().

    **Importante:**

* **O reajuste contratual existente, deverá ser desconsiderado em caso da utilização de reajuste "Por Item Associado";**
* **O processo "Reajustar Itens Associados ao Contrato" somente estará disponível para contratos do tipo "Prestação de Serviços";**
* **Aplicação do Reajuste:**
  + **Valor Inicial Contrato: Representa o valor o item antes do primeiro reajuste;**
  + **Valor Atual: Representa o valor atual do item, inclusive com reajustes já aplicados.**

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Contratos | [Alteração] | Controle -> Contrato -> Contratos | - |

## Protótipo de Tela

**Protótipo 01**

****Protótipo 02****

**Protótipo 03**

****Protótipo 04****

********Protótipo 05********

****Protótipo 06****

**Protótipo 07**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
