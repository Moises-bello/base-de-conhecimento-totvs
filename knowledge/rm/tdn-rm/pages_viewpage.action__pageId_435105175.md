---
content_hash: 387651f0a1b56e6e1627faf1938f6f44a1c00a941720f5da39124656560745e9
fetched_at: '2026-06-29T00:09:48.498944+00:00'
page_id: '435105175'
product: rm
source: tdn-rm
title: Contrato de Locação - Aditivos - Alteração Aluguel em Dobro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105175
version: 10
---

Este aditivo permite a inclusão, alteração e exclusão de informações de Aluguel em Dobro existentes em um contrato.

**Pré-condições**

* Ter habilitado a permissão para Efetivar / Desfazer aditivo de Alteração Aluguel em Dobro, do perfil do TOTVS Gestão de Imóveis, localizada em *Serviços Globais / Segurança / Perfis.*
* Ter efetivado o Contrato de Locação
* Ter incluído um Motivo do Aditivo

**Campos da tela:**

* **Código do aditivo:** Código do aditivo realizado, campo preenchido automaticamente  pelo sistema;
* **Data do aditivo:** Data da criação do aditivo. A partir dessa data será aplicado no Contrato de Locação as alterações do aditivo. No caso do Aditivo de Alteração dos Imóveis do Contrato, a inclusão ou alteração dos Imóveis do Contrato serão realizadas a partir da data do aditivo;
* **Tipo de aditivo:** Exibe o Tipo de Aditivo no qual está sendo cadastrado. Esse campo é preenchido automaticamente pelo sistema, onde o é preenchido pelo Tipo de Aditivo selecionado no Anexo do Contrato de Locação >> Aditivo;
* **Situação do aditivo:** Exibe a situação do aditivo, que pode ser:

* + **Preparação:** O aditivo tem essa situação quando está sendo cadastrado e ainda não foi executado o processo "Efetivar Aditivo" ou quando é executado o processo "Desfazer Aditivo" em um aditivo com a situação "Efetivado". Nessa situação é permitido alterar o aditivo e as modificações cadastradas não são aplicadas ao Contrato de Locação associado;
  + **Efetivado:**O aditivo tem essa situação quando é executado o processo "Efetivar Aditivo". Nessa situação não é possível alterar o aditivo. As modificações cadastradas já foram aplicadas ao Contrato de Locação, quando foi executado o processo "Efetivar Aditivo";

* **Motivo do aditivo:** Motivo do aditivo a ser executado. Novos motivos de aditivos podem ser criados através do Cadastro de Motivo do aditivo, que se encontra no seguinte caminho Aluguel >> Cadastros >> Motivo de aditivo.
* **Número do Aditivo no Cliente:** Campo onde o cliente informar o número do Aditivo no Contrato físico. Podendo assim realizar o agrupamento de vários aditivos do sistema a um aditivo físico.
* **Detalhes da Tela de Seleção de Aluguel em Dobro:**

* + **As ações possíveis são:**

* + - **Alterar:** Utilizado para alterar os campos: percentual e data final de um aluguel em dobro já existente no contrato de locação, ainda é possível o usuário informar a competência no momento de realizar a alteração.
    - **Incluir:** Utilizado para incluir um novo registro de Aluguel em Dobro informando os campos: competência, percentual e data final.
    - **Excluir:** Utilizado para excluir um Aluguel em Dobro no contrato.

* + **Atual:**

* + - **Aluguel em dobro anterior:** O usuário informa qual o aluguel em dobro será alterado/excluído. Na inclusão de um novo aluguel em dobro este campo e os demais abaixo estarão desabilitados.
    - **Competência anterior:** Exibe a competência do Aluguel em Dobro selecionado. Campo não editável.
    - **Novo percentual:** Exibe o percentual do Aluguel em Dobro selecionado.  Campo não editável.
    - **Data inicial anterior:** Exibe a Data inicial do Aluguel em Dobro selecionado.  Campo não editável.
    - **Data final anterior:** Exibe a Data final do Aluguel em Dobro selecionado.  Campo não editável.
    - **Considerar CTO Dobrado (Anterior):** Exibe se o registro selecionado atua somente sobre o CTO ou não. Campo não editável.
    - **Forma de Cobrança do Aluguel em Dobro (Anterior):** Exibe se o registro seleciona atua de forma desagregada, com lançamentos separados através do parâmetro de integração financeira. Campo não editável.

* + **Novo:**

* + - **Novo aluguel em dobro:** Após a efetivação do aditivo, exibe o novo registro de Aluguel em Dobro que foi alterado/incluído. Este campo não é editável e em caso de exclusão de aluguel em dobro este campo e os demais abaixo estão desabilitados.
    - **Nova competência:** Exibe a nova competência. Em caso de alteração, este campo não é editável. Para a inclusão de um novo aluguel em dobro o usuário precisa definir o seu valor.
    - **Novo percentual:** Permite o usuário informar um novo percentual para o Aluguel em Dobro. (campo editável).
    - **Nova data inicial:** Exibe a nova data inicial do aluguel em dobro. Essa data é a data do aditivo e o campo não é editável. A data é exibida ao salvar o registro.
    - **Nova data final:** Neste campo o usuário informa qual a data final para o Aluguel em Dobro (campo editável).
    - **Considerar CTO Dobrado (Novo):** Possibilita o usuário definir se o aluguel em dobro fará parte do cálculo de CTO, dobrando o mesmo quando existir.
    - **Forma de Cobrança do Aluguel em Dobro (Novo):** Possibilita ao usuário alterar ou inserir um novo parâmetro de integração financeira, que irá atuar na geração de lançamentos em dobro não agregados.

**Incluindo um Aditivo de Aluguel em Dobro**

* Selecione o Contrato de Locação e acesse: Anexo / Aditivo / Alteração de Aluguel em Dobro.
* Clique em Incluir Aditivo de Alteração de Aluguel em Dobro. Preencha os campos:

* + Data do Aditivo: A data do aditivo deve estar dentro do período de vigência do Contrato de Locação. Esta data será utilizada como data inicial dos novos registros de aluguel em dobro criados pelo aditivo.
  + Motivo do Aditivo: Informar um Motivo do Aditivo

* Clique em Adicionar para Alterar, Incluir ou Excluir um item de Aluguel em Dobro.
* Será exibida a tela para preenchimento dos dados do Aluguel em Dobro. Preencha os campos:

* Salvar e
* Verifique que o status do Aditivo foi alterado para Efetivado.

**Efetivação do Aditivo de Aluguel em Dobro**

* O sistema mantém um histórico de registros de aluguel em dobro através das datas de início e fim.
* Ao criar um aditivo com ação de alteração, o sistema irá gerar um novo registro de aluguel em dobro com a data inicial igual à data do aditivo e o registro alterado terá a sua data final alterada para um mês anterior à data do aditivo. Exemplo:
  + Aluguel em Dobro 1 já existente:
    - Competência: Dezembro
    - Percentual: 100%
    - Data Inicial 01/2017
    - Data Final 01/2019
  + Aditivo criado na data de 05/2018 para alterar o percentual para 50%. Após a efetivação o sistema irá possuir dois registros de aluguel em dobro com os dados:
  + Aluguel em Dobro 1:
    - Competência: Dezembro
    - Percentual: 100%
    - Data Inicial 01/2017
    - Data Final 04/2018
  + Aluguel em Dobro 2:
    - Competência: Dezembro
    - Percentual: 50%
    - Data Inicial 05/2018
    - Data Final 01/2019
* **ATENÇÃO**: Caso a data do aditivo seja igual à data inicial do aluguel em dobro, então o sistema irá substituir o registro já existente com os novos dados, e nenhum outro registro será criado.
* Quando a ação do aditivo for de inclusão, então um novo registro de aluguel em dobro será criado.
* Quando a ação do aditivo for de exclusão, então o aluguel em dobro selecionado não será excluído da base de dados, a sua data final será alterada para a data do aditivo.

Como Fazer

---
