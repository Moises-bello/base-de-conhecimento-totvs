---
article_id: 360028526532
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 0b4a8f1387d2f17f3484408c95c5fd9a669c26e4a20f41888617efc9956e266e
fetched_at: '2026-06-28T22:41:05.020920+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB -  CTBA211 - GRUPO DE
  PERGUNTAS
type: support-article
updated_at: '2025-01-22T21:29:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028526532-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA211-GRUPO-DE-PERGUNTAS
---

**Duvidas**

Como é composto o Grupo de perguntas apuração de resultado?  
  
**Ambiente**Microsiga Protheus  – Contabilidade – A partir da versão 11.80  
  
  
**Solução**

Através da tabela SX1 **(CTB211)** é possível verificar o grupo de perguntas da rotina de apuração de resultado?

**Obs ⚠️: essa analise deve ser realizada também no CTB215**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029485192)

### **IMPORTANTE 📢️:**

**Na tabela SX1, o campo X1\_GRUPO deve ser igual a CTB211.**

* Para as perguntas relacionadas à **Conta Contábil** (X1\_ORDEM 07 e X1\_ORDEM 08), o tamanho dos campos deve ser equivalente ao campo **CT1\_CONTA**, pertencendo ao grupo de campos **Conta Contábil**.
* Para as perguntas relacionadas às **Entidades Contábeis** (X1\_ORDEM 22, X1\_ORDEM 23, X1\_ORDEM 24, X1\_ORDEM 25, X1\_ORDEM 26 e X1\_ORDEM 27):   
  O tamanho dos campos deve ser equivalente aos campos **CTT\_CUSTO** (Centro de Custo), **CTD\_ITEM** (Item Contábil) e **CTH\_CLVL** (Classe Valor).  
  Esses campos devem pertencer aos grupos: **"Centro de Custo"**, **"Item Contábil"** e **"Classe Valor"**.

Verifique o tamanho dos campos "Centro de Custo", "Item Contábil" e "Classe Valor"   
[SIGACTB - ALTERAÇÃO DO TAMANHO DAS ENTIDADES CONTÁBEIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015543251-MP-SIGACTB-ALTERA%C3%87%C3%83O-DO-TAMANHO-DAS-ENTIDADES-CONT%C3%81BEIS?source=search) e [Tamanho do campo código das entidades contábeis Adicionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401031-MP-SIGACTB-Alterar-o-tamanho-do-campo-c%C3%B3digo-das-entidades-cont%C3%A1beis-adicionais?source=search)

 Verifique se o sistema replicou a alteração para todos os grupo de campos e todos os grupo de perguntas:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071061514)

Veja mais:

[Como realizar Apuração de resultados dentro do Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048472-MP-SIGACTB-Como-realizar-Apura%C3%A7%C3%A3o-de-resultados-dentro-do-Protheus-?source=search)

[CTBA211 Exemplo - Apuração Trimestral : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)

[CTBA211 Exemplo - Apuração Anual : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041555313-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Anual-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)

[CTBA211 Exemplo - Apuração Com Conta PONTE, Contas Transitórias e Encerramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041533493--MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Com-Conta-PONTE-Contas-Transit%C3%B3rias-e-Encerramento?source=search)

[CTBA211 Exemplo - Apuração Com Conta PONTE, Contas de Resultados e Encerramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041053194--MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Com-Conta-PONTE-Contas-de-Resultados-e-Encerramento?source=search)

[CHAVE DE APURAÇÃO CTBA211](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-MP-SIGACTB-CHAVE-DE-APURA%C3%87%C3%83O-CTBA211?source=search)

[AO REALIZAR ALTERAÇÃO NO TAMANHO DE GRUPO DE CAMPOS CONFIGURAR NÃO ESTA REFLETINDO PARA TODAS AS TABELAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search)
