---
content_hash: 9be5ca59a6d9c53b1d1b73d68ea856a1bd71b929ed7f7240a3d191ecc1bdc413
fetched_at: '2026-06-29T00:08:25.916501+00:00'
page_id: '271165211'
product: rm
source: tdn-rm
title: DT Taxa Oxigênio Litros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271165211
version: 116
---

# Taxa Oxigênio Litros

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Integração RM Nucleus | | Condições Contratuais | | Tabela de Procedimentos e Serviços | | Elaboração de Conta | | Prontuário | |
| **Parâmetro(s):** | Utiliza Faturamento de Gases em Litros |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada a rotina  de utilização de cobrança de taxa de gases na unidade de medida litros.

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

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse "****Opções/Parâmetros/Integração RM**** **Nucleus**".  
   Configure a unidade de medida Litros.
2. ****Acesse "**Cadastros/Faturamento/Condições Contratuais com****** **Convênios**"  
   Na aba "Gerais", verifique a tabela de preços configuradas.  
     
   Na aba "Parâmetros 3", marque "Utiliza Faturamento de Gases em Litros".
3. Acesse"******Cadastros/Faturamento/Tabela de Procedimentos e Serviços******"****.****  
   Acesse o item e configure o fator para a unidade de medida litros parametrizada.

## Procedimento para Utilização

Acesse Lançamentos na Conta do Paciente.

Lançar o item parametrizado, será necessário informar o inicio e fim do uso e a vazão que estava configurada no período.

O sistema ira calcular a quantidade a ser faturada.

Acesse Prontuário.

Na  aba "Enfermagem", selecione a aba "Equipamentos/Insumos".

Selecione um item da lista de itens que tenha item de débito vinculado para lançamento que esteja parametrizado.

Ao finalizar o lançamento, o sistema irá calcular a quantidade a ser faturada.

divs
