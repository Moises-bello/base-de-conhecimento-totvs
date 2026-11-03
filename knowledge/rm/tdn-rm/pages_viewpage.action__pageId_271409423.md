---
content_hash: 7c14830e7142710a427b7cd65dcb7012523a2f7105b0e1aa2056d38b2f70075f
fetched_at: '2026-06-29T00:08:27.384070+00:00'
page_id: '271409423'
product: rm
source: tdn-rm
title: DT Máscara de Telefone para Paciente e Prestador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271409423
version: 109
---

# Máscara de telefone para paciente e prestador

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Parâmetros Gerais | | Cadastro de Prestadores | | Dados de um Paciente | | Atendimento Externo | | Atendimento Interno | |
| **Parâmetro(s):** | Permite Máscara Celular incompleta  Salvar Máscara Celular |
| **Requisito:** | SAUHRM02-594 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

A partir dessa implementação, é possível configurar máscara para cadastrar o celular de pacientes e prestadores.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.16 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.16.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.16

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

Importante

Antes de configurar a máscara, o cliente deverá rever todo o seu cadastro de paciente e prestadores para ajustar à máscara desejada. Caso contrário, a aplicação da máscara poderá acarretar em perda da informação já cadastrada.

1. Acesse**Opções/Parâmetros/Parâmetros Gerais**aba **Registro e Controle**.
   1. Marque os parâmetros **Permite Máscara Celular incompleta**, **Salvar Máscara Celular** e preencha o padrão da máscara no campo **Máscara Celular**.

## Procedimento para Utilização

1. No menu **Atendimento/ Pronto Atendimento/Ambulatório/ Registro de Atendimento** crie ou altere um atendimento.
2. Com os parâmetros descritos acima marcados, a máscara será configurada no campo **Celular**.
3. Acesse **Atendimento/ Internação/ Registro de Internação** e crie ou altere um atendimento.
4. Com os parâmetros descritos acima marcados, a máscara será configurada no campo **Celular**.
5. Acesse o menu **Atendimento / Recepção** e os dados de um paciente.
6. Crie ou edite o cadastro de um paciente.
7. Com os parâmetros descritos acima marcados, a máscara será configurada no campo **Celular**.
8. Acesse **Cadastro / Uso Geral / Prestador**.
9. Crie ou edite o cadastro de um prestador.Com os parâmetros descritos acima marcados, a máscara será configurada na aba **Complemento 1**, no campo **Celular**.

divs
