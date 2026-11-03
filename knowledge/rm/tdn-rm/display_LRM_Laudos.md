---
content_hash: f7675b297c5198b4bf07f64a74de58a287b017cc89573208d945ca81759c3720
fetched_at: '2026-06-29T00:10:53.203270+00:00'
page_id: '577914256'
product: rm
source: tdn-rm
title: Laudos
type: documentation
url: https://tdn.totvs.com/display/LRM/Laudos
version: 14
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de Utilização**

itensVisão Geral

## **01. Visão Geral**

## 

Exemplo de Utilização

## **02. Exemplo de Utilização**

Para acessar a funcionalidade de criação de Laudos de Imagens para um exame, você irá navegar para o seguinte menu no módulo Saúde > Gestão Hospitalar > Unidade de Diagnóstico > Laudos de Imagem. Ao acessar essa funcionalidade será exibido os exames de Imagem para criação do Laudo.

A seguir será exibida a lista de exames para criação dos Laudos, selecione um exame e clique no botão Editar (ou clique duas vezes no exame).

Logo em seguida será exibida a tela de criação do laudo no status inicial.

Como podemos analisar na figura acima, o exame fica no status inicial e somente com o campo ação fica habilitado. Para inicializarmos a criação do laudo, basta você clicar na opção Digitar Exame e clicar no botão salvar.

Ao salvar a mudança de status todos campos que interagem com digitações do laudo ficaram habilitados, para que você realize a criação do documento de laudo. Abaixo vamos listar as ações que pode ser realizadas na edição do laudo.

* **Ação:** Nessa lista você pode selecionar o próximo status do laudo ou voltar para um status anterior, você irá liberar o resultado avançando no status a partir dessa lista. Ao clicar em F4 você pode avançar para o próximo status e automaticamente ele irá mudar o status e salvar o exame.
* **Quantidade de Películas:** Nesse  campo você pode aumentar a quantidade de películas que o exame irá gerar, o valor padrão é **Zero**.
* **Auto texto para laudo:** Quando é definido textos padrões para um exames, esse pode ser selecionado e ao clicar no botão substituir/incluir ou pelo atalho 'CTRL + Barra de Espaço' no documento o texto selecionado.
* **Modelo:** Você pode definir um modelo padrão para o exame, basta você selecionar um modelo que foi definido no cadastro de Métodos e parâmetros de exame.
* **Observações:** Esse campo somente leitura exibe as observações definidas a partir da funcionalidade conclusão, esse campo irá exibir o texto digitado na rotina de conclusão.
* **Imprimir laudo:** Realizar a impressão do laudo.
* **Filmes:** Define os filmes para o laudo.
* **Conclusão:** Ao clicar nesse botão será exibida uma tela com onde você pode informar em texto livre as conclusões do laudo.

### Observações:

* Para todo laudo com status diferente de **"Em Digitação"** (vide exceção no tópico abaixo), todas as ações e alterações no laudo ficarão bloqueadas, com exceção da mudança de status e do botão de impressão
* Para os status **"Aguardando Revisão" e "Revisado"**, todas as ações e possíveis alterações no laudo serão bloqueadas;

Exemplo:

Ao finalizar a criação do documento de laudo, você pode selecionar a opção Concluir digitação na lista de Ações e avançar para liberação do Laudo.

Essa funcionalidade no aplicativo RMSaude já ficará disponível se for incluída a tag **rmsaude\_HabilitarNovaTelaExame** com valor **true**no arquivo de configuração **RMSaude.exe.config,**conforme exemplo abaixo.
