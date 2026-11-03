---
article_id: 360004103232
category: RH - Fechamentos
content_hash: 8087ae4ea36e38af2877fe82672f2a9779d2d35925b169d6a72fc171eca5cafd
fetched_at: '2026-06-28T22:44:48.872477+00:00'
product: protheus
section_id: 32419231682455
source: central-protheus
title: RH - Linha Protheus - PON - Como efetuar o Fechamento Mensal do Ponto
type: support-article
updated_at: '2026-06-17T19:03:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004103232-RH-Linha-Protheus-PON-Como-efetuar-o-Fechamento-Mensal-do-Ponto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38351518364311) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como efetuar o Fechamento Mensal do Ponto?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**

**1.** Acesse o **Módulo 16 (SIGAPON),** utilize a data base para acesso ao sistema igual ao **último dia do período que deseja efetuar o fechamento mensal,** após isso acesse o caminho **Miscelânea> Fechamentos> Mensal.**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36131022419095)**  
  
  
**Importante:** É recomendado que efetue backup das tabelas da listagem abaixo, antes da execução do fechamento mensal. Para esta tarefa se tem por necessário o envolvimento do administrador do ambiente em sua TI local.  
  
  
**2.** Confira se o período está correto:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36131022423959)  
  
  
**3.** Caso necessário, é possível filtrar a filial a ser efetuado o fechamento do período:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36131022426519)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36131022430103)  
  
  
**4.** Após o processamento, o sistema apresentará um ***log*** **de ocorrências** informando os **colaboradores processados** **e período do fechamento** e se existir alguma inconsistência, essa será apresentada no ***log.***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36131022431895)  
  
  
**5.** Ao consultar a rotina de Períodos de Apontamentos em **Atualizações> Cadastro do Ponto> Períodos de Apontamentos o periodo que foi fechado poderá visualizar na tele incial na rotina conforme abaixo:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/40108516575127)**  
  
E ao consultar os parâmetros automaticamente foi ajustado para o próximo período ativo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40108516577815)

Para visualizar as movimentações após o fechamento do período acesse **Atualizações>Acumulados** e selecione a opção desejada (Marcações, Apontamentos, Refeições ou Resultados).  
  
  
**Importante:** A rotina de **Fechamento Mensal** faz com que todos os dados tratados de um período, sejam transferidos para tabelas de Acumulado, assim o usuário não possuirá mais acesso para realizar qualquer tipo de alteração, preservando a integridade dos dados. Por este motivo, recomemos que seja efetuado o backup de todas as tabelas envolvidas no processo, caso o fechamento mensal tenha sido efetuado incorretamente ou seja necessário retomar ao período processado no fechamento, podendo assim, retornar os backups destas tabelas envolvidas, para ajuste no período do apontamento.  
  
[RH - Linha Protheus - PON - Migração de dados no Fechamento Mensal do Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013084192-RH-Linha-Protheus-PON-Migra%C3%A7%C3%A3o-de-dados-no-Fechamento-Mensal-do-Ponto)  
- Refeições (SP5 para SPN)  
- Marcações (SP8 para SPG)  
- Apontamentos (SPC para SPH)  
- Resultados (SPB para SPL)  
- Pré Leitura (RFE para RFH)  
- Pré ACJEF (RFF para RFG)  
  
Após o fechamento, automaticamente o sistema:  
- Faz a abertura do [**Período de Apontamento**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290) subsequente, alterando o conteúdo dos parâmetros **MV\_PAPONTA e MV\_PONMES;**  
- Inclui o registro do período fechado na tabela **SPO (**Período de apontamento);  
- Cria o registro de Troca de [**Turno do funcionário**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671) com o primeiro dia do novo período.  
  
  
  
**Saiba mais :**

[MP - PON - O que verificar quando na execução do Fechamento Mensal, apresentar log de marcações ímpares](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012927531-MP-PON-O-que-verificar-quando-na-execu%C3%A7%C3%A3o-do-Fechamento-Mensal-apresentar-log-de-marca%C3%A7%C3%B5es-%C3%ADmpares?source=search)

[MP - PON - Após o fechamento mensal, o sistema não alterou o período de apontamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012922731-MP-PON-Ap%C3%B3s-o-fechamento-mensal-o-sistema-n%C3%A3o-alterou-o-per%C3%ADodo-de-apontamento?source=search)
