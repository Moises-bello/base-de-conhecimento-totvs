---
content_hash: 22c2a3d4bdcd9936b74f20a589315a22aa9b38d2a5e85b92cc66c9a7af23a8cf
fetched_at: '2026-06-28T21:35:30.911995+00:00'
page_id: '862123648'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Paralelo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862123648
version: 24
---

Consulte a documentação correta:

Esta documentação refere-se ao Editor de processo atual da plataforma. Caso esteja utilizando o Editor de processo clássico, acesse .

75%

5.\*ndice

25%

trueIdioma

# Falando de componente Paralelo...

---

O componente **Paralelo** representa o início de etapas paralelas no fluxo do processo.

Ao chegar nesse componente, a solicitação é bifurcada em várias saídas, permitindo a execução de atividades ou fluxos paralelos entre si. Nesse momento, são criadas duas ou mais atividades sem exibir a seleção de responsável. Sendo assim, se o mecanismo de atribuição de uma dessas atividades estiver definido para mais de um responsável – um grupo, por exemplo – ela é atribuída à primeira pessoa da lista de possíveis responsáveis.

No fim das etapas paralelas (atividades ou fluxos), é necessário adicionar um componente ***Join***, que indica o fim da execução paralela, voltando ao fluxo principal e único do processo. Todas as atividades e fluxos que estão depois do componente **Paralelo** e antes do componente ***Join*** são executados paralelamente.

#ebecf0

trueExemplo de uso  
Em um processo de **Organização de evento** como uma conferência, as etapas **Definir local**, **Definir palestrantes** e **Planejar logística** – como alimentação, equipamentos de áudio e vídeo e demais recursos necessários – podem ser feitas simultaneamente. Dessa forma, é necessário utilizar o componente **Paralelo** para indicar o início das etapas que serão **executadas em paralelo**.

## Configurar componente Paralelo

---

**100%true5%**

**01.** No  do processo, clique no componente **Paralelo**  que deseja configurar.

**02.** Defina um título ou nome para o componente que representa o início de etapas paralelas no fluxo do processo.

#f2f2f2#f2f2f2

O nome também pode ser alterado diretamente no componente, clicando sobre seu nome atual e depois em **Editar**– localizado no lado direito.

#ebecf0

trueExemplo de uso  
Em um processo de **Desenvolvimento de *software***, onde as etapas de ***Back-end*** e ***Front-end*** podem ser executadas simultaneamente, o componente poderia se chamar **Codificação**, indicando onde iniciam as etapas de desenvolvimento dos códigos que serão **executadas em paralelo**.

**03.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no componente **Paralelo**.

**04.** Na mensagem exibida, clique em **Ok, entendi**.

Fique atento!

Esta documentação é válida a partir da atualização**Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.

]]>
