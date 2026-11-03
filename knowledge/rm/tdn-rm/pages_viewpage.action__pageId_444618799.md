---
content_hash: 3027dcd435a44dc290ed4253079e186b3fd32b6e5f722c868893253bf0591a2a
fetched_at: '2026-06-29T00:09:54.422931+00:00'
page_id: '444618799'
product: rm
source: tdn-rm
title: Movimentações Bibliotecárias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=444618799
version: 40
---

O serviço de movimentação dá suporte ao setor de atendimento da unidade bibliotecária, permitindo operações de Empréstimos, Devoluções e Renovações de maneira global. Isso implica que todas as rotinas podem ser realizadas em uma única tela. O serviço permite, ainda, consulta de informações relativas a exemplares e usuários no que diz respeito as suas respectivas situações e dos empréstimos em andamento.

Este serviço envolve dois grupos de pessoas que serão identificadas pelos termos a seguir:

- Operadores: são os atendentes da unidade bibliotecária que possuem credencial de usuário no sistema com permissão para realizar as operações de movimentação.  
- [Usuários](https://tdn.totvs.com/x/5P1bGQ): são os clientes da unidade bibliotecária que possuem registro no cadastro de usuário da unidade bibliotecária e que poderão realizar empréstimos.

Ao ser utilizado, o serviço de movimentação sempre irá se apresentar ao operador em um dos seguintes estados:

**- Aguardando início de operação:** estado em que o serviço irá se encontrar sempre que for aberto ou após uma operação ser concluída ou cancelada. O serviço estará aguardando uma entrada do operador no sentido de localizar um exemplar ou um usuário a ser identificado para iniciar a próxima operação de empréstimo ou devolução.

Neste momento o operador tem funções disponíveis que permitirão identificar usuários e exemplares, são elas:

> Localização por código: essa função permitirá que um operador localize um usuário ou um exemplar informando um dos possíveis códigos que o serviço estiver configurado para reconhecer. A entrada do código poderá ocorrer através da digitação do código ou uso de leitura ótica (para uma estação de trabalho equipada com scanner de códigos de barra).
>
> Leitura biométrica: essa função permitirá que um operador localize um usuário através da [leitura biométrica](https://tdn.totvs.com/x/iP5bGQ) da impressão digital.
>
> Localização avançada: essa função permitirá que um operador localize um usuário pelo nome ou um exemplar pelo título da publicação.

**Observação:**

Para configurar os códigos utilizados na Localização por código existe um link na tela da movimentação para Códigos utilizados que permite ao operador marcar/desmarcar quais campos serão utilizados na localização do usuário e do exemplar. Caso ocorra de informar um código que corresponda tanto a um código de usuário como a número do tombo, o operador poderá selecionar qual ele deseja realmente identificar.

- **Usuário identificado:** o serviço assumirá este estado após um [usuário](https://tdn.totvs.com/x/5P1bGQ) ser identificado e passará a exibir todas as informações sobre ele. A partir desse estado será possível iniciar uma operação com o usuário que foi identificado.

Neste estado é visualizado a [situação do usuário](http://tdn.totvs.com/x/uP9bGQ).

Neste estado também é possível visualizar os empréstimos em andamento do usuário caso ele possua empréstimos, existindo empréstimos é possível realizar as operações de devolução ou renovação rápidas. Clique [aqui](http://tdn.totvs.com/x/JZVUE) para mais informações.

**- Operações em andamento (Usuário Identificado):** o serviço entrará nesse estado toda vez que um usuário for identificado e existir uma ou mais operações de [empréstimos](http://tdn.totvs.com/x/Mv5bGQ), [devoluções e renovações](http://tdn.totvs.com/x/Qf5bGQ)  em andamento.

**- Operações em Andamento (Usuário anônimo):** ao identificar um exemplar que está emprestado, o serviço assumirá este estado sempre que uma operação de [devolução](http://tdn.totvs.com/x/Qf5bGQ) for iniciada sem que antes um usuário tenha sido identificado.

**- Empréstimo iniciado (identificar usuário):** O serviço assumirá este estado sempre que o estado do serviço for "Aguardando início de operação" e o operador fornecer a identificação de um exemplar disponível para empréstimo. O serviço "entenderá" que o operador deseja iniciar um [empréstimo](http://tdn.totvs.com/x/Mv5bGQ) e irá obrigar que um usuário seja identificado para que a operação de empréstimo prossiga.

Neste estado é possível acessar os [detalhes do exemplar](https://tdn.totvs.com/x/QP5bGQ).

**Importante:** exemplares com data de baixa não serão retornados em nenhum momento nas operações de movimentação. 

Integração com TOTVS Gestão Educacional

A partir da versão 12.1.2302 caso TOTVS Gestão Bibliotecária esteja integrado ao TOTVS Educacional, será necessário realizar o cadastro de Serviços Taxas de Bibliotecária para gerar a Taxa de cadastro de usuário, Taxa de empréstimo ou Taxa de multa.

Para saber mais [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=710556941).

Quando a integração com o TOTVS Educacional estiver ativa, na aba "Lançamentos" da tela de movimentações serão exibidos somente os lançamentos gerados antes da versão 12.1.2302, após esta versão, os novos lançamentos gerados para alunos serão exibidos somente na aba de parcelas, ou seja, os novos lançamentos gerados não ficarão disponíveis nas duas visões, somente na visão de parcelas.

Quando existir a integração com o TOTVS Gestão Educacional e com TOTVS Gestão financeira, os empréstimos podem gerar lançamentos para os usuários. Caso o usuário da movimentação, seja um aluno, ao realizar a devolução da publicação, será gerado um contrato com o tipo "TOTVS Gestão Bibliotecária" para o aluno, nesse contrato, será gerado uma parcela, com o valor do empréstimo e se possuir multa, será gerado outra parcela para a multa. Essas parcelas, serão criadas com o serviço definido no cadastro de "Serviços para taxas das biblioteca".

**Observação**: caso a integração com o TOTVS Gestão Educacional não esteja ativa ou seja desativada, todas as taxas da biblioteca serão geradas somente no TOTVS Gestão Financeira, não gerando nenhum vínculo com o aluno.

Se o aluno possuir mais de uma matrícula, ao realizar a devolução da publicação será questionado em qual dessas matrículas, será cadastrado o contrato. Caso o contrato já exista, não será criado um novo contrato, somente será acrescentado novas parcelas dentro daquele contrato.

As novas parcelas serão geradas na filial da matrícula selecionada na devolução.

**Importante:**

* Para que um contrato seja gerado no TOTVS Educacional, é necessário que o período letivo da matrícula do aluno esteja com a opção destacada abaixo desmarcada.

* A situação da matrícula tenha na aba "Status no período letivo", o campo "Aluno ativo" marcado:

Caso estas condições não sejam atendidas será apresentada a mensagem abaixo e o lançamento será gerado diretamente no "TOTVS Financeiro", ou seja, neste caso não será gerado lançamento no contrato do aluno no TOTVS Educacional.

O lançamento será criado baseando nos parâmetros informados no cadastro de serviço. Caso essa parametrização não seja configurada, o sistema não será capaz de criar o lançamento.

 

**Utilizando parametrização de agrupar valores**

Caso a instituição utilize a seguinte parametrização "agrupa valores em um único lançamento", disponível em Parâmetros / Configurações → Integração → Financeiro → aba 2/4, ao finalizar a movimentação do aluno, que possua mais de uma publicação, então os valores referente a taxa de empréstimo serão agrupados em uma parcela e os valores referente as taxas de multa serão agrupados em outra parcela.

Exemplo:

Aluno "Jonas Dornelas" fez a devolução de 2 publicações em atraso, ambas possuíam valor de empréstimo de R$ 7,00 e estão gerando uma multa de R$ 1,00 cada. Ao finalizar a devolução dessas publicações, será gerado duas parcelas no contrato do aluno, uma parcela com o valor de R$ 14,00 para o serviço definido para a taxa de empréstimo e outra parcela com o valor de R$ 2,00 para o serviço definido para a taxa de multa.

Porém, se a parametrização acima não estiver marcada, então, no final do exemplo acima, seriam gerados 4 parcelas, cada um com seu respectivo valor.

Na tela de movimentações, é possível visualizar as parcelas geradas para aquele aluno, sem a necessidade acessar o módulo TOTVS Gestão Educacional.

Os lançamentos gerados, também serão visualizados em todas as telas de financeiro disponíveis para o aluno.

Importante

Para geração dos lançamentos das parcelas serão utilizados todos os parâmetros financeiros e do serviço do educacional configurados para geração das taxas, porém o centro de custo e o departamento serão utilizados da unidade bibliotecária do contexto da operação de movimentação.

>

 Informações Complementares

---

[Biometria](http://tdn.totvs.com/x/iP5bGQ)  
[Situação do usuário](http://tdn.totvs.com/x/uP9bGQ)  
[Detalhes do exemplar](http://tdn.totvs.com/x/QP5bGQ)  
[Empréstimos](http://tdn.totvs.com/x/Mv5bGQ)  
[Devoluções e renovações](http://tdn.totvs.com/x/Qf5bGQ)
