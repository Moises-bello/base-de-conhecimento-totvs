---
article_id: 360052399693
category: RH - Arquivos Magnéticos
content_hash: 19caa85f2f2ffe777d2c5e639444734bca866c6d079664f3cb6908fd78527715
fetched_at: '2026-06-28T22:44:55.246254+00:00'
product: protheus
section_id: 32302371669783
source: central-protheus
title: RH - Linha Protheus - PON - ACJEF Empresa sem Apontamentos
type: support-article
updated_at: '2025-06-13T18:42:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052399693-RH-Linha-Protheus-PON-ACJEF-Empresa-sem-Apontamentos
---

**Ocorrência**No módulo Ponto Eletrônico, ao gerar o arquivo fiscal ACJEF (Arquivo de Controle de Jornada para Efeitos Fiscais), o Sistema traz o *log* de ocorrência: Empresa sem Apontamentos  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**Este erro está relacionado à montagem de calendário nos períodos de apontamento, é necessário termos todos os períodos de apontamento anteriores fechados pelo Sistema e nunca pelo usuário. Com isso, irá ser criado linhas de troca de turno para todos os períodos de apontamento a todos os funcionários.  
O erro da não impressão do ACJEF é por causa dos fechamentos mensais não executados por muitas vezes, há meses, anos, ou até desde a implantação do Ponto Eletrônico na Empresa.  
  
**Solução**Temos uma documentação explicada de como deverá ser tratado este caso da falta do fechamento.  
Retroagir a data base do Protheus até o último dia do primeiro período de apontamento que irão fechar, alterar o MV\_PAPONTA e MV\_PONMES para este período, deletar da SPO a linha referente a esse período   
  
Em suma, realizar o fechamento correto de todos os períodos de apontamento em seu ambiente, assim todos os períodos ficarão com o campo PO\_RESPONS na tabela SPO como S, ou seja, fechados pelo Sistema.  
  
Veja mais em:  
[MP - PON - Como realizar o fechamento dos períodos anteriores de ponto ainda em aberto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052125273-MP-PON-Como-realizar-o-fechamento-dos-per%C3%ADodos-anteriores-de-ponto-ainda-em-aberto?source=search)  
  
Após realizar todos os fechamentos, deixando aberto somente os períodos que ainda estão tratando ultimamente, o ACJEF deverá ser gerado e impresso, pois as linhas de trocas de turno para todos os funcionários serão criadas e o calendário dos períodos estará correto.  
  
**Importante**  
No Sistema, existem dois parâmetros para controlar o período aberto de apontamento:  
MV\_PAPONTA - deve ser preenchido com o dia inicial / dia final daquele período que irão realizar o fechamento, exemplo 21/20, 11/10, 01/31, 26/25 ....  
MV\_PONMES - deve ser preenchido com o período completo de apontamento que está aberto.
