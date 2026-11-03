---
content_hash: 6e06b3fa4b64ac3897b8160fab71f2e0282eac7387f13aa88f895a2ccafd10c3
fetched_at: '2026-06-29T00:11:53.825079+00:00'
page_id: '852297417'
product: rm
source: tdn-rm
title: DT - Dependentes - Incidência Assistência Odontológica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=852297417
version: 9
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Dependentes - Incidência Assistência Odontológica |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-10274](https://jiraproducao.totvs.com.br/browse/DRHROTRM-10274) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2310.229
* 12.1.2402.173
* 12.1.2406.104 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Com a implementação do leiaute 1.2, as informações dos dados do dependentes passam a ser enviadas no evento S-1210 para declaração de desconto de assistência medica ou assistência odontológica, com isso surgiu a necessidade de criar um parâmetro na aba de incidências para indicar a utilização somente da assistência odontológica.

## **04. SOLUÇÃO**

Foi criado um parâmetro na aba de incidências possibilitando que o usuário marque a opção "Assistência Odontológica", conforme apresentado abaixo. Ao marcar este parâmetro, o sistema passa a enviar as informações dos dependentes para o eSocial.

Processos que passam a levar os dados do dependente (não possuí tag especifica para a assistência odontologica no xml do eSocial) considerando o novo campo:

* Geração do evento S-2200 e S-2205
* Geração do XML em lote S-2205
* Importação e exportação do dependente do funcionário
* Histórico de Assistência Médica flag “Somente com Incidência”, será considerado na seleção do beneficiário.

ATENÇÃO:

Para a criação do campo mencionado acima, será necessário atualizar a base de dados através do atualizador e reiniciar o host. Além disso, será preciso realizar uma avaliação das fórmulas existentes de assistência médica, para verificar a necessidade de possíveis ajustes.

## **5. DEMAIS INFORMAÇÕES**
