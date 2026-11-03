---
content_hash: a963a4f6e30db106a22c5f5b3834bb0a5664e4df6a6cd2e3a5efc4510bed3ca4
fetched_at: '2026-06-29T00:11:05.330284+00:00'
page_id: '629745609'
product: rm
source: tdn-rm
title: FISCAL01-15538 DT Transmissão\Consulta de Eventos REINF com Autenticação no
  TSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=629745609
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Totvs Gestão Fiscal |
| Função: | Transmissão\Consulta de Eventos Reinf |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15538 |

## **02. SITUAÇÃO/REQUISITO**

Implementar na chamada dos métodos da REINF o método de geração do Token

## **03. SOLUÇÃO**

Implementação consumo do Serviço de Autenticação do TSS pelo RM nos processos REINF.

Detalhe da gestão do Token de Autenticação fornecido pelo TSS:

Para que seja consumido o serviço de autenticação do TSS é obrigatório a informação do ClientId e Secret que no caso da REINF deve ser preenchido em: Parametrizar Client Id e Secret fornecido pelos serviços do TSS em RM -> Totvs Gestão Fiscal -> Ambiente -> Parâmetros -> TOTVS Gestão Fiscal -> 03.05 - Integração -> 03.05.06 - TSS -> Filial Reinf -> Gerais.

O processo de Autenticação do TSS é transparente para o usuário e não será necessário mais nenhuma ação do usuário além da parametrização do Client Id e Secret válidos.

No retorno serviço TOKEN do TSS é retornado a Tag: EXPIRES\_IN ela fornece o tempo limite da vida útil do ACCESS\_TOKEN então o ERP utiliza o ACCESS\_TOKEN durante este tempo até uma tolerância de 10% do tempo total para solicitar um novo ACCESS\_TOKEN.

Exemplo: EXPIRES\_IN é igual a 3600 segundos então o ERP ira utilizar o ACCESS\_TOKEN durante 3240 segundos, após este tempo, se enviado um novo evento REINF será solicitado um novo token para o TSS, mas utilizando somente a tag REFRESH\_TOKEN que estará em cache.

O cache do Token não será armazenado no Banco de Dados do ERP e existirá apenas em memória, caso o RM.HOST.EXE for reiniciado será necessário a solicitação de um novo token de autenticação no TSS.

Em caso de token no cache sempre que houver mudança de dia será solicitado um novo token de autenticação no TSS desprezando o token que está em cache caso exista.

Informações do Processo de Autenticação do TSS: <https://tdn.totvs.com.br/pages/viewpage.action?pageId=592292258>
