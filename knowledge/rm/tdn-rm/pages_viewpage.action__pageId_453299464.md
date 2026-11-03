---
content_hash: 292f1e3492cf8ef56cc3677633e6f355f6bdc27eb9e8b377282a7f92ef0b1dc8
fetched_at: '2026-06-29T00:10:11.905277+00:00'
page_id: '453299464'
product: rm
source: tdn-rm
title: Discriminação dos Serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453299464
version: 26
---

# Conteúdo

Conteúdononenone

# 1. Sobre

A descrição do serviço na NFS-e (Nota Fiscal Eletrônica de Serviço) pode ser detalhada nos campos Descrição, Discriminação e Observação. Entretanto, algumas prefeituras não disponibilizam todos estes campos e outras tem necessidade específicas.

O Backoffice RM criou uma solução dinâmica que permite ao usuário definir quais os campos serão gerados e qual a informação deve compor cada campo. Além disso, esta configuração pode ser realizada para cada prefeitura.

# 2. Parametrização de Campos

Nos parâmetros por Filial da NFS-e deve ser acessada a etapa “13 – Observações NFS-e”.

Imagem

**Ambiente -> Parâmetros -> Gestão de Estoque, Compras e Faturamento -> Integrações -> Fiscal -> Dados Fiscais -> Parâmetros por Filial -> Observações NFS-e**

Nestes parâmetros é possível configurar a ordem e quais os campos serão considerados para o preenchimento do XML da NFS-e conforme as opções abaixo.

## I. Descrição do Produto

A descrição do produto será gerada considerando a parametrização "[Definições de Produto 1/3](https://tdn.totvs.com/pages/viewpage.action?pageId=423938842)" do Módulo Gestão de Estoque, Compras e Faturamento.

## II. Histórico do Movimento

O Histórico do Movimento será gerado a partir dos campo "Histórico Longo" ou "Histórico Curto", dependendo da parametrização do tipo de histórico definido nos parâmetros do Tipo de Movimento etapa "".

## III. Histórico do Item

O Histórico do Item será gerado a partir dos campo "Histórico Longo" ou "Histórico Curto", dependendo da parametrização do tipo de histórico definido nos parâmetros do Tipo de Movimento, etapa "".

## IV. Número do Contrato

Será gerado com a descrição "Contrato Número: " + o código do contrato.

Observe que, para alguns municípios, é obrigatório que esta informação conste na nota fiscal; como, por exemplo, Belo Horizonte, através do decreto nº 4.032/81.

# 3. Geração do XML da NFS-e

Os campos serão gerados no XML da NFS-e conforme a disponibilidade de cada prefeitura. Além disso, o fato do campo ser gerado no XML não significa que ele será impresso no relatório da prefeitura. Esta regra deve ser consultada com cada prefeitura.

No layout único de integração da NFS-e com o TSS, serão gerados os campos **servico.discr**, **infcompl.descricao** e **infcompl.observacao** respeitando as regras abaixo.

### Regras

0leftRegras Gerais

* Os campos serão preenchidos com os dados de todos os itens do Movimento, mas serão considerados somente itens do tipo serviço;
* Os dados serão preenchidos respeitando a ordem na qual foram parametrizados;
* O tamanho dos campos serão limitados em 2000 caracteres.
* Se mais de um campo for parametrizado para o preenchimento das tags de descrição, discriminação e observação o conteúdo é separado por quebras de linha. Com exceção dos municípios que não aceitam quebras de linha, neste caso é usado pipe ("|").
Barueri

* O tamanho dos campos serão limitados em 1000 caracteres.
Belo Horizonte

* Todas as quebras de linha serão substituídas por pipe ("|").
Caçapava

* O tamanho dos campos serão limitados em 4000 caracteres.
Cuiabá

* Todas as quebras de linha serão substituídas por pipe ("|").
Porto Alegre

* Todas as quebras de linha serão substituídas por pipe ("|").
Rio Verde

* Todas as quebras de linha serão substituídas por pipe ("|").

# 4. Outras informações

* [Campo Discriminação](https://tdn.totvs.com/pages/viewpage.action?pageId=560653813)
* [Campos Observação e Descrição](https://tdn.totvs.com/pages/viewpage.action?pageId=560653881)
