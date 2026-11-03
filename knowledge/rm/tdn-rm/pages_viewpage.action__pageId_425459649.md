---
content_hash: c6f0e3fca5441471e8c567bb7c4227e9ac0bde82821b6dcd9c1ecd022b0307f0
fetched_at: '2026-06-29T00:09:37.908920+00:00'
page_id: '425459649'
product: rm
source: tdn-rm
title: Regras de Empréstimo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459649
version: 5
---

A Regra de Empréstimo consiste em configurações que definem as regras para a realização de empréstimo, reserva, renovação, bem como as penalidades por atraso na devolução. A regra de empréstimo irá impactar diretamente nas rotinas de movimentações dos usuários da biblioteca. Antes de ter uma regra de empréstimo é necessário que haja um "Tipo de Usuário" e um "Grupo de Publicação" para estabelecer o vínculo entre o tipo de usuário que deseja realizar o empréstimo e o grupo de publicação ao qual pertence a publicação desejada.  Ou seja, para cada tipo de usuário haverá um grupo de publicação associado a ele que irá permitir que o empréstimo seja realizado ou não, e em quais condições isso irá ocorrer.

**A regra de empréstimo pode ser definida por três tipos de empréstimos distintos, sendo eles:**

* **Normal**;
* **Consulta interna**: Empréstimos de consulta interna são realizados para exemplares que são assinalados com este atributo em seu cadastro;
* **Consulta externa**: Empréstimo realizado quando se deseja obter um empréstimo diferenciado ou quando o usuário esgotou o limite de empréstimos normais e de consulta interna.

O cadastro da regra de empréstimo é dividido nas seguintes abas:

**Empréstimo**

Nesta aba são definidas as regras que impactam diretamente no empréstimo.   
 Aqui é preciso vincular um Tipo de usuário e Grupo de publicação, informar o valor do empréstimo e Prazo para devolução do exemplar e se será calculado em dias ou em horas para os tipos de empréstimo.

* Além disso podemos definir alguns outros parâmetros para o empréstimo:
* Se o empréstimo é permitido;
* Permitir empréstimo de mais de um exemplar de uma determinada publicação para o mesmo usuário;
* Bloquear empréstimo para usuários com devoluções em atraso;
* Controlar empréstimos por faixa etária. Neste caso, deve ser configurada na regra a idade mínima para realização do empréstimo. Devem ser criados  específicos para faixas etárias e as devidas publicações devem ser relacionadas a estes grupos, onde no momento do empréstimo será verificada a idade do usuário (caso ela seja informada). O usuário não tenha a idade mínima, será bloqueado o empréstimo.

**Devolução**

Aqui serão definidos os valores e atributos relacionados à rotina de devolução. Pode-se configurar se é permitido renovar empréstimo e as penalidades por devolução em atraso. Considera-se que uma devolução está em atraso se a data de devolução prevista for anterior ao momento atual de devolução.  
 As penalidades serão configuradas distintamente para cada situação no momento da devolução:

* Se o empréstimo é normal, de consulta interna ou de consulta externa;
* Se o exemplar possui reserva.

Assim, em cada uma destas situações pode ser configurado:

* O valor da penalidade financeira;
* O número de dias de suspensão aplicado;
* Se a penalidade será: Por dia ou por hora de atraso; ou se não será aplicada nenhuma penalidade.

**Reserva**  
 Nesta aba é configurado a regra referente à rotina de reserva. É possível parametrizar se permite a reserva/reservar com a mesma publicação emprestada. Além de definir em quantos dias a reserva do exemplar estará disponível para o usuário assim que o exemplar for devolvido.
