---
content_hash: 611cd1930f793759156c04c535f7f702eef76c9873eb2b50bbace80e21f8f844
fetched_at: '2026-06-29T00:09:19.217712+00:00'
page_id: '421388830'
product: rm
source: tdn-rm
title: Conversão da contabilização de inclusão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388830
version: 3
---

Na migração do sistema para a contabilização on-line teremos duas situações a observar em relação à contabilização de inclusão do lançamento financeiro:

* Inclusão de lançamento contabilizada no modelo antigo de contabilidade e que não foi exportada para o módulo Gestão Contábil;
* Inclusão de lançamento contabilizada no modelo antigo de contabilidade e que foi exportada para o módulo Gestão Contábil.

Caso seja necessário estornar estas contabilizações, foram disponibilizadas rotinas que podem ser executadas pontualmente. No primeiro caso, contabilização não exportada, foi criado o botão "Estornar Contabilização" na tela da contabilização de inclusão, que pode ser acessada pelo botão "Inclusão" na aba Dados Adicionais do lançamento financeiro.

Para o segundo caso foi criado o processo "Conversão Contabilização Inclusão" disponível na opção Processos | Manutenção de Lançamentos no lançamento financeiro.  
 As duas rotinas estornam a contabilização antiga e regeram a contabilização de inclusão já no formato do novo modelo contábil.
