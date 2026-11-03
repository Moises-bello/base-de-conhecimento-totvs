---
content_hash: 7d4a3fb54a02ce89af9cd5ae1ed433d9e554336aab34908334583a95d2ede867
fetched_at: '2026-06-29T00:09:53.031633+00:00'
page_id: '440829201'
product: rm
source: tdn-rm
title: FIN - Controle Orçamentário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440829201
version: 15
---

**Controle Orçamentário**

O controle gerencial além de controlar o orçamento de despesa dentro do financeiro, controla também o orçamento de receita. Com o financeiro integrado ao controle orçamentário o sistema disponibiliza opções de ações sobre o lançamento ao exceder despesa e também receita. Esse controle será definido nos parâmetros do sistema por coligada com as seguintes opções:

Ação sobre o lançamento ao exceder despesa:

* Barra
* Avisa
* Bloqueia
* Não avisa

Ação sobre o lançamento ao exceder receita:

* Avisa
* Não avisa

**Tipo de Documento**

Para controle de orçamento, é preciso definir no Tipo de Documento se o controle será somente para lançamentos a receber, se somente para lançamentos a pagar ou para ambos.

* Se o controle for somente de despesa, defina que o tipo de documento será a pagar e defina qual a ação sobre o orçamento, aumenta o realizado, diminui o realizado ou nenhum efeito.
* Se o controle for somente de receita, defina que o tipo de documento será a receber e qual será a ação sobre o orçamento, aumenta o realizado, diminui o realizado ou nenhum efeito.
* Agora se o controle orçamentário for tanto de despesa quanto para receita, basta definir que o tipo de documento será a pagar e a receber (ambos), defina qual será a ação sobre o orçamento (aumenta realizado, diminui realizado ou nenhum efeito).

Ao informar a ação de aumenta ou diminui o realizado o campo Afeta orçamento para\* ficará habilitado, para que seja definido qual tipo de lançamento afetará o orçamento, se o lançamento for a apagar, se for a receber ou “a pagar e a receber”.

**Observações**

* O campo “Afeta Orçamento para” só será habilitado se o tipo de documento tem efeito sobre o orçamento e ficará indisponível se tipo de documento somente "A pagar" ou "A Receber".
* O controle de orçamento de receita do financeiro só estará disponível a partir da versão 12.1.23.
* O default para o campo afeta orçamento para será “A Pagar”.

**Processos que afetam o controle de orçamento**

* Inclusão de lançamento
* Alteração de data de emissão
* Alteração de valor original
* Alteração de centro de custo e ou Natureza orçamentária
* Alteração de Tipo de Documento
* Cancelamento do Lançamento
* Alteração global dos campos: valor Original, data de emissão, tipo de documento, centro de custo.
* Geração de lançamento padrão

**Processos que não afetam o controle de orçamento**

* Gerar Acordo
* Parcelamento
* Geração de borderô
* Remessa de pagamento
* Desvincular Lançamento do Borderô

**Tabelas relacionadas**

* FTDO.AFETAORCAPARA

 Veja Também

* [Tabelas de Orçamento](http://tdn.totvs.com/x/w8pEGQ)
* [Importação de Orçamento](http://tdn.totvs.com/x/38dEGQ)
* [Cadastro dos Valores Orçados](http://tdn.totvs.com/x/yshEGQ)
* [Consultar Valores de Orçamento](http://tdn.totvs.com/x/n8hEGQ)
