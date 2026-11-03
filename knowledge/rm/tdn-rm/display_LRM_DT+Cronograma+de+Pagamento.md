---
content_hash: 1219466b0af6c062139748adbd2a3720c1da55ddb7ab3c382bc285bbb1d6ebb2
fetched_at: '2026-06-29T00:08:27.961241+00:00'
page_id: '271652376'
product: rm
source: tdn-rm
title: DT Cronograma de Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Cronograma+de+Pagamento
version: 111
---

# Cronograma de Pagamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento de Convênio | |
| **Parâmetro(s):** | CALCFATDATAENTREGA |
| **Requisito****:** | SAUHRM02-590 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Tabelas Utilizadas:** | SZCADGERALINFORFAT |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementadas novas opções de cálculo para pagamento de **Faturamento dos Convênios,** utilizando uma data específica ou calculando um determinado número de meses a frente da data de entrega da fatura.

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

1. Acesse **Opções/Parâmetros/Parâmetros Gerais, aba Faturamento II**.
2. Marque o parâmetro **Calcula data de vencimento da fatura à partir da data de entrega**.

## Procedimento para Utilização

**Exemplo:**

       1.  Acesse **Cadastros / Convênio / Dados de Faturamento** (Anexos).

       2.  Selecione as regras para o tipo de entrega e para a data de cálculo do recebimento.

       3.  No exemplo da imagem abaixo, para as faturas recebidas entre os dias 01/02/2017 e 28/02/2017, será apresentada como data para pagamento o dia 01/05/2017 (data específica).

       4.  No exemplo da imagem abaixo, para os recebimentos realizados entre os dias 1 e 28 (de qualquer mês), a data de pagamento será no dia 7, 4 meses a frente do mês em que foi entregue a fatura.

       5.  Acesse**Faturamento / Faturamento para convênios / Faturamento de Convênio** (Processos).

Importante

O acesso a essa rotina ocorre no módulo RM.exe.

        6.  Ao processar o faturamento do convênio, caso a data de entrega não tenha sido informada, sistema apresentará a mensagem de erro conforme a imagem de exemplo abaixo.

       7.  Após selecionar os registros e avançar, o sistema apresentará a data de vencimento conforme a regra de cálculo selecionada para aquele convênio e que se encaixa nos critérios de entrega. Na imagem abaixo, o resultado é o cálculo da mesma regra selecionada anteriormente, ou seja, no dia 7 do mês, 4 meses à frente do dia em que foi efetuado o processamento (09/02).

       8. Acesse **Faturamento / Particular e Convênios / Faturamento para Convênios**.

Importante

Tela acessada através do módulo RMSaude.exe.

       9. Selecione a unidade de faturamento e o convênio, e clique no botão **Iniciar**. Será exibida tela solicitando informar a data de entrega da fatura do convênio.

       10. Conforme a regra configurada para calcular através do número de meses à frente, a data de recebimento será como a do exemplo da imagem abaixo.

divs
