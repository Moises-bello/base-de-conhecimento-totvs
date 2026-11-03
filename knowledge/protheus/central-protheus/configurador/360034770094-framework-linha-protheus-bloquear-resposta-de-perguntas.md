---
article_id: 360034770094
category: Configurador
content_hash: 98a58802cc181a6c403302b9f5f925a232945579a5092b6d170581323f56a41a
fetched_at: '2026-06-28T22:42:18.927176+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Bloquear resposta de Perguntas
type: support-article
updated_at: '2025-10-11T16:39:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034770094-Framework-Linha-Protheus-Bloquear-resposta-de-Perguntas
---

**Dúvida**Como bloquear a resposta de uma pergunta na rotina, deixando o usuário apenas visualizar?  
   
 **Ambiente**Protheus - Configurador - A partir da versão 11  
   
**Solução**Perguntas são parâmetros de rotinas que podem ser configurados no Protheus. Na rotina, esses parâmetros podem ser visualizados pressionando a tecla **F12** no browse da rotina. Algumas rotinas podem chamar automaticamente a tela de perguntas ao iniciar a rotina, afim de parametrizar a inicialização dessa rotina. Abaixo uma tela de exemplo de pergunta, na rotina Solicitação de Compras (MATA110).  
  
![PE_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045204554)  
  
Note que a rotina já possui algumas respostas nos parâmetros, mas os campos estão livres para edição. A rotina de **Configuração de Perguntas** do Configurador serve para definir uma resposta padrão a estes parâmetros e deixá-los bloqueados para que o usuário não possa alterar.  
  
![PE_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045211894)  
  
Segue abaixo procedimento de como efetuar este bloqueio.  
1. Acesse Configurador > Usuário > Senhas > Configuração de Perguntas  
2. Clique em **Incluir**  
3. Em **Grupo**, digite o código do Grupo de Perguntas (Ex.: MTA110)  
4. Em **Usuário** ou **Grupo de Usuário**, selecione um usuário ou grupo para associar essa regra de configuração de perguntas  
5. Seção **Perguntas** serão exibidas as perguntas referentes a este grupo. Elas estão todas marcadas em cinza, conforme exemplo da tela abaixo:  
  
![PE_03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046068993)  
  
6. Para bloquear uma pergunta, clique sobre ela, e pressione a tecle **DEL** do teclado. Neste momento ela já estará bloqueada na rotina. Se quiser inserir um novo valor padrão, digite-o abaixo da coluna **Conteúdo**, ou em casos de campos do tipo combo, selecione o valor padrão  
7. Na imagem de exemplo abaixo, foram bloqueados os 2 primeiros campos do grupo de perguntas  
  
![PE_04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046069313)  
  
8. Ao finalizar, clique em **Confirmar**. Na rotina, ao pressionar **F12**, a tela de parâmetros irá aparecer desta forma:  
  
![PE_05.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045213154)  
  
Note que os 2 primeiros campos estão cinzas, ou seja, bloqueados.
