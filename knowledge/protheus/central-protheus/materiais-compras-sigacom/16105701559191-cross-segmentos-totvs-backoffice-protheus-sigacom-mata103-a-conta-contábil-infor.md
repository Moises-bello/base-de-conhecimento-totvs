---
article_id: 16105701559191
category: Materiais - Compras (SIGACOM)
content_hash: 2bca2c2bab1fff84d40eaa45a2a0e48f62b0cbf50a797599403df4a3dfb63491
fetched_at: '2026-06-28T22:41:20.055890+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MATA103 - A conta contábil
  informada no pedido de compras é apagada após atualizar (dar enter) o campo D1_CONTA
  do documento de entrada
type: support-article
updated_at: '2023-07-18T13:08:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16105701559191-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA103-A-conta-cont%C3%A1bil-informada-no-pedido-de-compras-%C3%A9-apagada-ap%C3%B3s-atualizar-dar-enter-o-campo-D1-CONTA-do-documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16105690424727) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Após vincular um pedido de compras no documento de entrada e atualizar (pressionar *enter)* o campo D1\_CONTA, a conta contábil informada no pedido de compras desaparece do campo D1\_CONTA do documento de entrada.

**Ambiente**Protheus – Compras – A partir da versão 12.1.33  
  
**Solução**

O preenchimento padrão dos campos no item da Nota Fiscal obedece as seguintes regras:

1) Se o campo estiver vazio, ele é preenchido com o conteúdo do campo do cadastro de Produto.  
2) Se já estiver preenchido, ao alterar o produto do item da nota, o conteúdo dos campos descritos é mantido conforme o que já estava preenchido, exceto para o campo *D1\_CONTA.* No caso do campo *D1\_CONTA*, o padrão de preenchiment*o* é sempre sobrescrever o conteúdo do campo com àquele que corresponde ao cadastro de Produtos*.*

Assim, se o ponto de entrada *MT103CPO* estiver compilado e alguma posição do vetor de retorno possuir algum campo da nota, dentre os descritos, o conteúdo será preenchido conforme o cadastro de Produto, porém, no caso específico do campo *D1\_CONTA*, se ele for informado no vetor de retorno, não será carregado o conteúdo do cadastro de Produto.

Segue abaixo o link com a documentação relacionada:

[<https://tdn.totvs.com/pages/releaseview.action?pageId=6085731>]

**Saiba Mais*****:***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar para Apagar ou Não as Entidades Contábeis nos itens do Documento de Entrada ao Informar o Rateio ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061906214-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-para-Apagar-ou-N%C3%A3o-as-Entidades-Cont%C3%A1beis-nos-itens-do-Documento-de-Entrada-ao-Informar-o-Rateio-?source=search)

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
