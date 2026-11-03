---
content_hash: d8dcd7ae81b19ad78382b7e75f41ff1d96b9b9bed98d8c9cb0c2f5511821cffe
fetched_at: '2026-06-29T00:10:04.135422+00:00'
page_id: '452719201'
product: rm
source: tdn-rm
title: Resilição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719201
version: 3
---

**Campos para preenchimento da resilição**  
    
**ID**: Código identificador da resilição. Campo obrigatório com valor gerado automaticamente.  
   
**Data da Resilição**: Campo obrigatório para informar a data da resilição. A Data da Resilição não pode ser anterior à admissão do funcionário e deverá estar compreendida no mês de competência atual ou posterior.  
   
**Tipo da resilição**: Campo obrigatório para informar o tipo de resilição vinculado aos tipos de desligamento da rescisão. Este registro é cadastrado através do menu Folha de Pagamento | Rescisão | Resilição | Tipos de Resilição.  
   
**Data inicial do contrato**: Campo obrigatório para informar a data inicial do contrato de trabalho. A Data de Início do Contrato não pode ser anterior à admissão do funcionário.  
   
**Data Final do contrato**: Campo obrigatório para informar a data final do contrato de trabalho. A Data do Final do Contrato não pode ser anterior à Data da Resilição.  
   
**Grupo valores anteriores:**  
**Jornada:**Valor da jornada de trabalho do funcionário. Campo preenchido automaticamente.  
**Salário Hora:**Valor do salário hora do funcionário. Campo preenchido automaticamente.  
**Salário:**Valor calculado. Jornada x Salário hora do funcionário.  
   
**Grupo valores atuais:**  
**Jornada:**Campo para informar o valor da jornada atual. É a quantidade que será reduzida da jornada anterior e portanto não poderá ser informada uma jornada maior que a jornada anterior.  
**Salário Hora:**Valor do salário hora do funcionário, preenchido automaticamente.  
**Salário:**Valor calculado. Jornada x Salario hora do funcionário.  
   
**Grupo valores base para cálculo:**  
**Jornada:**Valor calculado. Jornada anterior – Jornada atual. Este valor servirá de base para o cálculo da resilição.  
**Salário Hora:**Valor do salário hora do funcionário, preenchido automaticamente.  
**Salário:**Valor calculado. Jornada x Salário hora do funcionário. É o valor do salário do funcionário após a redução da jornada de trabalho. Este valor servirá de base para o cálculo da resilição.  
   
**Motivo de mudança salarial**: Campo para informar o motivo de mudança salarial do funcionário. Obrigatório para habilitar o Lançamento da Resilição.  
   
**Restrições de cadastro e cálculo da resilição**  
   
As seguintes validações serão realizadas visando garantir a integridade do cadastro e cálculo da resilição. As restrições a seguir impedem ou impactam em um novo cadastro ou cálculo de uma resilição:  
1.     Funcionário com rescisão calculada.  
2.     Funcionário sem salário base  
3.     Funcionário com resilição pendente de lançamento  
4.     Funcionário com férias calculadas no período que compreende o mês de competência atual. Neste caso, o lançamento das férias deverá ser realizado para que o cálculo da resilição seja efetuado.  
5.     Funcionário com férias calculadas no período que compreende o mês posterior da competência atual. Neste caso, após efetuar o cálculo da resilição, as férias deverão ser recalculadas após a redução salarial.  
Para atender as particularidades de cada convenção coletiva, o sistema deve permitir a customização do cálculo. Diante desta necessidade, o cálculo da Resilição será realizado em 3 passos:

**1º - Cálculo da movimentação base**: O sistema irá calcular uma rescisão para o funcionário, usando como remuneração base o valor da redução da jornada.

**2º - Tratamento da movimentação base:** O sistema irá fazer o tratamento da movimentação calculada no 1º passo de acordo com a parametrização definida pelo usuário no tipo da Resilição.

**3º - Pagamento da Resilição**: Fazer o lançamento da Resilição para o envelope de pagamento  
   
A resilição parcial é efetuada quando se tem a redução da carga horaria do professor.  
O cálculo é realizado tomando por base a redução da Jornada, isto é:  
Se um professor tinha uma carga horária de 100 horas e a mesma teve redução para 70 horas, o cálculo da resilição terá como remuneração base o valor referente a jornada de 30 horas.  
    
**Casos mais comuns de resilição**

* **Término na data exata de sua extinção**
* **Término antecipado por iniciativa da empresa**
* **Termino antecipado por iniciativa do professor**

**Tipos de Resilição**  
Para informar o tipo de resilição cadastrado em Rescisão | Resilição | Tipos de Resilição.  
   
**Funcionário sem salário composto**:  informar o valor da nova jornada do funcionário e o sistema irá calcular os valores base para o cálculo da resilição. Ao fazer o lançamento o sistema irá atualizar a jornada e o salário no cadastro do funcionário e criar um novo registro no Histórico de Salário.  
   
**Funcionário com salário composto**:  informar o valor da nova jornada do funcionário para cada salário composto e o sistema irá calcular os valores base para o cálculo da resilição. Ao fazer o lançamento o sistema irá atualizar a jornada e o salário no cadastro do funcionário, o salário composto e criar um novo registro no Histórico de Salário.  
   
O botão para cálculo da resilição ficará habilitado após salvar a resilição e se a data da resilição estiver na competência atual ou posterior. E os botões para lançamento e visualização da movimentação ficarão habilitados após o cálculo da resilição.

* **Botão Calcular:**

O Cálculo da Resilição é feito de acordo com a parametrização de eventos do **Tipo de Resilição**. O sistema só irá calcular os eventos que forem configurados pelo usuário no **Tipo da Resilição**.  
São calculadas também as **Verbas Rescisórias** padrões para consulta.  
Após a execução do Cálculo o botão será bloqueado, e será habilitado os botões de **Lançar** e **Visualizar**. Caso queira recalcular é só selecionar a opção 'Habilitar recálculo da resilição', que o botão ficará ativo novamente para o recálculo.  
Referência Tipo Resilição está em Rescisão | Tipos de Resilição.

* **Botão Lançar:**

O processo de Lançamento da Resilição irá lançar todos os eventos existentes no Recibo para o envelope da movimentação, e executar a alteração salarial do funcionário para os novos valores informados no grupo "Valores Atuais" do cadastro da resilição, criando um registro no anexo de Histórico Salarial.  
Para a execução do Lançamento é obrigatório antes informar no Parametrizador, pasta Rescisão/Líquido de Rescisão, o evento para desconto do líquido da resilição.  
Neste processo será analisado se houve os descontos dos encargos, INSS e IRRF, no recibo da resilição. Caso tenha sido configurado para que esses descontos não ocorram no recibo, os eventos de INSS e IRRF serão lançados automaticamente no envelope da movimentação.  
Os valores do recibo serão lançados considerando os eventos cadastrados como "Evento Folha" no módulo de **Tipo de Resilição**.  
**Observação:** Ao realizar o lançamento da resilição que possua salário composto, serão atualizados o cadastro de salário composto, histórico salarial e o salário e jornada do cadastro de funcionário.

* **Botão Visualizar:**

Na visualização temos duas abas principais, **Movimentação** e **Verbas Rescisórias Resilição**.  
Na aba **Movimentação** é possível ver o **Recibo** e as **Bases**.  
**Recibo:** Mostra os eventos calculados relacionados aos eventos da parametrização do **Tipo de Resilição**.  
Temos 3 campos informativos:  
**Tipo Recebimento:** Forma de trabalho do funcionário (Horista, diarista, mensalista, ...).  
**Admissão:** Data de admissão do funcionário.  
**Salário Resilição:** O valor de referência para o cálculo da resilição, que é a diferença entre o salário antigo e o salário novo.  
   
No recibo também é possível editar e excluir os eventos existentes ou até inserir novos eventos com seus valores.  
Os eventos do recibo são divididos em 3 cores diferentes:  
**Azul:** Proventos  
**Vermelho:** Descontos  
**Verde:** Bases de Cálculo  
   
**Bases:** Mostra as bases de cálculo para INSS, FGTS e IRRF.  
**Atenção I:**  
Se não tiver nenhum evento da parametrização no **Tipo de Resilição**, o **Recibo** ficará vazio.  
Na aba **Verbas Rescisórias Resilição** tem todas os eventos para base de cálculo, mas é somente para consulta, caso queira colocar no **Recibo** posteriormente.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários
