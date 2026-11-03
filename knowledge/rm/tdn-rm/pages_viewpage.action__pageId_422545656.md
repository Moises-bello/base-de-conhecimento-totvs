---
content_hash: 3b7f4a4b88d25ce1a9e11bf3e471c6154c5f22c7b29d1b89f4180bdbafbf9f20
fetched_at: '2026-06-29T00:09:20.083224+00:00'
page_id: '422545656'
product: rm
source: tdn-rm
title: Período de Apuração (Cadastro)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545656
version: 11
---

O cadastro do Período da Apuração é composto das seguintes abas e campos:

**Identificação:**

* Código do Tributo
* Observação
* Início de Período
* Fim de Período
* Status do Período

**Apuração:**  
 Nesta pasta o usuário terá as informações de:

* Saldo Anterior Tributo
* Saldo Credor/Devedor
* Saldo Original
* Data Vencimento
* Débito Extemporâneo
* Total ICMS D.A. Entrada
* Valor FECP
* Valor FECP Consumidor Final

**Agrupador Regime Especial / Simples:**

* Alíquota Apuração
* Valor Faturamento
* Valor Exclusões Faturamento
* Valor Receita Bruta
* Receita Tributável
* Receitas Não Operacionais

**Outros Dados:**

* Local Entrega
* Data Entrega
* Observação de Entrega
* Histórico

**Valores Adicionais Apuração:**

* Código
* Valor
* Descrição

**Apuração Diferencial de Alíquota:**

* UF

**Agrupador Diferencial de Alíquota Crédito:**

* Crédito Diferencial de Alíquota
* Outos Crédito
* Estorno de Débitos
* Valor Deduções

**Agrupador Diferencial de Alíquota Débito:**

* Débito Diferencial de Alíquota
* Outos Débitos
* Estorno de Crédito

**Agrupador Saldo:**

* Saldo Credor/Devedor Anterior
* Saldo Devedor Antes das Deduções
* Saldo Credor/Devedor
* Agrupador Extra Apuração:
* Valor Débitos Especiais

**Agrupador FCP (Fundo de Combate a Pobreza)**

**Crédito**:

* Valor FECP Entrada
* Outros Créditos
* Estorno de Débito
* Valor Deduções

**Débito**:

* Valor FECP Saída
* Outros Débitos
* Estorno Crédito

**Agrupador Saldo:**

* Saldo Credor/Devedor Anterior
* Saldo Devedor Antes das Deduções
* Saldo Credor/Devedor
* Agrupador Extra Apuração:
* Valor Débitos Especiais

***Observações*:**O sistema calculará o [Crédito Outorgado](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422545889) referente aos serviços de Transporte automaticamente durante o encerramento dos períodos.   
 O cálculo será efetuado aplicando o percentual definido no Cadastro de Filiais - Anexos | Dados Fiscais | Tributos, sobre o saldo do débito do período, ou seja, do somatório do valor informado no campo Valor de ICMS do Lançamento Fiscal.   
 Serão considerados para esta totalização apenas os Lançamentos Fiscais de Saída associados aos códigos de Naturezas de Operação dos grupos 5.35X e 6.35X.  
 Somente serão considerados Lançamentos Fiscais de Saída associados às Naturezas Fiscais.  
 Lançamentos Fiscais Estornados e/ou Cancelados não serão selecionados para este cálculo.  
Acesse o link para maiores informações em relação ao [Crédito e Débito Extemporâneo - Outras Informações](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422545863).

* **Total ICMS D.A (Diferencial de alíquota) Entrada**  
  O Sistema calculará o valor do ICMS diferencial de alíquota referentes às Operações Interestaduais de Compra para o Ativo Imobilizado / Uso e Consumo em que a alíquota do Estado Origem é inferior a alíquota do Estado destino da mercadoria.   
  ***Atenção*:**Não será permitido incluir guias manuais ou automáticas caso o campo Data Vencimento não esteja preenchido.

**Detalhamento:**Essa pasta é habilitada para os impostos do Tipo IRPJ, CSLL, PIS, COFINS, OUTROS E RET.

**ICMS ST:**Ao encerrar o período deste tributo, o sistema calculará os saldos do imposto por Unidade de Federação com base nos Lançamentos Fiscais de Entrada/Saída com Incidência de ICMS ST.   
 No momento em que o encerrar o Período de ICMS ST, o sistema irá totalizar o ICMS ST Total Devido, totalizar o ICMSST Retido na Chancela e o valor do ICMS a Pagar.  
Maiores detalhes em .
