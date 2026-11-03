---
article_id: 360012372011
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: a383d1737eb70805545a92bbd1c716ae453f912ae200709ffbf6aa2eebbee444
fetched_at: '2026-06-28T22:40:32.355210+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - HELP: SEMPERM usuário
  sem permissão para efetuar Lançamentos Contábeis'
type: support-article
updated_at: '2023-12-01T16:18:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012372011-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-HELP-SEMPERM-usu%C3%A1rio-sem-permiss%C3%A3o-para-efetuar-Lan%C3%A7amentos-Cont%C3%A1beis
---

**Ocorrência**

Quando usuário tentar efetuar Lançamentos Contábeis pelas rotina **CTBA101 (Lançamento Contábil)** e **CTBA102 (Lançamento Contábil - Automático)** é apresentado **HELP: SEMPERM**

![sem_perm.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008636211)

**Ambiente**Microsiga Protheus - Contabilidade Gerencial - A partir da Versão 11.80

**Causa**

Este **HELP** é apresentado quando o **Acesso '191'** do **Cadastro Usuário** ou **Grupo de Usuários** está desmarcado.

**Solução**

Primeiramente verificar o **Cadastro de Usuários (CFGA510)**

**1.** Acesse o **Configurador (SIGACFG);**  
 **2.** Usuário > Senhas > **Usuários;**  
 **3.** Selecione o Usuário > **Alterar;**  
**4.** Aba **Restrições de acesso** > **Acessos;**  
**5.** Verifique se o Acesso '**191 - Permite efetuar lançamentos manuais através da rotina Lançamentos Contábeis**' está **Marcado;**

![sem_perm1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008610212)

Caso no cadastro de usuário esteja correto, verifique no **Cadastro de Grupos (CFGA520)**

**1.** Acesse o **Configurador (SIGACFG);  
 2.** Usuário > Senhas > **Grupos;  
 3.** Selecione o Grupo > **Alterar;  
4.** Aba **Restrições de acesso** > **Acessos;  
5.** Verifique se o Acesso '**191 - Permite efetuar lançamentos manuais através da rotina Lançamentos Contábeis**' está **Habilitado;**

**![sem_perm1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008610212)**

**Saiba mais  
[MP - SIGACTB - CTBA102 -Exclusão de lançamentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007062792-MP-SIGACTB-CTBA102-Exclus%C3%A3o-de-lan%C3%A7amentos)**

**[MP- SIGACTB - HELP ENTIDOBRIG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006689572-MP-SIGACTB-HELP-ENTIDOBRIG)**
