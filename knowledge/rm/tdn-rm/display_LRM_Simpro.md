---
content_hash: a28e67b7b349a667cb3c837c462f8eea3341121ddf98ad355ea83585076a861e
fetched_at: '2026-06-29T00:11:27.616629+00:00'
page_id: '727938953'
product: rm
source: tdn-rm
title: Simpro
type: documentation
url: https://tdn.totvs.com/display/LRM/Simpro
version: 9
---

## **CONTEÚDO**

CONTEÚDO

Atenção!

A importação na nova MDI não é compatível com arquivos texto de versões anteriores.

## **01. Visão Geral**

Esta função será utilizada para fazer a Importação das Revistas do SIMPRO e para Atualizar os Itens de Estoque, **desde que a tabela de preço esteja vinculada à um código Simpro.**

As tabelas que forem atualizadas através do SIMPRO, deverão ser parametrizadas em [Cadastro | Faturamento | Tabelas de MATMED Usadas](//tdn.totvs.com.br/IDH_SATabelasMATMEDUsadas.htm), bem como os fatores de atualização para Preços de Fábrica (PFB) e Preços Médio ao Consumidor (PMC).

A Tabela SIMPRO efetua a publicação de preços de Medicamentos e Produtos para a Saúde, seu banco de dados é atualizado regularmente com informações fornecidas por indústrias, importadores e distribuidores de Medicamentos e Produtos para Saúde.

## **02. Importação Simpro**

Para realizar uma nova importação do arquivo mensagem simpro, realizar os seguintes passos:

1. 1. Na nova MDI, vá para Faturamento > Atualização de Preços > Importação Simpro;
   2. Informe o **Número da Mensagem** Simpro que será importado;
   3. Informe a **Data de Atualização** da mensagem, ou seja, a data na qual a mesma foi publicada;
   4. Informe no **Caminho do Arquivo** o local onde o arquivo TXT está salvo em sua máquina que será utilizado no momento da importação;
   5. Quando todos os dados estiverem preenchidos de acordo, clique em **Executar** para dar inicio no processo.

| Ação | Descrição |
| --- | --- |
| **Número Mensagem** | Campo que define qual é o Número da Mensagem Simpro. Deve ser preenchido com o mesmo número da mensagem que está sendo importada.  OBS: O campo é preenchido automaticamente, levando em consideração a última mensagem que foi importada no ano. Exemplo: Se a última mensagem do ano de 2022 foi a 2022/0046, o campo será automaticamente preenchido com 2022/0047. Apesar disso, o campo pode ser modificado livremente pelo usuário. |
| **Data Atualização** | Campo que define a data na qual a mensagem foi publicada. |
| **Caminho do Arquivo** | Campo que especifica o caminho do arquivo TXT que foi publicado pela Simpro. |

## **03. Aualização Simpro**

Para realizar uma a atualização da mensagem simpro, realizar os seguintes passos:

1. 1. Na nova MDI, vá para Faturamento > Atualização de Preços > Atualização Simpro;
   2. Marque as opções e as tabelas que estão vinculadas que devem ser atualizadas;
   3. Quando todos os dados estiverem preenchidos de acordo, clique em **Executar** para dar inicio no processo.

| Opções | Descrição |
| --- | --- |
| **Atualizar produtos com o código TUSS** | Caso a opção estiver marcada, atualizará o código específico do produto com o seu código TUSS.  **Obs**: Os produtos somente serão atualizados caso a tabela MATMED estiver configurada para atualizar o código de seus produtos. |
| **Priorizar código SIMPRO quando não existir código TUSS** | Caso o produto não tenha um código TUSS, ele será atualizado com seu código SIMPRO.  A opção estará desativada caso a "Atualizar produtos com o código TUSS" não estiver selecionada. |
| **Atualizar o código específico (de 10 dígitos) com o código SIMPRO** | Se for marcada, atualizará o código específico de 10 dígitos do produto com seu código SIMPRO.  **Obs**: Esta opção atualizará o código de 10 dígitos, enquanto o código específico normal do produto possui apenas 8 dígitos. |
| **Tabelas de Materiais e Medicamentos Simpro** | Selecione as tabelas MATMED que deseja atualizar. Ao menos uma tabela deve ser selecionada.  **Obs**: Somente as tabelas que atualizam preço pela Simpro serão exibidas. |

Após configurar os parâmetros conforme desejar, clique no botão "Executar" para atualizar os produtos. Quando o processo finalizar, uma tela mostrando o número de produtos atualizados será exibida.

Será sempre atualizada a última revista importada.

## **04. Configuração da Tabela de Preço com a Simpro**

Para que a tabela de preço seja atualizada pela mensagem Simpro, nas opções Itens Simpro desse cadastro deve ser habilitado o campo "Atualiza itens automaticamente na importação.

Essa tela é acessada através do caminho Cadastros > Faturamento > Tabela de Preços Usadas.

Atenção!

Só serão importados os campos, conforme campos marcados no quadro Itens Simpro

## **05. Vinculo do Produto com o Item Simpro**

Para que o produto do cadastro do RM seja atualizado com os dados da Simpro, será necessário fazer o vinculo do produto com o seu respectivo código Simpro, conforme imagem abaixo.

Essa tela fica em anexo da tela de Tabela de Preços Usadas.

É possível priorizar o preço do item de forma diferenciada do cadastro da Tabela de Preços Usadas, ou seja, se o campo **Priorizar Preço** estiver selecionado Tabela, o sistema irá utilizar o valor definido no cadastro da tabela, caso queria seja utilizado PFB ou PMC, deverá ser selecionada a respectiva opção

## **06. Tabelas Utilizadas**

* SZSIMPRO
* SZITEMESTQPRECO
* SZSIMPROHISTORICO
