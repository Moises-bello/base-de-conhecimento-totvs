---
content_hash: 5c2bee9554ca2d287e38478cbbffe744be5c6fb0a615a5fb0b65e57bd6aa9efb
fetched_at: '2026-06-29T00:09:49.106567+00:00'
page_id: '435105234'
product: rm
source: tdn-rm
title: Condomínio - Básicos - Parâmetros de Integração Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105234
version: 4
---

Os Parâmetros de Integração Financeira são responsáveis por orientar o sistema  TOTVS Incorporação durante a execução de processos que integrem as despesas do Condomínio a lançamentos do sistema TOTVS Gestão Financeira,  como Filiais, Centros de Custos, Natureza Financeira dos lançamentos e até o Tipo de documento que será criado para pagamentos e recebimentos.

**Pré-Condições:**

* **1 -** Ter criado uma Filial
* **2 -** Ter cadastrado um
* **3 -** Ter cadastrado as

**Observação:** Este cadastro é o mesmo utilizado pelo módulo de Aluguel. Assim possui alguns campos que não irão impactar a geração de Lançamentos do Módulo de Condomínio, são eles:

* **Tipo de documento a pagar (Condicional)**
* **Utiliza lançamentos futuros como provisão**
* **Código tipo de documento a receber (Futuro)**
* **Código tipo de documento a pagar(Futuro)**

**Como cadastrar e utilizar o Parâmetro de Integração Financeira no módulo Condomínio:**

* **Passo 1 -** Acesse: TOTVS Incorporação/ Condomínio / Básicos/ Parâmetros de Integração Financeira.
* **Passo 2 -** Clique em Incluir. Preencha os campos conforme desejar e clique em salvar. Os campos são

* + **Id Parâmetro:** Código Identificador do Parâmetro de Integração, esse campo permite somente que seja inserido o valor. Ao editar o Parâmetro de Integração Financeira ele virá bloqueado;
  + **Coligada**: Permite selecionar a Coligada do Parâmetro de Integração Financeira. Através da Coligada selecionada, que serão realizados filtros nos demais campos do cadastro, onde só é permitido associar registro da mesma coligada;
  + **Descrição:** Descrição do Parâmetro de Integração;
  + **Centro de Custo**: Permite selecionar qual Centro de Custo será associado aos lançamentos gerados;
  + **Departamento**: Permite selecionar qual Departamento Empresarial será associado aos lançamentos gerados;
  + **Natureza Financeira a Pagar**: Permite selecionar qual Natureza Financeira a Pagar será associada aos lançamentos gerados;
  + **Natureza Financeira a Receber:** Permite selecionar qual Natureza Financeira a Pagar será associada aos lançamentos gerados;
  + **Tipo de Documento a Pagar:** Permite selecionar qual Tipo de Documento a pagar será associado aos lançamentos gerados para um Fornecedor ou Ambos;
  + **Tipo de Documento a Receber:** Permite selecionar qual Tipo de Documento a receber será associado aos lançamentos gerados para um Cliente ou Ambos;
  + **Conta Caixa:** Permite selecionar qual Conta Caixa será associada aos lançamentos gerados.
  + **Percentual multa de atraso / juros de mora:** Campos que permitem definir o comportamento de cobrança de juros e multa por atraso nos lançamentos que serão gerados pelo Condomínio. Seguem os campos para essa parametrização:

* + - **Tipo de Juros Dia:** Permite definir como será cobrado o Juros Dia, tendo como opções por Taxa (%) ou Valor;
    - **% de juros/mora:** Campo no qual permite definir o valor de Juros Dia dos lançamentos a serem gerados. Esse campo pode conter o valor na forma de Taxa (%) ou Valor (R$), conforme selecionado no campo "Tipo de Juros Dia";
    - **% multa atraso:** Campo no qual permite definir o valor da multa atraso. Esse campo sempre será preenchido com valores na forma de Taxa (%).

* **Passo 3 -** Acesse: TOTVS Incorporação | Condomínio | Manutenção de Empreendimento |  |
* **Passo 4 -** No campo "Parâmetros de Integração Financeira" selecione o registro desejado. Assim todos os Fechamentos associados ao Empreendimento, irão gerar os Lançamentos conforme o Parâmetros de Integração Financeira selecionado no campo.
  + **Observação:**Nesse campo será permitido somente associar Parâmetros de Integração Financeira, que possuem a mesma coligada do Empreendimento.

Veja Também

---
