---
content_hash: f24a67fc92643f723fe22c2807a60c7abbff6f8115dbb706c5f789634ab7392d
fetched_at: '2026-06-29T00:10:19.475066+00:00'
page_id: '4814538'
product: rm
source: tdn-rm
title: Cálculo de Saldo Devedor com Valores Opcionais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4814538
version: 4
---

BLOCK

Cálculo de Saldo Devedor com Valores Opcionais

FAQ: **Cálculo de Saldo Devedor com Valores Opcionais**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.20 |

Avaliação

Esse Documento auxiliará o usuário na Configuração dos Valores Opcionais dos Componentes de uma venda imobiliária.

Solução

**Alerta de Configuração Incorreta dos Valores Opcionais.**

Essa mensagem costuma ser apresentada ao iniciar o sistema do TOTVS Incorporação ou TOTVS Gestão Financeira e corresponde aos Valores Opcionais cadastrados nos Componentes do TOTVS Incorporação.

O alerta é meramente informativo, não gerando nenhum tipo de erro. Ele apenas indica quais são os Tipos de Componentes que estão recebendo os Valores Opcionais no sistema.

Os valores são utilizados no envio de informações do TOTVS Incorporação para o TOTVS Gestão Financeira, como o envio de Valores de Juros que é um Componente de Correção sendo um valor a ser acrescentado em uma determinada parcela.

O Cadastro dos Valores Opcionais é feitos através dos Parâmetros do TOTVS Gestão Financeira em Opções / Parâmetros / RM Fluxus / Contas a Pagar / Manutenção de Lançamentos / Valores Opcionais.

O Usuário poderá Parametrizar o Valor Opcional conforme o Componente que deseja associar no TOTVS Incorporação, no caso dos Juros Fixos será um Componente de Correção, logo, deverá ser parametrizado como Acrescentar.

Para cadastrar os *Tipos de Componentes a*cesse:

***Cadastros / Condições de Vendas / Tipo de Componente.***

Após a realização do filtro, favor buscar o Tipo de Componente de Juros Fixos e abrir a visão de Componentes em Anexo.

**\* Apenas Tipos de Componentes de Seguro, Juros e Correção deverão receber esses Valores Opcionais.**

Ao abrir a visão de Componentes dessa maneira, o usuário poderá verificar os Componentes do Tipo Juros Fixos que estão associados a um mesmo Valor Opcional do TOTVS Gestão Financeira.

Os valores Opcionais do Componente de Juros Fixos deverão ser parametrizados como Componentes de um mesmo Tipo de Componente com o mesmo valor opcional. Sendo que nenhum desses valores poderão estar com o Valor Opcional em branco ou diferente, pois gerará uma inconsistência no Momento da Baixa no TOTVS Gestão Financeira, impedindo tal processo.

Observações

I**nformações Adicionais**

*Esse documento o auxiliará a entender o conceito de Valores Opcionais no TOTVS Gestão FInanceira para o Sistema.*
