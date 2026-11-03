---
article_id: 360018747331
category: Materiais - Compras (SIGACOM)
content_hash: cc9329abfaa1c8f7ff80b06adbbf443371fef3e91d33c90aafbbfd1bedf30f69
fetched_at: '2026-06-28T22:41:18.909157+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help EMPTYFORM  ao
  cadastrar solicitantes
type: support-article
updated_at: '2022-05-18T20:58:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018747331-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-EMPTYFORM-ao-cadastrar-solicitantes
---

**Dúvida**Ao realizar o cadastramento de solicitantes no módulo Compras, o sistema apresenta *help* "EMPTYFORM - Problema: O formulário Solicitantes (SAI\_GD) não foi preenchido".

Como concluir o cadastro?   
  
**Ambiente**Microsiga Protheus – Compras – A partir da versão 12.1.017  
  
**Solução**

O *help* é gerado devido a estrutura de desenvolvimento da rotina (MVC), o qual verifica a consistência entre as informações cadastradas na sessão Produtos e Entidades Contábeis, quando informada uma entidade contábil.  
Deste modo se o solicitante possuir vinculo com entidade contábil, informe na sessão Produto a condição '\*' no campo que deseja realizar o controle (ex: Produto).

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
