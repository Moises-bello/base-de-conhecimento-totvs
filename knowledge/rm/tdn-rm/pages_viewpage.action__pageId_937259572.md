---
content_hash: ee089f5fda6129a775b2a631323b0302b10e2449e4521b944dc72e7495234a94
fetched_at: '2026-06-29T00:12:08.514934+00:00'
page_id: '937259572'
product: rm
source: tdn-rm
title: Crédito Trabalhador - Parametrizador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=937259572
version: 20
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Descontos de empréstimos**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Esta tela permite parametrizar a importação do arquivo recebido do governo, com o objetivo de incluir no sistema as parcelas dos empréstimos contraídos por funcionários por meio da plataforma governamental.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dica:

Veja também FAQ -

## **03. TELA CONFIGURAÇÃO ARQUIVO CRÉDITO TRABALHADOR**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Tipo do Empréstimo | Informar o código cadastrado em Administração de Pessoal | Cadastros Globais | Tabelas Dinâmicas, com o contexto Sistema selecionado como Folha de Pagamento Tabela INT30 - Código de empréstimo. |
| Evento de Desconto de Empréstimo | Retorna eventos cadastrados cujos campos Código de Cálculo 480 - DESCONTO EMPRÉSTIMO CRÉDITO DO TRABALHADOR e Rubrica eSocial 9253 - Empréstimos eConsignado - Desconto. |
| Máscara para código Empréstimo | Prefixo:  livre para preenchimento do usuário  Sequencial: Nº de casas para preencher com zeros à esquerda o contador automático.  Máscara: campo que apenas mostra o resultado do Prefixo + Contador alinhado conforme nº de casas definidas no sequencial. Observação: Essa máscara será incrementada por coligada na importação do Empréstimo Crédito do Trabalhador. |
| Fracionamento de Job's Qtde de Job's | Informar a quantidade de Job's que o processo fracionará no momento da execução. Esse campo será usado quando o sistema estiver parametrizado para fracionamento de Job's |
| Últ. Competência Importada | Nesse campo é demonstrado qual a última competência da base de dados que foi importado o arquivo do Crédito do Trabalhador e o campo foi criado para melhor precisão em casos como provisão de férias.   Não será calculada a provisão do empréstimo nas férias se a data da competência atual no cadastro de empréstimo for menor que a data de Últ. Competência Importada.  Em alguns casos de cálculo das férias em que a importação não tenha ocorrido ainda e a data da  Últ. Competência Importada for igual a data da competência atual no cadastro de empréstimo, então será calculada a provisão. Dica: Veja exemplos em [Cálculo de Férias - Provisionamento nas Férias verificando a data Últ. Competência Importada](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1049386448) Observação: Este campo é importado utilizando a **Competência Atual do Sistema.**    Este campo não é alterado ao liberar a competência ou por qualquer outro parâmetro da importação, sua atualização é única e exclusivamente realizada utilizando a  **Competência Atual do Sistema** no momento da execução da Importação do Crédito do Trabalhador. |
| Eventos do Crédito Trabalhador devem ser adicionados na base da Contribuição Previdenciária | Parâmetro utilizado para que os eventos informados no anexo do funcionário "[Eventos Remuneração Crédito do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=938311818)" e/ou no parametrizador em "[Eventos do Crédito Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=938311837)" serão somados com a base de eventos que incidem em INSS, INSS13º. Dica: Veja exemplo de utilização na FAQ - |

Esta configuração deve ser feita por Coligada.IMPORTANTE!

## **04. TABELAS UTILIZADAS**

* PPARAMADICIONAIS
