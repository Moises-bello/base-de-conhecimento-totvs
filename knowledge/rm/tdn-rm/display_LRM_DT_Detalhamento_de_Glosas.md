---
content_hash: aaeb01adec1a1a54254b49acdc6f48c83fedb8298e2b8b7f048baf9e1f6599c1
fetched_at: '2026-06-29T00:08:06.144056+00:00'
page_id: '236585121'
product: rm
source: tdn-rm
title: DT_Detalhamento_de_Glosas
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Detalhamento_de_Glosas
version: 115
---

# Detalhamento de Glosas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Controle de Glosas |  |  | | --- | | **Rotina(s) envolvida(s)** | | Recurso de glosas, Controle de Recebimento | |
| **Parâmetro(s):** | Permite informar o valor da glosa ou o pagamento a maior |
| **Requisito (ISSUE):** | PCREQ-10848 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZCONTROLEGLOSAITEM |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Implementação possibilita detalhar as informações do controle de glosa recebidas dos convênios. O sistema disponibiliza campos para se informar o valor da glosa, o valor do desconto, o pagamento a maior e o valor irrecuperável.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.11 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.11.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.11

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu O**pções/ Parâmetros/Parâmetros Gerais,** aba **Controle** **e Recurso de Glosas**. Marque o parâmetro “**Permite informar o valor da glosa ou o pagamento a maior**”.

## Procedimento para Utilização

1. Realize o controle de glosa de uma conta de uma remessa.
2. Selecione um item e realize a glosa.
3. No exemplo abaixo foi realizado uma glosa de 1,69 e um pagamento a maior de 60,00 e foi dado um desconto de 10,00.  
   101,69 – 1,69 + 60,00 – 10 = 150,00
4. Selecione alguns itens como Sem informação de pagamento.
5. Conclua o controle de glosa da conta.
6. Verifique que o controle de glosa é concluído com os valores calculados.
7. Acesse o **Recurso de Glosas**. Somente o valor da glosa é que poderá ser recursado. Caso exista valor irrecuperável, o sistema fará o cálculo e exibirá somente o valor "recursável".
8. Se existir valor recursado, o sistema gera uma conta com os itens recursado. Se existir itens sem informação de pagamento, será gerado uma conta com os itens correspondentes.
9. Conta com itens Sem informação de pagamento.
10. Conta com o itens com recurso.

divs
