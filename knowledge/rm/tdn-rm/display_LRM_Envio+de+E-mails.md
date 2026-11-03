---
content_hash: 60f80abf37807e6e911337fb8761175bb90eb6d529abdf81f2961d58093c4319
fetched_at: '2026-06-29T00:09:34.806996+00:00'
page_id: '425459252'
product: rm
source: tdn-rm
title: Envio de E-mails
type: documentation
url: https://tdn.totvs.com/display/LRM/Envio+de+E-mails
version: 12
---

Através deste processo é possível realizar o envio de e-mail para os usuários da biblioteca em diferentes situações.

Na primeira etapa da execução do processo é selecionado o tipo de e-mail a ser enviado:

**Aviso de devolução prevista:** Esta opção envia e-mails para todos os usuários que possuam empréstimos com status diferente de "Devolvido" e "Cancelado" e cuja data de devolução prevista esteja entre a data atual e o período de cobrança, definido no parâmetro do processo.

#### 👉Empréstimos por dia

Para efeito de comparação, **a hora não é considerada** na data de devolução prevista em empréstimos por dia.

Exemplo:

* Data de devolução prevista: **23/09/2025 09:00**
* Data/hora atual: **23/09/2025 12:00**

Mesmo a hora sendo diferente, o empréstimo deverá ser apresentado na **lista de devoluções previstas**, pois ambas as datas correspondem ao mesmo dia (**23/09/2025**).

#### 👉Empréstimos por hora

A **hora é considerada** na data de devolução prevista em empréstimos por hora.

Exemplo:

* Data de devolução prevista: **23/09/2025 10:52**
* Data/hora atual: **23/09/2025 13:30**

O sistema não ir a carregar este empréstimo pois ele considera o mesmo como vencido pois o horário atual é maior que o horário de devolução prevista.

**Cobrança de empréstimo atrasado:** Esta opção envia e-mails para todos os usuários que possuam empréstimos com situação igual a "atrasado".

**Áreas de interesse do usuário:** Serão enviados e-mails informando aos usuários, que contêm áreas de interesse cadastradas, informações sobre publicações existentes na biblioteca com áreas de conhecimento equivalentes aos seu interesse.

**E-mail livre:** O usuário pode acessar esta opção para enviar um e-mail livre. O texto dos e-mails também deve ser parametrizado. Poderão ser utilizadas algumas tags predefinidas, que serão trocadas por seus respectivos valores antes do envio do e-mail.

Importante

Algumas configurações para que os e-mails sejam enviados pelo sistema, podem ser definidas em: Parâmetros do Sistema | 14.05 - Envio de E-mails

**Configuração e Personalização no Envio de E-mail**

* Permite agendamento da execução do processo proporcionando envio de e-mail automático.
* Utilização de TAGs para auxiliar na inserção de informações (informações como nome do usuário, nome da publicação, número do tombo, data da devolução podem ser inseridas no e-mail enviado utilizando suas TAGs correspondentes).

**Atenção**

* Para que se tenha informações atualizadas, é aconselhável que o processo de atualização da biblioteca seja executado antes do acesso à tela de envio de e-mails.
* O e-mail de retorno deve ser parametrizado. as opções são: E-mail da biblioteca ou e-mail do usuário logado no sistema.

**Erros que podem impedir o envio de um E-mail**:

1. As configurações de envio de e-mail não foram corretamente definidas em "Parâmetros Globais";
2. O e-mail não se encontra corretamente preenchido no "Cadastro de Pessoas" para o candidato ou de "Clientes/fornecedores" para profissionais;

**Opções Disponíveis no envio de E-mail:**

Carregar de arquivo: Possibilita que texto do e-mail seja carregado a partir de um arquivo texto.

Salvar em arquivo: Possibilita que texto do e-mail digitado na caixa de texto seja salvo como arquivo texto.

Tags disponíveis: apresenta uma lista de tags que poderão ser inseridas no corpo do texto. As tags são marcações inteligentes que serão substituídas por textos específicos durante o processo de montagem do e-mail. Para que possam ser identificadas e "traduzidas", as tags devem ser utilizadas exatamente como os modelos, ao selecionar uma tag da lista esta será inserida no campo de texto correspondente ao e-mail.

**Simulação de Envio**

O último passo do assistente permite ao usuário escolher entre realizar uma simulação de envio ou efetivamente enviar os e-mails.
