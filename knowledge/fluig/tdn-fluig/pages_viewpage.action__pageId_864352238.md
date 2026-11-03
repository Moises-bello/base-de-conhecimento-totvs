---
content_hash: da542d7fc4ade767f9e9adc3ff6dc964fdbe823bcc47f9dabc432855f9dc5cb6
fetched_at: '2026-06-28T21:35:30.961375+00:00'
page_id: '864352238'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Join
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864352238
version: 24
---

Consulte a documentação correta:

Esta documentação refere-se ao Editor de processo atual da plataforma. Caso esteja utilizando o Editor de processo clássico, acesse .

75%

5.\*ndice

25%

trueIdioma

# Falando de componente *Join*...

---

O componente ***Join*** indica o fim do paralelismo no fluxo do processo, ou seja, o fim de etapas paralelas (atividades ou fluxos), retornando para o fluxo principal e único.

Esse componente, obrigatoriamente, deve ser utilizado no final de atividades e fluxos paralelos iniciados por um componente **Paralelo**.

Quando ainda existem etapas paralelas pendentes, a solicitação permanece posicionada no componente ***Join*** do processo até que todas elas sejam concluídas. Quando todas as etapas paralelas (atividades ou fluxos) são concluídas, a solicitação é enviada automaticamente para a próxima etapa.

Se o componente ***Join*** for relacionado a uma etapa que não possui mecanismo de atribuição definido, a solicitação é enviada para a primeira pessoa encontrada na lista de pessoas com  ativo na plataforma em ordem alfabética, mesmo que essa pessoa não tenha nenhuma participação ou envolvimento no processo em questão.

#ebecf0

trueExemplo  
Na plataforma existem as seguintes pessoas cadastradas e ativas no recurso  do Painel de controle**1**:

* Angelina Reek
* Alonso Cunha
* Francisco Vieira
* Poliana Santana
* Adelina da Costa

Neste caso, a solicitação será enviada automaticamente para a Adelina da Costa, mesmo que ela tenha sido a última pessoa a ser cadastrada na plataforma, visto que se a lista de pessoas for colocada em ordem alfabética, o seu nome será o primeiro da lista.

**1** → Os nomes listados nesse exemplo são fictícios e meramente ilustrativos.

#ebecf0

trueExemplo de uso  
Em um processo de **Organização de evento**como uma conferência, onde as etapas **Definir local**, **Definir palestrantes** e **Planejar logística** – como alimentação, equipamentos de áudio e vídeo e demais recursos necessários – foram executadas simultaneamente, é necessário utilizar o componente ***Join*** para indicar o fim das etapas **executadas em paralelo**, fazendo com que o processo retorne ao fluxo principal e siga para a próxima etapa.

## Configurar componente *Join*

---

**100%true5%**

**01.** No  do processo, clique no componente ***Join***  que deseja configurar.

**02.** Defina um título ou nome para o componente que representa o fim das etapas paralelas no fluxo do processo.

#f2f2f2#f2f2f2

O nome também pode ser alterado diretamente no componente, clicando sobre seu nome atual e depois em **Editar**– localizado no lado direito.

#ebecf0

trueExemplo de uso  
Em um processo de **Desenvolvimento de *software***, onde as etapas de ***Back-end*** e ***Front-end*** foram executadas simultaneamente, o componente poderia se chamar **Codificação concluída**, indicando o fim das etapas de desenvolvimento dos códigos que foram **executadas em paralelo**.

**03.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no componente ***Join***.

**04.** Na mensagem exibida, clique em **Ok, entendi**.

Fique atento!

Esta documentação é válida a partir da atualização**Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.

]]>
