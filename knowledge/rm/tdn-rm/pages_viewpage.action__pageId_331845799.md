---
content_hash: c99189e95ae2fe18b48dce636fef37fa812e95077d44adfc9546f2c1ea2a1bac
fetched_at: '2026-06-29T00:08:49.587851+00:00'
page_id: '331845799'
product: rm
source: tdn-rm
title: DT Remessa de Cobrança em Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331845799
version: 25
---

# Remessa de Cobrança em Lote.

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Remessa de Cobrança em Lote.* | *Remessa de Cobrança em Lote* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Integração Bancária* | *Integração Bancária* | |
| **Cadastros Iniciais:** | *Convênio, Boletos, Lançamento* |
| **Parâmetro(s):** | *Em Convênios, aba Remessa de Cobrança* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | Totvs0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-4545 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Sql e Oracle* |
| **Tabelas Utilizadas:** | *FCONVENIO, FBOLETO, FLAN* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Geração de arquivos de remessa de cobrança eletrônica em lote ou multi-coligadas, agrupados pelos dados do Convênio, ou seja, um arquivo por convênio, de acordo com o filtro utilizado.

## Procedimento para Implantação

* Para disponibilizar o recurso, deve ser habilitado a opção no cadastro de perfil do usuário.

* Informe o cadastro de Remessa de Cobrança no campo conforme imagem abaixo.

* Estes dados serão utilizados como default no processo.
  + Código do Layout do Gerador de Saídas,
  + Diretório de Destino,
  + Nome do Arquivo e extensão.
  + Remessa de Cobrança.

**Obs.:**  
O campo "Nome do Arquivo" pode ser composto por uma parte fixa e por uma parte variável, definida pelas seguintes tags:  
DDMMYYYY -  informação da data de geração do arquivo;  
# - Caractere para definir o número sequencial do arquivo.

## Procedimento para Utilização

* Acesse o Menu Movimentações Bancárias, Processos em Lote, Remessa de Cobrança em Lote.

* Ao abrir a tela, clique no botão de incluir filtro e selecione o filtro de acordo com as informações do Boleto.
* Caso deseje salvar em diretório diferente do default cadastrado no convênio, informe no campo Diretório de destino o caminho.

* Importante! O filtro selecionado deve-se estar referenciado o Código da Coligada que será realizado, caso não seja informado o sistema irá executar para todas as coligadas.
  + No exemplo da imagem acima, será realizado a remessa para Boletos que foram emitidos na semana das coligadas 1 e 6.
  + O Filtro é baseado nos dados do Boleto, então podem ser selecionados, convênios, status do boleto, status de remessa, datas e entre outras opções disponíveis do cadastro do Boleto.
  + Como default, o sistema já possui um filtro interno para não carregar boletos do Tipo "Débito Automático" e com Status de Remessa Cancelados, Registrado, Registrado Online e boletos com Status de Remessa baixado e Status baixado.

* Após selecionado o filtro, execute.

* No Log de execução teremos dois tipos, um Log para a geração dos arquivos e outro para informar quais os convênios, nomeados com Código da Coligada e Identificador do Convênio, tiveram a remessa concluída.
  + Veja o exemplo.

* Após a execução o sistema irá salvar os arquivos de acordo com o diretório parametrizado no convênio ou o que foi informado na tela do processo, conforme mostrado na etapa de procedimento de implantação.
  + Lembre-se de ter permissão à pasta caso esteja enviando o arquivo para um diretório na rede.

## Vídeo

600400
