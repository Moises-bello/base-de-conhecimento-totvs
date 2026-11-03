---
content_hash: 86973a7ad71c5710e636d7d44f9a3c26e91112d581c4cbb7ba86fb506613e72b
fetched_at: '2026-06-29T00:09:19.536869+00:00'
page_id: '422545604'
product: rm
source: tdn-rm
title: Grupo de Tributação do ICMS para UF de Destino
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545604
version: 8
---

A [Emenda Constitucional 87/15](http://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc87.htm), altera a forma de repartição do ICMS entre os Estados de Origem e Destino da mercadoria, introduzindo o Diferencial de Alíquotas nas operações de venda, através de comércio eletrônico, para consumidor final não contribuinte. O cálculo do Grupo de Tributação do ICMS para a UF de destino (ICMSUFDest) será preenchido respeitando todas as regras a seguir:

1. Para operações Interestaduais;
2. Operação para Consumidor Final;
3. Operações para destinatário Não Contribuinte do ICMS;
4. NF-e com de emissão anterior à 01/01/2016.

Para que o cálculo seja corretamente feito deverá:

* Ser criada uma Regra de ICMS com o tipo Tributado e Operação Tributária igual a Diferencial de Alíquota;
* Na Regra de ICMS a alíquota da operação deverá ser a correspondente com a operação interestadual da Filial emissora com o Estado de destino;
* No campo Alíquota Interna D.A. deverá ser informada a alíquota interna do Estado de Destino e também o % ICMS UF Destinatário e % FCP para que seja gerado o grupo ICMSUFDest referente ao ICMS compartilhado entre as UF´s.

A tags vFCPUFDest, vICMSUFDest e vICMSUFRemet serão calculadas automaticamente pelo sistema quando houver alíquotas informadas no cadastro da Regra de ICMS vinculada ao cadastro da Natureza selecionada no movimento.   
O Cálculo da tag **vFCPUFDest** Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) da UF de destino será feito considerando a fórmula a seguir:

* Base de Cálculo do ICMS   (%FCP-Fundo de Combate à Pobreza ¹ 100)

O Cálculo da tag **vICMSUFDest** - Valor do ICMS Interestadual para a UF de destino, já considerando o valor do ICMS relativo ao Fundo de Combate à Pobreza naquela UF será feito considerando a fórmula a seguir:

* (((Base de Cálculo do ICMS   (Alíquota S.T./Interna D.A.(%) ¹ 100))  ((Base de Cálculo do ICMS   Alíquota ICMS(%) ¹ 100)))   ( %ICMS UF Destinatário ¹ 100)

O Cálculo da tag **vICMSUFRemet** - Valor do ICMS Interestadual para a UF do remetente será feito considerando a fórmula a seguir:

* Valor do ICMS Interestadual para UF de destino (((Base de Cálculo do ICMS  (Alíquota S.T./Interna D.A.(%) ¹ 100))   ((Base de Cálculo do ICMS  Alíquota ICMS(%) ¹ 100)))

**Onde¹**  corresponde ao sinal de divisão.

Legislação

* [Nota Técnica 2015.003](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=uXFlhOSgUZc=)
* [Emenda Constitucional nº 87, de 16 de Abril de 2015](http://www.planalto.gov.br/ccivil_03/constituicao/Emendas/Emc/emc87.htm)
