---
article_id: 360046635074
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: af5e30ab0b000f61be70e7d228f6e980f663b815ddc2ad832da95dc24a726675
fetched_at: '2026-06-28T22:41:04.935998+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA211 - Apuração
  das Entidades: CENTRO DE CUSTO, ITEM CONTABIL E CLASSE DE VALOR'
type: support-article
updated_at: '2025-03-18T17:25:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA211-Apura%C3%A7%C3%A3o-das-Entidades-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR
---

**Dúvida**

Qual procedimento para realizar apuração das entidades Centro de Custo, Item contábil e Classe de valor?

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial-  A partir da versão 12  
  
**Solução**

Quando **não deseja apurar** as entidades centro de custo, item e classe de valor**não deve**  informar o intervalo de branco a **zzz,** basta **deixar em branco** .

![](https://totvssuporte.zendesk.com/attachments/token/EjvSnrmNV9SACykfBy3Fr82lj/?name=inline1843950023.png)

Porem caso deseje realiza a apuração das entidades  centro de custo , item e classe de valor, deve seguir todos os passos abaixo , se atentando ao preenchimento do parâmetro demonstrados no  passos 4º  
  
Caso queira apurar as entidades centro de **custo, item e/ou classe** **de valor** verifique:

**1º** Realize o cadastro da entidade de apuração

* Cadastro do centro de custo através da rotina CTBA030
* Cadastro do Item contábil  através da rotina CTBA040
* Cadastro do Classe de valor  através da rotina CTBA060
* Veja se a entidade esta com sua Status "Não bloqueada"

Obs: o código da entidade de apuração precisa ser criado  posterior  o código da entidade já existente

Exemplo : Cadastro Centro de custo :  
001 - Centro de custo de Despesa  
002 - Centro de custo de Receita  
003 - centro de custo de apuração

**2º** veja se as entidade estão ativas para utilização  através da rotina [CTBA130](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006661492-MP-SIGACTB-CTBA130-Altera%C3%A7%C3%A3o-de-Entidades-Cont%C3%A1beis?source=search)

**3º** Antes de executar a apuração de resultado emita relatórios da entidade para verificar se os saldos (Anterior, Saldo Final) e Movimento estão corretos

* Emita os relatórios Balancete CTBR200(Centro de custo) CTBR120 (Item contábil) CTBR210(classe de valor)
* Razão CTBR440 (Centro de custo) ,Razão CTBR480(Item)
* Balancete CTBR145 (Conta x Centro de custo),Balancete CTBR140 (Conta x item) ,Balancete CTBR190(Classe de valor x Conta).
* esse relatório permite demonstras se as entidades possuem saldo anterior, movimento no período e saldo final , caso possuam saldo anterior necessário avaliar a possibilidade de seu zeramento
* Veja se as tabelas(saldo anterior, movimento no período e saldo atual) abaixo reflete exatamente o que esta sendo apresentado nos relatórios
  + veja se os campos [\_LP e \_DTLP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024630411-MP-SIGACTB-PREENCHIMENTO-DO-CAMPO-CQ0-LP-e-CQ0-DTLP?source=search) estão populados
* ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075356574)não deve seguir para o próxima apuração se o sistema não apurou o centro de custo, item ou classe de valor de forma certa

CT2 Movimento contábeis

CQ0 e CQ1 Saldos Planos de Contas

CQ2 e CQ3 Saldos Centro de Custo

CQ4 e CQ5 Saldos Item Contábil

CQ8 e CQ9 Saldos Totais por Entidade

CQ6 e CQ7 Saldos da Classe de Valores

**4º** Através da rotina de apuração CTBA211 Realize a apuração   das contas de receita e despesa , informando a entidade que deseja apurar

Através do cadastro do centro de custo (CTBA030) , temos  as entidade 001 ,002 e 003

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415546940183)

Exemplo centro de custo :

Centro de custo de apuração :003  (**O ultimo código será o de apuração) Criar um centro de custo somente para receber o valor apurado**  
De :em **BRANCO**  
Até 002 **(o Penúltimo código)**  
  
![](https://totvssuporte.zendesk.com/attachments/token/SIxhJayWQiIu0vLTNANdoO0e7/?name=inline-1609045021.png)

* caso a apuração já tenha sido executada será necessário estonar a apuração e apurar novamente informando a entidade
* Após realizar apuração de resultado emita relatório da entidade  para verificar se as entidades de receita e despesa (001 e 002) foram realmente zerados e o se o saldo gerado na entidade de apuração(003) está correto
* Relatórios Balancete CTBR200(Centro de custo) CTBR120(Item contábil) CTBR210(classe de valor)caso exista diferença de saldo dos relatórios  da entidade será necessário revisar os movimentos existente.

**Importante :**

Ao gerar ECD ,ECF ou Lalur com centro de custo é necessário realizar a apuração de resultado do centro de custo ,pois caso o centro de custo possua saldo anterior, movimento no período ou saldo final , será gerado no arquivo , gerando assim diferença no saldos

* [LALUR - COM CENTRO DE CUSTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046640714-MP-SIGACTB-LALUR-COM-CENTRO-DE-CUSTO?source=search)
* [ECF - Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871231-MP-SIGACTB-ECF-Centro-de-Custo?source=search)
* [ECD - Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search)

Saiba mais

* [O SISTEMA NÃO ESTA ZERANDO AS CONTAS DE RECEITA E DESPESA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046954954-MP-SIGACTB-CTBA211-O-SISTEMA-N%C3%83O-ESTA-ZERANDO-AS-CONTAS-DE-RECEITA-E-DESPESA?source=search)
* [Como realizar estorno de apuração de resultados L/P?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010708171-MP-SIGACTB-ECF-Como-realizar-estorno-de-apura%C3%A7%C3%A3o-de-resultados-L-P-?source=search)
* Veja o conceito da apuração por conta ponte  
  [Exemplo - Apuração Com Conta PONTE, Contas Transitórias e Encerramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041533493--MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Com-Conta-PONTE-Contas-Transit%C3%B3rias-e-Encerramento?source=search)  
  [Exemplo - Apuração Com Conta PONTE, Contas de Resultados e Encerramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041053194--MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Com-Conta-PONTE-Contas-de-Resultados-e-Encerramento?source=search)
* Para que o sistema **Zere** as contas de receita e Despesa deve realizar a apuração de resultado **Não** informando a **Conta ponte** e o campo **"Conta ponte =Não"**  
    
  [Exemplo - Apuração Trimestral : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)  
  [Exemplo - Apuração Anual : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041555313-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Anual-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)
* Conceito apuração  
  [Como realizar Apuração de resultados dentro do Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048472-MP-SIGACTB-Como-realizar-Apura%C3%A7%C3%A3o-de-resultados-dentro-do-Protheus-?source=search)
* [ECD LEIAUTE 9 Modificação da chave do registro I051 X Centro de custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003493582-MP-SIGACTB-ECD-LEIAUTE-9-Modifica%C3%A7%C3%A3o-da-chave-do-registro-I051-X-Centro-de-custo-)
* [ECD - I100 - Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search)
* [ECD LEIAUTE 9 Modificação da chave do registro I051 X Centro de custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003493582-MP-SIGACTB-ECD-LEIAUTE-9-Modifica%C3%A7%C3%A3o-da-chave-do-registro-I051-X-Centro-de-custo-)
* [ECF - Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871231-MP-SIGACTB-ECF-Centro-de-Custo?source=search)
