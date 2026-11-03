---
content_hash: e04c0a8852fd461e7c487781c11993c0b1e959273162a762aac0c82081e1d835
fetched_at: '2026-06-29T00:08:11.352778+00:00'
page_id: '242389743'
product: rm
source: tdn-rm
title: DT_Integração_ACH
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=242389743
version: 108
---

# Integração ACH - SMS POA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Integração ACH |  |  | | --- | | **Rotina(s) envolvida(s)** | | Elaboração de AIH | |
| **Requisito (ISSUE):** | [SAUHRM01-165](http://jiraproducao.totvs.com.br/browse/SAUHRM01-165) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL®, Oracle® |
| **Tabelas Utilizadas:** | SZSUSACHCAB, SZSUSACH |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

   Esta implementação tem como objetivo permitir a geração e importação dos arquivos ACH, seguindo o padrão imposto pela SMS de Porto Alegre.

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

1. Acesse o menu **Opções / Parâmetros / Faturamento SUS**.
2. Acesse o registro referente a unidade de faturamento utilizada.
3. Acesse a aba **ACH** e preencha os parâmetros "**Id do Hospital na SMS POA**", "**Caminho do diretório de exportação da ACH**" e "**ID do relatório de etiqueta**".

## Procedimento para Utilização

**PROCESSO DE EXPORTAÇÃO (ARQUIVO DE ENVIO)**

1. Acesse o menu **Faturamento / Faturamento SUS / Elaboração de AIH**.
2. Selecione a AIH desejada (ou mais de uma, se for o caso).
3. Clique em **Processos / Processamento de Arquivos ACH**.
4. Clique em **Avançar** e selecione o diretório onde será salvo o arquivo.
5. Clique em **Avançar / Executar**. Neste momento, caso não ocorra nenhum erro, será gravado no diretório configurado o arquivo correspondente a AIH selecionada.
6. Ao término do processo de exportação, será exibido o botão **Imprimir Etiquetas**. Ao clicar nesse botão, serão impressas as etiquetas referentes aos laudos que foram gerados, sendo uma etiqueta para cada procedimento, seja ele principal ou suplementar.

**PROCESSO DE IMPORTAÇÃO (ARQUIVO DE RETORNO)**

1. Acesse o menu **Faturamento / Faturamento SUS / Elaboração de AIH**.
2. Clique em **Processos / Processamento de Arquivos ACH**.
3. Clique em **Avançar**, selecione a opção de importação e clique em **Avançar**. Neste momento será exibida a tela de seleção do arquivo de importação. Selecione o arquivo e clique em **Open**.
4. Clique em **Executar**.
5. Após a execução, os laudos correspondentes estarão atualizados. Caso algum laudo que tenha sido enviado não tenha retornado, este será entendido como negado.

**VERIFICAÇÃO DOS STATUS DE LAUDOS**

1. Após a exportação do arquivo, cada laudo terá seu registro ACH. Para visualizá-lo, acesse o menu **Faturamento / Faturamento SUS / Elaboração de AIH** e acessar a aba **Procedimentos**.
2. Nesta aba, podem ser visualizado o status, através da aba **Status ACH** e o arquivo em que foi enviado o procedimento, na aba **Cod Arquivo**.
3. Ao dar um duplo clique sobre um registro, são exibidos o procedimento e a aba **ACH**, onde é possível visualizar maiores detalhes sobre a ACH.

**IMPRESSÃO DE ETIQUETAS**

1. Acesse o menu **Faturamento / Faturamento SUS / Elaboração de AIH**.
2. Selecione a AIH desejada e clique em **Processos / Imprimir Etiquetas ACH**. Serão impressas as etiquetas dos laudos correspondentes à AIH selecionada.
3. Caso a AIH em questão tenha laudos gerados em arquivos diferentes, será impresso um relatório para cada arquivo gerado.
4. Caso tenha sido gerada juntamente com outras AIH, será impresso o arquivo constando todos os laudos correspondentes.

divs
