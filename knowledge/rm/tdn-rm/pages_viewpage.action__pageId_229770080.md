---
content_hash: 30ef72e83be461297af3e9a1676c01b1ff8adbace1c090e1f1df17444e541cf6
fetched_at: '2026-06-29T00:06:27.045256+00:00'
page_id: '229770080'
product: rm
source: tdn-rm
title: DT_Painéis_de_Chamados_Simultâneos_para_uma_Unidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=229770080
version: 122
---

# Permitir Mais de uma Conexão a uma Mesma Unidade no Painel de Chamados

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Painel de Chamadas |  |  | | --- | | **Rotina(s) envolvida(s)** | | Painel de Classificação de Riscos | | Cadastro de Unidades | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL, Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta implementação possibilita ao usuário utilizar mais de um Painel, simultaneamente, conectado a uma mesma unidade de atendimento, ou a um grupo delas.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.10 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.10.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.10

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu **Cadastros / Uso Geral / Unidades de Atendimento**.
2. Selecione a(s) unidade(s) desejada(s) e marque os parâmetros “**Realiza Classificação de Risco**” e “**Utiliza Senha de Atendimento**”. Caso deseje, é possível configurar também um prefixo de senha.
3. Acesse o menu **Cadastros / Registro e Controle / Totem** e crie um Totem, conforme desejado.
4. Acesse o menu **Atendimento / Pronto Atendimento / Painel de Classificação de Riscos** e selecione a aba “**Plantão**”.
5. Na grid da parte inferior, inclua as especialidades que serão atendidas pelas unidades de atendimento cadastradas no Totem.
6. Ainda na aba **Plantão**, inclua os profissionais para atender aos plantões nas unidades, clicando no botão **+**.

## Procedimento para Utilização

1. Acesse o menu **Atendimento / Pronto Atendimento / Ambulatório > Totem de Pronto Atendimento**, selecione o Totem configurado e gere algumas senhas.
2. Abra o Painel de Chamados em duas abas distintas do navegador, selecione as mesmas unidades de atendimento para monitorar e clique em **Acessar**.
3. Acesse novamente o **Painel de Classificação de Riscos**, e selecione a Unidade de Atendimento desejada.

Acesse a aba **Registro de Triagem** e dê duplo clique na senha que desejar chamar. Ambos painéis abertos deverão listar a unidade chamada, simultaneamente.

divs
