---
content_hash: 3cd39c76624ac599d407ad1cd58e69ae3b50db2d85ad90a1418cc6d853fa172b
fetched_at: '2026-06-29T00:09:34.539007+00:00'
page_id: '425459180'
product: rm
source: tdn-rm
title: 14.04 - Movimentação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459180
version: 16
---

**14.04.01 - Empréstimo**   
   
O objetivo desta etapa é definir as características gerais do processo de empréstimo.  
   
**Solicitar senha para empréstimo:** É possível parametrizar se será solicitada senha ao realizar empréstimo para: Todos os usuários, Não solicitar senha ou para todos usuários (exceto supervisores).  
   
**Cálculo da data de devolução do empréstimo**  
Aqui possível definir se no fim de semana o sábado e domingo é considerado como dia útil. E se a biblioteca irá considerar período de férias para definir a data de devolução prevista, informando data inicial e final do período e a data de prevista de devolução.

**Considerar período de férias para definir a data de devolução prevista**

O que é o período de férias?

O período de férias é usado pelo sistema para evitar que a **data de devolução prevista** de um empréstimo caia em um intervalo de indisponibilidade (exemplo: recesso da biblioteca).

Regras principais

1. Devolução dentro do período de férias → ajusta para o final.

   * Exemplo: devolução cairia em 07/07/2025 (durante férias).
   * O sistema **ajusta para 30/07/2025 (Data de devolução prevista)**.
2. Devolução após o período de férias → mantém data original.

   * Se a data prevista de devolução cair **fora do período de férias**, não há alteração: a data permanece a mesma definida pela regra de empréstimo.
   * **Exemplo:** a regra de empréstimo do exemplar especifica **20 dias a partir da data de empréstimo**, resultando em devolução prevista para **16/07/2025**.

     + Como essa data já está fora do período de férias, o sistema mantém **16/07/2025**.
3. O cálculo sempre verifica o intervalo configurado (01/07/2025 até 15/07/2025).

**Alterar prazo devolução maior que o definido na regra (Dias/Horas):** Este parâmetro define que os usuários terão acesso ao processo de alteração de prazo de devolução, na movimentação, permitindo que se estenda a data de devolução de um exemplar, no momento do empréstimo.  
   
**Liberar circulação de exemplares bloqueados:** Este parâmetro define que os exemplares de circulação interna (bloqueados) estarão disponíveis para empréstimo.

Importante

O parâmetro "**Liberar circulação de exemplares boqueados**" também irá permitir a reserva de exemplares de circulação interna (bloqueados) caso o parâmetro "**Bloquear reservas de exemplares de circulação interna"** esteja desmarcado.

**Permitir empréstimo de exemplares de circulação interna quando não existir mais nenhum outro exemplar disponível:** Este parâmetro define que os exemplares de circulação interna (bloqueados) estarão disponíveis para empréstimo quando não houver mais nenhum outro exemplar disponível para empréstimo.

Importante

Ao marcar o parâmetro "**Liberar circulação de exemplares boqueados**" o parâmetro "**Permitir empréstimo de exemplares de circulação interna quando não existir mais nenhum outro exemplar disponível**" ficará bloqueado. O mesmo acontecerá de modo inverso. Sendo assim, não é possível marcar os dois parâmetros ao mesmo tempo.

Observação

O parâmetro "**Permitir empréstimo de exemplares de circulação interna quando não existir mais nenhum outro exemplar disponível**" é exclusivo para a operação de empréstimo, sendo assim, não possui nenhuma relação com o parâmetro de reserva "**Bloquear reservas de exemplares de circulação interna"** que é exclusivo para reserva. 

**Considerar horário de funcionamento da biblioteca para empréstimo em horas:** Este parâmetro define que para empréstimos realizados com prazo de devolução em horas, o sistema calculará a data e o horário de devolução dos exemplares respeitando o horário de funcionamento da biblioteca.  
   
**Ao limitar o número máximo de empréstimo por tipo de usuário, não considerar separadamente os empréstimos de consulta interna e externa.**  
Habilitando este parâmetro o sistema passa a verificar, para todos os empréstimos, o número máximo de exemplares em cada movimentação. Caso esteja desabilitado, o sistema irá ignorar qualquer limite de exemplares por empréstimo para o tipo de usuário.  
   
Empréstimo de fascículos (material anexo de exemplares)  
   
**Emprestar material adicional de um exemplar junto com a obra principal:** É possível definir se será obrigatório o empréstimo do fascículo com a obra principal.  
   
**Considera empréstimo de fascículos na contagem do número máximo de empréstimo permitido:** Define se será contado o empréstimo do fascículo no número máximo de empréstimo permitido para o usuário.  
   
   
 **14.04.02 - Devolução**  
    
O objetivo desta etapa é definir as características gerais do processo de devolução.  
   
**Exibir mensagem que a publicação devolvida possui reservas:** Este parâmetro define que ao devolver um exemplar de uma publicação que possua reservas, o sistema apresentará uma mensagem informando que a publicação possui reservas.  
   
**Permitir cancelamento de empréstimo em atraso:** Este parâmetro define a permissão para cancelar empréstimos de exemplares.  
   
**Permitir abonar multa para devoluções em atraso:** Este parâmetro define a permissão para abonar multas de devoluções efetuadas em atraso.  
   
**Considerar somente dia útil para o cálculo da multa e suspensão:** Este parâmetro define que o cálculo da multa e dos dias de suspensão irá considerar somente dias úteis da semana.  
   
**Permitir desconto no valor total da multa:** Este parâmetro define que o usuário poderá informar um valor a ser descontado no valor total da multa.  
   
**Permitir alteração da data prevista de devolução:** Este parâmetro define que os usuários terão acesso ao processo de alteração da data prevista de devolução, permitindo que se altere esta data.  
   
   
**14.04.03 - Renovação de empréstimo**  
   
O objetivo desta etapa é definir as características gerais do processo de renovação de empréstimos.  
   
 **Limitar a quantidade de renovações para WEB:** Este parâmetro define que a quantidade de renovações, de cada empréstimo, que um usuário poderá realizar através do RM Portal, será limitada. E permite que seja informada a quantidade de renovações por publicação.  
   
**Atenção**

* Se o limite de renovações na Web for excedido, o sistema, através do Portal, informa ao usuário que as próximas renovações deverão ser realizadas no aplicativo.
* Se desejar que a quantidade de renovações seja ilimitada o parâmetro "Limitar Quantidade de Renovações" deve estar desmarcado.

**Permitir renovação somente no dia da devolução:** Este parâmetro define que renovações de empréstimos poderão ser realizadas somente no dia da devolução dos exemplares.  
   
**Alterar o prazo de devolução para maior que o definido na regra de empréstimo no momento da renovação:** Este parâmetro define que os usuários terão acesso ao processo de alteração de prazo de devolução, permitindo que se estenda a data de devolução de um exemplar, no momento da renovação de empréstimos.  
   
   
**14.04.04 - Reserva**  
   
O objetivo desta etapa é definir as características gerais do processo de reserva de publicações.  
   
**Permitir para usuários com devolução em atraso:** Este parâmetro define que usuários que possuem atrasos em devoluções de exemplares poderão realizar reservas de publicações.  
   
**Permitir reserva por volume, edição e ano (somente para WEB):** Este parâmetro define que ao realizar reservas através do RM Portal, serão apresentados campos para que o usuário informe volume, edição e ano do exemplar a reservar.  
   
 **Obrigar a seleção de volume, edição e ano na reserva:** Este parâmetro define que o usuário será obrigado a especificar sua reserva, informando volume, edição e ano do exemplar a reservar.  
   
**Atenção**

* A funcionalidade do parâmetro Obrigar a seleção de volume, edição e ano na reserva somente será válida caso o parâmetro Permitir reserva por volume, edição e ano (somente para WEB) esteja habilitado.

**Especificar filial e unidade bibliotecária no momento da reserva:** Este parâmetro define que o usuário será obrigado a informar a filial e a unidade bibliotecária em que deseja reservar exemplares de uma publicação.  
   
**Cálculo de data de liberação de reserva:** Neste parâmetro é possível definir se sábado e/ou domingo serão considerados como dias úteis para reserva.  
   
**Bloquear reservas de exemplares de circulação interna:**Neste parâmetro, é possível permitir/bloquear reservas de publicações de circulação interna.

Observação

O parâmetro "**Bloquear reservas de exemplares de circulação interna"** é exclusivo para reserva, sendo assim não fará nenhuma interferência no parâmetro "**Permitir empréstimo de exemplares de circulação interna quando não existir mais nenhum outro exemplar disponível**" que é exclusivo para a operação de empréstimos. 

**14.04.05 - Geral**  
   
O objetivo desta etapa é definir as características gerais das movimentações da biblioteca.  
   
**Considerar finais de semana e feriados:** Neste parâmetro é possível definir se a biblioteca irá considerar finais de semana e feriados nas movimentações da biblioteca e qual será o comportamento do sistema quando houver vencimento em dia não útil. Será possível definir uma das opções:

   - Manter data: O sistema irá manter a data de vencimento mesmo o dia não sendo útil;

   - Buscar próximo dia útil: O sistema irá considerar o próximo dia útil;

   - Busca dia útil anterior: O sistema irá considerar o dia útil anterior a data de vencimento.  
   
**Considera dia não útil para cálculo de data prevista de entrega:** Define que dias não úteis serão contabilizados no cálculo de data prevista, porém o sistema irá buscar o próximo dia útil para a devolução. Este parâmetro não será habilitado caso o parâmetro.

**Considerar finais de semana e feriados** esteja habilitado.   
   
 **Exibir log de movimentações:** Define que ao efetuar uma movimentação será exibido o log contendo informações das operações realizadas.  ]
