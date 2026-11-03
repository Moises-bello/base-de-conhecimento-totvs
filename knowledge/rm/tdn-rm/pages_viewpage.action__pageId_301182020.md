---
content_hash: 7b7b1b527211a8b93367c78804039fd65811e0e6eb827bea246b2e9568972ca8
fetched_at: '2026-06-29T00:08:43.009735+00:00'
page_id: '301182020'
product: rm
source: tdn-rm
title: 'DT Cópia de Itens de débito para: Processo e Exames, Divisão de honorários,
  Itens de enfermagem, Procedimento cirúrgico'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301182020
version: 99
---

# Cópia de Itens de débito para: Processo e Exames, Divisão de honorários, Itens de enfermagem, Procedimento cirúrgico

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Saúde* |
| **Módulo:** | *TOTVS Gestão Hospitalar* |
| **Rotina:** | |  | | --- | | **Rotina** | | *Faturamento / Condições contratuais com Convênios.* |  |  | | --- | | **Rotina(s) envolvida(s)** | | *Itens de lançamento (Cadastros / Cuidados com Paciente / Prescrição Médica / Itens de Enfermagem)* | | *Exames e serviços (Cadastros / Unidade Diagnóstico / Exames e Serviços, Item de Débito)* | | *Condições contratuais de convênio (Cadastros / Faturamento / Condições Contratuais / Divisão de Honorário)* | | *Procedimentos cirúrgicos (Cadastros / Cuidados com Paciente / Cirurgias)* | |
| **Tickets relacionados:** | [Ticket #775050](https://totvssuporte.zendesk.com/agent/tickets/775050 "Open ticket in Zendesk Support") |
| **Requisito:** | [RMSAU-168](http://jiraproducao.totvs.com.br/browse/RMSAU-168) |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server® e Oracle®* |
| **Tabelas Utilizadas:** | SZLABITEMDEB, SZITMDEBCIRURGIA, SZPROCSERVPEPENF, SZDIVISAOCOBRANCA |
| **Sistema(s) Operacional(is):** | *Windows®* |

## Descrição

Permitir  a cópia da relação entre itens de débito e tabela de preço, quando houver atualização na tabela de preço indicada nas condições contratuais com convênio.

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

Para exemplo: Acesse **Cuidados com o Paciente / Cirurgias / Procedimentos para Agenda de Cirurgias**

Selecione um procedimento e clique em editar.

Na aba itens de débito o da tela de Procedimentos Cirúrgicos

Note que o item de débito com convênio 63 e tabela 21 será posteriormente atualizado.

Acesse **Faturamento / Condições contratuais com Convênios**

Selecione um convênio com mais de uma vigência e acesse **Processos / Cópia Itens de Débito**

A tela de Processo de cópia será apresentada, Selecione a vigência que deseja atribuir. Na tela será possível visualizar os itens de débito que serão copiados baseado na origem para o destino, em Efetuar cópia dos itens em: é possível selecionar até quatro opções, Processos e Exames, Itens de Enfermagem, Procedimentos Cirúrgicos e Divisão de cobrança. Após configurar a cópia de itens de débito clique em Executar. Para este exemplo será utilizado o Itens de Enfermagem.

Após a conclusão do processo de cópia de itens de débito a tela apresentará o log dos itens de débitos que foram inseridos.

Acesse novamente **Procedimentos para Agenda de Cirurgias**e note que o novo item de débito para o procedimento cirúrgico foi copiado.

divs
