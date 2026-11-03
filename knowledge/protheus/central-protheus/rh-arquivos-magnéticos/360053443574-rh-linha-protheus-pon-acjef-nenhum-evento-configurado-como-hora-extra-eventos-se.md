---
article_id: 360053443574
category: RH - Arquivos Magnéticos
content_hash: 981fbee2104b6dbd2984e3025fe99013a043b278256812275d566e15245f1045
fetched_at: '2026-06-28T22:44:55.260522+00:00'
product: protheus
section_id: 32302371669783
source: central-protheus
title: RH - Linha Protheus - PON - ACJEF Nenhum evento configurado como Hora Extra
  (eventos sem classificação)
type: support-article
updated_at: '2025-06-13T18:42:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053443574-RH-Linha-Protheus-PON-ACJEF-Nenhum-evento-configurado-como-Hora-Extra-eventos-sem-classifica%C3%A7%C3%A3o
---

**Dúvida**ACJEF Nenhum evento configurado como Hora Extra (eventos sem classificação)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Este *log* se refere a duas rotinas... Cadastros dos Eventos e Cadastro dos Tipos de Horas Extras.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089198174/mceclip0.png)  
  
No cadastro dos eventos, deverá ser verificado duas parametrizações.  
A primeira é que todos os ids de ponto (até o 043A) devem estar cadastrados na base, mesmo que não utilizem e, todos eles com classificação.   
A segunda e mais importante, se refere ao campo Classificação.  
  
Temos tipos de classificação para os eventos.  
01 = Hora Extra;   
02 = Falta;   
03 = Atraso;   
04= Saída no Expediente;  
05 = Saída Antecipada;   
ZZ = Outros.  
  
Todos os eventos de Hora Extra devem ser classificados como 01, assim como todos os eventos de falta devem ser classificados como 02 e assim por diante. Outros eventos que não estão nessa lista acima, devem ser classificados como ZZ.  
  
Na rotina Tipos de Horas Extras, devemos ter os oito primeiros tipos cadastrados (4 diurnas e 4 noturnas) com eventos diferentes entre elas, todos estes eventos devem obrigatoriamente, estar classificados como Hora Extra.  
  
Lembrando que, essa configuração é para todas as filiais se, utilizarem a SP4 (tabela de tipos de Horas Extras), SP9 (tabela de eventos) e a SX5 (genéricos) onde a tabela 20 na SX5 refere-se aos id's de ponto.  
É recomendado que, essas três tabelas tenham o mesmo compartilhamento.
