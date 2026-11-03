---
content_hash: 8ebd505a9a428f0eceb81bae445745205325f62e596823cfc3cdf0766fe14b85
fetched_at: '2026-06-29T00:08:52.369386+00:00'
page_id: '338384814'
product: rm
source: tdn-rm
title: DT Remessa de Pagamento em Lote
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Remessa+de+Pagamento+em+Lote
version: 7
---

# REMESSA DE PAGAMENTO EM LOTE

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Remessa de Pagamento em Lote.* | *Remessa de Pagamento em Lote* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Integração Bancária* | *Integração Bancária* | |
| **Cadastros Iniciais:** | *Convênio, Borderô, Lançamento* |
| **Parâmetro(s):** | *Em Convênios, aba Remessa Bancária | Pagamento* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-4548> |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Sql e Oracle* |
| **Tabelas Utilizadas:** | *FCONVENIO, FBORDERO, FLAN* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Geração de arquivos de remessa de pagamento eletrônico em lote ou multi-coligadas, agrupados pelos dados do Convênio, ou seja, um arquivo por convênio, de acordo com o filtro utilizado.

## Procedimento para Implantação

* Para disponibilizar o recurso, deve ser habilitado a opção no cadastro de perfil do usuário.

* Informe o cadastro de Remessa de Pagamento no campo conforme imagem abaixo.

* Estes dados serão utilizados como default no processo.
  + Código do Layout do Gerador de Saídas,
  + Diretório de Destino,
  + Nome do Arquivo e extensão.
  + Remessa de Pagamento.

**Obs.:**  
O campo "Nome do Arquivo" pode ser composto por uma parte fixa e por uma parte variável, definida pelas seguintes tags:  
DDMMYYYY -  informação da data de geração do arquivo;  
# - Caractere para definir o número sequencial do arquivo.

## Procedimento para Utilização

* Acesse o Menu Movimentações Bancárias, Processos em Lote, Remessa de Cobrança em Lote.

* Ao abrir a tela, clique no botão de incluir filtro e selecione o filtro de acordo com as informações do Borderô.
* Caso deseje salvar em diretório diferente do default cadastrado no convênio, informe no campo Diretório de destino o caminho.

* Importante! O filtro selecionado deve-se estar referenciado o Código da Coligada que será realizado, caso não seja informado o sistema irá executar para todas as coligadas.
  + No exemplo da imagem acima, será realizado a remessa para Borderôs que foram criados "No mês" das coligadas 1 e 6.
  + O Filtro é baseado nos dados do Borderô, então podem ser selecionados de acordo com os campos disponíveis para filtro.
  + Como default, o sistema já possui um filtro interno para carregar somente borderôs autorizados que possuem lançamentos com status cnab diferente de remetido, registrado e recusado.

* Após selecionado o filtro, execute.

* No Log de execução teremos dois tipos, um Log para a geração dos arquivos e outro para informar quais os convênios, nomeados com Código da Coligada e Identificador do Convênio, tiveram a remessa concluída.
  + Veja o exemplo.

* Após a execução o sistema irá salvar os arquivos de acordo com o diretório parametrizado no convênio ou o que foi informado na tela do processo, conforme mostrado na etapa de procedimento de implantação.
  + Lembre-se de ter permissão à pasta caso esteja enviando o arquivo para um diretório na rede.

## Vídeo

600400
