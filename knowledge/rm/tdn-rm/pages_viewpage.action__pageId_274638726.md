---
content_hash: f763a924cd547d52b93a2828fd458434a362327e5a74751ad05459b2d0a653df
fetched_at: '2026-06-29T00:08:33.978595+00:00'
page_id: '274638726'
product: rm
source: tdn-rm
title: DT Mudança de Categoria por Perfil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274638726
version: 112
---

# Mudança de Categoria por Perfil

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Mudança de Categoria do Paciente |  |  | | --- | | **Rotina(s) envolvida(s)** | | Parâmetros por perfil RM Saúde | | Mudança de Categoria do Paciente | |
| **Parâmetro(s):** | Parâmetros por perfil RM Saúde / Geral 2 / Mudança de Categoria |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1002 |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Tabelas Utilizadas:** | SZPARAMPERFIL, SZCADGERAL |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Esta implementação possibilita o controle na alteração do convênio/categoria de um atendimento com base no perfil de acesso do usuário.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse **Cadastros / Segurança / Perfis**.
2. Selecione um perfil.
3. Acesse **Anexos / Parâmetros RM Saúde**.
4. Acesse a aba **Geral 2**.
5. O controle de mudança de categoria por perfil realiza as mudança com base na origem da categoria do registro e no destino da categoria desejada, conforme as seguintes configurações:
   1. Origem:
      1. Ambos: Os registros selecionados para realizar a mudança podem ser tanto da categoria Convênio como Particular.
      2. Convênio: Os registros selecionados para realizar a mudança podem ser apenas da categoria Convênio.
      3. Particular: Os registros selecionados para realizar a mudança podem ser apenas da categoria Particular.
   2. Destino:
      1. Ambos: A nova categoria selecionada para a mudança do registro pode ser tanto Convênio como Particular.
      2. Convênio: A nova categoria selecionada para a mudança do registro pode ser apenas do tipo Convênio.
      3. Particular: A nova categoria selecionada para a mudança do registro pode ser apenas do tipo Particular.

## Procedimento para Utilização

Observação

1. O comportamento desta funcionalidade irá variar conforme parametrização realizada conforme a sessão **CONFIGURAÇÃO DE PARÂMETROS**.
2. Neste exemplo a parametrização segue as configurações abaixo:  
     
   1. O registro de origem deve estar na categoria Convênio e só pode ser transferido para uma categoria Particular.

1. Acesse o menu **Faturamento / Particular e Convênios /  Mudança da Categoria do Paciente**.
2. Pesquise o Paciente.
3. Preencha as informações para auxilar na pesquisa.
4. Na nova categoria será apresentado apenas registros de categoria Particular\*.  
   \*Conforme parametrização exemplo, realizada inicialmente.
5. Sistema apresenta documento de alteração.

Exemplo da validação

1. Caso seja selecionado um registro de categoria Particular\*, no passo 3 da sessão anterior, é apresentada a seguinte mensagem de validação:  
   \*Conforme parametrização exemplo, realizada inicialmente.

divs
