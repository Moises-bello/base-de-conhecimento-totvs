---
article_id: 35677906798999
category: Financeiro - Smart View
content_hash: e0bf518dfb457060177db5e3a50fd6eb02839a7f4962d40ae96134a794f207f3
fetched_at: '2026-06-28T22:37:44.857349+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - Smartview FINSV014 - SIGAFIN
  - Extrato bancário multi-filiais
type: support-article
updated_at: '2025-10-29T18:03:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35677906798999-Cross-Segmentos-Backoffice-Linha-Protheus-Smartview-FINSV014-SIGAFIN-Extrato-banc%C3%A1rio-multi-filiais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35677906782231) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Ao acessar o FINSV014, o sistema não habilita a troca de filial no extrato bancário.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução:**  
A partir da **expedição contínua de maio de 2025**, foi implementado um **ajuste no SmartView FINSV014**, que passa a **validar o compartilhamento da tabela SA6** para definir a disponibilização dos filtros de **múltiplas filiais**.

Com essa atualização, o **filtro de Filiais será desabilitado** caso a **tabela SA6** esteja configurada como **exclusiva**.

Com a mudança, o sistema passa a validar de forma **obrigatória para utilização do objeto de negócio** um **novo grupo de perguntas** criado em dezembro/24 (**FINT035**).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35677906782615)

**Importante**

Se o grupo não for encontrado, execute o UPDDISTR para atualizar os dicionários com o último SDF do backoffice.

**Quando a tabela SA6 estiver configurada como exclusiva**, a exibição do **FINSV014** seguirá o modelo padrão, sem permitir seleção de múltiplas filiais.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35677952268311)

**Quando a tabela SA6 estiver configurada como compartilhada**, o sistema **permitirá a seleção de filiais** no filtro, oferecendo maior flexibilidade ao usuário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35677952269975)

**Saiba mais**

[Financeiro - Conciliador Backoffice](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30769054561431-Financeiro-Conciliador-Backoffice)
