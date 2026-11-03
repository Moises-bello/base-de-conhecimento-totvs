---
content_hash: acb45c54385e064ddb92014bfb6861234fabdffa559c2e6bffd525ac0a15618b
fetched_at: '2026-06-29T00:11:48.870439+00:00'
page_id: '828436902'
product: rm
source: tdn-rm
title: Brasíndice
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=828436902
version: 13
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Importação**
3. **Atualização**
4. **Configuração da tabela de preço**
5. **Vínculo do produto com o item Brasíndice**
6. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

Esta função será utilizada para fazer a **Importação** das Revistas do Brasíndice e para **Atualizar** os Itens de Estoque, **desde que a tabela de preço esteja vinculada à um código Brasíndice.**

As tabelas que forem atualizadas através do Brasíndice, deverão ser parametrizadas em Cadastro > Faturamento > Tabelas de MATMED Usadas, bem como os fatores de atualização para **Preços de Fábrica (PFB)** e **Preços Médio ao Consumidor (PMC)**.

A Tabela Brasíndice efetua a publicação de preços de materiais e medicamentos hospitalares do Brasil, seu banco de dados é atualizado regularmente com informações fornecidas pelos laboratórios responsáveis pelos produtos após a aprovação da ANVISA.

Importação

## **02. IMPORTAÇÃO**

Para realizar uma nova importação do arquivo Brasíndice, realizar os seguintes passos:

1) Na nova MDI, vá para Faturamento > Atualização de Preços > Brasíndice

2) Selecione o processo **Importação da Revista Brasíndice**

Importante

O layout do arquivo txt para ser importado deve ser no seguinte padrão:

* **Formato fixo ou seja cada campo possui um tamanho definido**
* **As colunas PMC e PFB não podem existir no mesmo arquivo. Deve-se gerar o arquivo o valor PMC e outro com o valor PFB**
* **Sem flag de genérico**

3) Aparecerá a tela inicial do assistente e clique em Avançar. Caso queira, marque a opção "Não exibir novamente para esse processo."

4) Em seguida aparecerá a tela do Agendamento. Deixe a primeira opção (Única) para que o processo execute apenas uma vez. Clique em Avançar

5) Informe o **Número da Revista** e a sua **Data de início da vigência** da tabela Brasíndice que será importada.

6) Se marcada a opção **Importar preço médio ao consumidor (PMC) para itens restritos ao hospital**, importará todos os itens. Caso esteja desmarcado, itens do tipo restrito não serão importados.

7) Informe um ou mais **Arquivos** TXT que serão importados.

8) Quando todos os dados estiverem preenchidos de acordo, clique em **Executar** para dar inicio no processo.

Atualização 

## **03. ATUALIZAÇÃO**

Para atualizar os produtos Brasíndice, vá para Faturamento > Atualização de Preços > Brasíndice;

1) Informe os campos que deverão ser atualizados e selecione as tabelas vinculadas ao Brasíndice

Todos as opções abaixo possuem efeito se o parâmetro "Atualiza itens automaticamente na importação", da tabela de MATMED selecionada estiver marcado.

* **Atualizar produto com o código TUSS:**Se marcado e o código TUSS **(3)** do item Brasíndice vinculado tiver valor, o campo Código **(1)** será preenchido
* **Atualizar o código de 10 dígitos com o código Brasíndice:**Se marcado, o campo Código Específico (10 dígitos) **(2)** será preenchido com o Código Brasíndice
* **Priorizar código Brasíndice quando não existir código TUSS:**Se marcado e não existir ou não utilizar o código TUSS,  o campo Código **(1)** será preenchido com o código Brasíndice

Configuração da tabela de preço

## **04. CONFIGURAÇÃO DA TABELA DE PREÇO**

Para que a tabela de preço seja atualizada pela revista, nas opções Itens Brasíndice desse cadastro deve ser habilitado o campo "Atualiza itens automaticamente na importação.

Essa tela é acessada através do caminho Cadastros > Faturamento > Tabela de Preços Usadas.

Vínculo do produto com o item Brasíndice

## **05. VÍNCULO DO PRODUTO COM O ITEM BRASÍNDICE**

Para que o produto do cadastro do RM seja atualizado com os dados do Brasíndice, será necessário fazer o vinculo do produto com o seu respectivo código Brasíndice, conforme imagem abaixo.

Essa tela fica em anexo da tela de Tabela de Preços Usadas.

É possível priorizar o preço do item de forma diferenciada do cadastro da Tabela de Preços Usadas, ou seja, se o campo **Priorizar Preço** estiver selecionado Tabela, o sistema irá utilizar o valor definido no cadastro da tabela, caso queria seja utilizado PFB ou PMC, deverá ser selecionada a respectiva opção

**Fator Atualização**

Este campo e utilizado para calcular o fator de atualização do produto.

Tabelas utilizadas

## **06. TABELAS UTILIZADAS**

* SZBRASINDICEHISTORICO
* SZITEMESTQPRECO
* SZITEMBRASINDICEPRECO
* SZCADAPRESENTACAO
* SZCADLABORATORIO
* SZREVBRASINDICE
