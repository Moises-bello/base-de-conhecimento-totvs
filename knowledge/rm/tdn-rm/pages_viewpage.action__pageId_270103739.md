---
content_hash: e0d62105b55c4d4afed44bf4b125719c33d297445c4aadf006edfb18323f266b
fetched_at: '2026-06-29T00:08:24.088597+00:00'
page_id: '270103739'
product: rm
source: tdn-rm
title: RMBIB00001_Devoluções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270103739
version: 11
---

**Devolução**

|  |  |
| --- | --- |
| **Produto:** | Gestão bibliotecária |
| **Versão:** | 12.1.14 |
| **Processo:** | Movimentação |
| **Subprocesso:** | Devolução |
| **Data da publicação:** |  |

Clique aqui para expandir o índice

# 1.Cadastros

## 1.1.Cadastro usuário

Cadastros | usuário | usuários

Para a realização da devolução, primeiramente, identifique o usuário que está com o livro emprestado.

O sistema permite identificar o usuário para devolução, de inúmeras formas diferentes:

* Código do usuário (usuário cadastrado no Biblios);
* Código da pessoa;
* Registro Acadêmico (Alunos);
* Chapa (Funcionários);
* Nº carteirinha;
* Leitura biométrica (Previamente cadastrada);
* Nome (Localização avançada);
* CPF (Localização avançada).

Parâmetros/configurações | parâmetros do sistema | integração | educacional

Para que o Registro Acadêmico (RA), seja apresentado como opção de seleção de usuário, é necessário que a integração com o Gestão Educacional, esteja marcada.

Parâmetros/configurações | parâmetros do sistema | integração | folha de pagamento

Para que a chapa, seja apresentada como opção de seleção de usuário, é necessário que a integração com o Folha de pagamento, esteja marcada.

Após identificar o usuário, é necessário identificar qual (is) livro (s) será (ão) devolvido (s). São apresentados todos os livros que o usuário possui emprestado, assim como sua situação.

O sistema permite identificar o exemplar para devolução, de inúmeras formas diferentes:

* Nº tombo;
* Nº tombo (antigo);
* Código auxiliar;
* Cód. Publicação\_Exemplar
* Ano (Localização avançada);
* Edição (Localização avançada);
* Num. Exemplar (Localização avançada);
* Título (Localização avançada);
* Volume (Localização avançada).

# 2.Parametrização

## 2.1.Regra de empréstimo

Parâmetros/Configurações | Regras de empréstimo

A rotina de devolução é parametrizada, pela regra de empréstimo e pelos parâmetros do sistema. A regra de empréstimo, é baseada no grupo de publicação e no tipo de usuário, dessa forma, para cada conjunto de situações, é possível ter regras diferentes, como para alunos, professores e publicações de grupos diferentes.

O grupo de publicação, é um campo que é cadastrado dentro da publicação e o tipo de usuário, é um campo cadastrado dentro do usuário.

Parâmetros/configurações | regras de empréstimo

Nesse cadastro, é informado o valor da multa para atraso, os dias de suspensão do usuário, se essa suspensão será por dia, hora ou se não será aplicada.

As penalidades ao usuário por devolver o exemplar em atraso, podem ser diferentes para os empréstimos normais, de consulta interna e externa e também, para os que possuem ou não reserva.

Parâmetros/Configurações | Parâmetros do sistema | Integração | Financeiro

Para que seja possível informar um valor para cobrança de multa, para devolução em atraso, a integração com o Gestão Financeira, deve estar marcada.

O usuário da biblioteca, também necessita de um responsável financeiro cadastrado:

## 2.2.Parâmetros

Parâmetros/Configurações | Parâmetros do sistema | Movimentações | Devolução

Os parâmetros do sistema são baseados na coligada, filial e unidade bibliotecária, dessa forma, para cada conjunto de situações, é possível ter parametrizações diferentes.

Nesse cadastro, é possível definir, se será exibida mensagem que a publicação devolvida possui reservas, se é permitido cancelar empréstimo em atraso, se é permitido abonar multa para devoluções em atraso, se será considerado somente dia útil para o cálculo da multa e da suspensão, será permitido desconto no valor total da multa e se será permitido alterar a data prevista de devolução.

Parâmetros | Configurações | Parâmetros do sistema | Movimentação | Geral

Algumas situações são definidas na guia geral, das parametrizações do sistema

Parâmetros/Configurações | Parâmetros do sistema | Emissão de recibos

É nessa parte dos parâmetros, onde é definido se será gerado um comprovante de devolução ao fim da movimentação.

Ao selecionar a saída padrão (forma como será criado o recibo de devolução). É possível selecionar apenas uma saída padrão:

* Impressora Bematech (Nesse caso o sistema possui um relatório interno, que não pode ser alterado e é gerado apenas, para alguns modelos desse fabricante);
* Gerador de relatórios (Nesse caso, é criado um relatório, de acordo com as necessidades da instituição e o mesmo é definido como padrão para as devoluções. Lembrando que o book de relatórios possui modelo de relatório, que pode ser utilizado);
* Envio de e-mail (É enviado para o e-mail cadastrado no usuário, o mesmo relatório interno da impressora Bematech, contendo informações referentes a devolução do empréstimo).

É possível definir se o relatório será visualizado antes da impressão e se será utilizado relatório do gerador antigo, ou do Totvs Reports:

Modelos de impressoras suportado pelo sistema, para quando a saída padrão for a impressora Bematech:

**OBS**: à partir da versão 12.1.21, foi incluído também a possibilidade de utilizar a impressora Bematech MP 4200 TH (para mais informações sobre a configuração a impressora clique [aqui](http://tdn.totvs.com/x/Hk1KE)).

É possível definir também, algumas das informações que serão incluídas nesse relatório:

# 3.Realizando a devolução

Movimentações | Movimentações

Essa é a única tela no sistema, que permite ficar aberta e utilizar o sistema, abrindo qualquer outra tela, sem a necessidade de fechar a mesma:

Identificamos o usuário através do seu código de cadastro no sistema, em seguida identificamos o exemplar através do número do tombo:

Pressione F9, ou clique no botão: confirmar:

O log de movimentações, mostrado ao final do processo, é parametrizado para exibição ou não, nos parâmetros do sistema, na guia geral da parte de movimentações:
