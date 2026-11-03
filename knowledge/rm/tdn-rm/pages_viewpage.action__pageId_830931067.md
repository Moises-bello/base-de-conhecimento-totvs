---
content_hash: 12d38443d2694af1ae1ff9a3c42cab34e040de0be91f65d70576c53470618fbe
fetched_at: '2026-06-29T00:11:49.334804+00:00'
page_id: '830931067'
product: rm
source: tdn-rm
title: Secretaria - Relatório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=830931067
version: 14
---

Nesta etapa é possível definir os relatórios padrões do sistema:

É possível definir até dois relatórios por classificação: **Aluno, Secretaria e Tesouraria.**

Esses relatórios estarão disponíveis para geração/impressão rápida nas respectivas telas de edição de "Aluno", "Matrículas no período letivo" e "Contrato", através de botões de ação disponibilizados na parte superior dessas telas da seguinte forma:

Caso ao acessar uma dessas telas, a seguinte mensagem for apresentada:

deve-se seguir as orientações presentes nos detalhes da mensagem para redefinir os relatórios e corrigir a configuração dos mesmos:

*"O código da coligada desse(s) relatório(s) não foi preenchido. É necessário vincular novamente o(s) relatório(s) na tela de configurações e salvar as configurações com a finalização do parametrizador."*

**Descontinuidade:**

A partir da versão 12.1.2310 foram descontinuados relatórios, planilhas, cubos e/ou outros objetos gerenciais em Delphi.

Devido a isso, o campo **Tipo de relatório** que era apresentado nesta tela para permitir a seleção entre o gerador de relatórios antigo (Delphi) ou atual RM Reports (.Net), foi removido.

Este campo também definia o tipo de gerador que seria utilizado nos relatórios na visão  de turmas (Turmas → Processos → Imprimir relatório).

Dessa forma, esses relatórios passaram a ser gerados utilizando o novo gerador .Net por padrão.
