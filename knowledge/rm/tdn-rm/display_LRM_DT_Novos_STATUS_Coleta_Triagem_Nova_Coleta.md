---
content_hash: 0d0de5d0ffe535e657a935f1ca8f1e8c4bebea5ee0ee4558b384164e16e23545
fetched_at: '2026-06-29T00:08:15.757575+00:00'
page_id: '244924082'
product: rm
source: tdn-rm
title: DT_Novos_STATUS_Coleta_Triagem_Nova_Coleta
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Novos_STATUS_Coleta_Triagem_Nova_Coleta
version: 119
---

# Novos STATUS Coleta,Triagem,Nova Coleta

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Controle de Pedidos de Exames | | Triagem de Amostras | |
| **Parâmetro(s):** | Utiliza Fluxo com Triagem de Amostras |
| **Requisito (ISSUE):** | SAUHRM01-43 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada a opção de Utilizar Fluxo com Triagem de Amostras.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.13 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.13.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.13

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesseo menu **Opções/Parâmetros/Parâmetros Gerais.**  
   Marque o parâmetro "**Utilizar Fluxo com Triagem de Amostras**".

## Procedimento para Utilização

EtapastrueCriar Atendimento

Acesse o menu**Unidade de Diagnóstico /Registro de Atendimentos Externos.**

Realize um novo atendimento ou altere um já existente no qual a unidade de atendimento seja Laboratório.

Solicite exames, incluindo o vasilhame, para que sejam geradas pelo sistema as amostras.

Ao registrar as alterações e imprimir as etiquetas, o status do exame será alterado para P – Saiu para coleta.

Triagem Amostras

Acesse o menu**Unidade de Diagnóstico / Controle de Pedidos de Exames**.

Para realizar o processo de triagem da coleta em status P, acesse a triagem de amostras , informe o agente e o departamento para pesquisar.

Selecione o pedido e processe a triagem.

Após a triagem, o status passa a ser S, Triado Lab.

Recoleta

Caso ocorra a necessidade de recoletar a amostra, acesse a **Recoleta de Amostras**. Preencha agente e departamento, pesquise, processe e informe uma justificativa para o procedimento.

Pode-se analisar o Controle de histórico dos status e verificar as justificativas.

Após o registro  da recoleta, status passa a ser N, Nova Coleta.

Para emitir as etiquetas da nova coleta, pode-se utilizar a opção de reimpressão de etiquetas.

Matrix

Para o processo de integração com a Matrix, quando o parâmetro **Utiliza Fluxo com Triagem de Amostras** estiver marcado, somente exames já triados são exportados. Caso não esteja marcado, permanecem exportando os exames com status inicial.

Após a integração, o exame passa a ter status de digitação, para que eventuais edições no retorno da Matrix possam ser realizadas.

divs
