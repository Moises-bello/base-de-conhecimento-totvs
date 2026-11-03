---
content_hash: c4254689ed3cb2ab4aa3c6e5c6df238449c60b4d925d4855585ea083c51f4deb
fetched_at: '2026-06-29T00:10:08.700705+00:00'
page_id: '452719561'
product: rm
source: tdn-rm
title: Parametrização Aumento Progressivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719561
version: 7
---

**Parametrização Aumento Progressivo**

A parametrização tem por objetivo criar um conjunto de regras que serão aplicadas na criação/edição das requisições e progressões e só pode ser criada para as requisições de "Alteração de dados funcionais" e "Transferência com alteração de dados funcionais".

Na criação de uma parametrização o usuário deverá informar as validações, as ações, filial e motivo.

**Validações**

As validações existentes são:

* Permitir progressão?: Permite o cadastro de progressões no sistema.
* Percentual máximo de aumento sobre o salário(%): Percentual máximo de aumento sobre o salário do funcionário.
* Prazo mínimo entre aumentos(dias): Este prazo deverá ser informado em dias. O sistema irá calcular o último dia de aumento registrado no histórico com a data de efetivação da requisição o resultado dessa diferença será comparado com o valor informado.
* Tempo mínimo de casa(dias): Este prazo deverá ser informado em dias. O sistema compara o valor informado com a data de admissão.
* Valor máximo sobre a fórmula customizada: O usuário informa um valor e escolhe uma fórmula. O resultado da fórmula será comparado com o valor informado pelo usuário.

**Ação sobre validações**

Para cada validação citada acima usuário poderá associar uma ação(exceto "Permitir progressão"). As ações disponíveis são:

* Validar com bloqueio: Impede  a continuidade do processo.
* Validar com mensagem de alerta: Exibe uma mensagem alertando o usuário, mas não impede a continuidade do processo.
* Não Validar: Não irá fazer nenhuma validação, é como se a regra estivesse desabilitada.

**Importante**

 Ao gerar as progressões o sistema utiliza como base as informações cadastradas na parametrização.

Neste caso se o usuário informar a seguinte regra:

  - Prazo mínimo entre aumentos: 30 dias e a ação: Não validar. O sistema permitirá o cadastro, mas as progressões que serão geradas seguirão o padrão de 30 dias de intervalo entre as suas datas de efetivações.

**Filial e Motivo**

Além das validações acima, deverão ser selecionadas a Filial e Motivo onde essas validações serão aplicadas na requisição. O usuário poderá selecionar uma filial e um motivo ou marcar a opção para todas as filiais e todos os motivos.

**Importante***:*

- Só poderá existir uma regra para uma filial e um mesmo motivo, ou seja, caso a filial Belo Horizonte esteja parametrizada para o motivo "Promoção", por exemplo, não poderá ser incluída uma outra parametrização contendo esses dois parâmetros.

- A validação da Filial e Motivo não é aplicado no histórico salarial do funcionário. Esta validação é aplicada na requisição.

Exemplo:

Definido filial 01 e Motivo Promoção. Ao abrir a requisição, serão validadas toda a parametrização informada e se o filtro de filial e/ou motivo é atendido. Ou seja, será levada em consideração os parâmetros para as requisições onde forem informadas a filial 01 e/ou motivo Promoção. OBSERVAÇÃO: Para validação do motivo, será levado em conta se o motivo informado na requisição é o mesmo informado no parametrizador (caso exista). O motivo informado no filtro é usado exclusivamente para validação na abertura de requisição não levando em consideração históricos existentes.

**Alguns comportamentos do sistema:**

* Nenhuma parametrização cadastrada: Caso não exista no sistema registro de parametrização e progressão, o sistema não exibe os menus de progressão.  Se existir somente registro de progressão, como não existe nenhuma parametrização o usuário poderá cadastrar progressões de forma livre sem validações.
* Bloqueando progressões. O usuário pode definir o bloqueio da progressão, selecionando a filial e motivo e deixando desmarcado o parâmetro "Permitir progressão".  Bloquear progressão só irá impedir o cadastro e edição, a visualização do menu fica disponível.

**Importante:**

Essas validações só ocorrem na visão da requisição enquanto o seu status é diferente de aprovado. Após a aprovação as requisições ficam disponíveis no menu de efetivação e neste menu não ocorre nenhuma validação das parametrizações cadastradas.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Aumento Progressivo

|  |  |
| --- | --- |
|  | Como Fazer |

---

Passo a Passo - Aumento Progressivo
