---
article_id: 360051734873
category: RH - Ponto Eletrônico
content_hash: 04f8ccc79a77217d3bcc8111a4ae28d45dff3055a52cfa7c885b353fabfde1c7
fetched_at: '2026-06-28T22:44:58.251837+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Turno 12x36 aponta Horas Extras e Faltas indevidas
type: support-article
updated_at: '2026-02-05T19:00:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051734873-RH-Linha-Protheus-PON-Turno-12x36-aponta-Horas-Extras-e-Faltas-indevidas
---

**Dúvida**  
Turno 12x36 está em **sequência incorreta**, trazendo **apontamentos errados de faltas e horas extras**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
O Turno com escala **12x36**, indica que o funcionário deverá **trabalhar um dia** e **descansar no dia seguinte.**  
Para isso, além de existir um cadastro correto do **Turno** e T**abela de Horário Padrão**, o **calendário mensal** deverá ser montado de forma correta.  
  
Para isso, é necessário validar inicialmente qual é o **Período de Apontamento** que está trabalhando atualmente. Para esta consulta, é necessário acessar a rotina **PONA290: Atualizações> Cadastro do Ponto> Período de Apontamento**, clicar em **Modificar Período de Apontamento>Apenas Visualizar>Salvar:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16484232231063)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38196899153431)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38196899154839)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16484365966103)  
  
Após identificar qual o **Período de Apontamento**, é necessário verificar se existe registro de [**Troca de Turno**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671-RH-Linha-Protheus-PON-Como-funciona-a-Troca-de-Turno-dos-funcion%C3%A1rios) para o funcionário.   
Para a correta [**montagem do calendário**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016361412-RH-Linha-Protheus-PON-Passos-a-verificar-na-montagem-do-calend%C3%A1rio-de-marca%C3%A7%C3%B5es), é **obrigatório** que exista minimamente um registro com o primeiro dia do período. A rotina pode é localizada **Atualizações> Cadastro de Funcionário> Troca de Turno:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16484424822679)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16484500762007)  
  
É necessário também validar se a **Sequência** indicada na **Troca de Turno** a partir do primeiro dia do período está correta. Se for preciso é necessário efetuar a conferência do cadastro da [**Tabela de Horário Padrão**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o) em **Atualizações> Cadastro do Ponto> Tabela de Horário Padrão:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16484584603799)  
Se necessário, deve-se corrigir o conteúdo do campo **Seq. Para.**  
  
**\*\*Importante ressaltar:** o sistema **altera** as **Sequências** automaticamente todas as **Segundas-Feiras do período**, ou seja, se o funcionário iniciou o período (dia 01.07 - Sábado) na Sequência 01, na próxima Segunda-Feira (dia 03.07) será alterado para a Sequência 02 e assim sucessivamente.  
  
Como exemplo, temos um **Turno** com **duas sequências** na **Tabela de Horário Padrão**. O cadastro está desta forma:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16484684238999)  
  
No dia 01.07 o funcionário **trabalhou** e **não** deve receber **Horas Extras**, porém, o sistema classificou como **DSR**, ou seja, está montando o **calendário** deste dia considerando a **Sequência 01** e gerando **Horas Extras**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16484821979287)  
  
Porém, se for necessário que este dia seja classificado como **Trabalhado** e o restante do período seja alterado, é necessário então ajustar a **Troca de Turno**, alterando para a **Sequência 02:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16484883240215)  
  
Retornando na rotina de **Integrados**, o sistema ajustou o **calendário do período**, e agora o dia 01.07 está sendo classificado como **Trabalhado**, ou seja, validando a **Sequência 02** da **Tabela de Horário Padrão:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16485066365591)  
  
  
  
**Saiba Mais:**  
[Manual Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote Acumulado RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)
