---
content_hash: 7c4b35ffd8f3e650c87b3e97cbc27212b87501def1aff13c6ddf172f21ce0278
fetched_at: '2026-06-29T00:11:29.389510+00:00'
page_id: '736959073'
product: rm
source: tdn-rm
title: Controle 2/2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=736959073
version: 7
---

**Cancelamento de Férias**

**Permite armazenar líquido no mês seguinte ao pagto, no caso de lib. competência**

Este parâmetro serve para que o sistema armazene o líquido de férias, quando as férias foram marcadas na competência anterior, antes da liberação da competência, para posterior lançamento do evento.

**Evento de desconto programado para ser lançado**

Destinado a informação do evento de desconto programado criado no cadastro de eventos, para ser lançado através do Grupo de Eventos - Eventos Programados.

**Observação:**

O evento para armazenar o valor do Liquido de Férias para posterior desconto, deverá será do Tipo Desconto, Sem Código de Cálculo, Valor.

**Tipo de Lançamento do evento programado**

Destinado a informação do tipo de lançamento de evento programado, criado na tabela dinâmica com o código **'TPEVTPROG - Tipo de Evento Programado'.**

**Observação:**

Deverá ser criado o tipo de Evento Programado a ser lançado, através do Grupo de Eventos, marcando o lançamento de 'Evento Programado'.

**Evento para pagamento do complemento salarial, quando período de férias atinge 3 meses**

Deverá ser informado o Evento para pagamento do complemento salarial, quando período de férias atinge 3 meses".

**Observação:**

Este evento obrigatoriamente deverá ter CC 1 ou 2.

**Cadastro das férias**

**Validar a quantidade de Dias de Gozo de Férias conforme as regras da Reforma Trabalhista**  
Desconsiderar os dias de abono na contagem  (Será desconsiderado os dias de abono na contagem de dias de gozo)

**Impedir início de férias em feriados, dias de descanso ou até 2 dias antes destes**

Com esse parâmetro marcado o sistema impede que o funcionário insira sugestões de férias em até dois dias que antecedem feriados e dias de descanso do funcionário.  
A verificação dos feriados cadastrados é de acordo com o calendário que está vinculado à seção do funcionário, no calendário deve ser informado os dias que são feriados. A verificação do dia de descanso é realizada de acordo com a jornada que o funcionário está vinculado, na jornada é inserido o dia de descanso.

**Não impedir marcação de férias para jornada 12x36**

Com este parâmetro marcado o sistema deverá permitir o a marcação de sugestão de férias, **desde que não seja dia de folga ou feriado** do respectivo funcionário. O Parâmetro acima só fica habilitado caso o parâmetro **Impedir início de férias em feriados, dias de descanso ou até 2 dias antes destes**esteja marcado.

**Desconsiderar dia Compensado (Utilizado para desconsiderar o dia compensado)**

Com este parâmetro marcado o sistema validar o tipo de Jornada cadastrada para o horário do funcionário e caso a mesma seja compensado, não irá impedir a marcação de férias até dois dias antes deste. O Parâmetro só fica habilitado caso o parâmetro **Impedir início de férias em feriados, dias de descanso ou até 2 dias antes destes**esteja marcado. 

**Observação:**

Para a marcação de todos esses novos parâmetros do cadastro das férias, se faz necessário que o parâmetro **'Ativar alterações da Reforma Trabalhista conforme a Lei nº 13.467 de 13 de Julho de 2017'** que se encontra no seguinte caminho:  **Parametrizador | 06.01.03 - Folha Normal | Geral 1/2**

<< Retornar para **Férias**
