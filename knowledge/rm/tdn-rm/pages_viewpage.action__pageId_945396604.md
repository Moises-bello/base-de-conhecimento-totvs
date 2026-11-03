---
content_hash: 94b301377be73b866288d4ea24c502c5d7dcd30ed513e67ab3134850b24bbbf0
fetched_at: '2026-06-29T00:12:09.358110+00:00'
page_id: '945396604'
product: rm
source: tdn-rm
title: DT - Integração RM X Ahgora - API de Sindicato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=945396604
version: 23
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM X Ahgora - API de Sindicato |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-13584](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13584 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2506 e superiores

## **03. SITUAÇÃO/REQUISITO**

Criação de API para integração dos dados dos sindicatos para o Ponto Web da Ahgora.

## **04. SOLUÇÃO**

Visando otimizar a integração entre os sistemas, foi disponibilizada a API ahgora/sindicatos. Essa API é responsável por enviar automaticamente as informações dos Sindicatos cadastradas na Folha de Pagamento para o Ponto Web da Ahgora, garantindo mais agilidade, padronização e segurança no compartilhamento de informações.

Este método é responsável por enviar uma lista de sindicatos da tabela RCE do Protheus.

* **Endpoint:**api/rh/v1/ahgora/sindicatos?page=1&pageSize=500&cnpjList='CNPJ da COLIGADA'
* **Método**: GET
* **Autenticação:**Basic

### Parâmetros de Consulta

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| page | Numérico | Sim | Número da página a ser consultada (inicia em 1). |
| --- | --- | --- | --- |
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
| cod | Código do Sindicato - PSINDIC.CODIGO |
| desc | Descrição do Sindicato - PSINDIC.NOME |
| cnpj | CNPJ da Coligada- GCOLIGADA.CGC |

**Será retornado uma lista com os sindicatos referente ao CNPJ da coligada que foi enviado na requisição.**

jsConfluenceOperação realizada com sucesso!trueImportante:

Caso o número de itens ultrapasse o limite da página, o campo hasNext será retornado como true, indicando que há mais dados a serem requisitados.  
O recomendável é solicitar 500 itens por página.

400bas400 - Solicitação inválidaBody

Verificar se todos os parâmetros foram passados na requisição

jsConfluencetrue

## **05. DEMAIS INFORMAÇÕES**

#### [Integração RM X Ahgora](https://tdn.totvs.com/pages/viewpage.action?pageId=877866931)
