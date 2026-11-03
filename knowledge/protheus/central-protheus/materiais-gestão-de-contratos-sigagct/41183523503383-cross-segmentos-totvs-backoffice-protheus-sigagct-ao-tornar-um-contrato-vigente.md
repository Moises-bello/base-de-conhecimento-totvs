---
article_id: 41183523503383
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 677c118d65c3959be43f5db98d5811b55381d6a475ced375607cd64392ec0ff0
fetched_at: '2026-06-28T22:37:21.382253+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ao tornar um Contrato
  Vigente ou Aprovar alçada de Contrato ou Revisão ocorre a Mensagem: AJUDA:OBRIGAT
  - Um ou mais campos obrigatórios não foram preenchidos'
type: support-article
updated_at: '2026-06-24T14:24:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41183523503383-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ao-tornar-um-Contrato-Vigente-ou-Aprovar-al%C3%A7ada-de-Contrato-ou-Revis%C3%A3o-ocorre-a-Mensagem-AJUDA-OBRIGAT-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos
---

Ao tornar um contrato Vigente ou Aprovar alçada de Contrato ou Revisão no TOTVS Gestão de Contratos, pode ocorrer a mensagem de erro "AJUDA:OBRIGAT" devido a campos obrigatórios não preenchidos na geração automática dos títulos financeiros "PR". Isso ocorre porque o sistema preenche apenas os campos obrigatórios padrão, e campos adicionais marcados como obrigatórios no configurador não são preenchidos. A solução é retirar a obrigatoriedade desses campos ou implementar customização para preenchê-los.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41183507974935) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Ao tornar mudar a situação e tornar um contrato Vigente ocorre a mensagem:

HELP - AJUDA:OBRIGAT - Um ou mais campos obrigatórios não foram preenchidos

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Ao Tornar um contratos Vigente ou Aprovar alçada de Contrato ou Revisão de Contrato, nos contratos que possuem Cronograma Financeiro, por padrão são ou podem gerados títulos financeiros "PR" referente às parcelas do Cronograma Financeiro.

Nesta geração, o sistema em seu padrão grava apenas os campos que são obrigatórios por padrão na inclusão do título, não sendo preenchidos outros campos que possam ser colocados como obrigatório na tabela do título pelo cliente.

A mensagem **"AJUDA:OBRIGAT"** em questão está relacionada a no ambiente em questão haver um campo na tabela de títulos que está sendo gerado, que está marcado como "Obrigatório" em seu cadastro no Configurador e o mesmo não estar sendo preenchido.

No caso, para não ocorrência do erro, deve-se retirar a obrigatoriedade dos campos que não são obrigatórios por padrão das tabelas de títulos. (Onde normalmente, na mensagem retornada pelo sistema, aparece a descrição/nome do campo)

Ou caso deseje pode-se avaliar a possibilidade através de uma customização para preenchimento destes campos no momento da geração dos títulos PR, conforme a necessidade.  
Abaixo artigos com os pontos de entrada disponíveis da rotina para que se possa avaliar o que melhor possa atender conforme a necessidade.  
   
[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ponto de Entrada Padrão MVC para a rotina de Manutenção de Contratos CNTA300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021875031-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ponto-de-Entrada-Padr%C3%A3o-MVC-para-a-rotina-de-Manuten%C3%A7%C3%A3o-de-Contratos-CNTA300)  
   
[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Acervo de Pontos de Entrada do módulo Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016678671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Acervo-de-Pontos-de-Entrada-do-m%C3%B3dulo-Gest%C3%A3o-de-Contratos)

***Saiba Mais:***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Conceito dos Títulos Provisórios (PR) gerados no Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32792869776663-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Conceito-dos-T%C3%ADtulos-Provis%C3%B3rios-PR-gerados-no-Gest%C3%A3o-de-Contratos)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
