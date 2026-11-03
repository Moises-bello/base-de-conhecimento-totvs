---
content_hash: e72f14403021162bb83bc1fdf06750b2c8737449b12b5842a4efcf998c53a2a5
fetched_at: '2026-06-29T00:10:37.787232+00:00'
page_id: '540888308'
product: rm
source: tdn-rm
title: Middleware - Edição de XML's - eSocial do Futuro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=540888308
version: 8
---

**CONTEÚDO**

**9230true**

## **01. Visão Geral**

Processo direcionado para alterações em XML’s a serem enviados ao governo, cuja alteração direta seja a última opção como saída de contorno de possíveis inconsistências sistêmicas, e não seja possível a correção do mesmo antes do seu prazo de envio.

**ATENÇÃO: Qualquer alteração feita através desse processo será de responsabilidade do usuário. Dessa forma ele deve garantir a persistência dos dados para que não ocorra divergências entre o ambiente do governo e a base de dados.**

## **02. Premissas**

É possível utilizar essa funcionalidade quando:

* Utilizar o middleware como forma de integração de eventos;
* O evento está nos status 1 - Gerado, 2 - Erro na geração ou 9 - Rejeitado Ret.

Caso tenha editado o XML, você deverá:

* Garantir que a informação alterada esteja devidamente preenchida conforme o leiaute e manual do eSocial. Isso se faz necessário pois o sistema não irá validar a informação alterada, acatando e enviando ao governo a informação alterada;
* Garantir que a alteração tenha sido feita no devido cadastro para manter consistentes  as informações. Caso tenha sido gerado um novo gatilho dessa alteração, deverá verificar a necessidade de envio desse, ou sua exclusão.

## **03. Exemplo de Utilização**

Para realizar a alteração, na fila de eventos deve selecionar o XML que deseja alterar e clicar na opção “Editar XML”:

Confirme a opção para edição:

Altere a informação desejada, e clique na opção “Salvar”:

Após a edição, o sistema salvará um histórico de edição do XML nos seus anexos:

**Observações:**

Caso o evento tenha sido editado, poderão ser enviados ao governo os que possuem status:

* "1 - Gerado";
* "2 - Erro na geração";
* "9 - Rejeitado Ret".

## **04.** **Tabelas Utilizadas**

* PESOCIALEVENTOS
* PESOCIALHISTORICOXML

]]>
