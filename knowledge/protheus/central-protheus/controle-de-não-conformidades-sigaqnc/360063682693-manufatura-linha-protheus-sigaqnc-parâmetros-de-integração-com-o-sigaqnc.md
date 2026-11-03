---
article_id: 360063682693
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 3a5ef318f9541cb34a415500a9b425b276c6c23bb989ebd6d325dba6a7f3e3d4
fetched_at: '2026-06-28T22:42:28.017138+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Parâmetros de integração com o SIGAQNC
type: support-article
updated_at: '2025-03-10T20:45:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063682693-Manufatura-Linha-Protheus-SIGAQNC-Par%C3%A2metros-de-integra%C3%A7%C3%A3o-com-o-SIGAQNC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30545087338903)**Tempo aproximado para leitura: **00:02:40 min**  
**Dúvida**Quais os parâmetros necessários para integração com o módulo **SIGAQNC - Controle de Não Conformidades**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Solução**O módulo **SIGAQNC** possui integração com os módulos **SIGAQIE - Inspeção de Entradas**, **SIGAQIP - Inspeção de Processos**, **SIGAQMT - Metrologia** e **Call Center.**Para que haja integração com os módulos **SIGAQIE**, **SIGAQMT**e **Call Center**, o parâmetro **MV\_QINTQNC - Define se as não-conformidades serão enviadas para tratamento no SIGAQNC (Não-conformidades)**, deve estar igual a **S - Sim**.  
E para que haja a integração com o **SIGAQIP** o parâmetro **MV\_QIPQNC - Define se haverá integração entre os ambientes de Controle de Não-conformidade e Inspeção de Processos (1=SIM / 2=NAO)**, deve estar igual a **1 - Sim.**  
  
Além dos parâmetros citados acima, os demais parâmetros devem ser validados para a correta integração destes módulos com o **SIGAQNC**:

* **MV\_QNCFORI - Define o código da Filial do Departamento origem da Ficha de N.C. gerada através da Integração com o ambiente de Não-****Conformidades**: filial de origem da **FNC - Ficha de Não Conformidade**.
* **MV\_QNCDORI -  Define o código do Departamento origem das Fichas de N.C. geradas através da Integração com o ambiente de Controle de Não-Conformidades**: código do departamento/centro de custo de origem da **FNC**.
* **MV\_QNCFDES - Define o código da Filial do Departamento Destino das Fichas de N.C. geradas através da Integração com o ambiente de Controle de Não-Conformidades**: filial destino da **FNC**.
* **MV\_QNCDDES - Define o código do Departamento Destinatário das Fichas de N.C. geradas através da Integração com o ambiente de Controle de Não-Conformidades**: código do departamento/centro de custo destino da **FNC**.
* **MV\_QNCFRES - Define o código da Filial do Usuário Responsável pela Ficha de N.C. gerada através da Integração com o ambiente de Controle de Não-Conformidades**: filial do usuário responsável pela **FNC**.
* **MV\_QNCMRES -Define na Integração com QNC a Matrícula do Responsável da FNC**: código/matrícula do usuário responsável pela **FNC**.
* **MV\_QNCFDIG - Define o código da Filial do Usuário Digitador das Fichas de N.C. geradas através da Integração com o ambiente de Controle de Não-Conformidades**: filial do usuário digitador/originador da **FNC**.
* **MV\_QNCMDIG - Define o código do Usuário Digitador da Ficha de N.C. gerada através da Integração com o ambiente de Controle de Não-Conformidades**: matrícula do usuário digitador/originador da **FNC**.
* **MV\_QNCDDIG - Define na Integração com QNC o Departamento do Digitador da FNC**: código do departamento/centro de custo do usuário digitador da **FNC**.

**Observação**  
O conteúdo dos parâmetros de integração é **único e individual**, ou seja, **não pode haver mais de uma filial, departamento ou usuários indicados nos parâmetros**.
