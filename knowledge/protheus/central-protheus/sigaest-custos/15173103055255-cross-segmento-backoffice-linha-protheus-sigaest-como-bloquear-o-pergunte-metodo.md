---
article_id: 15173103055255
category: SIGAEST - CUSTOS
content_hash: 8da85992e93c8667cd6562d400db427fc2746f942af55339bb97e998f94ed386
fetched_at: '2026-06-28T22:39:00.648654+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como bloquear o pergunte
  - metodo de apropriação no custo médio?
type: support-article
updated_at: '2026-03-02T16:51:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15173103055255-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-bloquear-o-pergunte-metodo-de-apropria%C3%A7%C3%A3o-no-custo-m%C3%A9dio
---

O artigo explica como bloquear a alteração do "pergunte" de método de apropriação na rotina de custo médio do TOTVS Protheus, detalhando o passo a passo no Configurador para restringir o campo, garantindo maior controle e segurança no cálculo e análise dos custos.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15186875482903) Tempo aproximado para leitura: **00:03:20 min**  
  
**Dúvida**

Como posso bloquear o pergunte de método de apropriação, na rotina de custo médio?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
A execução de custo médio é delicada, e um dos principais perguntes é o tipo de apropriação de calculo, pois é ele que definira a ordenação das movimentações como um todo no seu ambiente.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Quais são os Métodos de Apropriação para execução do Recálculo do Custo Médio?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033673914-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Quais-s%C3%A3o-os-M%C3%A9todos-de-Apropria%C3%A7%C3%A3o-para-execu%C3%A7%C3%A3o-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-)

**Como eu posso bloquear esse pergunte, para que o usuario não possa altera-lo durante a execução?**

**Antes do bloqueio:**

**MATA330 - Recalculo do custo médio - Pergunte selecionavel.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15172995393815)

**MATA038 - Acompanha Custos - Pergunte selecionavel.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15173014516887)

**Segue abaixo procedimento de como efetuar este bloqueio.**  
1. Acesse Configurador > Usuário > Senhas > Configuração de Perguntas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15172885158935)

2. Clique em **Incluir**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15172925625111)

3. Em **Grupo**, digite o código do Grupo de Perguntas > MTA330

4. Em **Usuário** ou **Grupo de Usuário**, selecione um usuário ou grupo para associar essa regra de configuração de perguntas  
5. Seção **Perguntas** serão exibidas as perguntas referentes a este grupo. Elas estão todas marcadas em cinza, conforme exemplo da tela abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15172945878679)

6. Para bloquear uma pergunta, clique sobre ela, e pressione a tecle **DEL** do teclado. Neste momento ela já estará bloqueada na rotina. Se quiser inserir um novo valor padrão, digite-o abaixo da coluna **Conteúdo**, ou em casos de campos do tipo combo, selecione o valor padrão  
7. Na imagem de exemplo abaixo, efetuamo o bloqueio do pergunte desejado "metodo de apropriação", após toda a ação clique em confirmar depois fechar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15172952133015)

8. Ao finalizar, acesse a rotina desejada, e veja que os perguntes se encontram restritos.

**MATA330 - Recalculo do custo médio - Pergunte bloqueado.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15173097688727)**

**MATA038 - Acompanha Custos - Pergunte bloqueado.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15173109093911)

Esse mesmo conceito pode ser utilizado para bloqueio de outros perguntes também, esse foi um especifico para o pergunte "metodo de apropriação", que tem uma ação muito importante para o correto funcionamento e analise dos custos de sua empresa.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
