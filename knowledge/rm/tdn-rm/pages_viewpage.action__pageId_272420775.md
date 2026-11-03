---
content_hash: 63fcf15fd7e26ed63972427b61c74fc66a19aaacd165524714ed8d7af27039b2
fetched_at: '2026-06-29T00:08:30.301473+00:00'
page_id: '272420775'
product: rm
source: tdn-rm
title: Parametrização para cálculo de Pensão Alimentícia no RM Labore
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272420775
version: 3
---

**Produto:** TOTVS Folha de Pagamento **Versão:** 12.1  
**Processo de Negocio:** Folha de Pagamento  
**Processo do Sistema:** Pensão Alimentícia

**Procedimento**

Como parametrizar o sistema para cálculo da Pensão Alimentícia:

**1º Passo:**

Acessar  "Cadastros | Eventos".

Verificar se já existem os eventos de pensão alimentícia como descrito abaixo.

Código de cálculo 13 - Pensão Alimentícia - Desconto do tipo valor.  
Código de cálculo 113 - Pensão Alimentícia nas Férias - Desconto do tipo valor.  
Código de cálculo 120 - Pensão Alimentícia na 2ª parcela de 13º salário- Desconto do tipo valor.  
Código de cálculo 121 - Pensão Alimentícia sobre participação nos lucros - Desconto do tipo valor.  
Caso não existam os eventos com as especificações acima cadastre dos mesmos.  
 

**2º Passo:**

Marcar "Incidências de pensão" em cada evento que será considerado para determinado  
cálculo da pensão alimentícia.

Exemplo:

Evento com Código de Calculo 2 - Dias trabalhados incidirá para cálculo de pensão na folha então  
deverá marcar na opção "Incidências de pensão" o item "Folha".

**Dica:**  
O evento com Código de Calculo 38 – Férias incidirá para cálculo de pensão nas férias então deverá  
marcar em "Incidências de pensão" o item "Férias".

**3º Passo:**

Acessar  "Cadastros | Tabelas Dinâmicas"

Na tabela dinâmica "INT42" (Tipo de Código fixo) cadastrar a opções de Tipos de Códigos Fixos que  
poderão ser utilizados para desconto da Pensão. Ex: 13º Salário, Rescisão.

**Dica:** Caso estes já existam não é necessário cria-los novamente.

**4º Passo:**

Acessar  "Parametrizador | 06.01.05 - 13º Salário"

Na Etapa 2  "Códigos fixos" marcar o tipo de código fixo criado no passo anterior.

**5º Passo:**

Marcar em " | Parametrizador | 06.01.06 - Rescisão | códigos Fixos ", e  
marcar o tipo de código fixo relacionado a pensão.

 

**6º Passo:**

Acesse o cadastro do funcionário que vai efetuar pagamento de pensão e localize a pasta  
"Dependentes". Edite o cadastro do dependente e na pasta "Incidências" marque  
a incidência de Pensão.

**7º Passo:**

Acesse no mesmo cadastro do dependente a pasta "Dados da pensão". Nesta pasta você  
vai informar a forma como o sistema deve calcular a pensão.

1 - Informe no campo "Percentual" o percentual da pensão.  
2 - Caso algum valor deva ser somado ao cálculo da pensão informe a fórmula com este valor no  
campo "Fórmula adicional de pensão".  
3 - Marque o campo "Ordenado Bruto" caso o queira considerar como base de calculo da pensão  
o valor bruto do salário do funcionário, caso o parâmetro fique desmarcado o sistema ira  
considerar o valor liquido do salário do funcionário.

**8º Passo:**

Caso exista algum evento que não deva ser considerado no cálculo da pensão informe  
este evento na pasta " Dependentes | Anexos | Eventos não considerados Para Pensão".

**9 º Passo:**

Acesse o cadastro do funcionário que vai efetuar pagamento de pensão e localize a pasta  
"Informações Para o Cálculo | Códigos Fixos". Cadastre os eventos com Código de Cálculo 13 como Código Fixo  
Tipo Folha ou Folha/Rescisão (caso deseje descontar a pensão também na rescisão) e Código de  
Cálculo 120 como Código Fixo Tipo 13ª Salário.

**10 º Passo:**

Acesse: Folha Mensal | Lançamentos  | Grupo de  
Eventos.

Edite um Grupo de Eventos e na pasta Códigos Fixos marque o Código Fixo Folha utilizado no 9º  
Passo, para que o evento Código de Cálculo 13 seja lançado no Envelope de Pagamento do  
funcionário.

Ao realizar o lançamento do Grupo de Eventos marque na pasta Identificação marque a opção  
“Lança Codigos Fixos”, salve as alterações e faça o lançamento.

**11 º Passo:**

Caso deseje descontar Pensão nas Férias, cadastre o evento de CC 113 - Pensão  
alimentícia nas férias em Administração de Pessoal | Cadastros | Funcionários | Férias | Anexos | Adicionais Férias.

Dica: Para que o calculo seja feito de forma correta é importante que o Evento do Recibo seja diferente do Evento da Folha. 

Ao lançar as férias será calculado o valor da pensão alimentícia nas férias, conforme  
parametrização do 7ª Passo.

**12 º Passo:**

Ao lançar a rescisão marque a opção de lançar códigos fixos e será lançado, conforme parametrização do 7ª Passo a pensão alimentícia que estiver marcada para lançar em rescisão, caso não esteja cadastrado em código fixo para lançamento em rescisão o usuário deverá lançar manualmente todos os eventos de CC 13 - Pensão alimentícia, CC 319 - Pensão alimentícia nas férias na rescisão, CC 120 - Pensão alimentícia s/ 13º salário e/ou CC 121 - Pensão alimentícia s/ participação nos lucros.

**13 º Passo:**

Ao lançar o 13º salário marque a opção lançar códigos fixos e será lançado, conforme parametrização do 7ª Passo a pensão alimentícia sobre o 13º salário.

Observação: Para que o sistema calcule a pensão alimentícia sobre a 1ª parcela de 13º salário nas férias é necessário informar o evento com CC(120) – Pensão Alimentícia de 13º salário no campo Evento adicional de Férias.

Este evento não poderá estar informado nos Eventos Adicionais Globais de 13º Salário.
