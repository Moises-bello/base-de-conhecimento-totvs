---
article_id: 21005984545175
category: BI - Business- Intelligence - Workflow
content_hash: 7130850eef9020abb45ebe750f00d4ac40393c346cc00bb9c39c8919869b61b9
fetched_at: '2026-06-28T22:37:03.136705+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Scheduler do Workflow
type: support-article
updated_at: '2024-01-31T17:11:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21005984545175-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Scheduler-do-Workflow
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21005921277975) Tempo aproximado para leitura: **02:00 min** **Dúvida**Como configurar e ativar o Scheduler do Workflow?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – BI - Workflow - Todas as versões.  
  
**Solução**Como o Workflow é uma ferramenta embutida dentro do Protheus, bastam algumas configurações no AppServer.ini para ativá-lo. Inicialmente, devemos colocar na seção "**ONSTART**" deste arquivo de configurações a Função "**WFONSTART**", para iniciar o agendamento das funções para o Workflow.  
Esta função inicia um Job que ficar verificando se existem agendamentos a serem executados.  
Acrescente no AppServer.ini as seguintes linhas:  
  
[ONSTART]  
jobs=SchedulerWF  
  
[SchedulerWF]  
Main=WFONSTART  
Environment=EnvTop11    *<- Coloque aqui o seu Environment (ambiente)*nParms=4Parm1=99                         <- *Indica o código da empresa onde será iniciado o Job*Parm2=01                         <- *Indica o código da Filial onde será iniciado o Job*parm3=EnvTop11             <- *Nome do Environment (ambiente) onde será iniciado o Job*parm4=T                           <- *Indica se inicia ou não os processos parados automaticamente***Dica**: Deixe o "**parm4**" como "**T**"  
  
As linhas acima indicam que sempre que o servidor do Protheus for iniciado, ele irá executar as funções contidas em cada Job.  
 **Saiba mais:**  
[WF0006\_Configurando\_e\_ativando\_o\_Scheduler\_do\_Workflow](https://tdn.totvs.com/display/PROT/WF0006_Configurando_e_ativando_o_Scheduler_do_Workflow)  
[WF0001\_Configuração\_do\_AppServer.ini para WF via Link](https://tdn.totvs.com/pages/viewpage.action?pageId=225268728)  
[Workflow](https://tdn.totvs.com/display/PROT/FAQs+-+Workflow)
