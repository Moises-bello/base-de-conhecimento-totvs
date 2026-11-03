---
content_hash: 6072631eb48d6aee3e3ba5b70cecde6bb84dba7897a72975f00a562ac5f14cea
fetched_at: '2026-06-29T00:08:24.684846+00:00'
page_id: '270899801'
product: rm
source: tdn-rm
title: RMBIB00003_Reserva
type: documentation
url: https://tdn.totvs.com/display/LRM/RMBIB00003_Reserva
version: 6
---

# Reserva

|  |  |
| --- | --- |
| **Produto:** | Gestão Bibliotecária |
| **Versões:** | 12.1.14 |
| **Processo:** | Movimentações |
| **Subprocesso:** | Reserva |
| **Data da publicação:** |  |

Este processo consiste na reserva de um exemplar que está emprestado para outro usuário da biblioteca.

Requisitos:

Para que a reserva de fato aconteça, a aplicação irá realizar algumas validações em relação ao usuário, são elas:

* Somente usuários com situação regular e com acesso à filial/unidade podem fazer reserva de publicações.
* O usuário só poderá fazer reserva caso não existam exemplares disponíveis nas filiais/unidades que ele tem acesso.

Cadastros | usuário | usuários

Somente usuários com situação regular e com acesso à filial/unidade podem fazer reserva de publicações.

Parâmetros/configurações | parâmetros do sistema | integração | financeiro

A reserva pode ser bloqueada para:

                     - Usuários com pendências financeiras na biblioteca, de acordo com parametrização.

                     - Alunos inadimplentes em qualquer coligada do TOTVS Educacional, de acordo com parametrização.

Parâmetros/configurações | parâmetros do sistema | integração | educacional

A permissão de reserva para usuários deve ser parametrizada para:

         - Alunos no Totvs Educacional: cursando disciplina ou não.

Parâmetros/configurações | parâmetros do sistema | integração | folha de pagamento

A permissão de reserva para usuários deve ser parametrizada para:

         - Funcionários no Totvs Folha de Pagamento: demitidos ou não.

Parâmetros/configurações | parâmetros do sistema | movimentação | reserva

Por padrão, não é permitido a reserva para usuários que estão com empréstimos em atraso. A liberação da reserva neste caso deve ser configurada nos parâmetros de reserva.

O objetivo desta etapa é definir as características gerais do processo de reserva de publicações.

**Permitir para usuários com devolução em atraso:**Este parâmetro define que usuários que possuem atrasos em devoluções de exemplares poderão realizar reservas de publicações.

**Permitir reserva por volume, edição e ano (somente para WEB):**Este parâmetro define que ao realizar reservas através do RM Portal, serão apresentados campos para que o usuário informe volume, edição e ano do exemplar a reservar.

**Obrigar a seleção de volume, edição e ano na reserva:**Este parâmetro define que o usuário será obrigado a especificar sua reserva, informando volume, edição e ano do exemplar a reservar.

**Atenção**

* A funcionalidade do parâmetro Obrigar a seleção de volume, edição e ano na reserva somente será válida caso o parâmetro Permitir reserva por volume, edição e ano (somente para WEB) esteja habilitado.

**Especificar filial e unidade bibliotecária no momento da reserva:**Este parâmetro define que o usuário será obrigado a informar a filial e a unidade bibliotecária em que deseja reservar exemplares de uma publicação.

**Cálculo de data de liberação de reserva:**Neste parâmetro é possível definir se sábado e/ou domingo serão considerados como dias úteis para reserva.

**Bloquear reservas de exemplares de circulação interna:**Neste parâmetro, é possível permitir/bloquear reservas de publicações de circulação interna.

Cadastros | usuário | tipos de usuário

O limite de reservas é definido por tipo de usuário no campo de “Número máximo de reservas”.

Parâmetros/configurações | parâmetros do sistema | movimentação | empréstimo 2/2

Outras validações em relação à publicação irão acontecer:

* Caso existam exemplares disponíveis da publicação selecionada, a reserva não é permitida. Exemplares com situação que não permitem empréstimo não devem ser considerados como disponível;
* Se já existir uma reserva com status “Reservada” para o usuário com a mesma publicação, não é permitido fazer uma nova reserva;
* Se todos os exemplares da publicação forem de circulação interna, a reserva só será permitida se o parâmetro "Bloquear reservas de exemplares de circulação interna" estiver desabilitado e o parâmetro "Liberar circulação de exemplares bloqueados" estiver marcado.

Parâmetros/configurações | regras de empréstimo

Na regra de empréstimo será validado:

* Se permite empréstimo e reserva para aquele tipo de usuário e o grupo de publicação;
* Se permite reserva com a mesma publicação emprestada para aquele tipo de usuário e o grupo de publicação;

Movimentações | reserva

Ao realizar uma reserva é possível selecionar o usuário através: do código do usuário, código pessoa, biometria, chapa de funcionário e registro acadêmico do aluno. Ao informar a publicação a ser reservada é possível definir critérios para filtrar exemplares da publicação. Estes critérios são volume, edição e ano. É possível também definir a localização da publicação selecionando a filial e unidade.

 

Após a realização da reserva a situação de reserva assume o status de "Efetuado", porém ele sofre alterações com decorrer das movimentações e a situação de reserva é alterada. E de acordo com as alterações ocorridas a reserva pode ter os seguintes status:

 

* **Reservado (R):** Esse status é atribuído quando é criada uma nova reserva.
* **Confirmado (F):**Esse status é atribuído quando a reserva está confirmada para o usuário, ou seja, pode ser feito o empréstimo desta reserva. Para isto é preciso estar com o status “Reservado” e ser o primeiro da fila de reserva cujo exemplar disponível atenda aos critérios da reserva. Depois de confirmada a reserva, os campos “Disponível para empréstimo” e “Limite para empréstimo” são preenchidos de acordo com a regra de empréstimo.
* **Efetuada (E):** Esse status é atribuído quando é realizado o empréstimo da reserva que estava com o status “Confirmado”.
* **Cancelado (C):**Esse status é atribuído quando a reserva é cancelada. Ele pode ser definido manualmente através do processo de Cancelar reservas, para isto é preciso estar com o status “Reservado” ou “Confirmado”. Ele é alterado automaticamente pelo sistema quando a reserva com o status “Confirmado” e tem a data do campo “Limite para empréstimo” ultrapassado.
