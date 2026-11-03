---
content_hash: e8fc5947d1720ea74a6a8ce1d086822ad9b83c053ba42c5e7f85f5b8d9b6cfcc
fetched_at: '2026-06-29T00:12:07.332964+00:00'
page_id: '923567060'
product: rm
source: tdn-rm
title: Atualizar Responsável Técnico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=923567060
version: 12
---

# Conteúdo

Conteúdo

# 1. Visão Geral

O processo de atualização de responsável técnico tem como propósito atualizar os dados de responsável técnico que são adicionados no momento do envio da NF-e.

Atenção

Não execute o processo se o sistema não estiver atualizado para um dos patches listados abaixo ou superiores:

* `12.1.2406.246`
* `12.1.2410.186`
* `12.1.2502.110`

É necessário também atualizar a base de dados com o último script disponível para os patches (**Executar o RM Atualizador**)

Para mais informações sobre os campos confira a documentação do

# 2. Permissões de usuário

Para a execução do processo é necessário que o usuário tenha a permissão 04.02.01.01.16:

Para mais informações clique [aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30934416662551-Atualiza%C3%A7%C3%A3o-de-V%C3%ADnculo-com-o-Fornecedor-na-SEFAZ-PR-TOTVS-Backoffice-Linha-RM).

# 3. Parametrizações

## 3.1 Filial

 Será necessário marcar a flag do campo Habilita NT 2018.05 nos dados fiscais do cadastro da Filial para informar se as notas emitidas pela mesma deverão seguir o padrão definido na NT 2018.005. Anexo Dados Fiscais do cadastro da filial:

## 3.2 Parâmetros Globais

Acesse o sistema RM, logo após navegue para aba Ambiente, posteriormente acesse o menu de **Parâmetros Globais,** após acessar a aba **Integração Mashup**, informe a URL para o serviços do TOTVS API Service possam ser consumidos diretamente no servidor.

**URL de serviços do Mashup:**  
<https://totvsapiservices.totvs.com.br>

**Importante:**Salve as configurações após preencher os parâmetros.

# 4. Execução do Processo

O processo Enviar pode ser Executado no módulo de Gestão de Estoque, Compras e Faturamento, acessando os processos da NF-e, conforme abaixo:
