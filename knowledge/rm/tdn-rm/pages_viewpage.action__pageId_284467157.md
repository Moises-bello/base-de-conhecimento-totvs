---
content_hash: 4d666b028e0e3c084efa605de68207f9358c3eb6cf80af397d957fc464eab9ff
fetched_at: '2026-06-29T00:08:36.189000+00:00'
page_id: '284467157'
product: rm
source: tdn-rm
title: DT Geração de XML de Contas de Internação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284467157
version: 104
---

# Geração de XML de contas de Internação

Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Condições Contratuais com convênio | SauCondContratAction | | Faturamento de Convênios | SauFaturaProcFatAction | |
| **Parâmetro(s):** | Condições Contratuais com convênio   * Nr Guias por Arquivo XML - Interno * Nr Guias por Arquivo XML - Externo |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Possibilitar a escolha de número de Guias por arquivo XML, até o limite de 100, que é o determinado pelas regras TISS.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados, bem como dos arquivos do Sistema(executáveis, *dlls* e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.18 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.18.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads, aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.18

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Cadastros/Faturamento/Condições Contratuais com convênio** acesse a aba Eletrônico III – TISS e a aba **Geral II**

   Configure o número de Guias por Arquivo XML de atendimentos interno e externo.

## Procedimento para Utilização

 

Na nova MDI,  acesse **Faturamento/Faturamento para Convênios**

Selecione a fatura.

 

Acesse nos processos **Faturamento de Convênio**.

Selecione o tipo de paciente 

Selecione os pacientes que terão as contas faturadas.

Informe a data de vencimento

Executar o processo.

Verificar quantas guias estão em cada arquivo XML

divs
