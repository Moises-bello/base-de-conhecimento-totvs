---
content_hash: 0f6ea72dc2b47d5a5922c4fe5fda86e0e81d6151e6841a074e7557c6f1251b5e
fetched_at: '2026-06-29T00:06:27.353335+00:00'
page_id: '232820288'
product: rm
source: tdn-rm
title: DT_Exibir_Horário_de_Suspensão_nas_Prescrições_Concluídas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232820288
version: 5
---

# Exibição do Horário de Suspensão do Item nas Prescrições Concluídas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | Rotina | Nome Técnico | | Prontuário Eletrônico | Prescrições Concluídas, Check de Medicamentos | |
| **Requisito (ISSUE):** | PCREQ-9994 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZITEMPRESCRICAO, SZAPRAZAMENTO |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Exibir o horário de suspensão do medicamento na grid de Prescrições concluídas e na página de Enfermagem, sub-aba Check de Medicamentos.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.10 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.10.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.10

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu **Prontuário**.
2. Selecione um paciente de faça uma prescrição médica.
3. Pesquise a prescrição, selecione o item e realize a sua suspensão.
4. Acesse a aba de **Enfermagem**, sub-aba **Check de Medicamentos** e verifique que os itens pós hora de estorno estão em vermelho.
