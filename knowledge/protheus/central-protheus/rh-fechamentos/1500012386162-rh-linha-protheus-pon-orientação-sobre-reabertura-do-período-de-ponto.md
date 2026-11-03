---
article_id: 1500012386162
category: RH - Fechamentos
content_hash: 43f1f1ca16406b40742f475a3c12dffc18a042a0c213bce7bef07911159791d1
fetched_at: '2026-06-28T22:44:48.922231+00:00'
product: protheus
section_id: 32419231682455
source: central-protheus
title: RH - Linha Protheus - PON - Orientação sobre Reabertura do Período de Ponto
type: support-article
updated_at: '2026-04-29T19:50:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012386162-RH-Linha-Protheus-PON-Orienta%C3%A7%C3%A3o-sobre-Reabertura-do-Per%C3%ADodo-de-Ponto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35601239502999) Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
É possível realizar a reabertura de um período já fechado no modulo do Ponto Eletrônico?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões.  
  
**Solução**  
O Fechamento Mensal do Ponto, executado pela rotina PONM090 é irreversível, ou seja, uma vez que ele é executado, não possuímos por padrão um rollback do processo, para isso é necessário efetuar o processo de reabertura conforme abaixo.  
  
O processo de reabertura envolve várias tabelas que são utilizadas no fechamento, sendo assim, a execução incorreta desse processo, pode prejudicar a integridade de todos os dados.  
  
Se for necessário realmente **reabrir o Ponto**, a orientação é **retornar um*****backup*****das tabelas** do ponto (abaixo procedimento para saber quais são), **anteriores ao fechamento** em uma **base de testes** e ir trabalhando paralelamente para os ajustes, para depois ser feito em produção.  
  
Caso não exista profissional de TI habilitado na empresa, indicamos o agendamento de um analista *in loco*, afim de fazer esse procedimento.   
*\*\*O suporte do Módulo de ponto Eetrônico não auxilia nesse processo*  
  
Para consultar quais são as tabelas do módulo SIGAPON, faça a consulta abaixo:

* Abra o Dicionário - **SX2**
* Faça um filtro por: **X2\_MODULO "Igual a" 16** (Módulo 16 = SIGAPON)
* Além destas tabelas, deve ajustar o **MV\_PONMES e MV\_PAPONTA** para o período que será reaberto

**Importante:**  
Atenção com todos lançamentos já integrados e muitas vezes já pagos aos funcionários.  
É recomendado criar um *backup* destas tabelas do módulo, além do *backup* completo

**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
