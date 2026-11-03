---
article_id: 360025017533
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 5f19d96b05a9ff8ad60ff2b3185dbfefeab6d8666aae899cfd14bfd5a8acc2e3
fetched_at: '2026-06-28T22:38:38.590505+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Nota sobre preenchimento
  do campo C6_COMIS
type: support-article
updated_at: '2022-11-08T13:38:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025017533-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-sobre-preenchimento-do-campo-C6-COMIS
---

**Dúvida**

O sistema preenche indevidamente como percentual de comissão do produto em todos campos de comissão dos itens do pedido do venda (SC6). 

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Não se trata de um erro, o sistema carrega as informações por default em todos os campos de comissão no grid tabela **SC6**, pois a comissão é referente ao produto informado.

As informações de comissão exibidas em tela não alteram o comportamento na posterior geração da comissão, que será efetuada somente após o faturamento ou baixa de título (conforme configuração). Por exemplo:

Caso tenha sido preenchido somente um vendedor no Pedido de Venda (**mata410**), o campo **C5\_VEND1**, será gerada somente uma comissão com a porcentagem correspondente à estabelecida no campo de comissão **C6\_COMIS1**.

Caso necessite limpar os demais campos ou zerar o percentual de comissões no item , o procedimento poderá ser efetuado manualmente ou tratar por ponto de entrada, podendo utilizar o ponto de entrada **M410LIOk (<https://tdn.totvs.com/pages/viewpage.action?pageId=6784149>).**

**Saiba mais:**

**[FAT0036\_Hierarquia\_priorização\_de\_busca\_de\_comissão\_para\_gerar\_comissão\_ao\_vendedor\_sobre\_Pedido\_de\_Vendas](http://tdn.totvs.com/pages/viewpage.action?pageId=232818579)**
