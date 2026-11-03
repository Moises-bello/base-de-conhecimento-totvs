---
content_hash: a8ff5b9eed952682b7bb26dbe7d1dcf44aae81ad1fbf100dbc4dcc25c4f955f1
fetched_at: '2026-06-29T00:10:21.299030+00:00'
page_id: '490981253'
product: rm
source: tdn-rm
title: Utilizando os Manipuladores do Fluxo de Trabalho Sequencial
type: documentation
url: https://tdn.totvs.com/display/LRM/Utilizando+os+Manipuladores+do+Fluxo+de+Trabalho+Sequencial
version: 2
---

# Índice:

---

* Objetivo:
* Especificação:

# Objetivo:

---

     Este documento tem por objetivo especificar como utilizar os Manipuladores "Completed e Initialized" nas propriedades do Fluxo de Trabalho Sequencial.

# Especificação:

---

   As propriedades Completed e Initialized possibilitam que seja associado à um evento de outra atividade, para que a mesma execute no momento em que a execução da Fórmula Visual inicia e no momento em que a execução é Finalizada.

| N° | Nome do Parâmetro | Descrição do Parâmetro | Obrigatoriedade | Tipo de Entrada |
| --- | --- | --- | --- | --- |
| 1 | Completed | Código à ser executado no momento em que a execução do WorkFlow termina. | YellowOpcional | System.EventHandler |
| 2 | Initialized | Código à ser executado no momento em que a execução do WorkFlow se inicia. | YellowOpcional | System.EventHandler |

Para utilizar as propriedades, podemos adicionar uma atividade de "[Executar Código](http://tdn.totvs.com/pages/releaseview.action?pageId=286522533)" onde a mesma disponibiliza um System.EventHandler para associar a propriedade.

Arraste uma Atividade Executar Código para o Fluxo de Trabalho.

Após a mesma ser exibida no Fluxo de Trabalho, Clicando duas vezes em cima da Propriedade **ExecuteCode,**um console de programação .Net irá aparecer abaixo do diagrama do**Workflow.**

Dentro do console de programação .Net escreve o código que desejar executar. No Exemplo estou exibindo uma mensagem para mostrar que a atividade foi executada.

Agora é necessário vincular a propriedade na atividade de Executar Código. Clicando no Ícone Amarelo ao lado das Propriedades ****Initialized / Completed**,**ou no ****botão [...]****que aparece ao lado das mesmas propriedades, a tela abaixo irá aparecer. Selecione o Raio na atividade codeActivity.

Agora quando a Fórmula Visual for executada, antes da mesma executar a atividade codeActivity será executada.

A Fórmula Visual foi adicionada no gatilho do DataServer de coligada, Após a Leitura da Visão.

Ao Abrir a visão a mensagem é exibida.

Atenção

Como a atividade de Executar Código está no Fluxo de Trabalho a mesma irá executar quando a Fórmula Iniciar e Durante a execução onde recomendamos inseria a atividade Executar Código dentro de uma atividade Se/Senão passando uma condição **inválida**.

O Exemplo acima fazendo um "MessageBox.Show" não é recomendado, pois a mensagem será exibida na tela onde em um ambientes 3 camadas a mensagem ficará no servidor, até que alguém finalize o form da mensagem, e a fórmula visual ficará em execução até ser cancelada ou clicar no form.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.17 ou Superior

false

**Processo:** Utilizando os Manipuladores do Fluxo de Trabalho Sequencial

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false
