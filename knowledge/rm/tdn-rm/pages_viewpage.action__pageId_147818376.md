---
content_hash: 80fb1ef4d4af44f001a0c630e270f46fe3257c2f5cd6c4e360deec7ddfcd9fa8
fetched_at: '2026-06-29T00:05:55.982643+00:00'
page_id: '147818376'
product: rm
source: tdn-rm
title: Utilizando a atividade "Tratar Exceção"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=147818376
version: 12
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework |
| **Processo** | **:** | Fórmula Visual |
| **Subprocesso** | **:** | Utilizando a atividade "Tratar Exceção" |
| **Data da publicação** | **:** | 18/07/2014 |
| **Data da última Alteração** | : | 30/12/2022 |

## **INTRODUÇÃO**

---

**O que é Exceção:**

Exceção significa algo que não é comum, que não faz parte das regras. A exceção ocorre quando acontece algo fora da regra comum, um fato inédito, que não era feito ou conhecido antes. Uma maneira de tentar contornar esses imprevistos é realizar o tratamento dos locais no código que podem vir a lançar possíveis exceções.

**Para que server a atividade de Tratar Exceção na Fórmula Visual**

A finalidade da atividade "Tratar Exceção" é capturar e tratar as exceções que ocorrem quando se utiliza uma fórmula visual. Ela se difere da atividade [Gerar Exceção](http://tdn.totvs.com/x/MgHvC), uma vez que, esta tende somente a gerar uma nova exceção interrompendo o processo e exibindo uma mensagem.

**Quando a atividade pode ser utilizada**

Essa atividade pode ser utilizada nos casos em que a fórmula visual gerar erros não tratados, ou desconhecidos.

## **FUNCIONALIDADE**

---

Esta atividade depende da funcionalidade de tratamento de falhas. Podendo ser utilizada diretamente pelo **Fluxo de Trabalho Sequencial** ou através de atividades com essa funcionalidade como por exemplo as atividades "[Enquanto](http://tdn.totvs.com/x/hIvCC) , [Sequência](http://tdn.totvs.com/x/I4zCC) , [Se/SeNão](http://tdn.totvs.com/x/_YvCC) , [Grupo de Condições](http://tdn.totvs.com/x/vIvCC), Para Cada Iteração e entre outras atividades disponíveis.

As opções de Tratamento disponíveis são:

**Manipuladores de Fault**

Essa opção é usada para manipular falhas ocorrentes durante a atividade

## **EXEMPLOS**

---

Utilizando o Fluxo de Trabalho Sequencial

### Utilizando o Fluxo de Trabalho Sequencial

**Passo 1:** Neste Exemplo, foi utilizada uma Fórmula Visual para criar um novo usuário. Para selecionar a funcionalidade de tratamento de falhas basta clicar no ícone  e selecionar a opção "Exibir Manipuladores de Fault".

**Passo 2:** Após selecionar a opção, será exibida a funcionalidade de tratamento de falhas.

|  |
| --- |

**Passo 3:** Agora é  necessário associar a atividade "Tratar Exceção" ao "fluxo de trabalho" à atividade Sequência.

|  |
| --- |

**Passo 4:** Após atividade ter sido associada, é necessário configurar as propriedades da atividade.

|  |  |
| --- | --- |
| Selecione a atividade  e preencha a propriedade FaultType. | No exemplo vamos utilizar a exceção System.Exception que é uma exceção genérica. |

**Passo 5:** Após configurar a exceção é necessário associar a atividade "[Gerar Exceção](http://tdn.totvs.com/x/MgHvC)" ao "Fluxo de Trabalho Sequencial".

|  |
| --- |
|  |

**Passo 6:** Após configurar a atividade "[Gerar Exceção](http://tdn.totvs.com/x/MgHvC)" caso a fórmula visual apresente algum erro, será exibida a mensagem de erro configurada na atividade "[Gerar Exceção](http://tdn.totvs.com/x/MgHvC)".

Após selecionar a opção, será exibida a funcionalidade de tratamento de falhas. Agora é  necessário associar a atividade "Tratar Exceção" as Exceções de Fluxo de Trabalho.

**Passo 7:** A atividade "Tratar Exceção" contêm tipos diferentes de alternativas para tratamento da exceção.

Para escolher, basta selecionar a atividade  e preencher a propriedade FaultType. Neste caso será utilizada o tipo **Exception.**

**Passo 8:** Após configurar a exceção é necessário associar a atividade "[Gerar Exceção](http://tdn.totvs.com/x/MgHvC)" à "Exceções de Fluxo de Trabalho".

**Passo 9:** Após configurar a atividade "[Gerar Exceção](http://tdn.totvs.com/x/MgHvC)" **caso a fórmula visual apresente algum erro**, será exibida a mensagem de erro configurada na atividade "[Gerar Exceção](http://tdn.totvs.com/x/MgHvC)".

Envio de e-mail da exceção 

### Envio de e-mail da exceção

É possível utilizar a funcionalidade "Tratar Exceção" para enviar um email com a exceção para pessoa responsável.

Neste Exemplo, foi utilizada a mesma fórmula visual do exemplo anterior para criação de um usuário.

Para simular um erro, foi realizada a alteração da senha do usuário criado

Após seguir  os passos do exemplo anterior, podemos adicionar o envio de email **antes**da atividade "Gerar Exceção"

Em seguida, deve selecionar a atividade rmsSendEmailActivity1 e adicionar as propriedades. Adicione o Assunto, o destinatário e o remetente desejado.

No campo **Texto do E-mail**deve ser adicionada a mensagem da falha da Exception. Para isso, clique no ícone de inserção e selecione a atividade de "Tratar Exception". O caminho para adicionar a mensagem é *RMSWorkflow > faultHandlersActivity > faultHandlerActivity > Fault > Message*

     

Após a configuração, basta salvar e executar a Fórmula Visual e o email com a exceção capturada será enviado ao destinatário. Como foi utilizada a atividade "Gerar Exception" a mensagem exibida  após a execução será a mensagem tratada.

Mensagem enviada para o email:

Utilizando uma atividade padrão

### **Utilizando uma atividade padrão**

Neste Exemplo, foi utilizada a mesma fórmula visual do exemplo anterior, no entanto foi adicionada uma atividade para enviar email dentro da atividade "[Sequência](http://tdn.totvs.com/x/I4zCC)" onde será adicionado o tratamento da exceção.

Para selecionar a funcionalidade de tratamento de falhas basta clicar no ícone  e selecionar a opção "Exibir Manipuladores de Fault".

Após selecionar a opção, basta seguir os passos 2 ao 9 do exemplo anterior.

É importante frisar que neste caso, o tratamento da exceção será válida somente para as falhas presentes dentro do fluxo da sequência.Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
