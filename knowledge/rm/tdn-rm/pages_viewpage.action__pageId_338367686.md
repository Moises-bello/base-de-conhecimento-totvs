---
content_hash: 282ee9c37e34cc8c849b349c4530d62d4515e4f7849c0990ab0fb2fa4d31c82a
fetched_at: '2026-06-29T00:08:51.866953+00:00'
page_id: '338367686'
product: rm
source: tdn-rm
title: FOP_ROTINASFOP_0009_Seção Centralizadora da Coligada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338367686
version: 89
---

# Geração do Arquivo DIRF Sem Erros em Empresas Que Não Possuem Seção Centralizadora da Coligada

|  |  |
| --- | --- |
| **Produto:** | TOTVS Folha de Pagamento |
| **Versões:** | 12.1.17.222 ou Superiores  12.1.18.143 ou Superiores  12.1.19.101 ou Superiores |
| **Ocorrência:** | Erros durante a importação da DIRF devido o arquivo está sendo gerado com vários registros DIRF: "DIRF - Este registro deve ser único". O erro ocorre quando no cadastro de seções não é encontrado apenas uma seção centralizando todas as outras da coligada. |
| **Ambiente:** | Anuais | DIRF |
| **Observações:** | Nome do parâmetro "**Forçar seção centralizadora (apenas para empresas que não possuem uma seção centralizadora de toda a coligada)**" |
| **Passo a passo:** | **Seção Centralizadora da Coligada**    Este recurso atende aos clientes que não tem seção centralizadora (seção empresa) no cadastro de seção e então deverá escolher qual será a seção que o sistema utilizará na geração da DIRF e Informe de Rendimentos.  Lembrando que a DIRF deve ser sempre gerada com a quebra “?” (uma interrogação).     Exemplos onde no cadastro de seções não existem uma seção centralizadora que represente toda a coligada:  **Exemplo 1: Não há seção com apenas 1 digito cadastrada**     01           Matriz - CNPJ DA MATRIZ  01.01  01.02  02           Filial   - CNPJ DA FILIAL 02  02.01  02.02     Neste caso deverá ser marcado o parâmetro e informar a seção 01 no campo “Código da Seção Centralizadora”.     **Exemplo 2:****Mais de uma seção com 1 digito:**    1             Matriz - CNPJ da Matriz  1.01  1.02  2             Filial - CNPJ da Filial 02  2.01  2.02     Neste caso deverá ser marcado o parâmetro e informar a seção 1 no campo “Código da Seção Centralizadora”.     **Exemplo 3:** Possui seção com 1 digito (apenas uma), porém em algumas seções há mudança no primeiro digito:     **0**        Matriz - CNPJ DA MATRIZ - Centralizadora da coligada  01        Matriz - CNPJ DA MATRIZ  01.01  01.02  02        Filial 02 - CNPJ DA FILIAL 02  02.01  02.02  ...  09        Filial 09 – CNPJ DA FILIAL 09  09.01     **10**       Filial 10 – CNPJ DA FILIA 10  **10**.01  **10**.02     Repare que quando chega na seção da filial 10 o primeiro digito passa a ser “1” e as outras seções o primeiro digito é 0, então no momento de gerar a DIRF o sistema vai quebrar o arquivo, gerando outro registro DIRF para essas seções que iniciam com 1.  **Neste caso deverá ser marcado o parâmetro e informar a seção 0 no campo “Código da Seção Centralizadora”.**     Então para gerar o arquivo DIRF centralizando todos os funcionários em apenas uma seção (matriz, que represente a coligada) deverá marcar o parâmetro **“Forçar seção centralizadora (apenas para empresas que não possuem uma seção centralizadora de toda a coligada)”** e preencher o campo “**Código da Seção Centralizadora”.**     Com o parâmetro desmarcado, o sistema buscará os dados da primeira seção do cadastro de seção.    **Exemplo:**    Estrutura de seção sem quebra da empresa, somente com quebra de coligada:     01 - Centralizadora do CNPJ 1  02 - Centralizadora do CNPJ 2  03 - Centralizadora do CNPJ 3        Ao processar a DIRF ou Informe de Rendimentos com o parâmetro desmarcado, o sistema buscará os dados da seção 01.  Com o parâmetro marcado o cliente poderá determinar de qual seção o sistema buscará os dados.     **Observação:**  É possível optar em utilizar a descrição da seção selecionada ou da coligada, para isso utilize o parâmetro “Utilizar descrição da seção selecionada na DIRF em Arquivo”. |

divs
