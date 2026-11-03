---
content_hash: 66c65f3208353ff5e28237a8cd174bef26c03e4294d550013f09f4c4833c6977
fetched_at: '2026-06-28T21:35:23.320752+00:00'
page_id: '244738194'
product: fluig
source: tdn-fluig
title: Visão geral qualidade da plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244738194
version: 37
---

# Índice

true.\*ndicenone

# Introdução

---

Esta página tem o objetivo de descrever de forma geral o processo de qualidade do TOTVS Fluig Plataforma, mostrando os níveis de testes que são executados nos processos de Inovação e Manutenção do produto.

Abaixo está ilustrado o fluxograma de desenvolvimento e níveis de teste que são executados em cada atualização da plataforma.

Legenda de cores:

# Processo de Inovação

---

Na inovação são implementadas as novidades no produto, ou seja, são desenvolvidos novos recursos funcionais. Após o desenvolvimento de uma novidade ser finalizado, esta é submetida aos seguintes níveis de testes:

## Teste de unidade

* Primeiro nível de auditoria funcional realizada em cada novidade.
* É realizado por um desenvolvedor par dentro da equipe.
* Verifica se os critérios de aceitação (casos de teste) especificados nas novidades foram atendidos.
* Se o teste for aprovado, a novidade é enviada para o teste integrado. Caso contrário é gerado um retrabalho.

## Teste integrado

* Segundo nível de auditoria funcional realizada em cada novidade.
* Executado pelo time SQA (*Software Quality Assurance*) em ambiente específico e adequado para este nível de teste, sendo que neste ambiente estão integradas todas as demais novidades que foram implementadas.
* Novamente são verificados se todos os critérios de aceitação foram atendidos, mas com a visão sistêmica do SQA.
* Se o teste for aprovado, a novidade fica aguardando o término das demais novidades planejadas para a atualização da plataforma, sendo represada para o próximo nível de teste, “*Quality* de Inovação”.
* Se for reprovado, é gerado retrabalho e passará novamente pelo teste de unidade e teste integrado.

## *Quality* Inovação

* Terceiro nível de testes que é realizado após o término de todas as novidades de uma atualização.
* SQAs executam todos os casos de teste que geraram impacto no produto, de acordo com as novidades que foram implementadas.
* Caso sejam identificadas não-conformidades são abertos chamados internos de *bugs*, os quais devem ser corrigidos para liberação da atualização.

Observação

Caso determinada novidade não esteja pronta e devidamente testada e aprovada, a mesma não é liberada para a atualização corrente, sendo transferida para a próxima atualização.

# Processo de Manutenção

---

Paralelamente ao processo de Inovação, na Manutenção ocorrem as correções dos chamados de *bugs* que foram devidamente priorizados para correção e que serão liberados na atualização corrente da plataforma.

Após finalizar o ajuste (correção) de um *bug*, este é submetido aos seguintes níveis de testes:

## Teste integrado:

* Após a correção de cada *bug* é realizado o teste integrado, ou seja, a auditoria funcional.
* É executado por SQA em ambiente específico e adequado para este nível de teste, sendo que este ambiente contém todas as demais correções de *bugs* já efetuadas.
* Se o teste for aprovado, a correção fica aguardando o término das demais correções planejadas para a atualização, sendo represada para o próximo nível de testes: *Quality* de Manutenção.
* Se for reprovado, é gerado retrabalho e passará novamente pelo teste integrado.

## *Quality* Manutenção:

* Última e mais importante bateria de testes realizada para liberação da atualização.
* Antes desta bateria de testes ser iniciada, ocorre a unificação de todas as novidades já testadas pela fase "*Quality* de Inovação" com os todos os *bugs* que foram corrigidos e testados, formando a atualização "candidata" que será liberada.
* Nesta versão unificada é executada uma bateria de testes contendo todos os casos de teste essenciais(\*) do produto em outro ambiente específico para este processo.
* Caso sejam identificadas não-conformidades nesta bateria de testes são abertos chamados internos para correção dos *bugs*. Estes *bugs* devem ser corrigidos para a liberação da atualização.

Observação

\* Cenários “essenciais” são casos de testes definidos como extremamente críticos para utilização do produto. Temos mais de 900 cenários de testes.

Cada novidade realizada no produto gera novos cenários de testes, sendo que alguns deles obrigatoriamente são definidos como “essenciais”, incrementando a bateria de testes do *Quality* Manutenção.

# Resumo Tipos de Testes e Responsabilidades

---

# Testes Automatizados e Integração Contínua

---

Complementando os níveis de testes citados anteriormente, utilizamos o Bamboo como *software* de integração contínua.

O Bamboo possui vários planos de compilação dos ambientes de Manutenção e Inovação, alertando as equipes responsáveis caso ocorra algum erro de compilação do produto.

Além de compilar o produto várias vezes por dia, o Bamboo também executa a bateria de testes automatizados. Seguem abaixo alguns detalhes destes testes:

* A bateria de testes automatizados possui mais de 1000 testes. Esta bateria é executada 1 vez por dia para cada um dos três bancos homologados: MySQL, SQL Server e Oracle.

* Em caso de falha (ou "quebra") de algum cenário de teste automatizado, a causa deve ser investigada e corrigida com urgência.

* A atualização não é liberada para clientes caso ocorra alguma quebra de teste automatizado.

**Trecho do *dashboard* de acompanhamento de execução de testes automatizados**
