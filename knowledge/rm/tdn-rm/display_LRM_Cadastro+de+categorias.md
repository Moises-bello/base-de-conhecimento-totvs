---
content_hash: 1aa70f1ce83b7999ac37736d2e15dc73dc9e44b575edcafe25088e51dd8f59d7
fetched_at: '2026-06-29T00:11:39.668060+00:00'
page_id: '789399074'
product: rm
source: tdn-rm
title: Cadastro de categorias
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+de+categorias
version: 10
---

Para que seja possível o envio de mensagens para o eduCONNECT, primeiramente, é preciso realizar o cadastro das categorias. Acessando o menu **'Sistema' Educacional | Acesso Menu|****Atividades acadêmicas | Central de Comunicações | eduCONNECT| Categoria do eduCONNECT.**

As categorias são agrupadores para as mensagens enviadas ao Meu eduCONNECT e seu principal objetivo é manter organizada a visão de mensagens dos usuários.

A seguir, temos a definição de cada um dos campos presentes na tela.

**Nome da Categoria:** informação de preenchimento obrigatório e que é apresentada como título da mensagem enviada.

Exemplos de categorias: "Enquete", "Aviso Importante", "Financeiro" e etc..

**Enviar notificação (Push):**indica se a mensagem enviada poderá chegar como uma notificação no dispositivo do usuário. Lembrando que, o usuário do Meu eduCONNECT poderá cancelar a exibição dessas notificações nas configurações do seu dispositivo.

**Cor da Categoria:**indica a cor da categoria da mensagem.

**Imagem:**imagem associada à categoria.

Validade das mensagens 

A partir da versão **12.1.2602**, será possível definir um período de validade para as mensagens durante a criação da categoria.  
Para isso, é necessário habilitar a opção **“Habilitar validade”**, selecionar se o **"Tipo de validade"** será contado em **dias** ou **horas**, e informar o valor desejado.

### Como funciona?

O sistema utiliza a data e hora do envio da mensagem e soma a **Duração** (em dias ou horas) configurada na categoria para calcular a **Data de Expiração**.

**Exemplo:**  
Se a categoria possui validade de **5 dias** e a mensagem é enviada em **21/11**, a data de expiração será **26/11**.

Caso a categoria não tenha a opção **“Habilitar validade”** ativada, a data de expiração **não será preenchida nem calculada**.

A **Data de Expiração** pode variar de acordo com o tempo total necessário para o envio de todas as mensagens.

**Exemplo:**  
Se uma mensagem for enviada em **21/11 às 13:00:00**, com uma validade de **5 dias**, porém o processo de envio levar **30 minutos** para ser concluído, então:

* A **primeira mensagem enviada** terá a data de expiração em **26/11 às 13:00:00**.
* A **última mensagem enviada** terá a data de expiração em **26/11 às 13:30:00**.
false

Visando melhorar a performance do App Meu eduCONNECT, as imagens das categorias não serão exibidas na timeline.  
Quando uma categoria tiver o nome no formato "#Destaques\_xxxxx", ex.: "#Destaques\_Formatura, a mensagem vinculada a esta categoria será exibida como um item da seção "**Destaques**" na exibição de mensagens da timeline.   
Para maiores informações sobre os destaques na timeline, favor acessar o [link](https://tdn.totvs.com/pages/viewpage.action?pageId=789399374).
