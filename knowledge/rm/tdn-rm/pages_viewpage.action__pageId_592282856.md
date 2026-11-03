---
content_hash: 9d79698f7e54a847339609d00df1b4fe04411e4faa96a28cecfa32764b56d4bf
fetched_at: '2026-06-29T00:10:56.240413+00:00'
page_id: '592282856'
product: rm
source: tdn-rm
title: Contabilização de Aditivo  - Alteração de valor da Parcela ( Código de Componente
  )
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=592282856
version: 17
---

## Melhoria que será liberada a partir da versão 12.1.32.

## Melhoria na contabilização , agora se pode inserir o código do componente no aditivo de alteração de valor de parcela.

## Se o aditivo afetar mais de um componente, então, não informar o código.

**Cadastro do Evento Contábil e sua parametrização:**

No contrato de Venda - Inserir o Evento contábil cadastrado para utilização da alteração de valor da parcela de um determinado componente.

Evento contábil cadastro ( OBSERVAÇÃO : **Calcular valor a partir de :  " FÓRMULA** " ) Tem que estar marcada a opção de Fórmula.

Cadastrando Itens do Evento:

Observação!

Não se pode incluir mais de **1 componente** na formula , neste caso a contabilização é realizada apenas para o componente selecionado , neste exemplo o código do componente é 26.

**Exemplo:** Feita uma alteração no valor do componente 26 – Será incluído nas contas de **Débito e Crédito** , se ocorrer uma alteração em valor de qualquer outro componente , diferente do 26 , os valores serão incluídos nas contas de **Debito 2 e Crédito 2 e Se o aditivo afetar mais de um componente, então, o código do componente não será preenchido.**

Fórmulas Utilizadas:

FórmulasContabilizando apenas para Conta do Componente |

## ( Inserindo na conta de Débito e Crédito os valores do Componente 26 )

Se CODCOMPN = 26

Entao

**GETVALORINCIDENCIACONTABILVENDA**('ValorAditivoVenda')

Senao

0

Fimse

Contabilizando para a conta geral do Evento.

## ( Inserindo na conta de Débito2 e Crédito2 os valores de Componentes diferentes do 26 )

Se CODCOMPN = 26

Entao

0

Senao

**GETVALORINCIDENCIACONTABILVENDA**('ValorAditivoVenda')

Fimse

Exemplos:Exemplos ao Contabilizar o AditivoExemplo 01 |

## Exemplo 1 ) Alterando valor de um componente diferente do 26.

Selecionando o Aditivo : Alteração de Valor de Parcela

Neste exemplo , alterei o valor do componente ( 2 - Mensal ), diferente do 26.

Selecionar o Componente : **Processos / Contabilizar Aditivo**

Exemplo 02 |

## Exemplo 2 ) Alterando valor do componente 26.

Alterando valor do Componente 26 apenas.

500 Reais para 550

Conforme parametrizado , caindo nas contas : DEBITO e CREDITO.

Exemplo 03

## Exemplo 3 ) Alterando valor do componente 26 e de outro ao mesmo tempo. ( Mais de um Componente ).

Componente 26 e 2 Alterados.

Caindo nas Contas : **DEBITO 2 E CREDITO 2** - Como informado anteriormente, para cair na conta exclusiva do componente 26, tem que ter apenas o componente alterado.
