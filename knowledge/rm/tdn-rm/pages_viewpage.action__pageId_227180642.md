---
content_hash: d4d0ba6af3812bcbcead6af2a7affc9143cf5865e13c9eecf60a636e36b98cfb
fetched_at: '2026-06-29T00:06:26.976317+00:00'
page_id: '227180642'
product: rm
source: tdn-rm
title: DT_Velocidade_de_Infusão_para_Enfermagem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=227180642
version: 121
---

# Velocidade de Infusão disponível para a Enfermagem

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Prontuário | Prontuário Eletrônico |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Prontuário | Prescrições Concluídas | | Prontuário | Check de Medicamentos | |
| **Requisito (ISSUE):** | PCREQ-9992 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Melhoria consiste em disponibilizar a informação da velocidade/tempo de infusão informada na Prescrição Médica para os locais em que o setor de Enfermagem tem acesso, ou seja, nas Prescrições Concluídas, na aba **Enfermagem/ Check de Medicamentos**.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.10 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.10.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).
2. Faça o login, com seu E-mail e Senha.
3. Na barra de menu superior, clique em DOWNLOAD.
4. No boxe Central de Downloads aplique os filtros conforme campos abaixo:  
   1. Linha: RM
   2. Versão: RM 12.1.10
   3. Tipo: Patch

Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.  
   Importante: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu **Prontuário** e selecione um atendimento.
2. Acesse a página **Prescrição Médica**, sub-aba **Prescrições Concluídas** e verifique a existência da coluna **Velocidade de Infusão**.
3. Acesse a aba **Enfermagem**, na sub-aba **Check de Medicamento**.

divs
