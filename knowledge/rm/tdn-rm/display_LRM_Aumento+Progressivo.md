---
content_hash: 3d7b38149054af5ead4409a9d7a0077b7afd68fe31193b7c1685100fa6ed364d
fetched_at: '2026-06-29T00:10:03.728473+00:00'
page_id: '452719149'
product: rm
source: tdn-rm
title: Aumento Progressivo
type: documentation
url: https://tdn.totvs.com/display/LRM/Aumento+Progressivo
version: 6
---

**Aumento Progressivo**

---

O Aumento progressivo é um complemento das requisições de "Alteração de dados funcionais" e "Transferência com alteração de dados funcionais" que permite programar mudanças (salário, seção e função) para o funcionário de acordo com algumas validações pré-estabelecidas pelo usuário por meio dos Tipos de Requisição.

**Por que utilizar aumento progressivo?**

Citaremos duas situações onde o usuário pode utilizar a funcionalidade de aumento progressivo:

Suponhamos que uma empresa só permita 10% de aumento a cada trimestre.

Neste caso devemos criar uma parametrização que atenda a essa regra da empresa, ficaria assim:

Parametrização:

Aumento máximo sobre salário: 10%.......Ação: Bloquear

Tempo mínimo entre aumentos: 90 dias....Ação: Bloquear

Permitir progressão: Marcado.

Parametrização aplicada para todas as filiais e todos os motivos.

Com a parametrização criada, temos as seguintes situações:

* Para cobrir uma proposta que o funcionário recebeu de uma outra empresa foi aprovado um aumento de 70%.

*-Neste caso o usuário poderá cadastrar uma requisição com 70% de aumento para o funcionário, como o limite da empresa é de 10%, o sistema irá bloquear e sugerir uma progressão, se o usuário aceitar ele criará as progressões até chegar no valor desejado respeitando as regras da empresa, se ele não aceitar o sistema cancela o cadastro da requisição.*

*Obs.: Talvez o sistema não consiga alcançar o valor solicitado por causa das regras cadastradas na parametrização, mas ele tenta aproximar ao máximo do valor desejado.*

*(Exemplo de progressões geradas automaticamente)*

* Salário do funcionário está defasado com relação aos outros funcionários da empresa, seria necessário 20% de aumento para ajustar o salário e mudar a função que já não existe mais.

*-Neste caso o usuário poderá cadastrar 1 requisição que contenha 2 progressões, onde uma contenha só o aumento de salário e a outra contenha o restante do aumento e a mudança de função.*

*(exemplo de progressão cadastrada manualmente, mas poderia ter sido gerada automaticamente também)*

**Como utilizar o aumento progressivo?**

Para utilizar o aumento progressivo o usuário deverá habilitar as visões no sistema e realizar o cadastro da parametrização e das progressões.

**Parametrização**: São regras que o usuário define para a criação das progressões. Essas regras podem ser aplicadas a filiais e motivos de alteração específicos no sistema.   
Para mais informações sobre parametrização clique no link no final da pagina.  
   
**Progressões**: São criadas dentro das requisições e nelas contém os dados do funcionário que serão alterados.  
As progressões podem ser criadas automaticamente pelo sistema quando o usuário tenta abrir uma requisição que seja maior que o permitido pela parametrização, neste caso, o sistema sugere a progressão.   
   
**Trabalhando com progressões**

Ao inserir uma requisição o sistema irá verificar se existe alguma parametrização para aquela filial e motivo, caso exista, serão verificadas as validações cadastradas e se a opção "permite progressão" está marcada.  
   
**Observação:**

A transferência entre filiais não permite a inclusão de progressões, ou seja, o sistema não sugere progressão e não permite que insira a mesma manualmente.   
Se o sistema identificar que alguma informação não foi atendida de acordo com as regras cadastradas no parâmetro, ele tentará criar progressões para que seja alcançado o valor informado pelo usuário obedecendo as regras.

Caso não consiga alcançar o valor será exibida uma mensagem de alerta ao usuário informando o ocorrido e exibindo ou não o valor máximo atingido pelo sistema.

Exemplo: Foi parametrizado as regras abaixo:

* Percentual máximo sobre o salário: 10% --- Bloquear.
* Prazo mínimo entre aumento: 180 dias (6 meses). -- Bloquear.
* Permite progressão? – Marcado.

Se for cadastrado uma requisição de 100% de aumento sobre o salário o sistema não irá permitir o cadastro, mas será sugerido progressões respeitando as regras. Ficaria da seguinte forma:

• 10 Progressões de 10% com data de efetivação com 6 meses de diferença.

**Progressões lançadas manualmente**

O usuário poderá remover as progressões criadas pelo sistema e lançar manualmente conforme desejar, mas as regras cadastradas na parametrização continuarão valendo. Também será possível editar as progressões.

**TABELAS SALARIAIS**

Se o sistema estiver com o parâmetro "Considerar os salários das tabelas salariais" marcado, ao gerar a progressão será considerado um valor que atenda os parâmetros configurados para a progressão e que exista na tabela. Existe a possibilidade da progressão não atingir o valor do salário proposto, mas será informado ao usuário por uma mensagem de alerta o resultado da progressão.

  Exemplo: Funcionário com salário atual de R$1.000, e foi criada uma requisição para alterar o salário para R$6.000. Na parametrização da progressão foi definido o percentual máximo de aumento de 50%.

Utilizando a tabela salarial abaixo como exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Inicial | Faixa B | Faixa C | Faixa D |
| Nível 1 | 1.000 | 1.500 | 2.000 | 2.500 |
| Nível 2 | 3.000 | 5.000 | 6.000 | 7.000 |

O sistema irá gerar as seguintes progressões:

* 1ª Progressão: Salário R$1.500. (Percentual de aumento sobre o salário: 50%)
* 2ª Progressão: Salário R$2.000. (Percentual de aumento sobre o salário: 33%)
* 3ª Progressão: Salário R$3.000. (Percentual de aumento sobre o salário: 50%)
* Fim da progressão. Não atingiu o valor de 6000, somente 3000.

**Explicação**:

O sistema calcula a porcentagem do salário atual e do próximo salário da tabela, essa porcentagem não pode ultrapassar o valor máximo parametrizado (50%).

Nesse momento ele gera a 1ª Progressão,

Em seguida ele repete o mesmo processo até chegar no valor desejado ou até o valor máximo obtido pela progressão.

Observe que ocorreu um salto do valor de 2000 para 3000, e não foi gerada a progressão da faixa D: 2.500.

Isso pode ocorrer, se o sistema identificar que não o salto não vai ultrapassar o valor limite parametrizado (50%).

A 4ª progressão não foi gerada por que o percentual de aumento seria maior que a parametrização: "4ª Progressão: De 3000 para 5000 (O percentual de aumento seria de 66,67%)."

**Particularidades das requisições**

O aumento progressivo está disponível nas duas requisições (alteração de dados funcionais e transferência com alteração de dados funcionais), mas existem algumas diferenças quanto ao tratamento das regras em cada uma, para mais informações consulte o link das requisições abaixo:

Aumento progressivo na requisição: Alteração de dados funcionais

Aumento progressivo na requisição: Transferência com alteração de dados funcionais

**Exibição de menus sobre Aumento Progressivo**

Não existe opção para desabilitar os menus referente ao aumento progressivo em "Globais > Segurança > Perfis", por que entende-se que a progressão é um complemento adicional da requisição e se o usuário tem acesso a requisição também terá acesso a progressão.  Mas os menus só ficam disponíveis se existir alguma progressão ou parametrização cadastrada no sistema.

**Aumento Progressivo no Portal**

Sugestão de progressão: O aumento progressivo também está disponível no Portal, mas existe uma diferença na sugestão de progressão.

No Portal o usuário deverá clicar no botão de aumento progressivo e clicar em sugerir progressões para que as progressões sejam sugeridas, diferente do sistema onde a sugestão ocorre no momento que ele cria a requisição.

**Observação**

Caso o usuário inclua uma progressão no Portal sem informar a função, o sistema considera a função atual da requisição até que essa função seja alterada em outra progressão.

**Observação:**     A progressão salarial não deve ser aplicada em ***requisições entre coligadas***, pois sua utilização nessa condição pode gerar erros e inconsistências nos dados.

Ressalta-se que, a partir da versão 12.1.2506, o sistema passará a exibir uma mensagem de alerta informando sobre a impossibilidade de realizar a progressão salarial entre coligadas, visando garantir a integridade e a confiabilidade das informações processadas.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Para maiores informações sobre a parametrização clique no link abaixo: Parametrização Aumento Progressivo

|  |  |
| --- | --- |
|  | Como Fazer |

---

Passo a Passo - Aumento Progressivo
