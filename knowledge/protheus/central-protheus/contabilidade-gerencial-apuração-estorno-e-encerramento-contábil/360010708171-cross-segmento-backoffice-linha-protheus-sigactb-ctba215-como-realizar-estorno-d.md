---
article_id: 360010708171
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: a53ff9c52dc26f39d8655d0190ac218133b1e76ad5b288d2c9a1d652061adea3
fetched_at: '2026-06-28T22:41:05.087200+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA215 - Como realizar
  estorno de apuração de resultados L/P?
type: support-article
updated_at: '2024-03-05T11:56:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010708171-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA215-Como-realizar-estorno-de-apura%C3%A7%C3%A3o-de-resultados-L-P
---

**Dúvida**

Como realizar estorno de apuração de resultados L/P?  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução**

Acessar a rotina, Estorno de apuração de resultados (CTBA215);

Preencher os parâmetros conforme desejado;

**Requisitos**

* caso tenha executado a rotina [CTBA400  Encerramento do Exercício](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021602792-MP-SIGACTB-CTBA400-Encerramento-do-Exerc%C3%ADcio-?source=search) será necessário abrir o [Status do calendário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006722952-MP-SIGACTB-CTBA010-Como-abrir-per%C3%ADodo-cont%C3%A1bil-bloqueado-fechado-para-movimenta%C3%A7%C3%A3o-?source=search)
* caso tenha realizado transferência do saldo de apuração manualmente através da rotina de lançamento contábeis(CTBA102 ou CTBA101) necessário excluir esse lançamentos
* O estorno da apuração deve ser feita de forma **retroativa** Ex.: caso queria estorna apuração de 2018 , porem tenha apurado até 2020, precisa realizar o estorno de 2020,2019 para assim estornar 2018

**Exemplo** :

* Anos apurados :

2017 - executou apuração e o saldo foi lançado na conta do Patrimônio liquido

2018 - executou apuração e o saldo foi lançado na conta do Patrimônio liquido

2019 - executou apuração e o saldo foi lançado na conta do Patrimônio liquido

2020 - executou apuração e o saldo foi lançado na conta do Patrimônio liquido

* Preciso estornar a apuração de 2018 para corrigir saldos
* Não deve ir direto em 2018 e estornar a apuração sem estornar os anos de 2020,2019 antes
* Segue o procedimento correto para estornar

**1º** execute o estorno da apuração  de 2020 - veja se o saldos foram devidamente estornados da conta de receita e despesa e se o saldo da conta de apuração (patrimônio ) ficou correto

* só siga para o próximo estorno após conferencia dos saldo , caso tenha apurado com as entidade (Centro de custo, Item contabil e Classe de valor) necessário conferencia do saldos delas também

**2º** execute o estorno da apuração de 2019 - veja se o saldos foram devidamente estornados da conta de receita e despesa e se o saldo da conta de apuração (patrimônio ) ficou correto

* só siga para o próximo estorno após conferencia dos saldo , caso tenha apurado com as entidade (Centro de custo, Item contabil e Classe de valor) necessário conferencia do saldos delas também

**3º** execute o estorno da apuração de 2018 - veja se o saldos foram devidamente estornados da conta de receita e despesa e se o saldo da conta de apuração (patrimônio ) ficou correto

* só siga para o próximo estorno após conferencia dos saldo , caso tenha apurado com as entidade (Centro de custo, Item contabil e Classe de valor) necessário conferencia do saldos delas também

**Passo 1**

* Através da rotina CTBA007 (tabela CW0) verifique se existe registro de apuração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024429632)

Se foi anual, ao consultar a chave LP na rotina Dados Auxiliares CTB (CTBA007) não deve conter 1 registro de apuração com final Z, para o ano de 2018, com montagem da chave conforme segue;  
[MP\_SIGACTB CHAVE DE APURAÇÃO CTBA211](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-MP-SIGACTB-CHAVE-DE-APURA%C3%87%C3%83O-CTBA211?source=search)

**Passo 2**

* Através da rotina CTBA215 realize o estorno da apuração para que o sistema limpe automaticamente o registro de apuração existente na rotina CTBA007

**Passo 3**

* Realize o reprocessamento de saldo do período completo através da rotina CTBA190
* acesse a rotina CTBA102 e verifique se foi excluído lançamento contábil
* Emita os relatórios Razão e balancete para verificar se o lançamento voltaram para as contas de receita e despesa , se possui saldo anterior
* Emita os relatórios Balancete CTBR200(Centro de custo) CTBR120(Item contábil) CTBR210(classe de valor) - esse relatório permite demonstras se as entidades possuem saldo anterior, movimento no período e saldo final , caso possuam saldo anterior necessário avaliar a possibilidade de seu zeramento
* veja se a tabela CTZ continua populada
* veja se os campos CT2\_DTLP e das tabelas tabelas CQx foram limpos pelo sistema
* tabelas CQx (1, 2, 3, 4, 5, 6, 7, 8 e 9) "CQ0",'CQ2','CQ4','CQ6','CQ8" não possua com o campo [CQ2\_LP = 'S' e o campo CQ0\_DTLP = data de apuração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024630411-MP-SIGACTB-PREENCHIMENTO-DO-CAMPO-CQ0-LP-e-CQ0-DTLP?source=search)
* Emita os relatórios  "Razão Contábil (CTBR400)" e " Balancete(CTBR040)",  para verificar se o lançamento foram estornados.

**Observação:** A data informada na pergunta, data de apuração? Deve ser a ultima data que realizou apuração, se for estornar mais que uma apuração a próxima data será da ultima apuração no sistema, anterior a ultima estornada.

Para consultar as datas que foram apuradas, acessar a rotina Dados contábeis auxiliares (CTBA007), e visualizar a chave LP.

Saiba mais :

[APURAÇÃO DAS ENTIDADES CENTRO DE CUSTO,ITEM CONTABIL E CLASSE DE VALOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DAS-ENTIDADES-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR?source=search)
