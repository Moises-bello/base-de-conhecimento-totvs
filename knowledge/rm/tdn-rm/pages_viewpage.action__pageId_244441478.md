---
content_hash: 4139d425c5cd47ad17c710c37d7273e15008eb0c186b7450f43bc4efb6948e3b
fetched_at: '2026-06-29T00:08:14.117903+00:00'
page_id: '244441478'
product: rm
source: tdn-rm
title: ER_SAUHRM01-283_Períodos_para_cálculo_de_data_hora_extraordinária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244441478
version: 3
---

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | RM SAÚDE |
| **Segmento Executor** | SAÚDE | | |
| **Projeto1** | SAUHRM01 | **IRM1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-390 |
| **Requisito1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-283 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-567 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

\_Toc355276661\_Toc355276662

# Objetivo

Atualmente o sistema só permite que seja informado o horário inicial para cobrança de valores extras no sábado.  
 A solicitação visa que estas informações sejam habilitadas para Domingos e feriados. Na parametrização atual, domingos e feriados são considerados extras as 24 horas do dia.  
 \_Toc355276664

# Definição da Regra de Negócio

**RN001** – Criação de parâmetros na tela de Padrões de faturamento e codificação, onde será possível informar o Horário extra no Domingo e nos Feriados a partir de um determinado horário.   
 Esta regra seguirá o mesmo padrão já existente para o sábado.   
 Exemplo:   
 A Base de horários extra é das 19:00 até 06:59; - Faixa Geral.   
 Horário Extra no sábado a partir das 19:00 até as 06:59 de domingo;   
 Horário Extra de Domingo a partir das 19:00 até as 06:59 de segunda feira.

* Fora deste período o horário será normal.   
   Horário Extra de feriados a Partir das 19:00 até 06:59 do próximo dia útil.
* Fora deste período o horário será normal.   
     
   **RN002** – Criação de percentual de acréscimo por dia de horário Extra.   
   Este percentual propiciará o cálculo de um percentual diferente para cada dia.   
   **RN003 –** Percentual de acréscimo Horário Extra.  
   Campo já existente no sistema. Se os percentuais por dia estiverem em branco o sistema irá considerar este como base.

  |  |  |  |
  | --- | --- | --- |
  | Rotinas Envolvidas |  |  |
  | **Rotina** | **Tipo de Operação** | **Opção de Menu** |
  | Registro de Atendimento Externo | Alteração | Atendimento/Pronto Atendimento /Ambulatório/Registro de atendimentos externos |

  # Escopo Negativo

  Não se aplica.

  # \_Toc355276665Protótipo de Tela

  As imagens de telas destacadas a seguir são consideradas apenas protótipos, as mesmas poderão sofrer alterações em função da atualização de componentes utilizados no sistema.

  |  |  |
  | --- | --- |
  | **RI-001** | **Na tela serão implementados os campos:**     **Percentual de Acréscimo:** Para sábado, Domingo e Feriado. Estes campos deverão ser informados se existirem percentuais específicos para estes. O Sistema deverá efetuar os cálculos sobre estes percentuais.     **Horário Extra no Domingo a partir de:** Este campo deve ser informado para que o sistema comece a contar o horário de extras somente a partir do horário informado até o horário final que é definido no campo horário extra final.Exemplo:   Horário Extra no Domingo a partir das **19:00**.   Com base no horário final o sistema entenderá a que a extra começará domingo as 19:00 e terá seu termino às 07:00 de segunda feira.     **Horário Extra no Feriado a partir de**: Este campo deve ser informado para que o sistema comece a contar o horário de extras somente a partir do horário informado até o horário final que é definido no campo horário extra final. Exemplo:\_GoBack   Horário Extra no Feriado a partir das **19:00**.   Com base no horário final (Print acima) O sistema entenderá a extra começará domingo as 19:00 e que o horário final da extra será às 07:00 do próximo dia útil. |
  | **RI-002** | **Campos Já existentes no sistema.**     **Horário Extra no Sábado a partir de:** Este campo deve ser informado para que o sistema comece a contar o horário de extras somente a partir do horário informado até o horário final que é definido no campo horário extra final.   Horário Extra no Sábado a partir das **19:00**.   Com base no horário final o sistema entenderá a que a extra começará domingo as 19:00 e terá seu termino às 07:00 de Domingo.       **Campo Percentual de acréscimo Horário Extra**     **Se Horário Extra** de algum dos dias estiverem preenchidos e os parâmetros de percentual de acréscimo estiverem em branco, o sistema deverá considerar o **Percentual de acréscimo Horário Extra** como base para o cálculo dos valores extras. |
  |  |  |

  # \_Toc355276667Fluxo do Processo

  # Dicionário de Dados

  Não necessário para o desenvolvimento deste requisito.   

  # Grupo de Perguntas

  Não necessário para o desenvolvimento deste requisito.

  # **Consulta Padrão**

  Não necessário para o desenvolvimento deste requisito.

  # Estrutura de Menu

  Não necessário para o desenvolvimento deste requisito.
