---
content_hash: b032f1ff22749b245a3b6fbc297bf4cf30452ce33999d41d964dc2fe864796f8
fetched_at: '2026-06-29T00:10:04.675932+00:00'
page_id: '452719231'
product: rm
source: tdn-rm
title: Controle de Lotação - Por Vagas e Verbas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719231
version: 3
---

**Controle de Lotação - Por Vagas e Verbas**   
   
**Controle de Lotação| Vagas**

Este controle é baseado na quantidade de Limite de Vagas definidas para preenchimento da lotação existente na empresa.

Tipo de Controle Sem Controle - Marcando este campo, ficará definido que não utiliza o Controle de Lotação por Vagas. Neste caso não será aplicado o controle de admissões e transferências de funcionários, podendo ser este processo realizado sem quaisquer restrições.

Seção Folha - Marcando este campo, somente poderão ser efetivadas admissões e transferências de funcionários, caso existam VAGAS, para a Seção em que os mesmos irão trabalhar.

**Observação:**

Ao realizar a admissão de um funcionário em uma dada seção, deverão existir vagas disponíveis na mesma, para efetuar esta contratação. Este controle é executado independente da função para qual o funcionário será admitido.

Seção em Qualquer Nível - Marcando este campo, somente poderão ser efetivadas admissões e transferências de funcionários, caso existam VAGAS, para o nível hierárquico da Seção em que os mesmos irão trabalhar.

**Exemplo:** Ao realizar a admissão de um funcionário para uma seção de código 01.01.002, e nesta não existir vagas disponíveis para serem preenchidas, será então verificado a existência de vagas em outras seções cadastradas como: na quebra do Departamento da Filial e da coligada conforme demonstrado:

Cód.Seção             Identificação da Seção    Limite Func.

0                             Totvs Ltda

100 01                    Filial SP

20 01.01                 Depo. Administrativo

10 01.01.001          Seção qualquer

5 01.01.002           Seção da admissão

0 01.01.003           Seção qualquer                             7

No exemplo citado, será permitida a admissão do funcionário na seção de código 01.01.002, para atender a Vaga disponível no departamento.

Função - Marcando este campo, somente poderão ser efetivadas admissões e transferências de funcionários, caso existam VAGAS, para a Função em que os mesmos irão trabalhar.

**Observação:**

Ao realizar a transferência de um funcionário para outra função, deverão existir vagas disponíveis para a função a qual o funcionário irá ser realocado. Este controle é executado independente da seção em que o mesmo se encontrar lotado.

Quadro de Lotação - Marcando este campo, deverá ser informada em cada função, as possíveis lotações da mesma.

Limite de Vaga na Contratação Nunca Excede - Após definir o Tipo de Controle a ser efetuado no quadro de Vagas, sendo este diferente de "Sem Controle", será bloqueada a contratação e/ou realocação de funcionários após atingir o limite de vaga informado.

Marcando este campo não será permitido realizar contratações e realocações após atingir o limite informado.

Excede Indefinidamente - Após definir o Tipo de Controle a ser efetuado no quadro de Vagas, sendo este diferente de "Sem Controle", será bloqueada a contratação e/ou realocação de funcionários após atingir o limite de vaga informado. Marcando este campo será permitido realizar contratações e realocações sem controle dos limites informados, definindo o preenchimento destas vagas como excedentes.

Excede Nº Afastados  - Após definir o Tipo de Controle a ser efetuado no quadro de Vagas, sendo este diferente de "Sem Controle", será bloqueada a contratação e/ou realocação de funcionários após atingir o limite de vaga informado. Marcando este campo será permitido realizar contratações e realocações acima dos limites informados, somente quando a pessoa ocupante da vaga for substituir outra pessoa que estiver com a situação permitida no item "Configurações".

**Controle de Lotação| Verba**

Este controle é baseado no recurso financeiro disponível para alocação de pessoas em Seções e Funções.

Tipo de Controle Sem Controle - Marcando este campo, ficará definido que não utiliza o Controle de Lotação por Verbas. Neste caso não será aplicado o controle de admissões e transferências de funcionários, podendo ser este processo realizado sem quaisquer restrições.

Seção Folha - Marcando este campo, somente poderão ser efetivadas admissões e transferências de funcionários, caso existam VERBAS, para a Seção em que os mesmos irão trabalhar.

**Observação:**

Ao realizar a admissão de um funcionário em uma dada seção, deverão existir verbas disponíveis na mesma, para efetuar esta contratação. Este controle é executado independente da função para qual o funcionário será admitido.

Seção em Qualquer Nível - Marcando este campo, somente poderão ser efetivadas admissões e transferências de funcionários, caso existam VERBAS, para o nível hierárquico da Seção em que os mesmos irão trabalhar.

**Exemplo:** Ao realizar a admissão de um funcionário para uma seção de código 01.01.002, e nesta não existir verbas disponíveis para serem preenchidas, será então verificado a existência de verbas em outras seções cadastradas como: na quebra do Departamento da Filial e da coligada conforme demonstrado:

Cód.Seção      Identificação da Seção      Limite Verba.  
0                     Totvs Ltda                          8500,00   
01                   Filial SP                              5000,00   
01.01              Depo. Administrativo         0,00   
01.01.001       Seção qualquer                  1.200,00  
01.01.002       Seção da admissão            0,00  
01.01.003       Seção qualquer                  2.400,00

No exemplo citado, será permitida a admissão do funcionário na seção de código 01.01.002, para atender a Verba disponível na filial.

Função Marcando este campo, somente poderão ser efetivadas admissões e transferências de funcionários, caso existam VERBAS, para a Função em que os mesmos irão trabalhar.

**Observação:**

Ao realizar a transferência de um funcionário para outra função, deverão existir verbas disponíveis para a função a qual o funcionário irá ser realocado. Este controle é executado independente da seção em que o mesmo se encontrar lotado.

Quadro de Lotação - Marcando este campo, deverão ser informadas em cada função, as possíveis verbas distribuídas nas lotações.

Limite de Vaga na Contratação Nunca Excede - Após definir o Tipo de Controle a ser efetuado no quadro de Verbas, sendo este diferente de "Sem Controle", será bloqueada a contratação e/ou realocação de funcionários após atingir o limite de verba informado.

Marcando este campo não será permitido realizar contratações e realocações após atingir o limite informado.

Excede Indefinidamente - Após definir o Tipo de Controle a ser efetuado no quadro de Verbas, sendo este diferente de "Sem Controle", será bloqueada a contratação e/ou realocação de funcionários após atingir o limite de verba informado.

Marcando este campo será permitido realizar contratações e realocações sem controle dos limites informados, definindo o preenchimento destas verbas como excedentes.

Excede Nº Afastados - Após definir o Tipo de Controle a ser efetuado no quadro de Verbas, sendo este diferente de "Sem Controle", será bloqueada a contratação e/ou realocação de funcionários após atingir o limite de verba informado.

Marcando este campo será permitido realizar contratações e realocações acima dos limites informados, somente quando a pessoa ocupante da vaga for substituir outra pessoa que estiver com a situação permitida no item "Configurações".

Parametrização Tipo Verba Por Valor - Considerando o tipo de controle desejado, deverão ser informados valores disponíveis para contratação e/ou realocação de pessoal, baseando-se nos salários dos funcionários.

**Exemplo:** Caso você defina o tipo de controle de verbas por SEÇÃO FOLHA e utilize este parâmetro, no cadastro de seções você informará o valor da verba disponível para contratação.

Por Percentual - Considerando o tipo de controle desejado, deverão ser informados percentuais disponíveis para contratação e/ou realocação de pessoal, baseando-se no valor da "Verba Geral" e nos salários dos funcionários.

**Exemplo:** Caso você defina o tipo de controle de verbas por FUNÇÃO e utilize este parâmetro, no cadastro de funções você informará o percentual aplicado na função em questão baseado na "Verba Geral" disponível.

Verba Geral - Caso a definição do Tipo de Verba seja por percentual, este campo é disponibilizado para que seja informado o Valor Geral da Verba, onde serão aplicados os percentuais definidos conforme o tipo de controle desejado.

**Exemplo:**

Valor da Verba            100.000,00

Tipo de Controle          Por seção

Tipo de Verba             Por Percentual/Utilização

Seção                         01.01

% Limite                     15

Valor total disponibilizado para alocação de pessoal na seção, a partir da soma dos salários alocados na mesma: R$ 15.000,00

**Controle de Lotação| Configurações**

Campo para definição de quais situações serão consideradas como afastamento no Controle de Lotação, sendo este por Vaga e/ou Verba.
