---
content_hash: a747976602f1dbbb3f3a9d36243327775383689ff443f37215e4412fc848b3de
fetched_at: '2026-06-29T00:12:10.850970+00:00'
page_id: '953003762'
product: rm
source: tdn-rm
title: Grupo ZD - Informações do Responsável Técnico na NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953003762
version: 2
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo ZD - Informações do Responsável Técnico na NF-e** | | | | | | | | | | | | |
| # | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Tamanho** | **Observação** | **Campo de Origem** | **Campo na Aplicação** | **Mais Informações** |
| 423a | ZD01 | infRespTec | Grupo de Informações Adicionais | G | A01 |  | 0-1 |  | Grupo para informações do responsável técnico pelo sistema de emissão do DF-e |  |  |  |
| 423b | ZD02 | CNPJ | CNPJ da pessoa jurídica responsável pelo sistema utilizado na emissão do documento fiscal eletrônico | E | ZD01 | N | 1-1 | 14 | Informar o CNPJ da pessoa jurídica responsável pelo sistema utilizado na emissão do documento fiscal eletrônico. | DRESPONSAVELTECNICONFE.CNPJ | Campo interno do sistema | Este campo é atualizado/preenchido na base de dados ao Executar o processo "Atualizar Responsável Técnico" na tela de NF-e |
| 423c | ZD04 | xContato | Nome da pessoa a ser contatada | E | ZD01 | C | 1-1 | 2-60 | Informar o nome da pessoa a ser contatada na empresa desenvolvedora do sistema utilizado na emissão do documento fiscal eletrônico | DRESPONSAVELTECNICONFE.NOME | Campo interno do sistema | Este campo é atualizado/preenchido na base de dados ao Executar o processo "Atualizar Responsável Técnico" na tela de NF-e |
| 423d | ZD05 | email | E-mail da pessoa jurídica a ser contatada | E | ZD01 | C | 1-1 | 6-60 | Informar o e-mail da pessoa a ser contatada na empresa desenvolvedora do sistema. | DRESPONSAVELTECNICONFE.EMAIL | Campo interno do sistema | Este campo é atualizado/preenchido na base de dados ao Executar o processo "Atualizar Responsável Técnico" na tela de NF-e |
| 423e | ZD06 | fone | Telefone da pessoa jurídica/física a ser contatada | E | ZD01 | N | 1-1 | 6-14 | Informar o telefone da pessoa a ser contatada na empresa desenvolvedora do sistema. Preencher com o Código DDD + número do telefone. | DRESPONSAVELTECNICONFE.TELEFONE | Campo interno do sistema | Este campo é atualizado/preenchido na base de dados ao Executar o processo "Atualizar Responsável Técnico" na tela de NF-e |
| 423f | ZD07 | -x- | Sequência XML | G | ZD01 |  | 0-1 |  | Grupo de informações do Código de Segurança do Responsável Técnico - CSTR |  |  |  |
| 423g | ZD08 | idCSRT | Identificador do CSRT | E | ZD07 | N | 1-1 | 2 | Identificador do CSRT utilizado para montar o hash do CSRT | DRESPONSAVELTECNICONFE.IDCSRT | Campo interno do sistema | Este campo é atualizado/preenchido na base de dados ao Executar o processo "Atualizar Responsável Técnico" na tela de NF-e |
| 423h | ZD09 | hashCSRT | Hash do CSRT | E | ZD07 | C | 1-1 | 28 | O hashCSRT é o resultado da função hash (SHA-1 – Base64) do CSRT fornecido pelo fisco mais a Chave de Acesso da NFe. |  |  | Campo calculado no momento de gerar o xml da nota conforme regras do manual |
