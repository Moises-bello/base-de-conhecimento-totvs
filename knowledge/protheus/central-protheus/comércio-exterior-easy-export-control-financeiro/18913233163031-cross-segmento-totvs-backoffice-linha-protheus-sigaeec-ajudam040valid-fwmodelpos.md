---
article_id: 18913233163031
category: Comércio Exterior - Easy Export Control - Financeiro
content_hash: 5042a78e2eef3e4cfac6149005750ad0e4e44e055cd5c29e04712dbb8cf88b12
fetched_at: '2026-06-28T22:36:58.183274+00:00'
product: protheus
section_id: 1500001538221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus- SIGAEEC-  AJUDA:M040VALID
  FWMODELPOS - Modelo invalido
type: support-article
updated_at: '2023-11-08T14:13:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18913233163031-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-AJUDA-M040VALID-FWMODELPOS-Modelo-invalido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18913242211863) Tempo aproximado para leitura:**00:02:00 min**

**Dúvida**

Ao tentar remover a data de embarque/exclusão de adiantamento, o sistema acusa falha de integração com financeiro **AJUDA:M040VALID FWMODELPOS - Modelo invalido,** como resolver ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – A partir da versão 12.1.2210.

**Solução**

A mensagem apresentada é de validação do módulo Financeiro, verifique todas as tabelas **FK´s** que devem possuir o mesmo compartilhamento de tabelas da **SE5** com exceção a tabela **FKB**.

Geralmente apresentada por rotinas desatualizadas no Financeiro, realize um teste de inclusão diretamente no módulo financeiro.

**Saiba mais**

[Reestruturação da tabela SE5 na família de tabelas FKx](https://tdn.totvs.com/pages/releaseview.action?pageId=203760476)

[Modulo 06 Financeiro Acumulado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005363562-Cross-Segmento-Protheus-Backoffice-Linha-Protheus-SIGAFIN-Atualiza%C3%A7%C3%A3o-do-Ambiente-Modulo-06-Financeiro-Acumulado)
