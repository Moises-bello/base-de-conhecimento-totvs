---
article_id: 18180123254295
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: e4998fb364625eb24b38a1b726eefdac3896946452f802f8852ff74e10920fda
fetched_at: '2026-06-28T22:39:08.103711+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como bloquear alterações
  nos Grupos de Perguntas (SX1)?
type: support-article
updated_at: '2023-10-11T11:33:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18180123254295-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-bloquear-altera%C3%A7%C3%B5es-nos-Grupos-de-Perguntas-SX1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18180144463767) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Como bloquear a resposta das perguntas nas rotinas, permitindo que o usuário apenas visualize? 

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque/Custos - Todas as versões  
  
**Solução**

Nas rotinas os parâmetros (Perguntas (SX1)) podem ser visualizados pressionando a **tecla** **F12** no Browse da rotina. Algumas rotinas podem chamar automaticamente a tela de perguntas ao iniciar a rotina, afim de parametrizar a inicialização dessa rotina. Abaixo uma tela de exemplo de pergunta, na rotina Transferências Múltiplas Modelo II (MATA261).

Note que a rotina já possui algumas respostas nos parâmetros, mas os campos estão livres para edição. A rotina de **Configuração de Perguntas** do Configurador serve para definir uma resposta padrão a estes parâmetros e deixá-los bloqueados para que o usuário não possa alterar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180273426967)

**Passo a passo para efetuar este bloqueio.**

**1. Acesse Configurador > Usuário > Senhas > Configuração de Perguntas**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180499601815)

**2. Clique em Incluir**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180494893975)

**3. Em Grupo, digite o código do Grupo de Perguntas em nosso exemplo MTA260**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180605318167)

**4. Em Usuário ou Grupo de Usuário, selecione um usuário ou grupo para associar essa regra de configuração de perguntas**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180798869399)

**5. Seção Perguntas serão exibidas as perguntas referentes a este grupo. Elas estão todas marcadas em cinza, conforme exemplo da tela abaixo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180815612951)

**6. Para bloquear uma pergunta, clique sobre ela, e pressione a tecla** **DELETE. Neste momento ela já estará bloqueada na rotina. Se quiser inserir um novo valor padrão, digite-o abaixo da coluna Conteúdo, ou em casos de campos do tipo combo, selecione o valor padrão. No print abaixo, foram bloqueadas as 2 últimas perguntas.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18181149770775)

**8. Ao finalizar, clique em Confirmar. Na rotina, ao pressionar F12, a tela de parâmetros irá aparecer desta forma. Note que as 2 perguntas estão cinzas, ou seja, bloqueadas.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18181277138583)

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CADASTROS E CONFIGURAÇÕES GERAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
