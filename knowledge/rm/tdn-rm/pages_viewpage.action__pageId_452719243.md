---
content_hash: 5e79fe2325127df2252eeda78253af0ceae8414db327dc56b94c4963c31aee1b
fetched_at: '2026-06-29T00:10:04.742282+00:00'
page_id: '452719243'
product: rm
source: tdn-rm
title: TRCT de Resilição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719243
version: 9
---

O Termo de Resilição foi desenvolvido baseado no termo de quitação de Rescisão do Contrato de Trabalho (TRCT), pois, não existe uma legislação própria para o modelo.   
Este termo é aceito e homologado pelos sindicatos do Brasil.

Através do módulo TOTVS Folha de Pagamento será gerado para os funcionários o termo de resilição para funcionários com Resilição Calculada.

Ao iniciar a parametrização do processo de geração do Termo de Resilição, poderá ser gravado um Perfil de Parâmetros para que todos os parâmetros definidos fiquem "salvos" para futuras gerações do relatório caso seja necessário gerar mais de uma vez ou caso seja reutilizada a mesma parametrização para outro funcionário.

Para gravar o perfil, na primeira tela do wizard deverá inserir uma descrição no campo "Perfil de Parâmetros" e clicar no Box "Salvar perfil ao concluir".

Se desejar, poderá informar uma Descrição do Processo, para que no histórico de processos executados seja identificado com a descrição.

Na geração do Termo de Resilição deverá definir a **Quebra de seção** e a grade de **Seleção de Funcionários**. Esta parametrização servirá como filtro, ou seja, serão gerados Termo Resilição cujas seções dos funcionários correspondam à quebra informada e os funcionários tenham dados compatíveis com a grade de seleção definida.

As datas dos campos Início e Término do "Período de Resilição" são obrigatórias, e determinarão um intervalo para que somente funcionários com resilição calculada dentre o intervalo, tenham o Termo de Resilição gerado.

O Módulo de geração do Termo de Resilição funcionará com a utilização do mesmo relatório da rescisão "**FOPREL0001 - Termo de Rescisão - Portaria 16212010 V. 12.1.TotvsReport**", que deverá estar importado na base de dados.

 No campo "Código do Relatório" deverá ser referenciado o relatório padrão do Termo de Resilição. Caso necessite importar no RM Reports o relatório do Termo de Resilição, proceda os passos:   
1)      Acesse Aba **Gestão | RM Reports**;  
2)      Acesse **Processos | Importar Estrutura de Relatório**;  
3)      Localize na sua máquina o arquivo do relatório e conclua a importação;

**Observação:** O relatório estará disponível na pasta "**Objetos Gerenciais**" no local de instalação do sistema.

**Atenção:** Emitir o relatório após lançamento da resilição para o envelope do funcionário.

No campo "**Fórmula para Saldo de Salário (Campo 50)**" deverá referenciar uma fórmula que tenha como retorno o valor do "Saldo de Salário Líquido" pago na resilição.

**Observação**

É necessário informar a fórmula para cálculo do Campo 50, porque não existem rubricas padrão pré-definidas pelo MTE para representar Faltas, DSR Perdido, Reflexo de DSR Perdido e etc.

Exemplificamos abaixo uma estrutura de fórmula a ser utilizada:

**(MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0001') + MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0002')) - (MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0008') + MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0182') + MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0070'))**

Detalhando a fórmula, temos:

**MV** = função de fórmula que retornará o valor de um evento. Os parâmetros desta função são: Mês Competência, Ano Competência, Código do Evento.  
**PARMQRY('MESCOMP')**, retornará o mês competência informado na geração do Termo de Resilição.  
**PARMQRY('ANOCOMP')**, retornará o ano competência informado na geração do Termo de Resilição.  
**'0001'** é o código do evento Horas Normais, da base exemplo.

Para obtenção do "Saldo de Salário Líquido" a fórmula utilizada na base exemplo considerou:

Para a **soma**, os valores dos eventos:   
0001 – Horas Normais  
0002 – Dias Trabalhados

Para **subtração**, os valores dos eventos:  
0008 – Faltas  
0182 – Horas de Faltas (atraso)  
0070 – DSR Perdido

**Observação**  
A fórmula acima contempla o cálculo de Saldo de Salário da base Exemplo. Desta forma o usuário deverá verificar os códigos de eventos a considerar no cálculo do Líquido Salarial pago na Resilição e adequar à fórmula.

No TOTVS Folha de Pagamento, o Termo de Resilição será gerado a partir das referências das Rubricas em cada campo correspondente, com exceção do campo 50 que como citado acima, é calculado por fórmula.

Nos cadastros dos eventos deverão existir as rubricas correspondentes a cada evento, sendo as rubricas pré-definidas pelo MTE que tem faixa de código 001 a 036, e as rubricas criadas pelo usuário a partir do número 100, de acordo com a necessidade.

As rubricas pré-definidas pelo MTE estão especificadas no manual 2.10 do Sistema HomologNet instituído pela Portaria Nº 1.620, de 14/07/2010, disponível no site do MTE.

O Cadastro de Rubricas no TOTVS Folha de Pagamento está localizado em Cadastros | Tabelas Dinâmicas | 'HOMOLOGRUB'. Nesta tabela poderá verificar as rubricas pré-definidas pelo MTE e cadastrar as rubricas que forem necessárias a partir do número 100.

Na geração do Termo de Resilição, para relacionar as rubricas aos campos correspondentes do relatório, marque o Box "**Alterar Rubricas**" e clique em "**Avançar**".

Será exibida a Tela "Edição das Rubricas", divididas em duas páginas Proventos e Desconto, com todos os campos do relatório que deverão ter relacionada sua respectiva rubrica.

Por existir rubricas pré-definidas pelo MTE, os campos de Rubricas para a geração do relatório Termo de Resilição  que são correspondentes as estas rubricas, estarão desabilitados.

Os campos desabilitados são: 51, 52, 53, 54, 55, 56, 57, 60, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93 e 98.

Os campos que não são correspondentes as rubricas pré-definidas pelo MTE, estarão habilitados e neles deverão ser informadas as rubricas correspondentes que foram cadastradas pelo usuário a partir do número 100.

**Observações**   
1)   A associação de rubricas aos eventos que são utilizados no sistema para movimentação da Folha de Pagamento é de responsabilidade do usuário.  
2)   Os campos de Rubricas habilitados na geração Termo de Resilição que devem ter Rubricas relacionadas, serão os campos que o usuário verificará que existem eventos pagos na movimentação da resilição sendo de responsabilidade do usuário identificar qual rubrica deverá estar relacionada aos eventos e qual rubrica referenciar aos campos.

Na tela de Parametrização de Geração do Termo de Resilição existe o parâmetro "**Imprimir verbas rescisórias pré-definidas**". Este parâmetro quando marcado, imprimirá todos os campos de verbas rescisórias que estão definidos no Anexo I, da Portaria Nº1.621 de 14/07/2010, mesmo que algum tenha valor igual zero. Neste caso ainda há a possiblidade escolher se imprime com valor **zerado** ou **em branco**.

Com o parâmetro desmarcado, serão impressos os campos definidos no Anexo I, que o valor for maior que zero.

Quando algum campo de Rubrica poderá apresentar valor igual zero?

1)   Campos de Rubricas do Termo de Resilição que têm código de Rubrica associado, mas na movimentação de Resilição não existe evento que possua a rubrica associada, serão gerados no Termo de Resilição com valor zerado.   
2)   Campos que não possuem código de Rubrica relacionada serão gerados com valor zerado.   
3)   Evento lançado na movimentação de rescisão com valor zero, mesmo que exista código de rubrica relacionado ao campo correspondente, fará com que o campo seja gerado com valor zero.

**Exemplo:**

A resilição parcial é efetuada quando se tem a redução da carga horaria.

O cálculo é realizado tomando por base a redução da Jornada.

Se um professor tinha uma carga horária de 100 horas e a mesma teve redução para 70 horas, o cálculo da resilição terá como remuneração base o valor referente a jornada de 30 horas.

**Casos mais comuns de resilição**

* **Término na data exata de sua extinção**
* **Término antecipado por iniciativa da empresa**
* **Termino antecipado por iniciativa do professor**

## **Parametrização**

Em **Rescisão | Resilição | Tipos de Resilição** deve-se cadastrar os Tipos de Resilição e suas particularidades para o cálculo, vinculando aos Tipos de Desligamento da Rescisão.

São solicitadas informações que serão importantes para o cálculo da resilição como o tipo de Demissão que só será possível informar os tipos: **2 - Inic. Empregador sem justa causa**, **4 - Inic. Empregado sem justa causa** e **T - Término de contrato de trabalho**.

Na Parametrização dos eventos permitirá customizações no cálculo da resilição para atender a diversas particularidades das convenções coletivas. Somente os eventos incluídos neste cadastro serão considerados no cálculo do recibo da resilição parcial. Neste módulo o usuário selecionará quais verbas rescisórias deverão entrar ou não no processo de resilição, bem como acrescentar novos eventos adicionais à execução.

No caso de eventos que não constam no grupo de verbas rescisórias calculadas pelo sistema, este será adicionado ao recibo da resilição.

Para os casos de alteração de valor do evento, no cadastro do evento da parametrização de eventos é permitido inserir uma fórmula para alterar o valor calculado para o evento.

É obrigatório a informação de um evento a ser lançado no envelope da movimentação. Sendo que, o evento informando no campo Código do Evento Folha deve ter o mesmo código de cálculo do evento informado no campo Código de Evento.

Há uma particularidade para os códigos de cálculo 1, 2, 3 e 4, onde o evento informado no campo Código do Evento Folha não pode ser o mesmo do campo Código do Evento, porém deve possuir o mesmo código de cálculo. Para os demais códigos de cálculo, pode ser informado ou não o mesmo evento em ambos os campos, ficando opcional ao usuário.

## **Cadastros/Processos**

Em **Administração de Pessoal | Funcionários | Anexos | Movimento | Resilição** deverão ser cadastradas as informações para cadastro, cálculo e lançamento da resilição considerando a parametrização do tipo de resilição cadastrado anteriormente.

A Data da Resilição não pode ser anterior à admissão do funcionário e deverá estar compreendida no mês de competência atual ou posterior.

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

Possibilidade de cálculo da resilição:

**Funcionário sem salário composto**:  informar o valor da nova jornada do funcionário e o sistema calculará os valores base para o cálculo da resilição. Ao fazer o lançamento o sistema irá atualizar a jornada e o salário no cadastro do funcionário e criar um novo registro no Histórico de Salário.

O botão para cálculo da resilição ficará habilitado após salvar a resilição e se a data da resilição estiver na competência atual ou posterior. E os botões para lançamento e visualização da movimentação ficarão habilitados após o cálculo da resilição.

O Cálculo da Resilição é feito de acordo com a parametrização de eventos do **Tipo de Resilição**. O sistema só calculará os eventos que forem configurados pelo usuário no **Tipo da Resilição**.

São calculadas também as **Verbas Rescisórias** padrões para consulta.

O processo de Lançamento da Resilição lançará todos os eventos existentes no Recibo para o envelope da movimentação, e executará a alteração salarial do funcionário para os novos valores informados no grupo “Valores Atuais” do cadastro da resilição, criando um registro no anexo de Histórico Salarial.

**Atenção:**para a execução do Lançamento é obrigatório antes informar no Parametrizador, pasta Rescisão/Líquido de Rescisão, o evento para desconto do líquido da resilição.

No processo de lançamento será analisado se houve os descontos dos encargos, INSS e IRRF, no recibo da resilição. Caso tenha sido configurado para que esses descontos não ocorram no recibo, os eventos de INSS e IRRF serão lançados automaticamente no envelope da movimentação.

Os valores do recibo serão lançados considerando os eventos cadastrados como “Evento Folha” no módulo de **Tipo de Resilição**.

Na visualização temos duas abas principais, **Movimentação** e **Verbas Rescisórias Resilição**.

Na aba **Movimentação** é possível ver o **Recibo**e as**Bases**.

## **Termo de Resilição**

Após todos os cálculos e lançamentos, deverá emitir o **Termo de Resilição** que foi desenvolvido baseado no termo de quitação de Rescisão do Contrato de Trabalho (TRCT), pois, não existe uma legislação própria para o modelo.

Através do módulo TOTVS Folha de Pagamento será gerado para os funcionários o termo de resilição para funcionários com Resilição Calculada.

O termo disponível no TOTVS Folha de Pagamento é aceito e homologado pelos sindicatos do Brasil.

O Módulo de geração do Termo de Resilição funcionará com a utilização do mesmo relatório da rescisão “**FOPREL0001 - Termo de Rescisão - Portaria 16212010 V. 12.1.TotvsReport**”, que deverá estar importado na base de dados. O relatório estará disponível na pasta "**Objetos Gerenciais**" no local de instalação do sistema.

**Tela de geração do TRCT de Resilição:**

a) Emitir Termo de Quitação/Homologação - **De acordo com o tempo de casa**;

Marcando este parâmetro, serão gerados os termos de quitação e homologação, considerando o tempo de casa do funcionário.

b) Emitir Termo de Quitação/Homologação - **Somente o Termo de Quitação independente do tempo de casa**;

Marcando este parâmetro, será gerado somente o termo de quitação independente do tempo de casa do funcionário.

c) Emitir Termo de Quitação/Homologação - **Somente o Termo de Homologação independente do tempo de casa**;

Marcando este parâmetro, será gerado somente o termo de homologação independente do tempo de casa do funcionário.
