---
content_hash: b2d9c0939c284f905b5935e3dfda7dd209662e804e822667b982f6b1c7a267da
fetched_at: '2026-06-29T00:10:03.934080+00:00'
page_id: '452719175'
product: rm
source: tdn-rm
title: Cadastro de Horários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719175
version: 43
---

Visualize todos os horários existentes, esse cadastro é compartilhado entre o Automação de Ponto e o Folha de Pagamento e sua manutenção poderá ser feita em qualquer um desses sistemas.

**Identificação:** Preencha conforme desejado os campos Código e Descrição do Horário sendo que o campo Código é de preenchimento obrigatório.

**Data Base:** Esse campo vem preenchido por default com o primeiro dia do período do Automação de Ponto. Pode ser alterado conforme a necessidade no cadastramento do horário.

**Tipo de Horário:** Os tipos de horário antes informado no cadastro do funcionário agora devem ser informados no cadastro de horário. São eles:

* Rígido: Para definir um horário em que o funcionário deverá respeitar rigorosamente as batidas cadastradas.
* Flexível: Para definir um horário em que o funcionário irá ter total flexibilidade para efetuar suas batidas, e caso haja atrasos os mesmo serão compensados com as extras. Vale ressaltar que existe pré-definição de jornada e algumas tratativas no sistema considera isso. Exemplos: atestados médicos, importação de batidas considerando jornada, etc.
* Núcleo: Para definir intervalos dentro do horário em que o funcionário deve respeitar rigorosamente as batidas cadastradas, os outros intervalos do horário serão intervalos compensáveis.
* Semi- Flexível: Para definir intervalos compensáveis dentro intervalo de refeição do horário, as batidas de início e fim da jornada devem ser respeitadas rigorosamente.

**Paga Adicional Noturno:** Permite que o usuário configure para que o adicional noturno seja pago de forma proporcional dentro do período de apuração do ponto.       
   
**Considera redução da jornada noturna:** Marcando este parâmetro será considerado a redução da jornada conforme a interseção do planejado com o intervalo de adicional noturno.

**Observação:** As jornadas deverão ser cadastradas já com a redução da jornada.

**Exemplo:**  
**Horário Padrão:** 22:00 | 06:00 **Horário reduzido que deve ser cadastrado:** 22:00 | 05:00

**Horário Alternativo Noturno:** Quando este parâmetro está habilitado, é considerado o índice alternativo para o dia que iniciou a jornada e o dia seguinte. Desconsiderando qualquer jornada que seria iniciada no dia seguinte, mesmo que as batidas registradas correspondam a jornada do próprio horário alternativo.

**Exemplo:**

*Horário do funcionário :* 08:00 - 12:00 - 14:00 - 18:00

*Horário alternativo:* 21:00 - 02:00 - 03:00 - 06:00

*Resultado:*

Dia 01/11/2022:  Horário do funcionário: 08:00 - 12:00 - 14:00 - 18:00

Dia 02/11/2022 : Horário alternativo:       21:00 - 02:00 - 03:00 - 06:00

Dia 03/11/2022:  (Desconsidera a jornada planejada)

Dia 04/11/2022: Horário do funcionário: 08:00 - 12:00 - 14:00 - 18:00

**Considera feriados no cálculo:** Por default esse parâmetro vem marcado e estará considerando os feriados cadastrados no calendário associado a seção do funcionário, caso ele seja desmarcado o sistema não irá considerar os feriados.       
   
**Horário de Escala:** Determine se o horário será de escala. O horário será apresentado no menu de alteração global de escala.       
   
**Considera feriado no dia de saída :** Para considerar a jornada iniciada no dia anterior ao feriado como início do feriado e seu término será no próprio dia em que o feriado foi cadastro.  

Exemplo:

Feriado dia 07/09

Data     Entrada 1   Saída 1

06/09   22:00

07/09                        05:00 

Com o parâmetro marcado o sistema irá considerar o intervalo de 22:00 do dia 06/09 ás 05:00 do dia 07/09 como feriado.    
   
**Observação:**  

Nos parâmetros do sindicato em Feriados o parâmetro "Substitui jornada planejada que terminou no feriado" terá o mesmo efeito desse parâmetro. Existe essas duas formas de parametrização porque caso queira utilizar somente para os dias que o funcionário esteja utilizando esse horário então parametrize por aqui, e caso queira utilizar para todo o período parametrize nos parâmetros do sindicato.

**Horário Inativo:** Um horário quando inativo não ficará visível para escolha nos parâmetros do funcionário, em alterações globais de horário ou no RM Portal. 

**Considerar a data final da jornada como data referência:** Por default esse parâmetro virá desmarcado e o sistema irá considerar a movimentação do funcionário com base na data de entrada da jornada, caso ele seja marcado será considerada a data final da jornada. Ao cadastrar um horário com jornada noturna obrigatoriamente deverá ser cadastrado com mais de uma jornada.

Maiores informações veja em : [Considerar a data final da jornada como data referência.](https://tdn.totvs.com/pages/viewpage.action?pageId=555272447)

**Tipo de Jornada e-Social**  
O parâmetro possui o objetivo de representar qual o tipo da jornada que será considerado para o e-Social. Existirá como opção de escolha os seguintes itens: - Jornada com horário diário e folga fixos; - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso); - Jornada com horário diário fixo e folga variável; - Demais tipos de jornada.  
A informação acima será considerado no leiaute do eSocial  nos eventos  "S-2200 - Evento Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador" e "S-2206 -Alteração de Contrato de Trabalho".

**Atenção:**  
Para atender ao eSocial, quando a jornada for semanal, o usuário poderá incluir horário padrão por dia da semana, e folga fixa.  
Exemplo:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Data | Índice | Letra | ID Jornada | Dia | Entrada 1 | Saída 1 | Entrada 2 | Saída 2 |
| 16/02/2016 | 1 |  | 1 | TER | 08:00 | 12:00 | 14:00 | 18:00 |
| 17/02/2016 | 2 |  | 1 | QUA | 08:00 | 12:00 | 14:00 | 18:00 |
| 18/02/2016 | 3 | A | 1 | QUI | 08:00 | 12:00 | 14:00 | 18:00 |
| 19/02/2016 | 4 |  | 1 | SEX | 08:00 | 12:00 | 14:00 | 18:00 |
| 20/02/2016 | 5 |  | 1 | SÁB | 08:00 | 12:00 | 14:00 | 18:00 |
| 21/02/2016 | 6 |  | 1 | DOM | 08:00 | 12:00 | 14:00 | 18:00 |
| 22/02/2016 | 7 |  | 1 | SEG | 00:00 | 00:00 |  |  |

---

Jornada  
eSocial Visualizar Horário Limite de Tolerância  
[Pausa Remunerada](https://tdn.totvs.com/display/LRM/Pausa+Remunerada)

|  |  |
| --- | --- |
|  | Como Fazer |

---

Cópia de Horário Cópia de Horário entre Coligadas Exportar Horário Importar Horário
