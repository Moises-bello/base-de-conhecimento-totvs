---
article_id: 360028979231
category: RH - Funcionários
content_hash: c34aceca75e6a560d994a2ce200509939e5790eaa18c53c0ffab8ccd17a0e9b3
fetched_at: '2026-06-28T22:43:27.713643+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Configuração para Matrícula automática de funcionários
type: support-article
updated_at: '2025-09-17T20:52:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028979231-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-para-Matr%C3%ADcula-autom%C3%A1tica-de-funcion%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34901006718615) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Configuração para **Matrícula automática de funcionários.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para solucionar essa dúvida, siga os seguintes passos:  
  
1 - **MV\_MATRICU,** configure com **1 (Por Filial)** ou **2 (Por Empresa)**. Neste exemplo utilizaremos como **1, para que o sistema traga automático por Filial;**Para mais informações sobre o MV\_MATRICU acesse: [Parâmetro MV\_MATRICU](https://tdn.totvs.com/pages/viewpage.action?pageId=847572323)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029795811)

2 - Deixe o campo **RA\_MAT** **sem validação** no Campo **Inic. Padrão** através do configurador**;**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029795851)  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029796651)

3 - Para gerar a próxima matrícula, o sistema verifica a **SRA**, o **Controle de Numeração (APCFG110)** e **adiciona +1**. Por exemplo, a **última matrícula da SRA** no exemplo abaixo, da filial **D MG 01 é 200775**. Ao incluir um novo funcionário, o sistema trará a **próxima matrícula que é 200776 conforme consta no controle de numeração no configurador.**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029795931)  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029796011)

**Observação: Se por algum motivo, o sistema não trouxer a matrícula correta, existe a rotina APCFG110 (Controle de Numeração), que dá a possibilidade de ajuste de onde iniciará a matrícula. Há casos em que é alterado o uso do parâmetro de numeração automática, que pode ocasionar essa ‘’perda’’ de sequência, por isso, sempre orientamos a manter um padrão, onde ou o usuário sempre informará a matrícula manualmente ou o sistema sempre trará de forma automática.**

4 - Caso haja este incidente de trazer a matrícula incorreta, **entre na rotina APCFG110 no configurador**, ao abrir a rotina, **na parte inferior**, informe qual é a **próxima matrícula que será usada**, e na **parte superior**, a **sequência desta próxima matrícula,** como no exemplo abaixo;  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029796051)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029806192)

Mais informações da rotina **APCFG110**: [Numeração automática pelo License Server](https://tdn.totvs.com/pages/releaseview.action?pageId=309411140)  
  
**Saiba Mais**[MP - FRAME - Acerto de Numeração Automática](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026703731-MP-FRAME-Acerto-de-Numera%C3%A7%C3%A3o-Autom%C3%A1tica?source=search)  
[RH - Linha Protheus - GPE - Configuração para Matrícula Automática Autônomos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028663892-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-para-Matr%C3%ADcula-Autom%C3%A1tica-Aut%C3%B4nomos?source=search)  
[RH - Linha Protheus - GPE - Parâmetros envolvidos no processo de Configuração para Matrícula automática](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406900205975-RH-Linha-Protheus-GPE-Par%C3%A2metros-envolvidos-no-processo-de-Configura%C3%A7%C3%A3o-para-Matr%C3%ADcula-autom%C3%A1tica?source=search)  
[RH - Linha Protheus - GPE - Sistema pula numeração de matrícula quando cancelada inclusão de funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052983333-RH-Linha-Protheus-GPE-Sistema-pula-numera%C3%A7%C3%A3o-de-matr%C3%ADcula-quando-cancelada-inclus%C3%A3o-de-funcion%C3%A1rio?source=search)
