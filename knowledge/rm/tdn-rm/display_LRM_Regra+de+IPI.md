---
content_hash: f136aba5fac43f859afb0c7642d6b83e3c675259092d0883bda2a562e6c3fce1
fetched_at: '2026-06-29T00:09:23.261311+00:00'
page_id: '422546088'
product: rm
source: tdn-rm
title: Regra de IPI
type: documentation
url: https://tdn.totvs.com/display/LRM/Regra+de+IPI
version: 9
---

Nas Regras de IPI deverão ser cadastradas todas as situações tributárias referentes ao IPI, existentes nas operações de Entrada/Saída ocorridas na empresa. O cálculo do IPI no lançamento fiscal, bem como a edição dos campos relacionados ao IPI, considera a informação contida neste cadastro, que irá ser associado à natureza de operação.

**Identificação Regras IPI**

**Global:** Define se a regra será global, ou seja, poderá ser vinculada a qualquer natureza de operação, independente do cadastro de naturezas ser Global ou Por Filial. Desabilitando este campo, a regra passa a ser Por Filial, só podendo ser vinculada à natureza de operação da filial em que a regra foi incluída.  
***Observações*:** A definição de regras de IPI Por Filial só estará disponível se o parâmetro Natureza Global estiver habilitado, no menu Opções | Parâmetros | Gerais/Tabelas | Apuração de Tributos | IPI | Natureza de Operação.  
A alteração de uma regra de Global para Por Filial só poderá ocorrer se não existir natureza de operação vinculada a lançamentos e/ou movimentos. Já a alteração da regra de Por Filial para Global poderá ocorrer sem restrições.

**Dados IPI**

* **Regras Tributárias**

**IPI Pautado:**Este campo deve ser marcado para a escrituração de operações de Saída, dos estabelecimentos industriais ou equiparados, onde o cálculo do IPI é feito por pauta, independente do valor da venda.

**NÃO somar IPI no Valor Contábil:** Habilitando esta opção, o valor do IPI não será somado ao valor contábil do lançamento fiscal.

**Situação Tributária de Entrada:** Preencher conforme disposto no manual da Nota Fiscal Eletrônica, para as operações de entrada do IPI

| Código | Situação Tributação |
| --- | --- |
| 00 | Entrada com Recuperação de Crédito |
| 01 | Entrada Tributada com Alíquota zero |
| 02 | Entrada Isenta |
| 03 | Entrada Não Tributada |
| 04 | Entrada Imune |
| 05 | Entrada com Suspensão |
| 49 | Outras Entradas |

**Situação Tributária de Saída:**Preencher conforme disposto no manual da Nota Fiscal Eletrônica, para as operações de saída do IPI.

| Código | Situação Tributária |
| --- | --- |
| 50 | Saída Tributada |
| 51 | Saída Tributada com Alíquota zero |
| 52 | Saída Isenta |
| 53 | Saída Não Tributada |
| 54 | Saída Imune |
| 55 | Saída com Suspensão |
| 99 | Outras Saídas |

Tipo Tributação Contém os tipos de IPI disponíveis no sistema. O tipo selecionado deverá corresponder à operação realizada,exemplo: Para uma operação com isenção de IPI, o tipo escolhido deverá ser o Isento

Cópia de Regra de IPI
