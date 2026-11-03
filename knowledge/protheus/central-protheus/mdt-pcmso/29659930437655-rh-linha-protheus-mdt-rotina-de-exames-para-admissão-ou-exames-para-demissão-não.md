---
article_id: 29659930437655
category: MDT - PCMSO
content_hash: 35c20153349adf214c29adbea57e4d7cd0252c723a8b28b7b34cb2bc45b5d8ce
fetched_at: '2026-06-28T22:44:28.556994+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Rotina de Exames para Admissão ou Exames para Demissão
  não carrega os exames relacionados na rotina Exames por Função
type: support-article
updated_at: '2025-09-03T14:27:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29659930437655-RH-Linha-Protheus-MDT-Rotina-de-Exames-para-Admiss%C3%A3o-ou-Exames-para-Demiss%C3%A3o-n%C3%A3o-carrega-os-exames-relacionados-na-rotina-Exames-por-Fun%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29659930401815) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Porque na Rotina de **Exames para Admissão** ou **Exames para Demissão** não carrega os exames relacionados na rotina Exames por Função?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Atualmente, o funcionamento é o seguinte: para que um exame seja exibido na rotina 'Exames para Admissão' ou 'Exames para Demissão', é necessário que, na rotina 'Exames', o campo que indica se é admissional ou demissional esteja marcado como '**SIM**'.  
  
Foi avaliado internamente que as rotinas não estavam funcionando conforme seu proposito, portanto foram realizados ajustes nos filtros por meio da issue [DNGRHUMDT-33.](https://tdn.totvs.com/pages/releaseview.action?pageId=867805806)  
Vale ressaltar que a rotina de exames por função possui uma finalidade diferente da rotina de exame  
para admissão e exames para demissão.  
  
A rotina de exames para admissão será alimentada somente quando, no cadastro do exame, o campo '**Exame Admissional**' estiver marcado como '**SIM**', sendo possível incluir exames manualmente. Essas rotinas são facilitadoras, mas sempre haverá casos específicos que não se encaixam perfeitamente, exigindo pequenos ajustes no cadastro. Por isso, a rotina de exames para admissão permite desmarcar exames quando necessário.   
  
O mesmo padrão segue na apresentação dos exames para demissão o campo '**Exame Demissional**' estiver marcado como '**SIM**'.

Já a rotina '**Exames por Função**', serve como um de facilitadores no controle e amarrações dos exames periódicos, tendo a finalidade de gerar os exames na rotina '**Exames do Funcionário**' quando a programação é realizada na rotina '**Gerar Programação**'.   
Consulte nossas documentações de Apoio:  
  
[RH - Linha Protheus - MDT - Como cadastrar e definir os exames que serão apresentado no PCMSO (Programa de Controle Médico de Saúde Ocupacional)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059540413-RH-Linha-Protheus-MDT-Como-cadastrar-e-definir-os-exames-que-ser%C3%A3o-apresentado-no-PCMSO-Programa-de-Controle-M%C3%A9dico-de-Sa%C3%BAde-Ocupacional)  
[RH - Linha Protheus - MDT - Exames por Função (MDTA450)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057694314-RH-Linha-Protheus-MDT-Exames-por-Fun%C3%A7%C3%A3o-MDTA450)

Se necessário, a rotina possui o ponto de entrada [MDT2751 - Exames para Admissão](http://tdn.totvs.com/pages/releaseview.action?pageId=6079896)

**Saiba Mais**[Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
