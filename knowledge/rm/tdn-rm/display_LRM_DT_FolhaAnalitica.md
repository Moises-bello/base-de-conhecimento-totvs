---
content_hash: ecb83df15ff074b5e6060b00c7f38af5e45046fc02673194b69f58b0e8760285
fetched_at: '2026-06-29T00:08:06.979446+00:00'
page_id: '236599542'
product: rm
source: tdn-rm
title: DT_FolhaAnalitica
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_FolhaAnalitica
version: 16
---

# FOLHA ANALÍTICA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Folha Mensal | Folha Analítica | |
| **Versões/Release:** | 12.1.11 |

## Descrição

O TOTVS Folha de Pagamento permite a migração do relatório da Folha Analítica Delphi para Folha Analítica .NET

## Procedimento para Utilização

Foi finalizada a migração da Folha Analítica para a arquitetura .Net. Para acessá-la deve-se utilizar a nova MDI através no menu **RH / Folha de Pagamento / Folha Mensal/ Folha Analítica**conforme imagem abaixo:

O layout da nova Folha Analítica foi desenvolvido utilizando o RM Reports, o que permite de forma simples fazer customização do relatório se necessário.  
 Antes da utilização do módulo é necessário importar o relatório padrão disponível no diretório de Objetos Gerenciais (FOPREL09.0009 - Folha Analítica).

Ao gerar a Folha Analítica deve-se selecionar o layout desejado conforme abaixo:

É premissa importar o relatório FOPRELFATXT – Folha Analítica (PDF) **ou** FOPREL0009 - Folha Analítica (TXT).

Na tela de Dados do Funcionário, o usuário pode informar fórmula de cabeçalho, também pode incluir ou excluir fórmulas de resumo de funcionário, conforme tela abaixo:

Na tela de configuração de impressão, deve-se selecionar o caminho onde será salvo os arquivos, conforme tela abaixo:

É possível na tela de configuração de impressão de parametrizar o formato de saída do relatório, conforme tela abaixo:

Na tela de Seleção de coligadas, pode-se adicionar ou remover parâmetros para a coligada selecionada.

Para adicionar parâmetros, clique em adicionar parâmetros à coligada. 

O sistema exibe nova tela de “Parâmetros específicos da coligada”. 

É premissa que, para avançar o processo para geração da folha analítica, deve-se selecionar uma coligada.

Ao executar o processo, será exibido um log com alerta de sucesso e erro. 

# Conversão de Perfis

Foi criado uma planilha com todo o mapeamento de campos de Delphi para .NET.

Todos os parâmetros do perfil Delphi que existem em .NET devem ser carregados na Folha Analítica .NET.

Foi adicionada a opção **Folha Analítica**dentro do processo "Conversão de perfis (Delphi x .NET)

Ao selecionar a opção **Folha Analítica**, o sistema irá trazer todos os perfis cadastrados em Delphi, filtrados pela coligada do contexto.

Após selecionar os perfis e executar o processo, serão criados novos perfis para .NET, onde o nome do perfil terá como sufixo "\_convertido".

Os perfis Delphi são salvos na tabela PPARAMRELAT, com TIPORELAT = 1 e IDRELAT = 1  
 Os perfis .NET são salvos na tabela PPARAMRELAT, com TIPORELAT = 501 e IDRELAT = 1

O processo da Folha Analítica .NET irá carregar todos os perfis convertidos para a coligada do contexto.

O log do processo é quebrado por perfil. O log mostra o alerta de sucesso ou erro. No caso de erro, a mensagem fala o motivo.

Mensagem de sucesso:

Exemplo de Mensagem de erro:

## Planilha de Mapeamento
