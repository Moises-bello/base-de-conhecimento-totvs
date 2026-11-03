---
article_id: 360046954954
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 76e1d6df478dd5861801a1b3b3b5695dc35c3dc236eb325743c8bb32d1641826
fetched_at: '2026-06-28T22:41:05.059814+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA211 - Apuração de
  resultados não zera as contas
type: support-article
updated_at: '2026-05-13T20:15:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046954954-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA211-Apura%C3%A7%C3%A3o-de-resultados-n%C3%A3o-zera-as-contas
---

**Dúvida**

Por que a apuração de resultado não está zerando os saldos das entidades (conta, centro de custo, item contábil e classe de valor) de receitas e despesas no sistema?  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - A partir da versão 12

**Imprescindível:**

Aplique o **Pacote Acumulado Contábil** e instale as [procedures nele contidas;](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes)

[Pacotes de Atualização - Contabilidade](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)

[Pacotes LIB](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/search/searchAll)

[Pacotes DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/search/searchAll)

[Binário AppServer](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)

[Binário SmartClient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/)

#### **Importante:** 📢️

É imprescindível aplicar o **pacote acumulado da contabilidade** e instalar a **Procedure** correspondente para garantir que os fontes de atualização de saldo (**CTBA190** e **CTBXATU**) estejam devidamente atualizados.

**Solução:**

* É necessário criar um histórico padrão utilizando o [**Histórico Inteligente**.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019193591-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA070-Cadastro-de-Hist%C3%B3rico-inteligente-?source=search)
* Realize o [reprocessamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452371-MP-SIGACTB-CTBA-190-Como-realizar-o-reprocessamento-de-saldos-no-SIGACTB-) de saldos a partir do **primeiro lançamento existente na CT2** até a data atual;
* Efetue um teste de apuração **sem informar as entidades** ([CENTRO DE CUSTO,ITEM CONTABIL E CLASSE DE VALOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DAS-ENTIDADES-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR?source=search)) e veja se o sistema realiza o zeramento de forma correta. Caso as contas sejam zeradas sem as entidades, mas o problema persista ao incluir essas informações, será necessário avaliar se as entidades possuem saldo anterior. Para que o sistema zere as contas de receita e despesa corretamente, **as entidades não devem possuir saldo anterior**.
* Verifique se o **status do calendário contábil** está como aberto: [Saiba Como abrir período contábil e se o compartilhamento das tabelas estão corretas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006722952-MP-SIGACTB-CTBA010-Como-abrir-per%C3%ADodo-cont%C3%A1bil-bloqueado-fechado-para-movimenta%C3%A7%C3%A3o-?source=search)
* Caso ocorra erro de chave duplicada nas rotinas **CTBA211** (Apuração de Resultado), **CTBA215** (Estorno) ou **CTBA190** (Reprocessamento de Saldos), tanto na tela quanto no **Trace**, verifique os seguintes itens:   
  Veja se o [GRUPO DE PERGUNTAS e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028526532-MP-SIGACTB-CTBA211-GRUPO-DE-PERGUNTAS-?source=search)[Tamanho de Campos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search) , [TAMANHO DAS ENTIDADES CONTÁBEIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015543251-MP-SIGACTB-ALTERA%C3%87%C3%83O-DO-TAMANHO-DAS-ENTIDADES-CONT%C3%81BEIS?source=search) e [Tamanho do campo código das entidades contábeis Adicionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401031-MP-SIGACTB-Alterar-o-tamanho-do-campo-c%C3%B3digo-das-entidades-cont%C3%A1beis-adicionais?source=search) estão corretos. Caso seja necessária alteração, confira se o ajuste foi **refletido para todas as tabelas**.
* Garanta que as entidades (Centro de Custo, Item Contábil e Classe de Valor) estão com o **status "Não bloqueada"**.
* Verifique também o status das [**Contas Contábeis**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021958832-MP-SIGACTB-CTBA020-Bloqueio-de-Conta-Cont%C3%A1bil?source=search) de receita, despesa e apuração que irão receber os lançamentos.
* Confirme se o [**compartilhamento das tabelas**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032-MP-SIGACTB-Como-realizar-compartilhamento-de-tabelas-no-Contabilidade-Gerencial-SIGACTB-?source=search) de saldo e movimento (CT2, CTC, CQ0...CQ9) está correto.
* Certifique-se de que o parâmetro [**MV\_ATUSAL,** está configurado para  atualização de saldos de forma online.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019534772-MP-SIGACTB-Saldos-n%C3%A3o-est%C3%A3o-sendo-atualizados-de-forma-online-?source=search)
* Confirme a instalação das **Procedures 01, 02, 06 e 23**, seguindo a documentação oficial.
* Acesse a rotina **CTBA007** verifique o sistema gravou a [CHAVE DE APURAÇÃO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-MP-SIGACTB-CHAVE-DE-APURA%C3%87%C3%83O-CTBA211?source=search)
* Veja se existe data com registro de apuração, caso exista registro e apuração será necessário realizar o [estorno de apuração de resultados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010708171-MP-SIGACTB-ECF-Como-realizar-estorno-de-apura%C3%A7%C3%A3o-de-resultados-L-P-?source=search)mesmo que as contas não tenham sido zeradas, para posteriormente realizar a apuração novamente.
* Caso não exista registro na [CW0](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-MP-SIGACTB-CTBA007-CTBA211-CHAVE-DE-APURA%C3%87%C3%83O-CW0-?source=search), realize a apuração de resultado.

**1º -** Ao realizar a apuração selecione "**Rotina de Apur**."  
  
![](https://totvssuporte.zendesk.com/attachments/token/iZgDgiBRyD0RAA17B53jQNAJQ/?name=inline1511591480.png)

**2º -** Ao realizar a apuração de resultado: **Não** informar 999 no lote, sub - lote e documento, pois existe [Limitação número documento na apuração de resultado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018247651-MP-SIGACTB-CTBA211-Limita%C3%A7%C3%A3o-n%C3%BAmero-documento-na-apura%C3%A7%C3%A3o-de-resultado?source=search)

![](https://totvssuporte.zendesk.com/attachments/token/NKfOlviwWFVvEkqKDNhKkiquP/?name=inline653182876.png)​

**3º -** Quando **não desejar apurar** centro de custo, item e classe de valor**não** **devemos** informar o intervalo de branco a **ZZZ,** basta **deixar em branco**, caso queira realizar a [Apuração da entidades CENTRO DE CUSTO,ITEM CONTABIL E CLASSE DE VALOR (Clique aqui)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DAS-ENTIDADES-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR?source=search)

**4º -** Para que o sistema **Zere** as contas de receita e Despesa deve realizar a apuração de resultado **Não** informando a **Conta Ponte** e o campo **"Conta Ponte =Não"**  
  
[Exemplo - Apuração Trimestral: Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)  
[Exemplo - Apuração Anual: Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041555313-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Anual-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)  
  
Conceito apuração: [Como realizar Apuração de resultados dentro do Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048472-MP-SIGACTB-Como-realizar-Apura%C3%A7%C3%A3o-de-resultados-dentro-do-Protheus-?source=search)

**5º -** Ao realizar a apuração com conta ponte as entidades (contas, centro de custo, item, classe de valor) de receita e despesa não são zeradas:

Veja o conceito da apuração por conta ponte  
[Exemplo - Apuração Com Conta PONTE, Contas Transitórias e Encerramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041533493--MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Com-Conta-PONTE-Contas-Transit%C3%B3rias-e-Encerramento?source=search)  
[Exemplo - Apuração Com Conta PONTE, Contas de Resultados e Encerramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041053194--MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Com-Conta-PONTE-Contas-de-Resultados-e-Encerramento?source=search)

**6º -** Realize o R**eprocessamento de Saldos**

**7º -** Veja se o sistema preencheu corretamente os campo  [\_LP e\_DTLP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024630411-MP-SIGACTB-PREENCHIMENTO-DO-CAMPO-CQ0-LP-e-CQ0-DTLP?source=search)

* Veja se os campos CT2\_DTLP e das tabelas CQs foram populados pelo sistema;
* Tabelas CQs (1, 2, 3, 4, 5, 6, 7, 8 e 9) "CQ0",'CQ2','CQ4','CQ6','CQ8"   possua com o campo CQ2\_LP = 'S' e o campo CQ0\_DTLP = data de apuração

**8º -** Emita os relatórios:

#### **Importante:** 📢️

Antes de realizar a apuração de resultado, é fundamental verificar se as entidades utilizadas — **Conta Contábil, Centro de Custo, Item Contábil e Classe de Valor** — possuem saldo anterior., **as entidades não devem possuir saldo anterior**.

* "Razão Contábil (CTBR400)" e" Balancete(CTBR040)", para verificar se o lançamento foram apurados nas contas contábeis emita os relatórios sem informar as entidades centro de custo, item contábil e classe de valor, verifique se existe saldo anterior nas contas, caso exista necessário realizar a apuração desse saldo.
* Balancete CTBR200 (Centro de custo) CTBR120 (Item contábil) CTBR210 (classe de valor)
* Razão CTBR440 (Centro de custo) ,Razão CTBR480 (Item).
* Balancete CTBR145 (Conta x Centro de custo), Balancete CTBR140 (Conta x item), Balancete CTBR190 (Classe de valor x Conta).
* Esse relatório permite demonstrar se as entidades possuem saldo anterior, movimento no período e saldo final, caso possuam saldo anterior necessário avaliar a possibilidade de seu zeramento.

**9º -** Garanta que as tabelas (saldo anterior, movimento no período e saldo atual) abaixo refletem **exatamente** o que esta sendo apresentado nos relatórios.

**Obs.**📢️**:** caso as entidades de receita e despesa tenham saldo anterior, poderá impedir o zeramento correto, com isso apresentar diferença de saldo nos relatórios.

CQ0 e CQ1 - Saldos entidade Planos de Contas;

CQ2 e CQ3 = Saldos entidade Centro de Custo;

CQ4 e CQ5  =Saldos entidade Item Contábil;

CQ8 e CQ9 = Saldos Totais por Entidade;

CQ6 e CQ7 = Saldos da entidade Classe de Valores;

CT2= Movimento Contábil;
