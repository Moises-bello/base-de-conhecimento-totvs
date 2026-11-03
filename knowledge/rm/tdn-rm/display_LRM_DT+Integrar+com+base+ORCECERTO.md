---
content_hash: 9d77baf05273c34cc1533eff30be1d7d660bcf21c6df46aae472a8e8651784d5
fetched_at: '2026-06-29T00:09:53.491099+00:00'
page_id: '440839603'
product: rm
source: tdn-rm
title: DT Integrar com base ORCECERTO
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Integrar+com+base+ORCECERTO
version: 3
---

# INTEGRAR COM BASE ORCECERTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Obras e Projetos |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Integrar com base ORCECERTO | Integrar com base ORCECERTO |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Insumo  Preço de Insumo  Composição  Recursos de composições | Insumo  Preço de Insumo  Composição  Recursos de composições | |
| **Cadastros Iniciais:** | Projeto, Web Service da Orcecerto |
| **Parâmetro(s):** | Não se aplica |
| **Ponto de Entrada:** | Não se aplica |
| **Tickets relacionados** | Não se aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [TOPORCAPLAN001-5592](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-5592) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Sql e Oracle |
| **Tabelas Utilizadas:** | Não se aplica |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | Não se aplica |

## Descrição

Importar insumos, preços de insumos, composições e recursos de composições das bases disponibilizadas pela ORCECERTO.

## Procedimento para importação

No menu de importações, acessar o processo "**Integrar com Base ORCECERTO"**.

Existem três tipos de versões que podem ser utilizadas para importação, sendo que o número das mesmas pode ser alterado em caso de necessidade de controle da ORCECERTO:

* OCxxxxx: Base de dados com padrões definidos pela ORCECERTO;
* SICROxxxxx: Base de dados com padrões definidos pelo DNIT que atendem ao SICRO;
* SINAPxxxxx: Base de dados  com padrões definidos pelo SINAPI.

* Ao executar a importação, a compatibilidade de Unidades de Insumos e Composições será realizada, e caso seja encontrado alguma Unidade que não esteja cadastrada na base destino, uma tela será exibida com todas as Unidades ausentes que necessitam de definição de uma unidade equivalente. É obrigatório o preenchimento de todas as Unidades:
* A última versão utilizada na importação é armazenada após a execução do processo, para que em futuras importações, ao abrir a tela, tal versão seja selecionada automaticamente para o projeto em aberto;
* Para as versões relacionadas ao SICRO, será possível importar preço desonerado, e os recursos vinculados das composições caso existam, serão importados automaticamente.
* Os recursos vinculados estão disponíveis na edição de 'Recursos da Composição', anexo **"Recursos Vinculados"**.
