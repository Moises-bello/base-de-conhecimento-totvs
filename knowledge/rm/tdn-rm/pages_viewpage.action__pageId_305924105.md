---
content_hash: 8ba09d20ffedd307201df41e5e5aeef2f03c4b41eb4a78b56e7ea10aeada0011
fetched_at: '2026-06-29T00:08:43.680065+00:00'
page_id: '305924105'
product: rm
source: tdn-rm
title: DT Valores Tabela MAT/MED - Fator de atualização de itens restritos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=305924105
version: 100
---

# Valores Tabela MAT/MED - Fator de atualização de itens restritos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | **RM** |
| **Segmento:** | **Saúde** |
| **Módulo:** | **TOTVS Gestão Hospitalar** |
| **Rotina:** | |  | | --- | | **Rotina** | | *Cadastros/Faturamento/Tabelas de MATMED Usadas* |  |  | | --- | | **Rotina(s) envolvida(s)** | | *Cadastros/Estoques/Produtos* | | Utilitários/Rotinas/Importação / Atualização SIMPRO | |
| **Ponto de Entrada:** | *[Ticket #910487](https://totvssuporte.zendesk.com/agent/tickets/910487 "Open ticket in Zendesk Support")* |
| **Tickets relacionados** | *[RMSAU-10](http://jiraproducao.totvs.com.br/browse/RMSAU-10)* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *Informe o requisito relacionado (Issue).* |
| **País(es):** | **Brasil** |
| **Banco(s) de Dados:** | **SQL Server® e Oracle®** |
| **Tabelas Utilizadas:** | *SZSIMPRO* |
| **Sistema(s) Operacional(is):** | **Windows®** |

## Descrição

Possibilitar a atualização de itens ***restritos*** vinculados ao Brasíndice ou Simpro com percentuais diferentes dos demais itens.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realize a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.18 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.18.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.18

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

Acessar o menu Cadastros/Faturamento/Tabelas de MATMED Usadas

Editar uma das tabelas

Foram adicionados os campos para informar os fatores para itens “Restritos”. Os campos identificados com um (R) na descrição. Para essa evidencia, está sendo abordado apenas o SIMPRO.

No caso acima, se o produto não for restrito, o sistema calcula o preço do produto com base no Fator PV MED.

Caso o produto seja restrito, o sistema calcula com base no Fator PV MED (R)

Este cadastro só é usado caso os fatores mostrados na imagem abaixo não estejam preenchidos.

Para chegar na tela da imagem acima, acesse o menu “Cadastros/Estoques/Produtos” em seguida, selecione o produto que deseja conferir, clique em “Anexos/Informações TOTVS Saúde”. Na tela de edição, clique em “Anexos/Tabela de preço”. Selecione a tabela de preço desejada e clique duas vezes para editar.

Neste caso estará informando uma condição de cálculo específica para este produto. Caso não sejam informados os fatores, o sistema levará em consideração os fatores do cadastro da tabela de preços (mostrado mais acima).

Para importar um arquivo SIMPRO, clique no menu “Utilitários/Rotinas/Importação / Atualização SIMPRO”

Será aberta a tela para escolha do arquivo SIMPRO a ser importado.

Preencha as informações e o local do arquivo SIMPRO e clique no botão “Atualizar produtos da tabela”

Ao finalizar, o sistema mostrará uma mensagem de sucesso.

Foram feitos dois testes para o mesmo produto. O primeiro com o checkbox “Restrito” marcado e o segundo desmarcado. O preço é calculado diferente para as duas condições.

Para alterar a propriedade “Restrito” acesse o menu “Cadastros/Estoques/Produtos” em seguida, selecione o produto que deseja conferir, clique em “Anexos/Informações TOTVS Saúde”.

**RESTRITO**

**NÃO RESTRITO**

**Atualização do Brasíndice**

1. Acessar o menu Utilitários / Rotinas / Importação – Atualização do Brasíndice
2. Informe o número do revista a ser importada e a data de início de vigência
3. Clique no botão “Importa dados”, selecione o arquivo do Brasíndice e aguarde finalizar a importação
4. Para visualizar os fatores de atualização da tabela selecionada para o Brasíndice, acesse o menu Cadastros / Faturamento / Tabela de MATMED usada.
5. Item configurado como Restrito para a realização do teste dos novos percentuais
6. Para atualizar os itens já vinculados com o Brasíndice, selecione uma tabela e clique no botão “Atualiza itens do estoque”
7. Após a atualização, verificar os valores atualizados  
     
       

   Preço = 1,46 \* 1,3% = **1,898**

   Preço = 15,19 \* 1,1 = **16,709**
8. Caso o usuário faça alguma alteração na configuração de preço, o sistema também refaz o cálculo de valor
9. Após a execução o resultado é o mesmo da rotina de Atualização pelo Brasíndice
10. O mesmo ocorre com o as configurações do Simpro. Caso o item esteja vinculado ao Simpro, o sistema também aplicará as mesmas regras parametrizadas.
11. Na funcionalidade de Tabelas de Preços (Anexo do Produto), o processo “Atualização de múltiplas informações” também consideram os novos campos de fator para o item restrito.
12. Após a execução do processo os registros devem ficar com as mesmas informações preenchidas no processo
13. Os novos campos relacionados ao fator para itens restritos também serão utilizados na exportação dos xmls de faturamento, especificamente na tag <reducaoAcrescimo>

divs
