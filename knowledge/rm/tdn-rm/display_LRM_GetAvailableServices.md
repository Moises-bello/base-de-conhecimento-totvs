---
content_hash: e78287582c8c8f21a9de7a12fd66c607403937c8c13ac448e8a34cec473f4c46
fetched_at: '2026-06-29T00:05:59.411900+00:00'
page_id: '190515888'
product: rm
source: tdn-rm
title: GetAvailableServices
type: documentation
url: https://tdn.totvs.com/display/LRM/GetAvailableServices
version: 9
---

Os serviços do Corpore RM com as funcionalidades para utilização do TOTVS | HTML Framework estarão disponíveis em 2016. No momento versões controladas serão disponibilizadas para as equipes de Segmentos envolvidas no projeto de Experiências de Uso

Versão

 Disponível à partir da versão 12.1.6 da linha RM.

# GetAvailableServices

Retorna um json com a lista contendo informações de todos os serviços REST dos DataServers RM.

## Parâmetros

* name (opcional) - nome do serviço.
* start (opcional) - registro inicial a ser retornado.
* limit (opcional) - número máximo de registros a serem retornados.

## Exemplo de utilização

Método: GET

URL: <http://localhost:8051/rmsrestdataserver/getavailableservices>

### Resposta da requisição

### Lista de serviços REST do RM

| Nome | Descrição |
| --- | --- |
| biblioteca | Serviços do módulo de Gestão de Biblioteca |
| compras | Serviços do módulo de Gestão de Compras |
| conector | Serviços do Conector |
| crm | Serviços do módulo CRM |
| contabil | Serviços do módulo de Gestão Contábil |
| contrato | Serviços do módulo de gestão de Contratos |
| educacional | Serviços do módulo de Gestão Educacional |
| estoque | Serviços do módulo de Gestão de Estoque |
| financeiro | Serviços do módulo de Gestão Financeira |
| fiscal | Serviços do módulo de Gestão Fiscal |
| folha | Serviços do módulo de Gestão de Folha de Pagamento |
| globais | Serviços do módulo Global |
| imobiliario | Serviços do módulo de Gestão Imobiliária |
| manutencao | Serviços do módulo de Gestão de Manutenção |
| movimento | Serviços do módulo de Gestão de Vendas e Faturamento |
| patrimonial | Serviços do módulo de Gestão Patrimonial |
| plan\_contr\_producao | Serviços do módulo de Planejamento de Controle da Produção |
| projetos | Serviços do módulo de Gestão de Projetos |
| controle\_ponto | Serviços do módulo de Controle de Ponto |
| rh | Serviços do módulo de Gestão de Recursos Humanos |
| saude | Serviços do módulo de Gestão Hospitalar |
| seg\_med\_trabalho | Serviços do módulo de Segurança e Medicina do Trabalho |
| avaliacao\_pesquisa | Serviços do módulo de Gestão de Avaliação e Pesquisa |
