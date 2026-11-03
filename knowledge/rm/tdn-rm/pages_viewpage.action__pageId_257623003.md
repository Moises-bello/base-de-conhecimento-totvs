---
content_hash: d7478872ac10ff2ce29ca70cd1015f60c3b68651f8a7fc4202e1208db4168327
fetched_at: '2026-06-29T00:08:17.698388+00:00'
page_id: '257623003'
product: rm
source: tdn-rm
title: DT_Item_para_Registro_de_Informações_Cirúrgicas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=257623003
version: 113
---

# Item para registro de informações cirúrgicas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Itens da Enfermagem |  |  | | --- | | **Rotina(s) envolvida(s)** | | Registro de Informações Cirúrgicas  Elaboração de Contas | |
| **Requisito (ISSUE):** | SAUHRM01-714 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL®, Oracle® |
| **Tabelas Utilizadas:** | SZPEPENFERMAGEM |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

* Implementada opção "**Itens p/ registro de inf. cirúrgica**" na tela de **Itens de Lançamento**.
* Implementada rotina que faz o lançamentos dos itens de débito na conta do paciente ao inserir um item no **Registro de Informações de Cirurgias**.

## Importante

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração): 

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção. 

   O Patch 12.1.13 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.13.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente. 

   Para acesso siga as instruções abaixo: 

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).  

   2. Faça o login, com seu E-mail e Senha. 

   3. Na barra de menu superior, clique em DOWNLOAD. 

   4. No boxe Central de Downloads aplique os filtros: 

   a. Linha: RM 

   b. Versão: RM 12.1.13 

   c. Tipo: Patch 

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download. 

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada. 

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão. 

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu **Cuidados com o Paciente / Prescrição Médica / Itens da Enfermagem**.
2. Na tela de **Itens de Enfermagem**, selecione um registro e na tela de Itens de Lançamento, a opção de “**Itens p/ Registro de Inf. Cirúrgica**” estará disponível. Na aba de “**Itens de Débito**”, os itens associados são exibidos listados.
3. Acesse o menu **Cuidados com o Paciente / Centro Cirúrgico / Registro de Informações Cirúrgicas**.
4. Ao acessar os detalhes de um registro, a opção para verificar os **Itens para Registro de Informação Cirúrgica** está disponível nos anexos.
5. Ao adicionar um novo **Item de Enfermagem**, os itens de débito associados serão lançados na conta do paciente.

divs
