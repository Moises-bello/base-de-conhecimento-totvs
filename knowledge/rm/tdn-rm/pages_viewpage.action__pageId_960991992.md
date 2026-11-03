---
content_hash: d4f3305d4a4f4eb507d1194b52e5a21bb1c7f76efdfbbe7faa067302b7faf4dd
fetched_at: '2026-06-29T00:12:13.916750+00:00'
page_id: '960991992'
product: rm
source: tdn-rm
title: FISCAL01-26021 - Gerar Grupo de prestação da NFS-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=960991992
version: 1
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | Envio NFS-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-26039 |

## **02. SITUAÇÃO/REQUISITO**

# Flexibilizar Município de prestação do serviço

A Prefeitura de São Paulo possui regra vigente para emissão de NFS-e que veda o preenchimento do grupo <prestacao> no XML quando:

* O serviço for tributado no município de São Paulo/SP, ou

* Se tratar de exportação de serviços.

Caso esta regra não seja respeitada, o sistema da Prefeitura retorna a **Rejeição 1223: “Para serviço tributado em São Paulo ou exportação de serviços não informe o município onde o serviço foi prestado.”**

Hoje, o RM gera o grupo <prestacao> com base nos campos "Município" e "UF" da aba Integrações > Fiscal do movimento. Para evitar a rejeição, a orientação atual exige que esses campos fiquem em branco, o que cria limitações operacionais relevantes para os clientes. Além disso, esses campos foram originalmente projetados para indicar a **incidência do ISS**, mas acabam sendo interpretados como local de prestação, gerando ambiguidade e confusão no uso e na integração dos dados.

# Objetivo

Adequar a geração do XML da NFS-e no RM para atender corretamente a regra de São Paulo/SP, evitando a rejeição "Rejeição 1223", sem exigir criação de tipos de movimento distintos ou intervenção manual do usuário em grande volume de notas. Além de flexibilizar o comportamento por município pois as regras mudam de acordo com a prefeitura do emitente.

## **03. SOLUÇÃO**

Será implementado um novo campo no anexo *Tributos do produto por Município* do Cadastro de Serviço, com o objetivo de controlar o preenchimento do grupo <prestacao> no XML da NFS-e de forma automatizada, sem depender da ação do usuário ou da criação de tipos de movimento específicos.

## Novo campo

**Local**: Aba *Anexos > Tributos do Produto por Município > NFSe*

**Nome do campo**: Não preencher Prestação do Serviço

## Geração da NFS-e

Quando marcado o novo campo, o grupo <prestacao> não será gerado no XML da NFS-e se o ISS for devido para o município de origem (emitente).

Quando desmarcado, mantém-se o comportamento atual, com preenchimento conforme as regras existentes.
