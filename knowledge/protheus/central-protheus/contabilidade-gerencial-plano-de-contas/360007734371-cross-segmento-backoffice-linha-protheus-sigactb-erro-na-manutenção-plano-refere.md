---
article_id: 360007734371
category: Contabilidade Gerencial - Plano de Contas
content_hash: 44fcf4efb68e35f445b82bd82ed310cb4b77616b7321cb632df797ba72775718
fetched_at: '2026-06-28T22:40:33.327449+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Erro na manutenção plano
  referencial
type: support-article
updated_at: '2021-12-14T12:59:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007734371-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Erro-na-manuten%C3%A7%C3%A3o-plano-referencial
---

**Ocorrência**

Tentativa de reservar registro no Alias CVE em EOF Stack de chamadas em MSROCK.eof .Tenta novamente? Essa mensagem será fechada em 5 segundos

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 12

**Causa**A mensagem referente a EOF Stack em MSRLOCK indica que o registro em questão está reservado por outro processo.

Esta mensagem pode acontecer em duas situações:

1º o uso do registro por outro usuário;

2º uma customização que iniciou o tratamento e unlock do registro.

**Solução:**Favor realizar os seguintes procedimentos:

1º - reiniciar o servidor (parando os serviços do TOP, Banco de dados e Server) e realizar novos testes.

Se erro persistir, seguir o segundo procedimento:

2º - verificar se o arquivo msrlock.eof gravado na pasta system existe alguma customização no sistema que envolva o alias apresentado na mensagem.

Saiba mais:

<http://tdn.totvs.com/pages/releaseview.action?pageId=235575485>

<http://tdn.totvs.com/pages/releaseview.action?pageId=6814812>
