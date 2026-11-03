---
content_hash: 62d9bf7a79dc183ffcd3e45ed121900f17431810698651fd840aafdc5ecae5a2
fetched_at: '2026-06-29T00:08:12.253348+00:00'
page_id: '243641400'
product: rm
source: tdn-rm
title: DT_Melhorias_no_Mapa_de_Dispensação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243641400
version: 110
---

# Melhorias no Mapa de Dispensação

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Mapa de Dispensação |  |  | | --- | | **Rotina(s) envolvida(s)** | | Prontuário Eletrônico | |
| **Requisito (ISSUE):** | SAUHRM01-330 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL®, Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

   Esta implementação tem como objetivo atender as necessidades de usabilidade por parte da Farmácia, na utilização do Mapa de Dispensação.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.12 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.12.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.12

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu Opções / Parâmetros / Parâmetros Gerais – Aba Estoques II.
2. Marque as opções Utiliza Dispensação Horária por Requisição e Utiliza Modelo Otimizado de Separação Prévia.

## Procedimento para Utilização

1. Acesse o menu **Prontuário** e selecione um paciente internado.
2. Acesse a aba **Prescrição Médica** e prescreva um medicamento para o paciente.
3. Confirme a prescrição através do botão.
4. Conclua a prescrição, clicando no botão.
5. Repita a mesma operação para mais alguns pacientes (no mínimo três pacientes).
6. Acesse o menu **Estoques / Mapa de Dispensação**.
7. Selecione o Local de estoque para o qual as solicitações foram realizadas e inclua o filtro desejado na tela.
8. Selecione as prescrições para as quais deseja gerar mapa (segurando a tecla ctrl) e clique no botão **Gerar Mapa** no ícone localizado no canto superior esquerdo da tela.
9. Crie diversos Mapas.
10. Após gerados os mapas, o sistema permitirá a navegação entre eles. Para isso, dê um duplo clique sobre um mapa gerado.
11. Ao clicar nos botões o sistema deverá navegar entre os prontuários da tela anterior, agrupando os itens de um mesmo paciente, que estejam em um único mapa. Porém, caso algum mapa possua mais de um paciente, ele deverá dividi-los.
12. O campo texto entre os botões de navegação, deverá permitir buscar pelo prontuário. Portanto, ao digitar o prontuário e clicar na tecla **Enter**, o sistema buscará o próximo mapa disponível para o prontuário digitado. Caso não exista, o sistema permanece no registro atual.
13. Dentro do registro de um mapa qualquer, clique com o botão direito e em “**Confirma Item selecionado**”, ou “**Confirma Toldos os Itens**”, conforme desejado (A mesma ação pode ser executada pelos botões disponíveis no canto superior esquerdo da tela).
14. Após confirmados os Itens Desejados, clique em **Processar**, no canto inferior direito da tela.
15. Após o processamento, o sistema irá para o próximo registro disponível.
16. Voltando ao registro anterior, é possível visualizar que o processamento parcial dos itens do mapa, foi realizado com sucesso.
17. Confirme e processe os itens remanescentes. O processamento ocorrerá sem erros.

divs
