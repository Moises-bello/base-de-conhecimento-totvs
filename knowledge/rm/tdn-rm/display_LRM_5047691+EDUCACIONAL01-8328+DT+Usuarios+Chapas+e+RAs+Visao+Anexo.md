---
content_hash: 74f755efa0c152e26fd090a7ddf9b72176f1f82267da9ec067f37a6ac2ae35f9
fetched_at: '2026-06-29T00:10:14.560426+00:00'
page_id: '461908694'
product: rm
source: tdn-rm
title: 5047691 EDUCACIONAL01-8328 DT Usuarios Chapas e RAs Visao Anexo
type: documentation
url: https://tdn.totvs.com/display/LRM/5047691+EDUCACIONAL01-8328+DT+Usuarios+Chapas+e+RAs+Visao+Anexo
version: 4
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Gestão Bibliotecária |
| Função: | Usuários - Chapas e RA's |
| Ticket: | 5047691 |
| Requisito/Story/Issue (informe o requisito relacionado): | Usuários |

**02. SITUAÇÃO/REQUISITO**

Identificamos um ponto no sistema que estava causando lentidão na visualização dos usuários da biblioteca. 

**03. SOLUÇÃO**

Para cada usuário o sistema estava carregando e concatenando os registros acadêmicos e as chapas da pessoa vinculada ao usuário da biblioteca, esta operação estava onerando muito a performance do sistema, para solução, os dados de registro acadêmico e chapa não serão mais mostrados como uma coluna na visão de usuários, foi criado um anexo "Chapas e RA's" que irá exibir estes dados por usuário, assim só é carregado os dados do usuário que estiver selecionado, melhorando bem o desempenho do sistema.
