---
article_id: 360053714633
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 6b989527351588e67758ec6bc3dbf000102b28896f6517343c4ab4ac0fba25db
fetched_at: '2026-06-28T22:38:31.298310+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-MV_REDSTOR
type: support-article
updated_at: '2021-04-28T15:52:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053714633-MP-FAT-MV-REDSTOR
---

**Dúvida**

Qual a utilização do parâmetro **MV\_REDSTOR** chamado na contabilização de saída **(CTBANFS)**?

**Ambiente**

Microsiga Protheus - a partir da release 12.1.17.

**Solução**

O parâmetro **MV\_REDSTOR**foi desenvolvido para tratar o ambiente da Rússia e somente é acionado se o pais local estiver como Russía e o parâmetro estiver como Falso, não é tratado para país Brasil e não é tratado na contabilização  
  
A implementação é datada de 18.09.2017 ainda na release 12.1.17 na rotina de integração contábil CTBXATU.  
  
**Nome: MV\_REDSTOR  
Tipo: Lógico  
Descrição: Parameter to activate Red Storn - uso Rússia  
Conteúdo Padrão: .F.**

Na release 12.1.17, a  implementação deste parâmetro causou efeito colateral para ambientes diferentes de Rússia ao utilizar a função **DETPROVA** da Contabilização, sendo corrigido através do pacote contábil de 07.12.2017 contido no artigo: **<https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016023687-MP-SIGACTB-Erro-MV-REDSTOR>**

Caso haja algum problema nas releases atuais, aplique o pacote da rotina **Matxfuna** mais atual relacionado a release utilizada:

**12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=917748> ;**

**12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=917747> ;**

**12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=917746> ; (com garantia estendida)**

**12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=856981> ; (em garantia estendida)**

Caso ainda reste dúvidas para o uso do parâmetro, contate a equipe de atendimento Ativo e Contábil.
