---
article_id: 360017683991
category: RH - Folha de Pagamento
content_hash: a3d606439fdc986ecd791dd2bfa95dda4396525ad2e0d67d0a47c96f04947bd8
fetched_at: '2026-06-28T22:44:14.932793+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - É possível reabrir um período/ e ou roteiro de
  cálculo
type: support-article
updated_at: '2026-04-24T12:43:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017683991-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-reabrir-um-per%C3%ADodo-e-ou-roteiro-de-c%C3%A1lculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21181705005719)  Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**  
 É possível reabrir um período/ e ou roteiro de cálculo?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Se for necessário **reabrir** a folha, a orientação é **retornar** um ***backup*** das tabelas da folha (abaixo procedimento para saber quais são), **anteriores** a data de fechamento em uma base de **testes** e assim ir trabalhando **paralelamente** para os ajustes, para depois ser feito em produção.

Caso não exista profissional de TI habilitado na empresa, indicamos o agendamento de um **analista** ***in loco***, afim de fazer esse procedimento. 

Para consultar quais são as tabelas do módulo SIGAGPE, faça a consulta abaixo:

* Abra o banco de dados;
* Localize a tabela SX2
* Realize um filtro por: X2\_MODULO "Igual a" 7 (Módulo 7 = SIGAGPE)

Feito esse filtro, **todas** as tabelas listadas, são as tabelas envolvidas no processo de fechamento a folha dentro do módulo **SIGAGPE.**   
É necessário avaliar tabelas **integradas** de **outros módulos** e demais customizações que possam interferir no módulo SIGAGPE. 

**Importante:**  
Atenção com todos os **encargos** já calculados e muitas vezes já **pagos.** Orientamos que qualquer diferença de pagamento, seja paga na folha atual (aberta) ou em casos de rescisão, que seja feita rescisão complementar.  
  
É recomendado criar um ***backup*** somente **destas tabelas** do módulo, além do ***backup*** **completo,** pois será mais simples para restaurá-lo.

**Saber Mais:**

[RH - Linha Protheus - GPE - Passo a passo para o processo de fechamento da folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057785494-RH-Linha-Protheus-GPE-Passo-a-passo-para-o-processo-de-fechamento-da-folha?source=search)

[RH - Linha Protheus - GPE - Como efetuar o cálculo da folha de pagamento na versão 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026974232-RH-Linha-Protheus-GPE-Como-efetuar-o-c%C3%A1lculo-da-folha-de-pagamento-na-vers%C3%A3o-12?source=search)

[RH - Linha Protheus - GPE - Error log invalid property PHONECODE1 on PTSREPOBJ:WSNATURAL(PTSREPOBJ.PRW)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027923711-RH-Linha-Protheus-GPE-Error-log-invalid-property-PHONECODE1-on-PTSREPOBJ-WSNATURAL-PTSREPOBJ-PRW-?source=search)

[RH - Linha Protheus - GPE - Implementação do Multi Thread no fechamento da folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034908554-RH-Linha-Protheus-GPE-Implementa%C3%A7%C3%A3o-do-Multi-Thread-no-fechamento-da-folha?source=search)

[RH - Linha Protheus - GPE - Como replicar a programação de rateio de um mês para o outro durante o fechamento da folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004775882-RH-Linha-Protheus-GPE-Como-replicar-a-programa%C3%A7%C3%A3o-de-rateio-de-um-m%C3%AAs-para-o-outro-durante-o-fechamento-da-folha?source=search)
