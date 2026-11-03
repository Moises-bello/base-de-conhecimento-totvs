---
article_id: 35216731695511
category: Financeiro - Configurador de Tributos
content_hash: ccf086e2dd14411ad6ae449e11251a7cc95e16595754f2f78222c502c45171e9
fetched_at: '2026-06-28T22:37:45.765982+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FISA170 - Compartilhamento das
  tabelas do Configurador de Tributos
type: support-article
updated_at: '2025-09-26T16:28:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35216731695511-Cross-Segmento-Backoffice-Linha-Protheus-FISA170-Compartilhamento-das-tabelas-do-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35216715364119) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como realizar a configuração do compartilhamento das tabelas do Configurador de Tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - a partir da release 12.1.2210  
  
**Solução**  
**A definição da estrutura das tabelas deve ser realizada durante a implantação das configurações de tributos (FISA170), conforme as necessidades previamente estabelecidas.**  
**Não é recomendada a alteração do compartilhamento das tabelas após a implantação do sistema, pois tal procedimento pode comprometer a confiabilidade da base de dados.**

**Tabelas com relacionamento 1:n**

Não é permitido o uso de tabelas de movimentos mais compartilhadas do que as tabelas de cadastro.

Mais informações: [Compartilhamento de tabelas de cadastro x movimento (1:n)](https://tdn.totvs.com/pages/viewpage.action?pageId=844959467)

### Tabelas da Família FK e FO (Configurador de Tributos)

**Tabela FK0**

* A tabela **FK0 (Títulos Gerados Impostos)** deve, **obrigatoriamente**, possuir o mesmo nível de compartilhamento definido para as tabelas da reestruturação da **SE5.**

  Conforme especificado no documento a seguir:

  [Reestruturação da tabela SE5 na família de tabelas FKx](https://tdn.totvs.com/pages/releaseview.action?pageId=183730415)

**Tabelas FO**

* As tabelas **FOI, FOJ e FOK**, que vinculam os cadastros financeiros às regras financeiras do Configurador de Tributos (**FKK**), devem respeitar o modo de compartilhamento dos respectivos cadastros relacionados (naturezas, clientes e fornecedores).
* Não é recomendado definir nível de compartilhamento superior ao dos cadastros correspondentes. Seguem as correlações:

  + **SED** → compartilhamento igual **FOI**;
  + **SA1** → compartilhamento igual **FOJ**;
  + **SA2** → compartilhamento igual **FOK**.

**Demais tabelas da família FO**

* As demais tabelas iniciadas com **FO** devem seguir, obrigatoriamente, o mesmo nível de compartilhamento da tabela de **Regra Financeira (FKK)**. Exemplos:

  + **FOO** → compartilhamento igual ao da **FKK**;
  + **FOU** → compartilhamento igual ao da **FKK**;
  + **FOT** → compartilhamento igual ao da **FKK**;
  + **FOS** → compartilhamento igual ao da **FKK**;
  + **FKV** → compartilhamento igual ao da **FKK**.

**Nota:**  
É imprescindível observar rigorosamente as recomendações de compartilhamento acima especificadas para assegurar o correto funcionamento do **Configurador de Tributos** e, consequentemente, a geração adequada dos tributos sobre os títulos no módulo **Financeiro**.

**Saiba mais**

[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras#01-01)

[Cross Segmento - Backoffice Linha Protheus - FISA170 - Configurador de tributos novas tabelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35215990451863-Cross-Segmento-Backoffice-Linha-Protheus-FISA170-Configurador-de-tributos-novas-tabelas)
