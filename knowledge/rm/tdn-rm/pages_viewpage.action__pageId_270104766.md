---
content_hash: 01e94633f3def533217722477bfb71578185c4bcf89a9c7432cbe9319484430e
fetched_at: '2026-06-29T00:08:24.110661+00:00'
page_id: '270104766'
product: rm
source: tdn-rm
title: RMBIB00002_Empréstimo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270104766
version: 6
---

### **Empréstimo**

|  |  |
| --- | --- |
| **Produto:** | Gestão Bibliotecária |
| **Versão:** | 12.1.14 |
| **Processo:** | Movimentação |
| **Subprocesso:** | Empréstimo |
| **Data da publicação:** |  |

Clique aqui para expandir o índice

# 1.Cadastros

## 1.1.Cadastro do usuário

Cadastros | usuário | usuários

Para a realização do empréstimo, primeiramente, identifique o usuário que irá pegar o livro emprestado.

O sistema permite identificar o usuário para empréstimo, de inúmeras formas diferentes:

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

Acervo | publicação | publicações

Após identificar o usuário, é necessário identificar o livro que será emprestado. O item a ser emprestado, é exemplar da publicação e este é um anexo do cadastro:

O sistema permite identificar o exemplar para empréstimo, de inúmeras formas diferentes:

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

A rotina de empréstimo é parametrizada, pela regra de empréstimo e pelos parâmetros do sistema. A regra de empréstimo, é baseada no grupo de publicação e no tipo de usuário, dessa forma, para cada conjunto de situações, é possível ter regras diferentes, como para alunos, professores e publicações de grupos diferentes.

O grupo de publicação, é um campo que é cadastrado dentro da publicação e o tipo de usuário, é um campo cadastrado dentro do usuário.

Parâmetros/configurações | regras de empréstimo

Nesse cadastro, é informado o valor do empréstimo, qual prazo o usuário pode ficar com o exemplar, ser o usuário pode pegar mais de um exemplar de uma mesma publicação, se o empréstimo ficará bloqueado, para os usuários que estiverem com devoluções em atraso e realizar o controle por faixa etária. Também é definido se o empréstimo será por dia ou por horas e para quais tipos de empréstimo essa definição é válida. Exemplo, em uma mesma regra de empréstimo, pode-se ter empréstimo de 7 dias para os exemplares normais e de 3 horas para os de circulação interna (não saem da biblioteca).

Parâmetros/configurações | parâmetros do sistema | integração

Para que seja possível informar um valor para o empréstimo, a integração com o Gestão Financeira, deve estar marcada.

O usuário da biblioteca, também necessita de um responsável financeiro cadastrado:

## 2.2.Parâmetros

Parâmetros/Configurações | Parâmetros do sistema | Movimentações | Empréstimo

Os parâmetros do sistema são baseados na coligada, filial e unidade bibliotecária, dessa forma, para cada conjunto de situações, é possível ter parametrizações diferentes.

Nesse cadastro, é possível definir, se será solicitada senha do usuário, para realização do empréstimo, se será definido período de férias, alterando dessa forma a data de devolução, se o usuário da biblioteca, poderá alterar a data de devolução para maior que o definido na regra de empréstimos, se os exemplares bloqueados (circulação interna), poderão ser emprestados, se no caso de empréstimo em horas, o horário de funcionamento da biblioteca será considerado, entre outros.

No caso da utilização de senha, a mesma é informada no cadastro do usuário:

Parâmetros | Configurações | Parâmetros do sistema | Movimentação | Geral

Algumas situações são definidas na guia geral, das parametrizações do sistema

Parâmetros/Configurações | Parâmetros do sistema | Emissão de recibos

É nessa parte dos parâmetros, onde é definido se será gerado um comprovante de empréstimo ao fim da movimentação.

Ao selecionar a saída padrão (forma como será criado o recibo de empréstimo). É possível selecionar apenas uma saída padrão:

* Impressora Bematech (Nesse caso o sistema possui um relatório interno, que não pode ser alterado e é gerado apenas, para alguns modelos desse fabricante);
* Gerador de relatórios (Nesse caso, é criado um relatório, de acordo com as necessidades da instituição e o mesmo é definido como padrão para os empréstimos. Lembrando que o book de relatórios possui modelo de relatório, que pode ser utilizado);
* Envio de e-mail (É enviado para o e-mail cadastrado no usuário, o mesmo relatório interno da impressora Bematech, contendo informações referentes ao empréstimo).

É possível definir se o relatório será visualizado antes da impressão e se será utilizado relatório do gerador antigo, ou do Totvs Reports:

Modelos de impressoras suportado pelo sistema, para quando a saída padrão for a impressora Bematech:

**OBS**: à partir da versão 12.1.21, foi incluído também a possibilidade de utilizar a impressora Bematech MP 4200 TH (para mais informações sobre a configuração a impressora clique [aqui](http://tdn.totvs.com/x/Hk1KE)).

É possível definir também, algumas das informações que serão incluídas nesse relatório:

# 3.Realizando o empréstimo

Movimentações | Movimentações

Essa é a única tela no sistema, que permite ficar aberta e utilizar o sistema, abrindo qualquer outra tela, sem a necessidade de fechar a mesma:

Identificamos o usuário através do seu código de cadastro no sistema, em seguida identificamos o exemplar através do número do tombo:

É possível verificar que várias informações são exibidas nas telas da movimentação:

Pressione F9, ou clique no botão: confirmar:

O log de movimentações, mostrado ao final do processo, é parametrizado para exibição ou não, nos parâmetros do sistema, na guia geral da parte de movimentações:

Voltando a tela de movimentações e digitando o código do usuário, é mostrado o exemplar emprestado e todas as informações referentes ao empréstimo:
