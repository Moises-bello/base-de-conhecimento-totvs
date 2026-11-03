---
article_id: 360009345312
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 78d8f28a805e409d0dfa4b83aefb078c113a002dda352a160f862697faf66857
fetched_at: '2026-06-28T22:41:05.028252+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB -  CTBA211 - Tabela Processadas
  na execução da apuração de resultados
type: support-article
updated_at: '2025-01-22T22:51:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009345312-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA211-Tabela-Processadas-na-execu%C3%A7%C3%A3o-da-apura%C3%A7%C3%A3o-de-resultados
---

**Dúvida**

Tabelas Processadas na execução da apuração de resultados  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - TOTVS Contabilidade Gerencial - Todas as versões

**Solução**

Versão P11

• CT1 - Cadastro de Plano de Contas.  
• CT2 - Cadastro de Lançamentos Contábeis.  
• CT3 - Saldo de Centro de Custo.  
• CT4 - Saldo Item Contábil.  
• CT7 - Saldo Plano de Contas.  
• CTI - Saldo da Classe de Valores.

Versão P12

• CT1 - Cadastro de Plano de Contas.  
• CT2 - Cadastro de Lançamentos Contábeis.  
• CQ0 – Saldo por Conta No Mês.  
• CQ1 – Saldo por Conta No Dia.  
• CQ2 – Saldo por Centro de Custo No Mês.  
• CQ3 – Saldo por Centro de Custo No Dia.  
• CQ4 – Saldo por Item Contábil No Mês.  
• CQ5 – Saldo por Item Contábil No Dia.  
• CQ6 – Saldo por Classe de Valor No Mês.  
• CQ7 – Saldo por Classe de Valor No Dia.

### 

**IMPORTANTE 📢️ :**

* Os campos **CTT\_CUSTO**, **CTD\_ITEM**, **CTH\_CLVL** e **CT1\_CONTA**, consultados via **APSDU** na tabela **SX3**, devem ter o mesmo tamanho definido no respectivo grupo de campos.
* O campo **CT1\_CONTA** deve possuir o mesmo tamanho do campo **Conta Contábil** configurado no **Grupo de Campos** do **SIGACFG**.
* É fundamental que, na tabela **SX1**, o campo **X1\_GRUPO = CTB211** e que:

  + Para as perguntas relacionadas à **Conta Contábil** (X1\_ORDEM 07 e X1\_ORDEM 08), o tamanho dos campos seja equivalente ao de **CT1\_CONTA** e ao **Grupo de Campos - Conta Contábil**.
  + Para as perguntas relacionadas às **Entidades Contábeis**  (X1\_ORDEM 22, X1\_ORDEM 23, X1\_ORDEM 24, X1\_ORDEM 25, X1\_ORDEM 26 e X1\_ORDEM 27), o tamanho dos campos deve corresponder aos de **CTT\_CUSTO**, **CTD\_ITEM** e **CTH\_CLVL**, pertencendo aos Grupos de Campos: **"Centro de Custo"**, **"Item Contábil"** e **"Classe Valor"**.

Por fim, certifique-se de que o **pacote geral acumulado** esteja devidamente aplicado.

* Orientações referentes ao tamanho das entidades estão disponíveis nos links:  
  [SIGACTB - ALTERAÇÃO DO TAMANHO DAS ENTIDADES CONTÁBEIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015543251-MP-SIGACTB-ALTERA%C3%87%C3%83O-DO-TAMANHO-DAS-ENTIDADES-CONT%C3%81BEIS?source=search)  
  [SIGACTB - Alterar o tamanho do campo código das entidades contábeis adicionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401031-MP-SIGACTB-Alterar-o-tamanho-do-campo-c%C3%B3digo-das-entidades-cont%C3%A1beis-adicionais?source=search)

**Saiba Mais:**

* Help Online  :[Apuração de Resultados por Movimento](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba210.htm)
* Conceito sobre e parâmetros para a execução da  Apuração de Resultado: [Clique aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=334338459)
* Verifique o compartilhamento das tabelas  :[Compartilhamento das Tabelas Contábeis](http://tdn.totvs.com/display/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)
* O compartilhamento das tabelas CTG, CTO, CQD e CTE estejam iguais, conforme orientado no link  [Como realizar compartilhamento de tabelas na Contabilidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032-MP-SIGACTB-Como-realizar-compartilhamento-de-tabelas-no-Contabilidade-Gerencial-SIGACTB-?source=search)
* O compartilhamento das tabelas CQ0, CQ1, CQ2, CQ3, CQ4, CQ5, CQ6, CQ07 CQ8, CQ9 e CT2 estejam iguais, conforme orientado no link [Como realizar compartilhamento de tabelas na Contabilidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032-MP-SIGACTB-Como-realizar-compartilhamento-de-tabelas-no-Contabilidade-Gerencial-SIGACTB-?source=search)
* Performance na apuração de resultado: [DT Performance](http://tdn.totvs.com/pages/viewpage.action?pageId=239039851) e [Performance CTBA211](http://tdn.totvs.com/display/PROT/CTB0127_Performance_CTBA211)
* Encerramento do Exercício: [Clique aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=334338624)
* Atualização de saldos em fila: [Clique aqui](http://tdn.totvs.com/display/PROT/CTB113_REPROCESSAMENTO_SALDOS_POR_FILA_P12)
* [SIGACTB - Ambiente desatualizado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000043507)
* [SIGACTB - CTBA 190 Como realizar o reprocessamento de saldos no SIGACTB?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452371-MP-SIGACTB-CTBA-190-Como-realizar-o-reprocessamento-de-saldos-no-SIGACTB-)
* Verifique o tamanho dos campos "Conta contábil" ,"Centro de Custo", "Item Contábil" e "Classe Valor"   
  [SIGACTB - ALTERAÇÃO DO TAMANHO DAS ENTIDADES CONTÁBEIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015543251-MP-SIGACTB-ALTERA%C3%87%C3%83O-DO-TAMANHO-DAS-ENTIDADES-CONT%C3%81BEIS?source=search) e [Tamanho do campo código das entidades contábeis Adicionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401031-MP-SIGACTB-Alterar-o-tamanho-do-campo-c%C3%B3digo-das-entidades-cont%C3%A1beis-adicionais?source=search)e [GRUPO DE PERGUNTAS CTB211](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028526532-MP-SIGACTB-CTBA211-GRUPO-DE-PERGUNTAS-?source=search)
