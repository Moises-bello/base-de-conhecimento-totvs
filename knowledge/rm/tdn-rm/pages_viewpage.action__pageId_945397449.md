---
content_hash: 56baacf78b5c724e65c51ebb01d8999ff2b4e0cccb179584ff2daaf1489e49fe
fetched_at: '2026-06-29T00:12:09.365817+00:00'
page_id: '945397449'
product: rm
source: tdn-rm
title: DT - Integração RM X Ahgora - API de Eventos/Verbas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=945397449
version: 31
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM X Ahgora - API de Eventos/Verbas |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-13585](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13585 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2506 e superiores

## **03. SITUAÇÃO/REQUISITO**

Criação de API para integração dos dados dos eventos/verbas para o Ponto Web da Ahgora.

## **04. SOLUÇÃO**

Visando otimizar a integração entre os sistemas, foi disponibilizada a API ahgora/verbas. Essa API é responsável por enviar automaticamente as informações dos Eventos/Verbas cadastradas na Folha de Pagamento para o Ponto Web da Ahgora, garantindo mais agilidade, padronização e segurança no compartilhamento de informações.

Este método é responsável por enviar uma lista de verbas da tabela GCOLIGADA da linha de produto RM.

* **Endpoint:**api/rh/v1/ahgora/verbas?page=1&pageSize=500&cnpjList= 'CNPJ da COLIGADA'
* **Método**: GET
* **Autenticação:**Basic

### Parâmetros de Consulta

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| page | Numérico | Sim | Número da página a ser consultada (inicia em 1). |
| pageSize | Numérico | Sim | Quantidade de registros por página. |
| cnpjList | String | Sim | CNPJ(s) da(s) Coligada(s) que serão consultadas na base do RM |

Importante:

O sistema da Ahgora não está dentro da sua rede, logo, para funcionar a busca das verbas, seu REST no RM deve permitir esse acesso externo.

Configurações de porta no firewall, IP público, DNS e redirecionamento de portas devem ser verificadas junto com o seu time de TI/Redes.

Atenção:

Autenticação Basic: Enviar usuário e senha do RM no header da requisição.

**Retorno**

falseretornotrue200ok200 - OKSucesso

| Propriedades API | Descrição |
| --- | --- |
| cod | Código da Verba - PEVENTO.CODIGO |
| desc | Descrição da Verba - PEVENTO.DESCRICAO |
| cnpj | CNPJ da Coligada- GCOLIGADA.CGC |
| categoria | Provento - Hora ou Dia; Desconto - Hora ou Dia; Base de Cálculo - Hora ou Dia; - PEVENTO.PROVDESCBASE e PEVENTO.VALHORDIAREF |

**Será retornado uma lista com as verbas referente ao CNPJ da coligada que foi enviado na requisição e caso tenha algum erro será enviado no array de erros dentro do response.**

jsOperação realizada com sucesso!trueImportante:

Caso o número de itens ultrapasse o limite da página, o campo hasNext será retornado como true, indicando que há mais dados a serem requisitados.  
O recomendável é solicitar 500 itens por página.

400bas400 - Solicitação inválidaBody

Verificar se todos os parâmetros foram passados na requisição

jsConfluencetrue

## **05. DEMAIS INFORMAÇÕES**

#### [Integração RM X Ahgora](https://tdn.totvs.com/pages/viewpage.action?pageId=877866931)
