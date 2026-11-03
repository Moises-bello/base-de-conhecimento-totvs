---
content_hash: c8b7e1f773f2e280650493367d90377dc417ebf08da3fc0ecf70380f6c00996f
fetched_at: '2026-06-29T00:09:23.925106+00:00'
page_id: '422546161'
product: rm
source: tdn-rm
title: Rotina Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/Rotina+Fiscal
version: 65
---

# Conteúdo

Conteúdononenone

true

# 1. Introdução

Neste cadastro vamos informar os dados referentes as Rotinas Fiscais, como: Código, Descrição, Tipo de Rotina e Vigência. Estes dados serão utilizados na geração das Rotinas Fiscais.

# 2. Tela para inclusão da Rotina

# 3. Regras

Regras Específicas

* Ao criar uma Rotina Fiscal que será usada na apuração do PIS/COFINS e no [Pré-Processamento](https://tdn.totvs.com/pages/viewpage.action?pageId=853282471), a mesma deve ter a vigência abranja a vigência do [Período de Apuração](https://tdn.totvs.com/pages/viewpage.action?pageId=422545773).

# 4. Parâmetro de Geração Gerador de Saídas

* A configuração dos parâmetros da rotina é realizada incluindo os campos "Chave" e "Valor" no cadastro. O campo chave é a referencia dos campos dos parâmetros da rotina, e o campo valor é o conteúdo do campo.
* Podemos encontrar os dados referente a chave e valor na configuração do layout da rotina, em contexto, parâmetros de geração.
* O time de desenvolvimento é quem disponibiliza o campo chave e valor para configuração conforme necessidade específica das rotinas fiscais.

Exemplo do campo chave no Gerador de Saídas

# 5. Conteúdo Relacionado

* [Parâmetros da Rotina (Anexos)](https://tdn.totvs.com/pages/viewpage.action?pageId=842699260)
* [Processo Parâmetros da Rotina (Processos)](https://tdn.totvs.com/pages/viewpage.action?pageId=904623381)
