---
article_id: 360018927811
category: Contabilidade Gerencial - Entidades
content_hash: 31c02fda19bde850ad09c53154b150c1a699bddc1b065d889c5fc4470625feaa
fetched_at: '2026-06-28T22:40:49.804644+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: 'MP - SIGACTB: Como configurar a rotina de privilégios (CFGA530) para efeito
  no cadastro do Centro de Custo, Item Contábil e Classe de Valor?'
type: support-article
updated_at: '2022-09-08T17:09:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018927811-MP-SIGACTB-Como-configurar-a-rotina-de-privil%C3%A9gios-CFGA530-para-efeito-no-cadastro-do-Centro-de-Custo-Item-Cont%C3%A1bil-e-Classe-de-Valor
---

**Dúvida**Como configurar a rotina de privilégios (CFGA530) para efeito no cadastro do Centro de Custo, I. Contábil e Classe de Valor?  
  
**Ambiente**Protheus – SIGACTB – A partir da versão 11.80  
  
  
**Solução**

Somente se pode realizar o bloqueio de funções cadastradas no menu do módulo. Ou seja, ao acessar a rotina CTBA180 e selecionar por exemplo, Centro de Custos (CTBA030) sem ser pelo menu, então neste caso o bloqueio não surte efeito.

Neste caso, o correto a se fazer é efetuar bloqueio completo da rotina CTBA180. E através da rotina de configurador de menu(CFGX013) incluir no menu a rotina CTBA030(Centro de custo) dentro da raiz "Entidades" e realizar o Bloqueio dos menus da rotina CTBA030 de acordo com a necessidade.

O mesmo processo deverá ser executado para o cadastro de Item Contábil e classe de valor.
