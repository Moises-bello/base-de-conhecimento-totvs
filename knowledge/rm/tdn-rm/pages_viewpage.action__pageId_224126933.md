---
content_hash: 76f31a1e048276a290399ce4b7f06122d7ed4fca6d90f22277b63455b8beb1d9
fetched_at: '2026-06-29T00:06:24.913719+00:00'
page_id: '224126933'
product: rm
source: tdn-rm
title: TUBU86_DT_Parâmetro_Identifica_Glosa_XML_Retorno_do_Convênio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224126933
version: 122
---

# Parâmetro para identificar glosa no XML de retorno do convênio

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Faturamento | Faturamento para convênios |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Faturamento | Controle de glosa | |
| **Cadastros Iniciais:** | Condições contratuais dos convênios |
| **Parâmetro(s):** | Verifica glosa pelo valor processado no XML de recebimento de contas |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL, Oracle |

## Descrição

Quando o sistema recebe o XML de retorno do convênio, o sistema estava identificando a glosa pela tag “valorProcessado” e o correta era pela tag “valorLiberado”. Sendo assim, foi criado um novo parâmetro nas condição contratuais com o convênio, para que o usuário possa decidir se a glosa vai ser identificada pela tag “valorProcessado” ou pela tag “valorLiberado”.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.9.102 da biblioteca do RM.

## Procedimento para Utilização

1. Acesse a condição contratual do convênio e marque o parâmetro “**Verifica glosa pelo valor processado no XML de recebimento de contas**”.Se o parâmetro estiver desmarcado, por padrão o sistema identificará a glosa pela tag "valorLiberado".
2. Acesse a tela de faturamento para convênios.
3. Localize uma remessa já faturada.
4. Importe o XML de retorno do convênio.
5. Após a conclusão do processo, verificar no controle de glosa a conta foi glosada corretamente de acordo com o XML.

divs
