---
article_id: 25911586708375
category: Gestão de Frotas
content_hash: 44383f262761fe405692fa80d7dd0dfa23b9ea59abaa1435c5fa20280dae269f
fetched_at: '2026-06-28T22:42:39.440786+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Inconsistência na numeração dos abastecimentos
type: support-article
updated_at: '2024-08-27T12:19:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25911586708375-Manufatura-Linha-Protheus-MNT-Inconsist%C3%AAncia-na-numera%C3%A7%C3%A3o-dos-abastecimentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25911633330071) Tempo aproximado para leitura: **00:01:40 min****Ocorrência**Número do abastecimento em duplicidade.   
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Todas as versões  
  
**Causa**Ao utilizar as rotinas que realizam a inclusão de **Abastecimentos**, acontecia duplicidade na numeração do campo **Número de Abastecimento - TQN\_NABAST**, impossibilitando o cadastro de novos abastecimentos.   
  
**Solução**Para correção dos registros que estão com a numeração duplicada, é necessário seguir os passos conforme abaixo:  
  
1. Acessar o **Configurador - SIGACFG / Ambientes / Cadastros / Menus**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25915685351063)

2. Selecionar o menu do módulo **Gestão de Frotas** e clicar no botão **Ok**.  
  
3. Selecionar o caminho e clicar no botão **Novo Item**para adicionar a nova função, e preencher conforme sugestão:  
  
**Desc. Português: Ajusta base TQN/TTV**  
**Programa: MNTFIX001**  
**Status: Habilitado**  
**Módulo: Gestão de Frotas**  
**Tipo: Função de Usuário**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25916210834071)**

4. Clicar no botão **OK** para confirmar as alterações realizadas.  
  
5. Para salvar as alterações no menu, é necessário clicar no botão **Gerar** e informar o nome do menu selecionado ou novo menu para que as alterações sejam confirmadas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25916210837911)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25916182904471)

6. Acessar a **filial** onde existem os abastecimento duplicados, acessar o **Módulo/Menu** criados no passo anterior, navegar até o caminho especificado e executar a rotina:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25916182908055)

7. Aguardar a execução da rotina e validar que os registros duplicados foram corrigidos.  
  
**Importante**  
O tempo de execução da rotina vai depender da quantidade de registros nas tabelas **Entrada Manual Abastecimento - TQN / Contador da Bomba - TTV.**
