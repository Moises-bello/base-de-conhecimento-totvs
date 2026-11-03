---
content_hash: e3946dd87c92303e6000fb852cc13d1783821ecb19ab0775a1ccdbd6aea903a0
fetched_at: '2026-06-29T00:08:46.961021+00:00'
page_id: '317312689'
product: rm
source: tdn-rm
title: DT Processo para a associação de matrizes aplicadas à campus/polo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317312689
version: 3
---

# Processo para a associação de matrizes aplicadas à campus/polo

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | ****TOTVS Gestão Educacional**** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Associação de Matrizes Aplicadas à Campus/Polo.* | **Associação de Matrizes Aplicadas à Campus/Polo** | |
| **Cadastros Iniciais:** | *Cadastros necessários para a realização da associação:*   * *Cadastro de Campus/Polo* * *Matrizes Aplicadas* |
| **Ponto de Entrada:** | * **Currículo e Oferta | Matrizes curriculares**   ***Processos | Associar matrizes aplicadas à Campus/Polo***     * **Currículo e Oferta | Mais... | Assistente para associação de matrizes aplicadas à Campus/Polo** |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *EDUCACIONAL01-2847* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | **SQL e Oracle** |
| **Tabelas Utilizadas:** | *SHABILITACAOFILIALCAMPUS* |
| **Sistema(s) Operacional(is):** | **Windows** |

## Descrição

O processo de associação tem como objetivo a criação de vínculos entre as matrizes aplicadas e os Campus/Polos cadastrados, em lote. É possível que sejam selecionadas várias matrizes e vários campus/polo para a criação de um vínculo entre eles. O acesso ao processo se dar por meio de duas formas:

* De um assistente, localizado em Currículo e Oferta | Estrutura Curricular | Mais | Assistente para associação de matrizes aplicadas à campus/polo;
* Do item Associar matrizes aplicadas à campus/polos, localizado no cadastro da Matriz Curricular | Processos.

Neste processo é possível definir se os vínculos já existentes serão sobrepostos na execução do mesmo, pelo parâmetro **Sobrescrever vínculos existentes**. Quando este parâmetro estiver marcado todos os campus/polos das matrizes selecionadas serão excluídos e os novos campus/polos selecionados serão incluídos. Por outro lado, se o parâmetro estiver desmarcado e na execução do processo já existir o campus/polo em uma matriz o mesmo permanecerá, porém um Log no final do processo será informado que o vínculo já existe.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PERMISSÕES**

1. No cadastro de perfis de usuário, é necessário que seja atribuída as permissões para de acesso à menus para execução do processo :

* + ***Educacional |  [01] Currículo e Oferta | [01.02] Estrutura curricular | [01.02.05] Mais... | [01.02.05.12] Assistente para associação de matrizes aplicadas à campus/polo***
  + ***Educacional |  [01] Currículo e Oferta | [01.02] Estrutura curricular | [01.02.02] Matrizes curriculares | [01.02.02.15] Associação de matrizes aplicadas à campus/polo***
