---
content_hash: 0df70e65f312fc6eeedd6edcc5ce764f96a5b8f5364a09793d052bf4a10db271
fetched_at: '2026-06-29T00:08:49.428784+00:00'
page_id: '330829718'
product: rm
source: tdn-rm
title: ENVIAR O LOCAL DE USO MATMED NO TISS UTILIZANDO PADRÃO IMAS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=330829718
version: 2
---

# 1989928 - RMSAU-2163 - ALTERAÇÃO DO CAMPO HORAFINAL PARA ENVIAR O LOCAL DE USO MATMED NO TISS UTILIZANDO PADRÃO IMAS

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Saúde* |
| **Módulo:** | *Gestão Hospitalar* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Faturamento para Convênios | SauAnsXmlGuiasMod30000.cs | | Condições Contratuais com Convênios | SauCondContratForm | |
| **Cadastros Iniciais:** | *Condições contratuais com convênios (utilizar informação específicas = IMAS)* |
| **Tickets relacionados** | *1989928* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | RMSAU-2163 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL SERVER® e ORACLE®* |
| **Sistema(s) Operacional(is):** | *Windows®* |

## Descrição

O objetivo desta implementação é informar no campo horafinal do xml tiss o local de uso do material/medicamento listado.

Seguinto a seguinte tabela:

| LOCAL DE USO | HORA FINAL |
| --- | --- |
| Leito | 01:00:00 |
| Sala Cirúrgica | 02:00:00 |
| Ambulatório | 03:00:00 |
| Berçário | 04:00:00 |
| UTI | 05:00:00 |
| Outros | Hora Inicial |

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

  **NO SISTEMA: RMSaude**

* Acesse **Cadastros/Faturamento/Condições Contratuais com Convênios**
* *Duplo clique no Convênio que deseja alterar*
* Aba Eletrônico ||| - TISS
* No combo Informações Especificas selecione o tipo **IMAS**e clique em OK.
* Ao utilizar este convênio em uma conta considere os **locais de uso** dos itens na aba **matmed**
* Encerrar a conta que deseja gerar remessa.  
    
    
   **NO SISTEMA : RM.exe**
* Acesse **Faturamento/Faturamento para Convênios .**
* Clique duas vezes na remessa que deseja enviar
* Acesse **Processos/Faturamento de Convênio.**
* Avance a pagina até o processamento de Fatura/Remessa
* selecione a conta que deseja gerar e clique em avançar até que o XML seja gerado

* Abra o XML gerado da Remessa  TISS
* As horas de cada MATMED estarão compatíveis com seu local de uso segundo a tabela apresentada anteriormente

,
