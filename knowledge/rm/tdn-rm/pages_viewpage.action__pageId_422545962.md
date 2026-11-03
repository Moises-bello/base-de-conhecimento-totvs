---
content_hash: 8d04c15505debfaa80852798a151ffe7d5c0990aedf3bf4465f9952dddccfcde
fetched_at: '2026-06-29T00:09:22.090245+00:00'
page_id: '422545962'
product: rm
source: tdn-rm
title: Cálculo CIAP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545962
version: 18
---

# Conteúdo 4Conteúdo

## **1. Regras de Parametrização**

As mercadorias adquiridas pelas empresas e que serão destinadas ao ativo imobilizado podem se creditar do CIAP. Este controle pode ser feito pelo Totvs Gestão fiscal desde que feita as devidas para parametrizações  e obedecendo a regras do sistema.

**Regras e Parametrizações para apuração do crédito de ICMS:**

* Nos parâmetros do fiscal em apuração de icms , selecionar no cadastro de filial o município que irá fazer o controledo ciap, livro e data;
* Nos parâmetros de processo  calculo CIAP em grupos e subgrupos informar as cfops tributadas de saída e as cfops não tributadas informações importante para o calculo do CIAP, veja a [Documentação](https://tdn.totvs.com/pages/viewpage.action?pageId=490650588#Processos-289824006).
* Cadastro da natureza fiscal de ativo imobilizado com tipo de operação igual a ativo permanente  na aba outros dados;
* Cadastro da data de aproveitamento de credito no lançamento de entrada
* Informar a chapa do bem no item do lançamento previamente cadastrada seja no TOTVS Gestão Fiscal em cadastro bens ou através da gestão patrimonial em cadastro, patrimônio (cadastro conforme licença de uso)
* No item do lançamento ter o valor do ICMS destacado no documento fiscal, este valor servirá de base para calculo do crédito do Imposto;

## **2. Controle de crédito**

**No TOTVS Gestão Fiscal existem 3 opções de controle de crédito de icms referente ao Ativo Imobilizado**

0Lançamento de entrada

Lançamento de entrada | obrigações principais | entrada

**Processo:**

* Criar o código de patrimônio para ser vinculado ao item na inclusão do lançamento de entrada (seja pelo cadastro de bem no Totvs Gestão Fiscal  ou cadastro de patrimônio (no Totvs Gestão Patrimonial)
* Incluir o lançamento referente a nota de entrada do bem.
* Na aba situações tributárias selecionar CFOP de Ativo Imobilizado.
* Informar a data de início de crédito
* Na aba item, informações adicionais, patrimônio, associar o patrimônio criado.
* Na aba item, informações adicionais, referências, outros dados informar o tipo de movimentação do bem.
Lançamento de Ativo Imobilizado

Lançamento de Ativo Imobilizado | obrigações principais | mais

**Processo:**

* Incluir um novo registro.
* Informar os dados referente a nota de compra do bem e a data de início de credito, na aba identificação.
* Na aba itens informar o produto e patrimônio criado anteriormente e os valores ICMS, diferencial de alíquota e frete caso existam.
Integrar Aquisições de Compra

Integrar aquisições de compra | Patrimônio | Integrações

**Processo:**

* Inclusão da nota de compra pelo modulo TOTVS gestão de estoque compras e faturamento
* Informa no movimento na aba integrações, fiscal a data de aproveitamento do crédito de ICMS.
* No TOTVS gestão patrimonial na aba relatórios/integrações em integrar aquisições de compra.

Nesta etapa é possível através da nota selecionada herdar algumas informações do documento a serem levadas para a geração do patrimônio através do item da nota de forma automática.

Você tem a opção de gerar patrimônios individuais ou constituir patrimônio

Na integração de patrimônio, na aba tipos de campos você tem a opção de constituir patrimônios ou avançar. Se desejar avançar ele irá gerar o patrimônio sem fazer a constituição de um patrimônio a partir dos itens da nota baseada nas configurações do processo. Se clicar em constituir patrimônios ele abrira uma nova tela composta de duas abas, a aba nota onde é apresentado os dados da nota fiscal e a aba patrimônio onde ele agrupa todos os itens selecionados para a constituição de um patrimônio. Para maiores detalhes acesse **[Composição do Patrimônio](https://tdn.totvs.com.br/pages/viewpage.action?pageId=423938345).**

## **3. Cálculo do crédito**

Os documentos referentes a aquisição de imobilizado e que apresentam ICMS destacado na nota, ICMS diferencial de alíquota e ICMS sobre frete serão considerados para o cálculo do CIAP e divido por 48 avos para as empresas se [creditarem](https://tdn.totvs.com/pages/releaseview.action?pageId=422546005) das compras de ativo imobilizado o cálculo será executado como base nas vendas tributadas parametrizadas e não tributadas conforme mencionado anteriormente.

As informações referente ao crédito de ICMS do CIAP para constituição de patrimônio serão enviadas para o [SPED Fiscal](https://tdn.totvs.com/display/public/LRM/SPED+Fiscal+-+Bloco+G#BLOCOG-Demais%20Informa%C3%A7%C3%B5es.) em demais informações.

## **4. Relatório CIAP**

Verifique como gerar o Relatório CIAP a partir da Documentação [Relatório CIAP](https://tdn.totvs.com/pages/viewpage.action?pageId=874203128)
