---
content_hash: e429e6453519c08bf0785a2d0d0555092ac562d3cd33d8152727273073768ab0
fetched_at: '2026-06-29T00:08:25.071828+00:00'
page_id: '270911769'
product: rm
source: tdn-rm
title: DT Parâmetro Obrigatoriedade do Médico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270911769
version: 116
---

# Obrigatoriedade do Médico

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | Rotina | | Parâmetros Gerais | | Atendimento Interno | | Atendimento Externo | |
| **Parâmetro(s):** | Obriga Médico Responsável e Solicitante no registro de atendimento interno  Obriga Médico Responsável e Solicitante no registro de atendimento externo |
| **Requisito (informe o requisito relacionado):** | SAUHRM02-484 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

A partir dessa implementação, é possível parametrizar a obrigatoriedade do médico responsável e do médico solicitante no registro de atendimentos interno e externos.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.15 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.15.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.15

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse**Opções/Parâmetros/Parâmetros Gerais**aba Registro e Controle II.
   1. Marque os parâmetros **Obriga Médico Responsável e Solicitante no registro de atendimento interno** e**Obriga Médico Responsável e Solicitante no registro de atendimento externo**

## Procedimento para Utilização

1. **Acesse Atendimento-> Internação-> Registro de Internação**  
   Crie ou altere um atendimento.  
   Com os parâmetros descritos acima marcados, caso as informações de Médicos Responsáveis não estejam preenchidas, será exibida a mensagem abaixo.

1. **Atendimento-> Pronto Atendimento/Ambulatório-> Registro de Atendimento**  
   Crie ou altere um atendimento.  
   Com os parâmetros descritos acima marcados, caso as informações de Médicos Responsáveis não estejam preenchidas, será exibida a mensagem abaixo.

divs
