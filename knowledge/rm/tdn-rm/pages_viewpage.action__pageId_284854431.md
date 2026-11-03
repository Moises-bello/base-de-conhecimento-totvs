---
content_hash: 5ac794cd1faa57218b8126762800c57c0f4343a222f159683af03c372172657e
fetched_at: '2026-06-29T00:08:36.911400+00:00'
page_id: '284854431'
product: rm
source: tdn-rm
title: DT Resilição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284854431
version: 103
---

# Resilição

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| **Segmento Executor:** | Recursos Humanos | | |
| **Módulo:** | TOTVS Folha de Pagamento | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Resilição | Resilição | | | |
| **País:** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

# Contexto de negócio

A resilição parcial é efetuada quando se tem a redução da carga horaria.

O cálculo é realizado tomando por base a redução da Jornada.

**Exemplo:**

Se um professor tinha uma carga horária de 100 horas e a mesma teve redução para 70 horas, o cálculo da resilição terá como remuneração base o valor referente a jornada de 30 horas.

**Casos mais comuns de resilição**

* **Término na data exata de sua extinção**
* **Término antecipado por iniciativa da empresa**
* **Termino antecipado por iniciativa do professor**

# Detalhamento do Processo

## Parametrização

Em **Rescisão | Resilição | Tipos de Resilição** deve-se cadastrar os Tipos de Resilição e suas particularidades para o cálculo, vinculando aos Tipos de Desligamento da Rescisão.

São solicitadas informações que serão importantes para o cálculo da resilição como o tipo de Demissão que só será possível informar os tipos: 2 - Inic.Empregador sem justa causa, 4 - Inic.Empregado sem justa causa e T - Término de contrato de trabalho.

Na Parametrização dos eventos permitirá customizações no cálculo da resilição para atender a diversas particularidades das convenções coletivas. Somente os eventos incluídos neste cadastro serão considerados no cálculo do recibo da resilição parcial. Neste módulo o usuário selecionará quais verbas rescisórias deverão entrar ou não no processo de resilição, bem como acrescentar novos eventos adicionais à execução.

No caso de eventos que não constam no grupo de verbas rescisórias calculadas pelo sistema, este será adicionado ao recibo da resilição.

Para os casos de alteração de valor do evento, no cadastro do evento da parametrização de eventos é permitido inserir uma fórmula para alterar o valor calculado para o evento.

É obrigatório a informação de um evento a ser lançado no envelope da movimentação. Sendo que, o evento informando no campo Código do Evento Folha deve ter o mesmo código de cálculo do evento informado no campo Código de Evento.

Há uma particularidade para os códigos de cálculo 1, 2, 3 e 4, onde o evento informado no campo Código do Evento Folha não pode ser o mesmo do campo Código do Evento, porém deve possuir o mesmo código de cálculo. Para os demais códigos de cálculo, pode ser informado ou não o mesmo evento em ambos os campos, ficando opcional ao usuário.

## Cadastros/Processos

Em Administração de Pessoal | Funcionários | Anexos | Movimento | Resilição deverão ser cadastradas as informações para cadastro, cálculo e lançamento da resilição considerando a parametrização do tipo de resilição cadastrado anteriormente.

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

O Cálculo da Resilição é feito de acordo com a parametrização de eventos do **Tipo de Resilição**. O sistema só calculará os eventos que forem configurados pelo usuário no **Tipo da Resilição**.

São calculadas também as **Verbas Rescisórias** padrões para consulta.

O processo de Lançamento da Resilição lançará todos os eventos existentes no Recibo para o envelope da movimentação, e executará a alteração salarial do funcionário para os novos valores informados no grupo “Valores Atuais” do cadastro da resilição, criando um registro no anexo de Histórico Salarial.

**Atenção:** para a execução do Lançamento é obrigatório antes informar no Parametrizador, pasta Rescisão/Líquido de Rescisão, o evento para desconto do líquido da resilição.

No processo de lançamento será analisado se houve os descontos dos encargos, INSS e IRRF, no recibo da resilição. Caso tenha sido configurado para que esses descontos não ocorram no recibo, os eventos de INSS e IRRF serão lançados automaticamente no envelope da movimentação.

Os valores do recibo serão lançados considerando os eventos cadastrados como “Evento Folha” no módulo de **Tipo de Resilição**.

Na visualização temos duas abas principais, **Movimentação** e **Verbas Rescisórias Resilição**.

Na aba **Movimentação** é possível ver o **Recibo** e as **Bases**.

## Termo de Resilição

Após todos os cálculos e lançamentos, deverá emitir o **Termo de Resilição** que foi desenvolvido baseado no termo de quitação de Rescisão do Contrato de Trabalho (TRCT), pois, não existe uma legislação própria para o modelo.

Através do módulo TOTVS Folha de Pagamento será gerado para os funcionários o termo de resilição para funcionários com Resilição Calculada.

O termo disponível no TOTVS Folha de Pagamento é aceito e homologado pelos sindicatos do Brasil.

O Módulo de geração do Termo de Resilição funcionará com a utilização do mesmo relatório da rescisão “FOPREL0001 - Termo de Rescisão - Portaria 16212010 V. 12.1.TotvsReport”, que deverá estar importado na base de dados. O relatório estará disponível na pasta "Objetos Gerenciais" no local de instalação do sistema.

divs
