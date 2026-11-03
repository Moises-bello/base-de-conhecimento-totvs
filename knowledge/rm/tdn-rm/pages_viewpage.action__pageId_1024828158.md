---
content_hash: 22e911384ec66a4068582804250b97eb3522f535c8a1f92a7f6f5f3f13ba5f5f
fetched_at: '2026-06-29T00:05:48.487212+00:00'
page_id: '1024828158'
product: rm
source: tdn-rm
title: Propostas - Ajuste de Inconsistências
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1024828158
version: 4
---

### Introdução

---

O **Ajuste de Inconsistência** é uma ferramenta de diagnóstico e correção destinada a regularizar propostas originadas no Portal de Imóveis que apresentaram falhas de dados durante a integração com o RM, que ficaram impossibilitadas de serem carregadas normalmente na visão de Propostas.

**Por que isso acontece?** Eventuais instabilidades ou oscilações na rede podem afetar a comunicação entre o Portal de Imóveis e o sistema RM no momento da criação do registro. Isso pode resultar em propostas gravadas sem informações essenciais, como:

* Dados do Comprador ou Comprador Principal;
* Vínculo com Tabelas de Preço.

**Procedimentos para Utilização**

---

Ao carregar as propostas, em *Frontend / Propostas*, clique em "*Filtros*".

Selecione o Filtro "Propostas Inconsistentes".

Esta tela, ao carregar, vai listar de forma simplificada somente as propostas com algum tipo de inconsistência.

No exemplo da imagem, duas propostas, Uma sem tabela de preço e outra, sem comprador.

Ao executar a ação de ajuste, indo no botão "..." e selecionando "Ajustar inconsistência" o sistema recupera e corrige os dados faltantes para cada proposta selecionada.

Após o processamento, será exibido um resumo das alterações realizadas.

Uma vez corrigida, a proposta estará apta e novamente visível nas visões padrão de **Propostas** ou **Contratos**.

Quando uma proposta está inconsistente, porém, seu status é "**Cancelada**" há também a possibilidade de excluí-la, diretamente pelo menu de ajuste. Obs.: a situação tem que estar parametrizada para permitir exclusão.
