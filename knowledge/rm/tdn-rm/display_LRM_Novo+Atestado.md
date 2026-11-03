---
content_hash: 494b0dff64c29553c2bf4ffe8a1f1f200af14f5d15e109905060a0138b8bfe51
fetched_at: '2026-06-29T00:10:32.704019+00:00'
page_id: '527836552'
product: rm
source: tdn-rm
title: Novo Atestado
type: documentation
url: https://tdn.totvs.com/display/LRM/Novo+Atestado
version: 21
---

## **01. VISÃO GERAL**

A reformulação do modelo de atestado médico foi necessária devido à obsolescência do modelo legado, que não atendia mais às solicitações e exigências do mercado. Com a atualização, o atestado passou pelas seguintes melhorias:

* **Desvinculação dos Períodos de Atestado dos Períodos de Afastamento:**  
  Após a liberação do novo modelo, o sistema passará a desvincular os períodos de atestado dos períodos de afastamento. Para isso, foi criado um novo campo chamado **Data Término do Afastamento**, que possibilita ao usuário definir a data efetiva de encerramento do afastamento.  
  Esse campo só é habilitado quando a soma dos “Dias de Atestado” ou dos períodos de afastamento (dentro da carência) para o mesmo tipo e motivo ultrapassa 15 dias.
* **Análise Automática da Continuidade no Período de Carência:**  
  A análise da continuidade dos afastamentos dentro do período de carência agora é feita automaticamente. Caso o usuário lance um atestado com quantidade de dias inferior a 16, mas que, somado a atestados anteriores, ultrapasse 15 dias no período de carência, o sistema considerará a continuidade e habilitará o campo de término do afastamento.
* **Visibilidade Restrita à Coligada de Origem:**  
  O atestado cadastrado ficará visível somente na coligada que originou o registro, assim como ocorre com o afastamento.
* **Correção no Envio do Evento S-2230 - Afastamento Temporário:**  
  Com essas adequações, o sistema corrige uma falha no envio das informações do evento **S-2230**, possibilitando, já no momento do cadastro, o envio correto da quantidade de dias de atestado. Isso evita a necessidade de geração de retificações no início do afastamento, que ocorriam anteriormente ao informar o término do atestado.
* **Restructuração da Tela:**  
  A tela foi reformulada para proporcionar uma melhor experiência ao usuário.
* **Funcionário com Múltiplos Vínculos:**  
  O atestado passa a ser vinculado à pessoa física, e, consequentemente, será automaticamente associado a todas as chapas vinculadas à pessoa na coligada contexto.

ATENÇÃO!

Caso o usuário possua um filtro que restrinja o acesso a apenas uma filial e registre um atestado para um colaborador com múltiplos vínculos, o atestado será vinculado **apenas à matrícula (chapa)** da filial à qual o usuário tem permissão de acesso.

## **02.** **PARAMETRIZAÇÃO**

### 02.01 - Configuração

Para acessar o **Novo Atestado**, o usuário deve acessar o menu: RH | Segurança e Saúde Ocupacional | Ambiente | Parâmetros | Segurança e Medicina do Trabalho | Validações e marcar o parâmetro: **“Encerra Histórico de Afastamento (TOTVS Folha de Pagamento) conforme Data Término Afastamento do Atestado (TOTVS Segurança e Saúde Ocupacional)”**

### 02.02 - Cadastramento

Após habilitar o **Novo Atestado**, esta passará a ser a tela padrão para a utilização do atestado.

Tela exibida quando o atestado gera afastamento:

Tela exibida quando o atestado gera abono:

Tela exibida quando o atestado for referente a acidente de trabalho:

## **03.** **REGRAS**

### 03.01 - ATESTADO DENTRO DA COMPETÊNCIA

### Menos ou igual a 15 dias

* Quando o atestado for lançado na competência atual e tiver duração menor ou igual a 15 dias, o sistema **não exibirá na tela** as informações referentes às perícias e previsões, nem habilitará o campo de **Data de Término do Afastamento**.
* O sistema preencherá os históricos de afastamento e situação com as datas de início e término do afastamento.

### Mais que 15 dias

* Quando o atestado ultrapassa 15 dias, o sistema **habilita o campo “Data Término de Afastamento”**, cujo preenchimento determina se o afastamento está concluído ou não.

---

#### Não informando a data término:

* O atestado médico é lançado para todas as chapas do funcionário;
* A situação do funcionário e de suas chapas relacionadas é alterada para a situação de afastamento correspondente ao tipo de atestado;
* Os históricos de situação e afastamento são preenchidos **sem a data de retorno**, em todas as chapas do funcionário.

---

#### Informando a data término em um atestado já cadastrado:

* O sistema emitirá uma mensagem informando que irá:

  + Alterar a situação do funcionário para **ativo** (se o afastamento terminar na competência atual);
  + Atualizar o histórico de afastamento com a data término;
  + Inserir um novo registro no histórico de situação, referente ao retorno à atividade (caso o atestado termine na competência atual).

---

#### Já preenchendo a data de término no cadastro inicial:

* Quando a data de término é na mesma competência, o sistema:

  + Atualiza os históricos de situação e afastamento com as datas de início e término do afastamento;
  + Cria os atestados e históricos em todas as chapas do funcionário;
  + Mantém a situação do funcionário conforme estava antes do atestado.

### Menos ou igual a 15 dias, com continuidade que totaliza mais de 15 dias

#### Informando a data término:

* Atualiza o histórico de afastamento com as datas de início e término do afastamento;
* Atualiza o histórico de situação apenas com o início do afastamento;
* A situação do funcionário e de suas chapas relacionadas é alterada para a situação de afastamento correspondente ao tipo de atestado.

#### Não informando a data término:

* O atestado médico é lançado para todas as chapas do funcionário;
* A situação do funcionário e de suas chapas relacionadas é alterada para a situação de afastamento do tipo de atestado;
* Os históricos de situação e afastamento são preenchidos sem a data de retorno, em todas as chapas do funcionário.

#### Informando a data término em atestado em aberto:

* Atualiza os históricos de situação e afastamento com a data término do atestado;
* Insere um novo registro no histórico de situação, referente ao retorno à atividade.

### 03.02 - ATESTANDO TERMINANDO NA PRÓXIMA COMPETÊNCIA

#### Mais de 15 dias

* O sistema habilita o campo **“Data Término de Afastamento”**.

**Não informando a data término:**

* O atestado médico é lançado para todas as chapas do funcionário;
* A situação do funcionário e de suas chapas relacionadas é alterada para a situação de afastamento correspondente ao tipo de atestado;
* Os históricos de situação e afastamento são preenchidos sem a data de retorno, em todas as chapas do funcionário.

**Informando a data término:**

* Atualiza o histórico de afastamento com as datas de início e término do afastamento;
* Atualiza o histórico de situação apenas com o início do afastamento;
* A situação do funcionário e de suas chapas relacionadas é alterada para a situação de afastamento do tipo de atestado;
* Na execução da rotina de liberação da competência (no TOTVS Folha de Pagamento) para a competência de término do afastamento, o sistema atualizará o histórico de afastamento com a data término e retornará a situação do funcionário para a situação anterior ao afastamento.

---

#### Menos ou igual a 15 dias

* Quando o atestado tiver duração inferior ou igual a 15 dias e ultrapassar o período de um mês para outro, a situação será alterada para afastamento vinculado ao atestado, pois o funcionário estará de atestado no último dia da competência;
* Na liberação da competência, a situação do funcionário será revertida para **Ativo**.

ATENÇÃO:

Quando a situação do funcionário estiver marcada como **"V - Aviso Prévio"**, o sistema não permitirá o cadastro do atestado médico, independentemente de o atestado ocorrer antes, durante ou após o término do Aviso Prévio, ou mesmo se não houver data final para o atestado.

Nesses casos, o usuário deverá avaliar junto ao setor Jurídico a possibilidade de cancelamento, interrupção, suspensão ou prorrogação do Aviso Prévio para permitir o lançamento do atestado.

⚠️ Será exibida a seguinte mensagem:

**"**A situação do funcionário está como '**V - Aviso Prévio**' e o período do atestado ocorre durante ou ultrapassa o Aviso Prévio. Favor consultar o setor Jurídico para verificar se o Aviso Prévio deverá ser interrompido, suspenso ou prorrogado antes de prosseguir.**"**
