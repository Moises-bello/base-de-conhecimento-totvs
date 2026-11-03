---
content_hash: 779fbe59b2dffb4baef5644f1ef7fea43de9c70edfd1aec745ebce4b11cf7ad8
fetched_at: '2026-06-29T00:08:24.219468+00:00'
page_id: '270895000'
product: rm
source: tdn-rm
title: DT Prestador para Elegibilidade e Envio XML TISS
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Prestador+para+Elegibilidade+e+Envio+XML+TISS
version: 116
---

# Prestador para Elegibilidade e Envio XML TISS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Condições Contatuais | | Atendimento Interno | | Atendimento Externo | | Agendamento de Atendimento | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada a rotina  de escolha de prestador para as transações de envio arquivos XML TISS.

Essa implementação esta disponível a partir da versão 3.0 da TISS para as transações de Solicitação de Procedimento, Solicita Status Autorização, Verifica Elegibilidade e Cancela Guia..

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.15 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.15.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em "DOWNLOAD".

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM;

   b. Versão: RM 12.1.15;

   c. Tipo: Patch.

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

  1. Acesse "**Cadastros/Faturamento/Condições Contratuais com** **Convênios**".

Na guia Eletrônico III - TISS, acesse a aba Prestador e configure qual código referente ao prestador que deve ir no arquivo xml. As opções são CPF,CNPJ ou  código na operadora  e não utilizar, o que mantem o prestador conforme as regras já existentes.

2. Acesse "**Atendimento/Internação/Registro de Internações**".

Pesquise ou crie um atendimento.

Ao clicar "Histórico de Elegibilidade", ira gerar o arquivo XML com o prestador parametrizado.

XML Gerado

 3. Para o atendimento externo, os passos são os mesmos do item 2 

4. Acesse "**Atendimento/Agendamento/ Agendamento de Atendimento**".

Inclua um paciente na agenda.

Ao pesquisar o paciente irá verificar a elegibilidade e ao salvar a marcação irá gerar o XML de solicitação de autorização.

XML Solicitação Autorização.

Caso queria consultar o status da autorização, clique no botão "Solicitação/Cancelamento", e após no botão conforme imagem 

XML gerado

divs
