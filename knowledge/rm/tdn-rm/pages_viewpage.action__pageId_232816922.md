---
content_hash: 70c3633955c17112f86896aa4cc97037c65e087f21b467c91e291c0833deab4f
fetched_at: '2026-06-29T00:06:27.281491+00:00'
page_id: '232816922'
product: rm
source: tdn-rm
title: DT_Tempo_do_Paciente_em_Observação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232816922
version: 122
---

# Tempo em Observação do paciente na Classificação de Risco

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Atendimento | Painel de Classificação de Risco | |
| **Requisito (ISSUE):** | PCREQ-9988 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZCLASSIFICACAORISCO, SZLOGATENDIMENTO |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Para pacientes em observação, a coluna "Espera" ficava em branco.

Melhoria consiste na inclusão do tempo em que o paciente está em observação a partir da data/hora que o mesmo foi transferido para observação (aba de "Atendimento Médico" e "Posto de Enfermagem").

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

## Procedimento para Utilização

É necessário que exista plantonista cadastrado no dia desejado e as especialidades atendidas.

1. Acesse o menu **Atendimento/Pronto Atendimento/Toten de Pronto Atendimento**.
2. Selecione a unidade de atendimento.
3. Selecione a especialidade deseja e gere uma senha.
4. Acesse o menu **Atendimento/Pronto Atendimento/Painel de Classificação de Risco**.
5. Selecione a mesma unidade em que a senha foi gerada.
6. Selecione a aba "**Registro de Triagem**" e faça o registro.
7. Selecione a aba "**Registro de atendimento**" e realize o registro do paciente.
8. Acesse o sistema com um usuário de perfil médico e realize a chamada da senha para colocar o paciente com o status de "**Em atendimento**".
9. Com o registro do paciente selecionado, clique em "**Enviar p/ Observação**". Neste momento a coluna "**Espera**" exibirá o tempo que o paciente está em espera.
10. Na aba **Posto de Enfermagem** a informação também será exibida.

divs
