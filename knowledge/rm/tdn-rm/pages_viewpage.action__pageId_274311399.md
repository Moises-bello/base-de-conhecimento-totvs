---
content_hash: d1c38e4ae184f370bdfffc4dda3cd19138a2bf40642a9c645b0f76ed17d15d82
fetched_at: '2026-06-29T00:08:33.273443+00:00'
page_id: '274311399'
product: rm
source: tdn-rm
title: RPT00009.1.3 - Visibilidade de Bandas Mestre em Relação às Bandas Detalhe
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274311399
version: 14
---

# Índice:

---

.\*ndice:

# Visibilidade de Bandas Mestre em Relação às Bandas Detalhe

---

A funcionalidade de **Visibilidade de Bandas Mestre em Relação às Bandas Detalhe** corresponde a capacidade de uma banda mestre **aparecer (ou não)**, o que depende **da quantidade de registros da banda filha**.

# Propriedades "Número de Impressões" e "Detalhe Contagem Quando a Fonte de Dados está vazia"

---

Existem 2 propriedades que são responsáveis pela funcionalidade de **Visibilidade de Bandas Mestre em Relação às Bandas Detalhe**, são elas:

* **Número de Impressões** (Todas as Bandas de Detalhe)

* **Detalhe Contagem Quando a Fonte de Dados está Vazia** (Componente Principal RptReport1 e em todos os Subdetalhes)

# Descrição da Funcionalidade Visibilidade de Bandas Mestre em Relação às Bandas Detalhe

---

A funcionalidade **Visibilidade de Bandas Mestre em Relação às Bandas Detalhe** funciona da seguinte maneira:

A **visibilidade da banda pai** poderá ser visível ou não dependendo da quantidade de registros da **banda filha**.

**EX1 - NÚMERO DE IMPRESSÕES : PSECAO - 0 | PFUNC - 0 | PFDEPEND - 0**

**EX2 - NÚMERO DE IMPRESSÕES : PSECAO - 0 | PFUNC - 0 | PFDEPEND - 1**

**EX3 - NÚMERO DE IMPRESSÕES : PSECAO - 0 | PFUNC - 1 | PFDEPEND - 0**

**EX4 - NÚMERO DE IMPRESSÕES : PSECAO - 0 | PFUNC - 1 | PFDEPEND - 1**

**EX5 - NÚMERO DE IMPRESSÕES : PSECAO - 1 | PFUNC - 0 | PFDEPEND - 0**

**EX6 - NÚMERO DE IMPRESSÕES : PSECAO - 1 | PFUNC - 0 | PFDEPEND - 1**

**EX7 - NÚMERO DE IMPRESSÕES : PSECAO - 1 | PFUNC - 1 | PFDEPEND - 0**

**EX8 - NÚMERO DE IMPRESSÕES : PSECAO - 1 | PFUNC - 1 | PFDEPEND - 1**

# Estrutura do diagrama

---

O Diagrama que será apresentado abaixo é divido em:

* **Árvore de Visibilidade (Apresentação das Bandas / Estrutura do Relatório)**

* **Árvore de Visibilidade (Caminho Percorrido pela Funcionalidade / Estrutura de Fonte de Dados/Valores do Relatório)**

# Explicação da Visibilidade das Bandas

---

Iremos tomar como exemplo o teste 01, onde o **NÚMERO DE IMPRESSÕES** é : **PSECAO - 0 | PFUNC - 0 | PFDEPEND - 0**

* **PSECAO (01.01) -->** *Existe Filhos ?* **-->** *SIM* **--> PFUNC (00001) -->** *Existe Filhos ?* **-->** *SIM* **--> PFDEPEND (JOÃO) -->** *É Folha ?* **-->** *SIM*

* **PFDEPEND (JOÃO) -->** *Mostra* **--> **PFUNC (00001) -->**** *Mostra* ****--> **PSECAO (01.01) -->****** *Mostra*

* **PSECAO (01.01) -->** *Existe Filhos ?* **-->** *SIM* **--> PFUNC (00002) -->** *Existe Filhos ?* **-->** *SIM* **--> PFDEPEND (JOSÉ) -->** *É Folha ?* **-->** *SIM*

 

* **PFDEPEND (JOSÉ) -->** *Mostra* **--> **PFUNC (00002) -->**** *Mostra* ****--> **PSECAO (01.01) -->****** *Mostra*

* **PSECAO (01.03) -->** *Existe Filhos ?* **-->** *SIM* **--> PFUNC (00011) -->** *Existe Filhos ?* **-->** *NÃO*

* ****PFUNC (00011) -->**** *NãoMostra* ****--> **PSECAO (01.03) -->****** *NãoMostra*

* **PSECAO (02.02) -->** *Existe Filhos ?* **-->** *SIM* **--> PFUNC (00077) -->** *Existe Filhos ?* **-->** *SIM* **--> PFDEPEND (MARIA) -->** *É Folha ?* **-->** *SIM*

 

* **PFDEPEND (MARIA) -->** *Mostra* **--> **PFUNC (00077) -->**** *Mostra* ****--> **PSECAO (02.02) -->****** *Mostra*

* **PSECAO (04.11) -->** *Existe Filhos ?* **-->** *NÃO*

* **PSECAO (04.11) -->** *Não Mostra*
falsefalse

**Produto:** Framework

false

**Versão:** 12.1.16 e superiores

false

**Processo:** Visibilidade de Bandas Mestre em Relação às Bandas Detalhe

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
