---
article_id: 40910300698903
category: TAF - REINF
content_hash: 4e5ae8665432d3a1ce734c5417f65e49aca627d312533fb081e2a8f1cf728bce
fetched_at: '2026-06-28T22:41:33.478623+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - Como configurar o TSI (TAF Service
  Integration) via Smartschedule?
type: support-article
updated_at: '2026-06-15T12:23:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40910300698903-Cross-Segmentos-Backoffice-Protheus-TAF-Como-configurar-o-TSI-TAF-Service-Integration-via-Smartschedule
---

**Dúvida**  
Como configurar o novo serviço de integração TSI?  
  
**Ambiente**  
TAF – A partir da versão 12.1.27  
  
**Solução**

    O TSI é uma solução de integração entre o Fiscal e o TAF, para ambientes que utilizam exclusivamente o TAF como módulo do Protheus, onde substitui o processo das rotinas Extrator Fiscal (EXTFISXTAF) e Processamentos (TAFAINTEG).

A integração On-line depende do novo campo **S\_T\_A\_M\_P\_** e sua criação está disponível para os Banco de Dados MSSQL, ORACLE e POSTGRES.

Para mais detalhes sobre o campo: [Implementação - Campo de controle adicional no DBAccess - S\_T\_A\_M\_P\_](https://tdn.totvs.com/pages/viewpage.action?pageId=515681471)

**Este campo será criado apenas para as tabelas do lado do ERP-Protheus.**

    Após o término de todo o processo de configuração, as tabelas que terão a criação do campo são:

SB1, SFT, SF4, SB5, SA1, SA2, SA4, SAH, CT1, F2Q, CDN, SE1, SE2, CCF, SF1, SF2, SF3, CCE, SYD, CDH, SON, CKX, CDT e CDG.

O controle de integração confrontará o campo **S\_T\_A\_M\_P\_** (*com underline ERP-Protheus*) com o campo **STAMP** (*sem underline TAF*).

A base de dados deve conter os campos C1G\_STAMP, C1H\_STAMP, C1J\_STAMP, C1L\_STAMP, C1N\_STAMP, C1O\_STAMP, NYS\_TSTAMP, C20\_STAMP, LEM\_STAMP, V5R\_STAMP, C3Q\_STAMP, C0A\_STAMP, C2S\_STAMP, C3J\_STAMP, T9C\_STAMP e C5M\_STAMP.

Os campos serão criados via UPDDISTR com a atualização abaixo:

[TAF - REINF - Atualização Completa Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026673572-TAF-REINF-Atualiza%C3%A7%C3%A3o-Completa-Reinf?source=search)

**1 -** **Wizard de Configuração do TAF**

    Para fazer uso desse modelo de integração, você deverá acessar a **Wizard de Configuração do TAF** e marcar essa opção, ao final da execução aparecendo a mensagem de sucesso para criação do campo " **S\_T\_A\_M\_P\_**", seu ambiente já estará preparado para a configuração do schedule da integração.

![TSI.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40910300675991)

**2 - Configurar Schedule**

    O job TSI responsável por executar o serviço de integração ERP x TAF, deve ser configurado em SIGACFG com a opção sempre ativo.

Desta maneira, ao incluir ou alterar um novo cadastro / movimentação no ERP, o JOB se encarregará de executar a integração automaticamente de forma transparente ao usuário.

Controle feito através da comparação dos campos do ERP-Protheus **S\_T\_A\_M\_P\_** *Vs* **XXX\_STAMP** do TAF.

**Configuração do Agendamento**

    O novo cadastro de agendamentos consiste em três etapas:  
        1. Agendamento  
        2. Parametrização  
        3. Concluir

Na etapa do agendamento  possui algumas opções de  periodicidade:

**Diária**

**Opção Frequência:** Se marcada como sim, deve-se informar uma frequência de execução por horas ou minutos, sendo que deve haver uma horário inicial e final para essa execução. Se marcada como não, deve-se apenas informar um único horário para a execução do agendamento.

**Opção Recorrente:** Se marcada como sim, considera os parâmetros de frequência para a execução. Se marcada como não, considera apenas os parâmetros de primeira execução.

**Mensal**

**Opção Frequência:** Se marcada como sim, deve-se informar uma frequência de execução por dias, horas ou minutos, sendo que deve haver uma horário inicial e final e dia inicial e final. Se marcada como não, deve-se informar apenas o dia e horário para a execução.

**Opção Recorrente:** Se marcada como sim, considera os parâmetros de frequência para a execução. Se marcada como não, considera apenas os parâmetros de primeira execução.

**Semanal**

**Opção Frequência:** Se marcada como sim, deve-se informar uma frequência de execução por horas ou minutos, sendo que deve haver uma horário inicial e final. Se marcada como não, deve-se apenas informar um único horário. Para as duas opções, devem ser informados os dias da semana para a execução.

**Opção Recorrente:** Se marcada como sim, considera os parâmetros de frequência para a execução. Se marcada como não, considera apenas os parâmetros de primeira execução.

**Única**

Irá executar apenas no dia e hora informados nos campos Dia e Horário.

Exemplo:

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40910300677143)![Screenshot_4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40910276217623)

**Concluir**

    A etapa Concluir é a final antes de incluir ou atualizar o agendamento e disponibiliza um resumo da periodicidade do agendamento.

![Screenshot_5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40910276222103)

Para que o TSI seja operacional, é necessário realizar a execução do **Smart Schedule**. Optando pela execução do **Smart Scheduler**, a execução do agente TSI não será necessária.

Ao selecionar a execução do **Smart Scheduler**, o sistema indica que será necessário reiniciar os serviços do **appserver**.

![Screenshot_6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40910300684183)

Após reiniciar os serviços, o **Smart Schedule** para o TSI será executado automaticamente.

![Screenshot_7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40910276229399)

**IMPORTANTE:** Quando configurado o TSI, deve ser avaliado a utilização do extrator fiscal para que não haja duplicidade nos documentos.

Para mais detalhes da configuração, **log de integração** e **erros de integração**, consulte:

[TSI - TAF Service Integration](https://tdn.totvs.com/display/public/TAF/TSI+-+TAF+Service+Integration)

[TAF0185 - Tamanho do campo e decimal com impacto na integração](https://tdn.totvs.com/pages/releaseview.action?pageId=1072719964)
