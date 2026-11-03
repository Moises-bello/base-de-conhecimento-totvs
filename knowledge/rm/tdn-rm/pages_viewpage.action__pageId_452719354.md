---
content_hash: dab13682764b45d3f28e8c633583698378730cc0cd43cb7107333bde70a43a02
fetched_at: '2026-06-29T00:10:06.974016+00:00'
page_id: '452719354'
product: rm
source: tdn-rm
title: Cadastro de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719354
version: 25
---

Efetuar o cadastramento das Férias seguindo as regras da CLT para Férias Normais ou regras do sindicato.  
  
É necessário que antes do cadastramento, sejam verificados os parâmetros de férias nos Sindicatos e nos parâmetros do Labore.  
  
A marcação das férias pode ser através da interface 'Férias' ou 'Período Aquisitivo'.  
  
Através da interface dos períodos aquisitivos do funcionário é exibido o status de cada período, sendo períodos Fechados e um período Aberto.  
O período Aberto é a referência para o cadastro de gozo de férias atual.  
Através deste cadastro o usuário pode informar períodos aquisitivos ou período de gozo futuro.  
Porém para maior agilidade é recomendado a utilização da interface 'Férias'.  
Para cadastrar o mesmo período de gozo para mais de um funcionário utilizar o módulo Férias | Coletivas Globais.  
  
É possível executar os processos: calcular, cancelar, lançar e finalizar férias.  
Estes processos são liberados conforme situação das férias, sendo:

* Processo Calcular  = Situação de férias = 'M-Marcadas';
* Processo Cancelar = Situação de férias = 'M-Marcadas';
* Processo Lançar    = Situação de férias = 'M-Marcadas';
* Processo Finalizar  = Situação de férias = 'P-Pagas'.

A opção 'Calcular' é habilitada para períodos de gozo que tem início de gozo maior ou igual a competência corrente.

**Observação**  
Quando é marcado um período de gozo de férias, o registro é armazenado na tabela PFUFERIASPER.

Os campos INICPROGFERIAS1, FIMPROGFERIAS1 e DTPAGTOFERIAS da tabela PFUNC é preenchido com a data de início do próximo período de gozo marcado na fila.

Quando as férias são finalizadas, o campo INICPROGFERIAS1, FIMPROGFERIAS1 e DTPAGTOFERIAS são atualizados para a data de início e pagamento do próximo período de gozo marcado.

Caso não exista nenhum próximo período de gozo de férias marcado, os campos são atualizados para null. 

No caso de sugestão de férias criadas através do portal (Situação G ou D), os campos INICPROGFERIAS1, FIMPROGFERIAS1 e DTPAGTOFERIAS também irão atualizar os campos da PFUNC. No entanto, somente se não houver férias anterior em andamento. As férias sugeridas pelo Portal podem  ou não ser aprovadas, logo, não é um início de férias programada ainda. 

A tabela PFUNC será atualizada com os dados das segundas férias somente após a finalização das primeiras férias.

**Exemplo:**

* Sugestão 1: Início 18/08/2025 - Fim: 27/08/2025 e Pagamento em 14/08/2025.
  + Os campos INICPROGFERIAS1, FIMPROGFERIAS1 e DTPAGTOFERIAS são atualizados para os dados destas férias.
  + INICPROGFERIAS1: 18/08/2025
  + FIMPROGFERIAS1: 27/08/2025
  + DTPAGTOFERIAS: 14/08/2025
* Sugestão 2: Início 15/09/2025 - Fim: 24/09/2025 e Pagamento em 11/09/2025.
  + Os campos INICPROGFERIAS1, FIMPROGFERIAS1 e DTPAGTOFERIAS são atualizados para os dados destas férias, somente após a sugestão da primeira ser finalizada.
  + INICPROGFERIAS1: 15/09/2025
  + FIMPROGFERIAS1:  24/09/2025
  + DTPAGTOFERIAS:  11/09/2025

*Dica!!!*

Como o sistema permite criar mais de uma sugestão de período de gozo de férias ou até mesmo ter vários períodos de férias marcados, os campos da PFUNC não comportam todos os períodos cadastrados.

Foi criado o armazenamento da tabela PFUFERIASPER tornando possível armazenar mais períodos independente da situação.

Desta forma, orientamos os clientes para usar as informações das tabelas PFUFERIAS, PFUFERIASPER e não mais estes campos, devido a sua limitação.

**Observações:**

01 - Caso o parâmetro '**Não calcula Recibo de Férias**', disponível em**RH | Administração de Pessoal | Funcionários | Informações para o Cálculo | Parâmetros**, esteja 'marcado', o sistema não irá calcular o recibo de férias para o funcionário e também não serão exibidos no cadastro de férias o campo 'Data Pagamento' e os botões de 'Calcular' e 'Visualizar Recibo' de férias.

02 - Pelo botão "Visualizar Recibo" é permitido ao usuário, sob sua responsabilidade, a alteração de valores calculados dentro de cada verba. Para isso será observado o seguinte:

* Quando os valores calculados forem alterados será marcado o parâmetro "Alterado Manualmente" e somente será recalculado se for desmarcado e os valores ainda não estiverem lançados no envelope de pagamento.
* Se os valores de férias já estiverem lançados para o envelope de pagamento, mesmo que o parâmetro seja desmarcado, não será feito o recálculo do recibo.
* Com a alteração de valores e o parâmetro "Alterado Manualmente" marcado, os encargos serão recalculados com os novos valores informados pelo usuário. Caso não queira o recálculo dos encargos deverá marcar o parâmetro "Não Recalcular" na visão dos valores do recibo de férias.

A mudança da situação do funcionário para 'Férias', continuará sendo feito pelo processo 'Lançar' férias'.

O processo 'Finalizar' férias vai mudar a situação do funcionário de 'Férias' para 'Ativo' e atualizar os dados cadastrais do período aquisitivo de férias.

O sistema não irá consistir na Liberação de Competência se constam no envelope do funcionário os códigos de cálculo específicos de férias para funcionários com o parâmetro marcado.

Data de Pagamento  
É preenchido automaticamente, sendo a data dois dias antes da data de início de gozo das férias, desconsiderando os sábados, domingos e feriados (conforme calendário vigente da seção do funcionário), podendo ser alterada.  
  
Quando o parâmetro 'Data de Pagamento de Férias' existente em Configurações | Parametrizador | Férias | Fórmulas está preenchido, é disponibilizado o ícone para calcular esta fórmula.  
  
Caso o recibo de férias já esteja calculado e exista pensão alimentícia, sempre que a data de pagamento é alterada, ao salvar os dados, o campo 'Data Pagto Férias' do movimento da pensão é atualizado.  
  
  
Faltas  
Apuração das faltas nas Férias é conforme previsto no art. 130 da CLT, observados os casos especiais (marítimos, professores, domésticos, entre outros), após cada período de 12 meses de vigência do contrato de trabalho (período aquisitivo), o empregado tem direito a férias na seguinte proporção:  
Qtd Faltas                     Dias de direito  
até 5 faltas                   30 dias  
de 6 a 14 faltas             24 dias  
de 15 a 23 faltas           18 dias  
de 24 a 32 faltas           12 dias  
mais de 32 dias de faltas não justificadas no período aquisitivo implica a perda do direito às férias correspondentes.  
  
Quando utilizar controle de faltas os avos de férias são calculados verificando as faltas do primeiro ao último dia do período aquisitivo, ou seja, considera o dia efetivo da falta.  
Mais detalhes sobre o controle de faltas veja em Configurações | Parametrizador | Folha Normal | Controle de Faltas  
Quando não utilizar o controle de faltas, são verificadas as faltas do mês posterior ao mês de início do período aquisitivo até o mês fim do período aquisitivo.  
  
**Exemplo:**  
Período aquisitivo: 16/04/2010 a 15/04/2011  
Período para verificação das faltas  
Parâmetro marcado: 16/04/2010 a 15/04/2011  
Parâmetro desmarcado: 05/2010 a 04/2011

Limite início de gozo  
É um campo informativo, sendo 30 dias antes do vencimento do segundo período aquisitivo de férias.  
É gerada uma mensagem de alerta considerando o período concessivo e mencionando a data limite para gozo das férias, para que não transforme em férias em dobro.  
Esta mensagem é gerada 6 (seis) meses antes do funcionário adquirir as férias em dobro.  
  
**Exemplo:**  
Admissão: 17/10/2011  
Período aquisitivo sem gozo: 17/10/2011 a 16/10/2012 e 17/10/2012 a 16/10/2013  
Limite início de gozo: 17/09/2013 para que não haja o pagamento em dobro.  
Em 04/2013 a mensagem passa a ser apresentada no cadastro de férias.

**Observação:**

O pagamento das férias em dobro somente é realizado quando está configurado para este procedimento em Parametrizador / Férias / Férias em dobro, marcando o parâmetro “Paga férias em dobro”

Log de cálculo da data limite para início das férias

Botão para demonstração do cálculo no cadastro de férias referente ao limite de concessão das férias em dobro.

Serão contabilizados os dias de afastamentos durante o período concessivo, ou seja, após o vencimento do período aquisitivo.

O período concessivo de férias considerará, além do histórico de afastamento, os parâmetros:

* Não interrompe contagem do período para pagto. de férias em dobro no afast.por Licença Maternidade (E)
* Interrompe contagem do período para pagto. de férias em dobro nos afastamentos I - L - M - P - T - Q
* Desconsidera período de atestado médico na interrupção

**Exemplo:**

**Esse exemplo é fictício informando todas as possibilidades de afastamentos dentro do período concessivo para apresentar no cálculo do limite de dias.**

**Considerando os parâmetros marcados para serem considerados da seguinte forma:**

Parâmetro 'Não interrompe contagem do período para pagto. de férias em dobro no afast.por Licença Maternidade (E)' está Desmarcado.

Parâmetro 'Interrompe contagem do período para pagto. de férias em dobro nos afastamentos I - L - M - P - T - Q' está Marcado.

Parâmetro 'Desconsidera período de atestado médico na interrupção' está Marcado.

Férias em Dobro  
É calculado automaticamente quando o parâmetro existente no Parametrizador | Férias | Férias em Dobro está marcado. É necessário que exista eventos com os códigos de cálculo abaixo:  
309 - FÉRIAS EM DOBRO  
310 - ADICIONAL 1/3 DE FÉRIAS EM DOBRO  
311 - ABONO DE FÉRIAS EM DOBRO  
312 - ADICIONAL 1/3 DE ABONO DE FÉRIAS EM DOBRO  
  
             
             
Considerações quando no cadastro do Sindicato, o parâmetro 'Ignora feriados na contagem das férias' está marcado.  
  
Dias de Feriados  
É total de feriados a serem desconsiderados no período do gozo das férias.  
  
Feriados  
São apresentadas as datas dos feriados a serem desconsiderados no período do gozo das férias.   
  
**Observação:**  
Os valores destes campos são gravados/atualizados ao salvar os dados da tela.  
  
Estes campos NÃO são habilitados para edição, e o cálculo do número de dias de férias sempre observa estes campos.  
  
Quando os campos 'Início Per. Gozo' e 'Final Per. Gozo' são preenchidos, é verificado quantos dias tem entre as datas informadas e subtraído o total de dias de feriados para calcular o campo 'Dias de Férias'.  
  
**Exemplo:**  
No calendário informado na seção do funcionário, a data 07/09/2009 esta com o parâmetro marcado.  
No cadastro de férias são preenchidos os seguintes campos:  
Início Per. Gozo = 01/09/2009  
Final Per. Gozo  = 30/09/2009  
Ao salvar o cadastro o campo 'Dias de Férias' é preenchido com o valor de 29.  
  
**Observação:**  
Ao preencher o campo 'Final Per. Gozo' o campo 'Dias de Férias' fica desabilitado para edição.  
  
Quando os campos 'Início Per. Gozo' e o campo 'Dias de Férias' são preenchidos, o campo 'Final Per. Gozo' é preenchido automaticamente de maneira que o número de dias de férias ignorando os dias feriados seja igual ao número informado.   
  
**Exemplo:**  
No calendário informado na seção do funcionário, a data 07/09/2009 está com o parâmetro marcado.  
No cadastro de férias do funcionário são preenchidos os seguintes campos:  
Início Per. Gozo = 01/09/2009  
Dias de Férias   = 30  
Ao salvar o cadastro o campo 'Final Per. Gozo' é preenchido com a data 01/10/2009.  
  
**Observação:**  
Ao preencher o campo 'Dias de Férias' o campo 'Final Per. Gozo' fica desabilitado para edição.  
  
Os campos 'Dias de Feriados' e 'Feriados', somente ficam visíveis no cadastro de férias, quando no sindicato do funcionário o parâmetro 'Ignora feriados na contagem das férias' está marcado.  
  
**Atenção I:**  
Mesmo quando o feriado cair em dia de compensação ou descanso do funcionário (conforme horário informado no cadastro do funcionário) o feriado nas férias é desconsiderado.  
  
**Atenção II:**  
No cálculo da folha de pagamento, os dias de feriados a desconsiderar serão somados nos códigos de cálculos: 1-Horas Normais e 2-Dias Trabalhados.   
  
Todos os processos que verificam o total de dias de férias gozadas no período irão tratar os feriados a desconsiderar. Tais como provisão, variáveis de fórmulas, diferença de férias, finalização de férias, etc.  
  
**Atenção III:**  
Atualmente não tem tratamento para a situação em que, devido os feriados o funcionário tem 3 meses de gozo de férias.  
  
**Exemplo:**  
No calendário informado na seção do funcionário existem as seguintes datas com o parâmetro marcado:  
23/02/2009 - Carnaval  
24/02/2009 - Carnaval  
  
No cadastro de férias do funcionário foram preenchidos os seguintes campos:  
Data Início = 30/01/2009  
Dias de Férias = 30  
O campo 'Data Fim' deverá ser 02/03/2009.  
  
  
Dias de Abono  
O empregado tem direito de converter um terço do período de férias a que faz jus, em abono pecuniário.  
Informar os dias referentes ao abono de férias.  
Para atender a convenções coletivas, existe a possibilidade de cadastrar somente abono pecuniário, sendo obrigatório apenas o preenchimento da data de pagamento.  
O processo é semelhante ao de férias, porém a base para verificação do salário, lançamento, diferenças e outros é a data de pagamento, uma vez que não existe o período do abono.  
No lançamento das férias, os eventos são lançados, porém não altera a situação do funcionário para 'F-Férias' e não registra o histórico de situação, devido não existir período de gozo.  
  
  
1ª Parc. 13º Salário  
Caso o funcionário já tenha recebido a 1ª parcela e este parâmetro seja marcado, ao salvar é gerada a mensagem informando quando foi pago e não é processado no lançamento da 1ª parcela nas férias.  
  
  
Situação das Férias  
O preenchimento deste campo depende do processo executado, conforme abaixo:  
G – Aguardando Aprovação do Gestor (quando o subordinado cadastra a sugestão de férias);  
D – Aguardando Aprovação do DP (quando o gestor aprova a sugestão e não tem permissão de marcar férias);  
M – Marcadas (quando o DP aprova ou quando o gestor tem permissão para marcar);  
P – Pagas (quando calcula as férias e as mesmas são lançadas na movimentação);  
F – Finalizadas (quando fecha o período aquisitivo e abre outro período aquisitivo, independente de ser um novo ou o mesmo);  
X - Finalizadas para o próximo mês (quando é processada a finalização de férias para a próxima competência. Na liberação de competência este campo é alterado para F – Finalizadas).  
  
  
Empréstimo de Férias  
É habilitando conforme parametrização existente em [Configurações | Parametrizador | Férias | Empréstimo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719223). Com isso, o processo de cálculo das férias passa a guardar no recibo de férias o histórico dos empréstimos descontados, para controlar empréstimos com eventos iguais, e em caso de descontar em folha no mesmo mês em que já foi descontado nas férias partidas.

Observação:

O empréstimo na modalidade "Crédito do trabalhador e-Social" não será descontado nas férias.  Após o lançamento das férias no envelope de pagamento o usuário deve lançar o grupo de eventos para o desconto do empréstimo dessa modalidade.

Outros Períodos de Gozo  
São apresentados todos os períodos de gozo cadastrados para o período aquisitivo selecionado.  
  
  
Antecipação de Férias  
Quando nos parâmetros de férias do Sindicato o parâmetro 'Permite antecipação de dias de férias do próximo período aquisitivo' está marcado são antecipados dias de férias do próximo período aquisitivo caso o funcionário não tenha saldo suficiente para total de dias de férias.  
Veja mais detalhes no help do Sindicato.  
  
  
Anexo Adicionais de Férias  
Cadastrar os adicionais de férias que serão lançados no recibo.  
Sendo obrigatório informar Evento do Recibo e Evento da folha, os demais são opcionais.  
  
Os eventos adicionais de férias podem ser cadastrados como globais no Parametrizador | Férias | Eventos Adicionais Globais. Estes são lançados para todos os funcionários que obedecerem à fórmula de seleção.

Integração com o TSA / Suricato - Envio do Afastamento

Caso o produto RM esteja configurado para integrar com o TSA, segue as orientações listadas abaixo para alterações de períodos de férias:

No produto RM, a substituição ou alteração de um período de afastamento exige duas operações: Inclusão do novo período e Exclusão do período antigo.

Recomendamos as seguintes operações abaixo:

1. **Inclusão do Novo Período:** Abra a tela de Período de Gozo > Acesse a aba Identificação> pressione o botão  (**Incluir**) > cadastrar o novo período > pressione o botão **Salvar.**
2. **Exclusão do Período Antigo:** Abrir a tela de Período de Gozo> Acessar a aba Outros Períodos de Gozo> selecione o período a ser excluído> pressione o botão ❌(**Excluir**) > será exibida e tela de confirmação da operação> pressione o botão **Sim**.

Realizando essas duas operações uma por vez, não haverá duplicidade de períodos de afastamento no produto Suricato. Serão gerados os dois xml's necessários para efetivar a operação com sucesso.

Atenção

 Se existir informações de afastamento no Suricato que não estejam listadas na aba "Outros Períodos de Gozo" do produto RM, essas informações deverão ser excluídas manualmente do histórico de afastamento do produto Suricato.

|  |  |
| --- | --- |
|  | Informações Complementares |

**Importante:**Informações das Férias para o eSocial

[Exemplo Cálculo de INSS Férias de Múltiplos Vínculos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=556880081)

Local da Chamada Processo Visão de Funcionário | Férias Processo Visão de Funcionário | Período Aquisitivo
