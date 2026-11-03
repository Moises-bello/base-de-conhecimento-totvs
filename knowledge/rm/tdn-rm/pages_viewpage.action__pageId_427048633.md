---
content_hash: 50a38098d1af267d39d0b48a0eafdbd6bb4dde261f6c76b9e32f3fd3b5744946
fetched_at: '2026-06-29T00:09:38.566142+00:00'
page_id: '427048633'
product: rm
source: tdn-rm
title: Cálculo Contribuições Documentos não escriturados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=427048633
version: 48
---

O processo **Cálculo das Contribuições Docs Não Escriturados** (*Utilitários*) preenche os tributos PIS e COFINS nos lançamentos financeiros. Para fazer esse preenchimento o sistema considera os filtros criados nos cadastro de Parâmetros de processos.

false1true1Passo 1

Acesse o Cadastro de Parâmetros de Processos do F100, no menu Anexos | Filtro de operações faça a parametrização desejada e informe os tributos PIS e COFINS

ImagemImagemImagemImagem2Passo 2

No menu Utilitários| Cálculo das Contribuições Docs Não Escriturados execute o processo para o Mês\Ano desejado. Esse processo vai preencher os tributos PIS e COFINS nos lançamentos financeiros que atendam aos filtros criados no item 1.

Imagem2Passo 3

Lançamento financeiros RM FLUXUS com os tributos preenchidos (Lançamento será considerado no registro F100 do EFD Contribuições).

Imagem

Conteúdo

## **01. Executar Processo de Cálculo dos DOCS não Escriturados**

O processo **Cálculo das Contribuições Docs Não Escriturados** (*Utilitários*) preenche os tributos PIS e COFINS nos lançamentos financeiros. Para fazer esse preenchimento o sistema considera os filtros criados nos cadastro de Parâmetros de processos.

false1true1Passo 1

Acesse o Cadastro de Parâmetros de Processos do F100, no menu Anexos | Filtro de operações faça a parametrização desejada e informe os tributos PIS e COFINS

ImagemImagemImagemImagem2Passo 2

No menu Utilitários| Cálculo das Contribuições Docs Não Escriturados execute o processo para o Mês\Ano desejado. Esse processo vai preencher os tributos PIS e COFINS nos lançamentos financeiros que atendam aos filtros criados no item 1.

Imagem2Passo 3

Lançamento financeiros RM FLUXUS com os tributos preenchidos (Lançamento será considerado no registro F100 do EFD Contribuições).

Imagemtrue

## **02. Cálculo dos Docs não escriturados no Encerramento do Período**

A partir das versões 12.1.2406 o Cálculo dos DOCS não escriturados poderá ser executado no encerramento do Período, desde que o parâmetro interno esteja configurado corretamente.

Encerramento dos períodos de Apuração PIS e COFINS

Após encerrar os períodos, os Tributos foram gravados no lançamento Financeiro de acordo com os Parâmetros de Processos:

Tributo no Lançamento Financeiro

O Registro F100 da rotina EFD-Contribuições, será gerado com os valores que estão gravados no anexo Detalhamento Apuração, para mais informações acesse a documentação da [EFD-Contribuições](https://tdn.totvs.com/pages/viewpage.action?pageId=422545925).

Detalhamento Apuração

Quando o usuário executar o processo de Cálculo das Contribuições Docs Não Escriturados (Pelo menu *Utilitários*) e o sistema esteja parametrizado para fazer o cálculo no encerramento do período, o sistema irá apresentar um alerta informando que o cálculo será realizado automaticamente no Encerramento dos Períodos dos Tributos PIS / COFINS.

Imagem do alerta

No Encerramento do Período de Apuração só vão ser atualizados os dados para o Tributo específico (PIS / COFINS) selecionado.
