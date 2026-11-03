---
content_hash: df23a1f16fbf2b2949c0f25a7838c2c7d2e9daa09763eaf91dedbd5b6c000277
fetched_at: '2026-06-29T00:09:44.369982+00:00'
page_id: '431681119'
product: rm
source: tdn-rm
title: Natureza Inversa para Importação XML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=431681119
version: 4
---

Cadastros | Natureza de Operação | Anexos | Natureza Inversa para Importação de XML, é onde deverão ser cadastradas as possíveis naturezas de operação inversas para uma determinada natureza sintética.  
Uma natureza de operação sintética, poderá ter a ela vinculada, várias naturezas de operação inversas, sejam elas sintéticas ou analíticas.  
Entre as naturezas inversas cadastradas, o usuário poderá definir ‘Defaults’, ou seja, registros que devem ser considerados prioritários caso existam várias naturezas possíveis para um determinado movimento.  
Este cadastro será utilizado apenas caso através da aplicação das Regras de Seleção da Natureza tenha sido encontrada mais de uma natureza inversa possível para o item. O sistema procederá da seguinte forma:

* Se apenas uma das naturezas selecionadas estiver cadastrada como ‘Default’, ela será utilizada para a criação de movimento;
* Se mais de uma das naturezas selecionadas estiver cadastrada como 'Default", o sistema não saberá qual Natureza Inversa escolher e o movimento será criado com o Status Inclusão via arquivo XML como ‘Natureza Incompleta';
* Se apenas uma das naturezas selecionadas estiver cadastrada como Natureza Inversa, mesmo não sendo como ‘Default’, ela será utilizada para a criação do movimento;
* Se mais de uma das naturezas selecionadas estiver cadastrada como Natureza Inversa mas nenhuma delas é 'Default", o sistema não saberá qual Natureza Inversa escolher e o movimento será criado com o Status da Inclusão via arquivo XML como ‘Natureza Incompleta';
* Se nenhuma das naturezas selecionadas estiver no cadastro de Natureza inversa, o movimento será criado com o Status da Inclusão via arquivo XML como ‘Natureza Incompleta'.
