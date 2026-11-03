---
content_hash: 99d0d2c79fa595a053b8ecdf9f4084ecf4d88c98d95f2b0efad88eaac14854de
fetched_at: '2026-06-29T00:10:53.254295+00:00'
page_id: '578039153'
product: rm
source: tdn-rm
title: Métodos e Parâmetros de Exame
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=578039153
version: 9
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Tela Métodos e Parâmetros de Exame**
3. **Tela Métodos e Parâmetros de Exame Aba Identificação**
4. **Tela Métodos e Parâmetros de Exame Aba Parâmetros**
5. **Tela Métodos e Parâmetros de Exame Botões de Propriedades**
6. **Resultado Padrão e Expressão Calculada**

itensVisão Geral

## **01. Visão Geral**

Esta funcionalidade tem por objetivo realizar a configuração de parâmetros de exames.

Tela Métodos e Parâmetros de Exame

## **02. TELA MÉTODOS E PARÂMETROS DE EXAME**

1. Abrir o menu de métodos e parâmetros de exame.
2. Selecionar um exame de sua escolha e dê um duplo clique.

Tela Métodos e Parâmetros de Exame Aba Identificação

## **03. TELA MÉTODOS E PARÂMETROS DE EXAME ABA IDENTIFICAÇÃO**

1. Tela de identificação de exame onde podemos selecionar:

* "Método"
* "Tipo de Relatório Laudo"
* "Relatório de Laudo"

Tela Métodos e Parâmetros de Exame Aba Parâmetros

## **04. TELA MÉTODOS E PARÂMETROS DE EXAME ABA PARÂMETROS**

1. Tela de parâmetros onde podemos incluir ou modificar os parâmetros

2. Ao efetuar um duplo click em algum parâmetro na tela de métodos e parâmetros de exame.

3. Abre a nova janela de identificação dos parâmetros.

  

4. Na aba de Dados de Referência podemos alterar ou inserir parâmetros de referencia.

5. Ao efetuar um duplo click nos dados de referência ou no botão de inclusão.

6. Preencha a tela de dados de referência de exames. Salve a alteração.

Tela Métodos e Parâmetros de Exame Botões de Propriedades

## **05. TELA MÉTODOS E PARÂMETROS DE EXAME BOTÕES DE PROPRIEDADES**

Foi feita uma mudança na tela para transformar todos os botões de propriedades do tipo  
checkbox para groupbox:

A ideia é que sempre que um parâmetro seja adicionado, alguma propriedade seja escolhida. Lembrando que essa configuração do parâmetro vai impactar exclusivamente   
na tela de resultados laboratoriais.   
Explicando as propriedades:

   • Subtítulo

Transforma o nome do parâmetro em negrito com caixa alta e não deve obrigar preenchimento de resultado.

• Espaço

Deve limpar todos os campos. Preenchimento de resultado não obrigatório.

• Comentário

Deve tirar a unidade de medida e resultado, mantendo apenas o nome do   
parâmetro. Preenchimento do resultado não deve ser obrigatório.

• Resultado Obrigatório

Deve manter todos os campos na tela de resultado igual um parâmetro normal,   
mas obrigando o usuário a preencher o resultado (esse é o funcionamento padrão   
de um parâmetro, e sempre que um novo parâmetro for criado essa caixa vai vir   
marcada automaticamente).

Caso o resultado não seja preenchido:

• Resultado Opcional

Deve habilitar a edição do campo de resultado, só não deve obrigar o seu preenchimento. É a nova funcionalidade que satisfaz a requisição do cliente.

Com a alteração, só é possível selecionar uma das opções de propriedade. Naturalmente é o correto, visto que não faz sentido o usuário marcar um parâmetro por exemplo como   
‘Espaço’ e ‘Subtítulo’ ao mesmo tempo, ou até mesmo ‘Comentário’ e ‘Espaço’. Cada um tem a sua propriedade e comportamento, não devem coexistir juntos.  
Para não comprometer os cadastros anteriores, foi mantida a prioridade sobre os parâmetros também:

- Caso o exame tivesse um parâmetro cadastrado como ‘Comentário’, ‘Subtítulo’ e ‘Espaço’, o sistema vai deixar marcado automaticamente somente o Espaço. Caso não   
tivesse o Espaço marcado e sim os outros dois, deixaria apenas o Subtítulo.  
Essa medida foi tomada para que a mudança não interferisse em nada na formatação de parâmetros anterior do usuário

Resultado Padrão e Expressão Calculada

## **06. RESULTADO PADRÃO E EXPRESSÃO CALCULADA**

Na tela de cadastro de parâmetro, existem os dois campos de Resultado Padrão e Expressão Calculada.

**Expressão Calculada**

O campo de Expressão Calculada irá receber uma operação matemática sobre os parâmetros filhos, no qual irá calcular o valor final do parâmetro pai.  
Exemplo:

No exemplo acima, o valor final do parâmetro pai ureia deve ser correspondente a soma dos parâmetros P2, P3 e P4.

**Resultado Padrão**

Já o campo de Resultado Padrão tem a funcionalidade de determinar o valor final que esse parâmetro deve ter para que o status de "Digitar Exame" possa ser avançado para "Digitação Concluída";

Nesse mesmo exemplo, caso a soma de P2+P3+P4 for DIFERENTE de 110, ao tentar avançar o status para "Digitação Concluída" na tela de resultados, temos a seguinte mensagem:
