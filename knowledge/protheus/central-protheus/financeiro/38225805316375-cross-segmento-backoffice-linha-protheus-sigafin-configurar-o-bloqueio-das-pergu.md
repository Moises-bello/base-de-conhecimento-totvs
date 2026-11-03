---
article_id: 38225805316375
category: Financeiro
content_hash: 2ebf77dc9240c3b43065f5ef1e15a3322a5530811d1f3275f43627180c207cf6
fetched_at: '2026-06-28T22:38:00.832987+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Configurar o bloqueio
  das perguntas dos parâmetros acessados pela tecla F12
type: support-article
updated_at: '2026-02-06T19:54:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38225805316375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Configurar-o-bloqueio-das-perguntas-dos-par%C3%A2metros-acessados-pela-tecla-F12
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38225770949399) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
Configurar o bloqueio das perguntas dos parâmetros acessados pela tecla **F12**, de modo a impedir a edição por parte dos usuários.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
As perguntas (parâmetros) de rotinas no Protheus podem ser pré-configuradas e bloqueadas para edição através do módulo **Configurador**. Este recurso permite definir um conteúdo padrão e impedir que o usuário modifique a parametrização (ex: Contabilização Online, Aglutina Lançamentos, etc.) ao acessar a rotina ou pressionar a tecla **F12**.

Ao pressionar a tecla **F1** sobre o parâmetro, serão apresentados os detalhes do campo, contendo suas respectivas informações e orientações de uso, conforme demonstrado na imagem abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38225770950807)

Para efetuar o bloqueio de uma pergunta, siga o procedimento abaixo:

1. Acesse o módulo **Configurador (SIGACFG)**;
2. Vá em **Usuário > Senhas > Configuração de Perguntas**;
3. Clique em **Incluir**;
4. No campo **Grupo**, digite o código do Grupo de Perguntas desejado (Exemplo: **FIN050** conforme imagem anterior)

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38225770951447)
5. No campo **Usuário** ou **Grupo de Usuário**, selecione para quem esta regra será aplicada, ou seja, pode realizar o bloqueio por usuário ou grupos de usuário;

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38225770951959)
6. Na seção **Perguntas**, serão exibidas as perguntas referentes a este grupo. Note que, por padrão, elas estarão habilitadas;

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38225805287959)
7. Para **bloquear** uma pergunta:

   * Clique sobre a linha da pergunta desejada;
   * Pressione a tecla **DEL** no teclado. A linha ficará com uma sinalização visual, **geralmente cinza-claro,** indicando o bloqueio.
   * Se desejar fixar um valor padrão, digite o novo valor na coluna **Conteúdo**, neste cenário o conteúdo é 1 referente à contabilização online.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38225805289239)

1. Clique em **Confirmar** para salvar a configuração.

Após este processo, quando o usuário acessar a rotina ou pressionar **F12**, os campos configurados estarão **desabilitados (cinzas)** para alteração, respeitando o conteúdo definido no Configurador.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38225770956695)

**Saiba mais**

[Configuração de Perguntas - Bloquear Parâmetros](https://tdn.totvs.com/pages/releaseview.action?pageId=271390085)
