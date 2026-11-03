---
content_hash: a3eb9146549ed73e190fdb48d8bf9a9c336ef9384a85ee49be95876f8cae292a
fetched_at: '2026-06-29T00:08:50.312154+00:00'
page_id: '334334066'
product: rm
source: tdn-rm
title: Como gerar evento S-1210 de pagamento de Autônomos?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334334066
version: 7
---

|  |  |
| --- | --- |
| Descrição | Integração TOTVS Folha de Pagamento x TOTVS Gestão Financeira - Gerar XML do evento S-1210 |
| Observações | Documento tem como objetivo mostrar a integração do financeiro com a folha de pagamento, para gerar informações do evento S-1210 referente a pagamento de autônomos. |

1. Acesse o modulo **Gestão Financeira | Cadastro | Cliente/Fornecedor**:

2. Insira um lançamento financeiro para um Cliente/Fornecedor:

3. Realize a baixa do lançamento financeiro:

**OBS**: O sistema considera da data da baixa lançamento financeiro para gerar o evento S-1210, ou seja, o evento será gerado no período de apuração conforme mês e ano da baixa realizada.

4. Acesse o modulo de Folha de Pagamento | eSocial  | Gerar XML:

5. No processo de Gerar XML, selecione o evento S-1210 marcando o parâmetro "Gerar Autônomos Fluxus/Externos " e execute o processo:

**OBS:** Em caso de utilização do Middleware, o parâmetro não será apresentado e os autônomos serão gerados sempre que executado o processo.

6.Acesse a fila de Eventos Periódicos para conferir a geração do arquivo XML:

**OBS**: Caso o usuário não utilize a integração com o modulo de Gestão Financeira,  é possível utilizar a integração com sistemas de terceiros alimentando as informações referentes as retenções dos autônomos no cadastro de Autônomos Externos:
