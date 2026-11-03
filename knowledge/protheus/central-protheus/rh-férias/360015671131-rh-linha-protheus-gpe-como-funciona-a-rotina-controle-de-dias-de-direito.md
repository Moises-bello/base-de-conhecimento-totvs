---
article_id: 360015671131
category: RH - Férias
content_hash: 162dd3837a0682ef9bbcf858da1c8053872f3aa36253e9030812286a68a47c5e
fetched_at: '2026-06-28T22:43:58.134472+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como Funciona a rotina Controle de Dias de Direito
type: support-article
updated_at: '2025-08-20T17:10:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015671131-RH-Linha-Protheus-GPE-Como-Funciona-a-rotina-Controle-de-Dias-de-Direito
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31766783146135) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como Funciona a rotina Controle Dias de Direito?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A rotina de **Programação de Férias** passou a se chamar **Controle de Dias de Direito** na versão 12, porém, os registros continuam a ser gravados na tabela **SRF** (Programação de Férias).   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31766822843927)

As principais diferenças entre elas, são:  
**>** Demonstra **histórico de períodos aquisitivos** anteriores da matrícula em questão;  
**>** Possibilita a **visualização e geração** de **mais de um período em aberto**;  
**>** Facilita a **consulta de períodos** pelos usuários e participantes via portal;  
**>** **Atualização automática** de informações no **fechamento das Férias e Folha**, contemplando inclusive os afastamentos com perda de períodos e alteração do período aquisitivo.   
  
Ao realizar o **Fechamento** **GPEM120**, todo o **Controle de Dias de Direito é atualizado** **automaticamente,** não sendo necessário cadastrá-los manualmente.  
  
Informações sobre os principais campos:  
**> Qtd. Ref. Per** **(RF\_DIASDIR):** Quantidade de dias de direito, geralmente esse campo fica com o conteúdo 30, mas [pode ser menor em decorrência de Férias Coletivas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018992811-RH-Linha-Protheus-GPE-Como-o-sistema-altera-o-Per%C3%ADodo-Aquisitivo-do-Funcion%C3%A1rio-ap%C3%B3s-c%C3%A1lculo-de-F%C3%A9rias-Coletivas), quando o Funcionário possui menos de um ano.  
**> Dias.F.Venc** (**RF\_DFERVAT)****:** Número de dias de Férias vencidas aos quais o Funcionário tem direito, de acordo com seu período aquisitivo e sua data base de Férias. Esse campo é preenchido com conteúdo 30 quando o Funcionário completa o período aquisitivo, mas [pode ser menor em decorrência de Férias Coletivas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018992811-RH-Linha-Protheus-GPE-Como-o-sistema-altera-o-Per%C3%ADodo-Aquisitivo-do-Funcion%C3%A1rio-ap%C3%B3s-c%C3%A1lculo-de-F%C3%A9rias-Coletivas), quando o Funcionário possui menos de um ano.  
**> D.Fer.Prop (RF\_DFERAAT):** Dias de Férias proporcionais, este campo é atualizado a cada fechamento do período e quando completado 30 dias de direito, o campo é zerado a partir do momento que aquele período aquisitivo é completado (o valor 30 é preenchido no campo Dias.F.Venc)  
**> Dias pagos (RF\_DFERANT):** Dias de Férias que já foram pagas.   
**> Situação (RF\_STATUS)**: Status do Período de Férias, sendo 1=Ativo (quando ainda restam férias a serem gozadas), 2=Prescrito (Em decorrência de faltas ou afastamentos, como por exemplo, auxilio doença) e 3=Pago (quando todo o período foi quitado).  
  
  
**Saiba Mais:**[RH - Linha Protheus - GPE - Relatório de dias de direito Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8206149113623-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-dias-de-direito-F%C3%A9rias)  
[RH - Linha Protheus - GPE - Ordem Padrão dos campos da Tabela SRF - Controle dias de Direito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061815274-RH-Linha-Protheus-GPE-Ordem-Padr%C3%A3o-dos-campos-da-Tabela-SRF-Controle-dias-de-Direito)  
[RH - Linha Protheus - GPE - Atualização dos Períodos Aquisitivos Quando há Afastamento sem Data de Retorno](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16110041641623-RH-Linha-Protheus-GPE-Atualiza%C3%A7%C3%A3o-dos-Per%C3%ADodos-Aquisitivos-Quando-h%C3%A1-Afastamento-sem-Data-de-Retorno)
