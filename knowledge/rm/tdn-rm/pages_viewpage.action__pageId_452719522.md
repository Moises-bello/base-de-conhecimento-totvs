---
content_hash: 2be0a0f6cedf3891ecf814961b483cea08074cea9646bf96d0fb7711f8f9c6b1
fetched_at: '2026-06-29T00:10:08.481694+00:00'
page_id: '452719522'
product: rm
source: tdn-rm
title: Parâmetros do Cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719522
version: 13
---

**Parâmetros do Cálculo**

---

* **Usa novo cálculo:** Habilitando este parâmetro, o sistema irá considerar o cálculo.net. A partir da versão 11.80, a utilização deste parâmetro é obrigatória.
* **Considera extra autorizada por intervalo:** Habilitando esta opção o sistema irá considerar os intervalos de extras autorizadas na data e não mais o número de horas autorizadas para a data. Quando essa opção está desmarcada o número de horas autorizados será aplicado nas ocorrências que tem a mesma jornada de referência da data.

* **Considera a data de demissão como dia útil:** Com este parâmetro habilitado o funcionário deverá cumprir a sua jornada normalmente calculando assim exceções se acontecerem. Se o parâmetro não estiver marcado, o sistema irá continuar o cálculo, tratando a data de demissão como dia não útil.

**Exemplo:** Funcionário com data de demissão 15/08/2000. Com o parâmetro marcado, o funcionário terá a sua movimentação calculada até o dia 15/08. Com o parâmetro desmarcado, o funcionário terá a sua movimentação calculada até o dia 14/08.

* **Considera horário alternativo para dias sem batidas no horário padrão:** Ao habilitar este parâmetro o sistema irá considerar o horário alternativo para dias sem trabalho no horário padrão. Mesmo se no horário do funcionário for um dia de descanso e compensado, o sistema irá substituir o horário do funcionário pelo horário alternativo.

**Observação:** Este parâmetro só  será considerado se os horários alternativos vinculados aos funcionários possuírem o mesmo número de índices do horário cadastrado para o funcionário.  Para aplicação do cálculo é necessário que o parâmetro do sindicato **[Considera início da jornada para definir tipo de extra](https://tdn.totvs.com.br/display/public/LRM/Extra)**esteja *marcado*.

**Exemplo:** Horário Padrão: Seg: 08:00E - 12:00S - 14:00E - 18:00S

Ter: 08:00E - 12:00S - 14:00E - 18:00S

Qua: 08:00E - 12:00S - 14:00E - 18:00S

Qui: 08:00E - 12:00S - 14:00E - 18:00S

Sex: 08:00E - 12:00S - 14:00E - 18:00S

Sab: Comp

Dom: Desc

Horário Alternativo Noturno:

Seg: 22:00E

Ter:  01:00S  02:00E 05:00S 22:00E

Qua:  01:00S  02:00E 05:00S 22:00E

Qui:  01:00S  02:00E 05:00S 22:00E

Sex:  01:00S  02:00E 05:00S 22:00E

Sab:  01:00S  02:00E 05:00S 22:00E

Dom:01:00S  02:00E 05:00S.

Batidas dos funcionários:

Qui: 22:00E  Sex:  01:00S - 02:00E - 05:00S - 22:00E  Sab:  01:00S - 02:00E - 05:00S

Para estes dias o sistema vai considerar o horário alternativo. Se não marcar o parâmetro "Considera Horário Alternativo para dias sem batida no horário padrão" o sistema não calculará horas base para o dia de Sábado, somente calculando corretamente este dia se o parâmetro "Considera Horário Alternativo para dias sem batida no horário padrão" estiver selecionado.

* **Executa cálculo a partir da data de transferência:** Este parâmetro será usado nos cálculos da movimentação dos funcionários demitidos por transferência. Habilitando este campo o sistema passa a considerar a data de transferência para a nova chapa do funcionário.

**Observação:** Ao efetuar o lançamento dos eventos para o RM Labore, deve-se fazer um filtro para não lançar também a movimentação constante na chapa antiga.

* **Utiliza justificativa de exceção:** Habilitando este parâmetro, o sistema irá armazenar os intervalos de atrasos, faltas e extras diárias efetuadas para que o funcionário possa justificá-los. As justificativas das exceções são feitas apenas no RM Portal.
* **Executa o cálculo até:** **Fim do Período mensal:** O sistema vai fazer o cálculo da movimentação dos funcionários de acordo com o período mensal informado na pasta de Identificação do parâmetro do sistema.
* **A data atual:** O sistema vai fazer o cálculo da movimentação dos funcionários com a data inicial definida no período mensal do parâmetro do sistema até a data atual do servidor. Se a data atual do servidor for maior que a data final do período mensal determinado na pasta de Identificação, o sistema vai considerar a data final do período mensal.

**Observação:** Este parâmetro não pode ser utilizado por funcionários que utilizam banco de horas por período onde tenha alguma movimentação do banco calculada por fórmula.

* **A data atual menos 1 dia:** O sistema vai fazer o cálculo da movimentação dos funcionários com a data inicial definida no período mensal do parâmetro do sistema até um dia anterior a data atual do servidor (ontem). Se a data atual menos um dia do servidor for maior que a data final do período mensal determinado na pasta de Identificação, o sistema vai considerar a data final do período mensal.

**Observação:** Este parâmetro não pode ser utilizado por funcionários que utilizam banco de horas por período onde tenha alguma movimentação do banco calculada por fórmula.

* **Realiza recálculo após a edição global de batidas:** após realizar a edição de batidas globais através do espelho do funcionário o sistema efetuará o recálculo automaticamente caso o usuário tenha feito alteração.

**Observação:** O recálculo será realizado inclusive para os eventos calculados por fórmula.

* **Extra aprovada sobrepõe as extras parametrizadas para o funcionário:** Este parâmetro ficará por padrão selecionado. Sendo utilizado para controlar o fluxo de aprovação de extras e também o recálculo para extras pré-autorizadas na parametrização do funcionário.
  + Quando marcado: as horas extras parametrizadas para o funcionário são exibidas na tela de aprovação e qualquer lançamento de autorização prevalece sobre as horas parametrizadas.
  + Quando desmarcado: utiliza as horas extras parametrizadas no cálculo sempre que forem maiores ou iguais as extras geradas por ocorrências. Além disso, as extras pré-autorizadas não são exibidas na tela de Aprovação de extras no portal.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Assistente de Implantação de Processos
