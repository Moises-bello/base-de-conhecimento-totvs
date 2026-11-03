---
content_hash: c88610fd0f774d85ac86cd11acc232eca5cfb1fa23d2dd662ec3e9d71b423b49
fetched_at: '2026-06-29T00:09:49.563591+00:00'
page_id: '435105320'
product: rm
source: tdn-rm
title: Contratos de Venda - Anexo - Distrato Contratual
type: documentation
url: https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Anexo+-+Distrato+Contratual
version: 9
---

O processo de Distrato visa o cancelamento de uma venda, podendo haver ou não a devolução.

Este Anexo deverá ser acessado através do menu Contratos  | Contratos de Vendas | Anexos | Vendas.  
 Ao final de cada processo de distrato, na tela de edição de Vendas, é gravada a Data de Cancelamento na pasta de Identificação.

Para distratar uma Venda/Aluguel, a sua situação deve estar "Efetivada" e ter o número do contrato gerado.  
Depois que a Venda/Aluguel for Distratada, a situação da subunidade irá para a situação que estiver cadastrada no cadastro de Motivos de Cancelamento. Se estiver em branco neste cadastro, a situação irá para "Disponível para Venda".

O processo de Distrato terá etapas para a sua conclusão. Poderemos criar um Distrato e o mesmo ficar em Preparação até que seja aprovado por um fluxo de aprovação e posteriormente ser concluído. O Distrato será um anexo da Venda/Aluguel e as suas etapas, serão Processo da visão do Distrato. O Fluxo de Aprovação é um recurso do produto RM e é opcional a sua utilização. As etapas do Distrato são:

* **Em Aberto:**Ao criar o Distrato, o mesmo ficará com o status "Em Aberto", onde iremos cadastrar as informações básicas, como:
  + Data base do distrato: A Data Base do Distrato, é a Data que foi distratada a venda mediante contrato.
  + Fórmula: Utilizada para parametrizar o valor total do distrato.
  + Evento Contábil: Caso esta venda, possua uma contabilização, o distrato também poderá utilizar um Evento Contábil.
  + Situação da Venda/Aluguel: Neste campo será definido que a situação da venda. Os tipos básicos são:

* + - Cancelada: Cancela a Venda e as parcelas em aberto sem gerar devolução para o Cliente.
    - Distratada: Cancela a Venda e as parcelas que não foram enviadas a banco, possibilidade de gerar devolução para o Cliente.
    - Distrato Unilateral: Cancela a Venda e todas as parcelas até as que foram enviadas a banco, não gera devolução para o Cliente.
    - Outros: Cancela a Venda e as parcelas em aberto sem gerar devolução para o Cliente.
    - Inadimplência: Cancela a Venda e as parcelas em aberto sem gerar devolução para o Cliente.
    - Desistência Cliente: Cancela a Venda e as parcelas em aberto sem gerar devolução para o Cliente.

Importante lembrar que todos estes tipos citados são parametrizados. Para parametrizar basta acessar: Menu Cadastros | Gerais | Situação da Venda e Motivos de Cancelamento

Caso seja escolhido o tipo de distrato 'Distratada', deve-se acessar a aba Condições do Plano, incluir um novo grupo e um novo componente, sendo que este componente deverá ser do tipo Devolução.

O cálculo do distrato será por Fórmula e é realizado todas as vezes que uma informação for alterada e o distrato for salvo.

* **Em Preparação:** No processo de preparação do distrato, caso seja necessário devolver algum valor para o cliente, serão gerados lançamentos no financeiro para que seja feita a provisão dos valores financeiros.
* Estando o distrato nesta fase e o mesmo ser excluído, os lançamentos financeiros também serão excluídos.
* **Efetivado:** Caso o distrato seja efetivado não será possível desfazê-lo. Visto que os lançamentos financeiros não pagos que haviam sido cancelados na efetivação do distrato não poderão ser habilitados novamente. A efetivação do distrato contratual consiste em cancelar as parcelas em aberto e parcialmente quitadas no Totvs Incorporação, cancelar os lançamentos financeiros, carregar o evento contábil de distrato, incluir lançamento ou operação contábil, alterar a situação do contrato, incluir o histórico no contrato, alterar a situação da sub unidade e incluir o histórico de sub unidade.
* **Cancelado:**Caso o distrato seja confirmado, ele poderá ser cancelado, más a venda permanecerá Distratada, não retornando para o status de Efetivada. Os lançamentos financeiros de devolução gerados serão todos cancelados e a contabilidade gerada será excluída.

O processo de Distrato é realizado da seguinte forma:

1 - Deve ser selecionada uma venda na situação de "Efetivada", em seguida clicar no botão Novo no Anexo Distrato Contratual da visão da Venda;  
 2 - Na tela inicial do processo de Distrato, o usuário deve informar a Data do Distrato, a fórmula para o cálculo do Distrato , Evento Contábil e o Tipo de Distrato, sendo que é neste motivo que está definido se haverá devolução ou não, e qual será a situação da sub-unidade após a finalização do processo de Distrato;  
 Os motivos de cancelamentos, podem ser:

* Cancelada;
* Distratada;
* Distrato Unilateral;
* Outros;
* Inadimplência;
* Desistência Cliente.

Se houver devolução, será apresentado a aba Condições do Plano e Plano de financiamento, onde iremos informar os componentes e o plano de devolução.  
 3 - Executar os processos das etapas para a conclusão do Distrato.

Foi implementado o Campo Complementar do Distrato, onde poderemos inserir novos campos no Distrato para que estes possam compor a fórmula que irá calcular o Distrato.

false

Informações Complementares

---

false

Como Fazer

---

false

Recursos Adicionais

---
