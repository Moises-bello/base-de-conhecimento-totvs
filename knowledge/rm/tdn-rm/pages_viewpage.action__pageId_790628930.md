---
content_hash: 47e973c6add0414d7f269b77d085392f6c63ecd390cb4111a86d341acfb5c78c
fetched_at: '2026-06-29T00:11:39.843774+00:00'
page_id: '790628930'
product: rm
source: tdn-rm
title: Escrituração de Lançamento Fiscais - ICMS Monofásico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=790628930
version: 10
---

42Cadastro do TributoCadastro do Tributo

No cadastro do tributo é imprescindível que exista **apenas um tributo ICMS cadastrado**.

Para ser calculado o ICMS Monofásico é necessário selecionar a opção "Pauta do Produto" no parâmetro Burcas Alíquota do cadastro do tributo.

Acesse Cadastros | Tributos e cadastre o tributo IPI Pautado com as seguintes informações:

**Sigla**: ICMS

**Tipo tributo fiscal**: ICMS

**Abrangência do Tributo**: Mensal

**Tipo**: Variável

**Incidência**: Produto

**Buscar Alíquota:** Pauta do Produto

Figura2Cadastro do ProdutoCadastro do Produto

Necessário o preenchimento da Pauto do Produto no cadastro do produto

Acesse o menu Cadastro | Produto | Anexo | Pautas do Produto e preencher os seguintes campos pertinentes a pauta do produto:

**Estado**: Selecionar o estado de acordo com operação.

**Código do Tributo**: Preencher do tributo a ser considerado na pauta (ICMS).

**Início de Vigência**: Informar data inicial pauta deste tributo.

**Fim de Vigência:** Informar data final pauta deste tributo.

**Alíquota Débito:** Aplica-se apenas para os tributos ICMS e ICMS-ST.

**Alíquota Crédito**: Aplica-se apenas para os tributos ICMS e ICMS-ST.

**Unidade:** Informar unidade utilizada para a Alíquota AD REM, esta é a unidade do fator de conversão da unidade do produto preenchida em Cadastro | Produto | Controle de Estoque | Unidades | Unidade de Controle.

**Preço/Pauta**: Preencher conforme a pauta do produto.

***Observação***: Não poderão ser inseridos registros com a mesma combinação de Código, Coligada, Tributo e em um mesmo intervalo de vigência.

2Cadastro do Tipo de MovimentoCadastro do Tipo de Movimento

É necessário selecionar o tributo no cadastro do Tipo de Movimento. Acesse Ambientes | Parâmetros | Gestão de Estoque, Compra e Faturamento | Avançar...| Selecione o processo onde se encontra o tipo de movimento | Editar | Avançar | Etapa 65 Fis - Tributação - Item | na coluna "Procurar Alíquota Em" **Pauta do produto**.

Figura2Parametrização da Regra de ICMSParametrização Regra de ICMS / IPI

**Identificação**

Tipo Tributação: Tributado

Figura

Tipo Tributação: Diferido

Segue a mesma regra do ICMS Diferido, porém deve ser usado o CST 53.

Consultar as regras sobre o ICMS Diferido:

2Exemplo do MovimentoExemplo do Lançamento Fiscal

Cálculo considerando a alíquota de débito/crédito informada na Pauta do Produto:

Com os valores acima o movimento criado no TOTVS Gestão de Estoque, Compra e Faturamento apresenta da seguinte forma:

|  |  |  |
| --- | --- | --- |
| Valor | = | 950 |
| Alíquota AD REM | = | 1,94% |

Figura2Lançamento Fiscal EscrituradoLançamento Fiscal Escriturado

Segue detalhamento do Lançamento Fiscal após a execução do processo de Escrituração de Lançamentos, lembrando que toso os valores serão gravados automaticamente, visto que essas informações já foram inseridas no módulo TOTVS Gestão de Estoque, Compra e Faturamento.

**Valor da Mercadoria**

|  |  |
| --- | --- |
| Valor do ICMS | 950,00 |

Figura

**ICMS****Tributado**

```

```

|  |  |
| --- | --- |
| Alíquota AD REM | 1,94% |
| Valor ICMS | 950,00 |

Figura

**Valor Total da Situação Tributária: 950,00**
