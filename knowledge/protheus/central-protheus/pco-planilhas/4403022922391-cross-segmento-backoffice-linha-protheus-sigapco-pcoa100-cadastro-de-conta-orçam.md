---
article_id: 4403022922391
category: PCO - Planilhas
content_hash: ffe50bfcd898a36556f8b56fcf0cbbebfb98e38448052524ca42c96c2a64c325
fetched_at: '2026-06-28T22:37:05.412588+00:00'
product: protheus
section_id: 1500001539901
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO- PCOA100 - Cadastro de
  conta orçamentária na planilha.
type: support-article
updated_at: '2021-06-21T18:52:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403022922391-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA100-Cadastro-de-conta-or%C3%A7ament%C3%A1ria-na-planilha
---

**Dúvida**Como incluir uma conta orçamentária na planilha?

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - TOTVS Planejamento e Controle Orçamentário - Todas as versões.  
  
**Solução**

* Rotina PCOA010- Contas orçamentárias.

O cadastro das contas orçamentárias pode ser feita de forma manual ou sincronizando com o plano de contas contábil.

O parâmetro MV\_PCOSINC habilitar o sincronismo entre os plano de contas (tabela CT1).

A rotina PCOA010 realizará  uma carga inicial na tabela de contas orçamentárias (AK5) com os dados das contas do módulo SIGACTB (CT1). Também será habilitado o botão sincronizar na tela da rotina, que permitirá iniciar o processo manualmente em caso de alterações do plano de contas contábil.

**Importante**

Com o sincronismo das contas orçamentárias habilitado a inclusão de novas contas será desabilitada na rotina PCOA010, sendo necessário realizá-la através do SIGACTB.

* Rotina PCOA100 - Após a inclusão da planilha orçamentária siga para "Outras ações" + "Estrutura" e "Incluir conta orçamentária"

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403019454743/mceclip2.png)

Saiba Mais:

[PCOA010, Sincronismo com plano de contas contábil.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018757451-MP-SIGAPCO-Utiliza%C3%A7%C3%A3o-de-plano-de-contas-or%C3%A7ament%C3%A1rio-sincronizado-com-o-plano-de-contas-cont%C3%A1bil-)
