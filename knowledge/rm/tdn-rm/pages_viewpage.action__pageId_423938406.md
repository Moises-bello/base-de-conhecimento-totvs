---
content_hash: 3fb96223f5930ca219fa4ca54ae0e82faa394e563ce96f0fc96094201e946db2
fetched_at: '2026-06-29T00:09:26.750289+00:00'
page_id: '423938406'
product: rm
source: tdn-rm
title: Objeto de Manutenção (Pasta Indicador(es) de Uso)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938406
version: 4
---

Esta pasta permite analisar o histórico do objeto de manutenção, permitindo visualizar os lançamentos de indicadores de uso do objeto selecionado.   
***Observação:***

* Esta pasta só aparecerá se houver indicadores de uso habilitados no cadastro de Tipos de Objeto de Manutenção, em Opções | Parâmetros | Tipos de Objeto de Manutenção.
* Como a descrição do Indicador de Uso é baseada no Tipo de Objeto de Manutenção, os campos Medidor, Acumulado e Média/Dia são fixos. O título da caixa que engloba estes três campos será de acordo com o Tipo do Objeto de Manutenção, e é cadastrado em Opções | Parâmetros |Tipos de Objetos de Manutenção, edição do Tipo de Objeto, Pasta Identificação.

**Medidor**: Informe o valor do indicador de uso registrado no aparelho utilizado na medição.  
 **Acumulado**: Informe o valor do indicador de uso real. Isto é, mesmo em situações onde o aparelho medidor não apresenta o valor real, este campo o apresentará. Ex: Troca de medidor em caso de quebra.  
**Média dia**: Média diária dos indicadores de uso, calculada em um intervalo de tempo informado pelo usuário ou em um período parametrizado pelo sistema. Para configurar estes parâmetros acesse Opções | Parâmetros | Sistema, Tipo do Cálculo da média dos Indicadores de Uso.   
**Dica**Uma vez calculada a média, você poderá fazer o controle de média de inclusão diária de indicadores de uso. Essa funcionalidade trabalha conjuntamente com os parâmetros da Consistência de Média de Uso, que avisará ou bloqueará a inclusão de indicadores de uso caso ultrapasse as porcentagens definidas.   
***Atenção!***Para que o cálculo seja efetuado, é preciso clicar no botão Calcular Média/Dia.

**Após Reforma**: Este campo informa o valor acumulado do Indicador de Uso medido para o objeto desde a sua última reforma. Ele apresentará o valor do Acumulado caso ainda não exista reforma para o Objeto de Manutenção.   
Quando houver reforma, ele será zerado e passará a contar o valor acumulado após a última reforma.  
Não é possível alterar indicadores de uso em objetos-filhos, devendo proceder a alteração apenas nos objetos-pai.  
O valor de indicador de uso do objeto-pai será distribuído entre todos os objetos filhos agregados, sendo que, se este objeto filho já possuir um grau de identificador de uso, ao determinar um novo valor para o objeto pai, será efetuado a distribuição por diferença para todos os objetos-filhos agregados.  
Quando o Objeto de Manutenção for do tipo Pneu e no cadastro de índice de Acompanhamento o flag "Decrescente" estiver marcado, só será possível lançar índice de Acompanhamento com valores decrescente.
