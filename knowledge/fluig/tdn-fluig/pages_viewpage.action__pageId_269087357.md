---
content_hash: 26e99b70ea11a39a305657d32498e2f56a5640c55654da1346e7a1aac25b9d3e
fetched_at: '2026-06-28T21:35:24.249057+00:00'
page_id: '269087357'
product: fluig
source: tdn-fluig
title: LMS 037 - Por que é exibida a mensagem de aprovado no pós-teste sem atingir
  a nota de aprovação do treinamento?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269087357
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

***Card*:** LMS

# Ocorrência

No pós-teste o aluno foi considerado aprovado com a pontuação 20.00, sendo que no treinamento está configurado para considerar aprovado apenas quando atingir a nota igual 70.00 ou superior. Por que é exibida a mensagem de aprovado nesse caso?

# Causa

O índice de aprovação da avaliação que é o pós-teste está configurado como 0.00 (zero).

# Solução

Se na avaliação (pós-teste) o índice de aprovação estiver configurado como 0.00 e no treinamento a pontuação para aprovação estiver configurada como 70.00, ao tirar a nota 20.00 no pós-teste, o aluno será aprovado na avaliação (pós-teste), pois o índice é zero, *mas não será aprovado no treinamento*. Para ser aprovado no treinamento, a nota atingida deve ser, no mínimo, 70.00.

A plataforma permite que o índice de aprovação de avaliações seja zero porque o teste pode se tratar, por exemplo, de uma avaliação de reação, que geralmente não é contabilizada. O valor máximo permitido para esse campo é 100.

Importante!

A partir da atualização **[1.6.5-190219](http://tdn.totvs.com/pages/viewpage.action?pageId=442961412#Atualiza%C3%A7%C3%B5es(1.6.5)-190219)**, o **LMS** não faz mais parte da plataforma para **novas instalações**.

Mas, não se preocupe: se você adquiriu a plataforma com o **LMS incluso**, entre em contato com o [Suporte Fluig](https://suporte.fluig.com/) para que você consiga utiliza-lo normalmente – mesmo após a atualização **1.6.5-190219**. Se você não lembra se o LMS está incluso ou não no seu pacote, consulte sua proposta comercial ou entre em contato com o seu ESN.
