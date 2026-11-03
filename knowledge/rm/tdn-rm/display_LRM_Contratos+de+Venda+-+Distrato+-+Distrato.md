---
content_hash: e3deb1bc3a67f0b8fefc461b01ca12d0f5da7ba97f663b0a390a29cdf007043b
fetched_at: '2026-06-29T00:09:49.534089+00:00'
page_id: '435105315'
product: rm
source: tdn-rm
title: Contratos de Venda - Distrato - Distrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Distrato+-+Distrato
version: 24
---

Contabilizacao do Distrato

## Contabilização obrigatória na efetivação do distrato da venda

**Disponível a partir da versão 12.1.2602.**

### 

### Objetivo

Permitir que a empresa defina se a contabilização deverá ser obrigatória no momento da efetivação do distrato da venda, evitando inconsistências contábeis e retrabalho operacional, ou mantendo o comportamento atual conforme a necessidade da operação.

### Descrição

Foi disponibilizado um parâmetro sistêmico para controlar a obrigatoriedade da contabilização durante o processo de distrato da venda.

Quando o parâetro estiver habilitado, o sistema realizará validações da contabilização antes de concluir a efetivação do distrato.

Caso a contabilização não tenha sido gerada corretamente ou esteja inconsistente, a efetivação do distrato não será concluída e o sistema apresentará uma mensagem de erro ao usuário.

### Localização do parâmetro

**Parâmetros > Venda > Plano de Financiamento > Plano de Financiamento**

### Características

* Parâmetro de abrangência global.
* Controla a obrigatoriedade da contabilização na efetivação do distrato da venda.
* Visa garantir maior integridade contábil no processo de distrato.

### Regra de validação

Durante a efetivação do distrato da venda:

* Se o parâmetro estiver desabilitado:
  + O sistema manterá o comportamento atual, permitindo a efetivação do distrato mesmo sem contabilização.
* Se o parâmetro estiver habilitado:
  + O sistema validará se a contabilização foi gerada corretamente.
  + Caso não exista contabilização ou sejam identificadas inconsistências, o distrato não será efetivado.
  + Será apresentada uma mensagem de erro informando a necessidade de regularização da contabilização antes da conclusão do processo.

### Benefícios

* Redução de inconsistências contábeis.
* Maior segurança operacional no processo de distrato.
* Prevenção de retrabalho contábil e fiscal.
* Padronização do processo conforme as regras da empresa.
Atenção

O comportamento do sistema durante a efetivação do distrato é condicionado ao parâmetro de **Bloqueio de Alterações**, localizado em: `Parâmetros Gestão de Imóveis > Integração Financeira > Bloqueio de Lançamento Venda > Bloquear alterações de dados financeiros e baixas, quando estiver usando data base e o mês competência da alteração for diferente do mês competência do reajuste.`

#### 1. Com o parâmetro MARCADO:

O sistema **obrigatoriamente** tentará realizar o reajuste das parcelas na data-base do aditivo. Isso garante que o distrato não ocorra com valores indevidos, porém:

* Exige que a cotação do índice (ex: IPCA) esteja cadastrada para o mês de competência.
* Caso o índice não tenha sido publicado, o sistema impedirá a gravação apresentando erro de cotação.

#### 2. Com o parâmetro DESMARCADO:

O sistema **ignorará o reajuste** para o mês de competência da alteração.

* Isso permite a efetivação do distrato mesmo que o índice da moeda ainda não tenha sido cadastrado/publicado, pois a validação de cotação não será executada.

---

#### Congelamento Manual de Valores

Independente do parâmetro acima, caso precise que os valores sejam congelados em uma data:, utilize a rotina:

* **Venda > Lançamentos Financeiros > Processos > Congelar Reajuste** (ou **Descongelar**, para retomar a atualização).

O Distrato visa o cancelamento de uma venda, podendo haver ou não a devolução.   
Este Anexo deverá ser acessado através do menu Cadastro de Vendas e Aluguéis | Anexos | Distrato.    
Para saber como o Processo de Distrato é realizado, .   
Ao Efetivar o Distrato, na tela de edição de Vendas, é gravada a Data de Cancelamento na pasta de Identificação e o contrato fica na situação Distratada.  
Para distratar uma Venda/Aluguel, a sua situação deve estar "Efetivada".  
Depois que a Venda/Aluguel for Distratada, a situação da subunidade irá para a situação que estiver cadastrada no cadastro de Motivos de Cancelamento. Se estiver em branco neste cadastro, a situação irá para "Disponível para Venda".

O Distrato possui etapas para a sua conclusão. São elas:

**Em Preparação:** Ao criar o Distrato, o mesmo ficará com o status "Em Preparação", onde iremos cadastrar as informações básicas, como:

* **Data base do distrato**: A Data Base do Distrato, é a Data que foi distratada a venda mediante contrato.
* **Situação do distrato:** Este campo exibe a Situação que o Distrato se encontra, esse campo é preenchido automaticamente pelo sistema.
* **Código Tipo Distrato:** Este campo define qual o tipo de Distrato será cadastrado, possui as seguintes opções:
  + Unilateral
  + Bilateral
* **Código Motivo Distrato**: Este campo define qual o Motivo o Distrato será cadastrado. O Motivo Distrato pode ser cadastrado na funcionalidade Motivo Distrato, através desse cadastro pode se definir a descrição do Motivo e se o Distrato irá gerar parcela. Para maiores informações sobre .
* **Evento Contábil:** Este campo define qual o Evento Contábil será utilizado para a contabilização.
* **Id Operação:** Este capo exibe o Id da Operação de Contabilização do Distrato.
* **Código da fórmula:** Este campo define a fórmula que será utilizada para o calculo do Valor do Distrato;
* **Valor do Distrato:** Campo que exibe o valor do Distrato, campo preenchido automaticamente pelo sistema, conforme o valor retornado pela fórmula.
* **Memória de Cálculo:** Campo que exibe a memória de cálculo da fórmula, preenchido automaticamente pelo sistema, quando o usuário clique no botão de Calcular Fórmula.
* **Observação:** Campo livre, onde o usuário pode inserir observações que achar necessário.
* **Condições de financiamento Distrato**: Caso o Motivo de Distrato vinculado ao Distrato, tenha a possibilidade de Gerar Parcelas, essa tela será habilitada. Nessa tela será possível cadastrar as condições da venda, para maiores informações 
  + Após cadastrar as condições de financiamento do Distrato, será possível Gerar o Plano de Financiamento, aonde será criado os lançamentos financeiros, Bloqueados ou Provisionados conforme for parametrizado pelo usuário nos parâmetros do Distrato, para maiores informações .
* Lançamento de distrato: Nesta tela será possível visualizar os lançamentos criado pelo Distrato, assim como executar os processos que pertence aos Lançamentos Financeiros. Para maiores informações

**Efetivado:** Ao efetivar o Distrato o sistema verifica se algum lançamento do contrato de venda foi securitizado, encontrando não será possível concluir a efetivação do distrato. Após executar o processo Efetivar Distrato, o Distrato passar a ter como Situação do distrato Efetivado. Os lançamentos financeiros da Venda serão bloqueados e os lançamentos do Distrato serão desbloqueados.

Existe a possibilidade de voltar a Situação do Distrato para Em Preparação através do processo Desfazer Aditivo.

**Cancelado:** Caso o distrato esteja Efetivado, ele poderá ser Cancelado, mas a venda permanecerá Distratada, não retornando para o status de Efetivada. Os lançamentos financeiros de devolução gerados serão todos cancelados e a contabilidade gerada será excluída.   
**Quitado:** Ao baixar todos os lançamentos financeiros do Distrato ou executar o processo de Quitar Distrato, o Distrato passará a ter a Situação igual a Quitado.

false

Informações Complementares

---



Quando houver geração do plano do distrato o sistema utilizará campo do dia de vencimento que fica na edição da venda, se estiver com zero utilizará a data base da regra do componente de devolução

Atenção!

Caso a Integração com a [Registradora de Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=729222653) esteja parametrizada, verifique as **[Premissas](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora)** em relação ao **Distrato** ao se executar o Processo [Integrar com Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora).

false

Como Fazer

---

* [Situação da Venda](http://tdn.totvs.com/pages/viewpage.action?pageId=435105409)


false

Integração TINxProtheus

---

Quando integrado ao Backoffice Protheus, o TIN irá disponibilizar dentro do processo de geração de parcelas a pagar do distrato, a visão para selecionar ou mesmo demonstrar o fornecedor que será gerada as parcelas do plano de distrato do imóvel do contrato. Quando tiver mais de um comprador no contrato de venda ficará a cargo do usuário selecionar qual dos fornecedores irá receber as parcelas de devolução.
