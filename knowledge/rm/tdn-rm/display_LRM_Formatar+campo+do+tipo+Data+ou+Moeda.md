---
content_hash: 1cb95209a6b8a4460c9ab8e9b90fb39e4fefb06971ebb8611ec7195ade402d3a
fetched_at: '2026-06-29T00:08:56.520481+00:00'
page_id: '351377936'
product: rm
source: tdn-rm
title: Formatar campo do tipo Data ou Moeda
type: documentation
url: https://tdn.totvs.com/display/LRM/Formatar+campo+do+tipo+Data+ou+Moeda
version: 8
---

# Índice

---

.\*ndice:

# Objetivo

---

       A funcionalidade de formatar campos do tipo Data ou Moeda em um projeto de metadados está em desenvolvimento, ou seja, não está totalmente finalizada, algumas melhorias estão em andamento, e serão liberadas em breve.

       Entretanto, a partir da **versão 12.1.23**, é possível utilizá-la desde que os requisitos abaixo sejam obedecidos:

* Utilizar a formatação com o tipo de controle: Caixa de edição;
* Tipo de dados que podem utilizar o 'Formato': Float, Decimal (com tamanho e escala), Money, DateTime.

       Veja a seguir um exemplo.

# Exemplo

---

     O exemplo a seguir é da criação de um metadados simples, apenas com dois campos: ID e Data. Serão mostrados alguns formatos aceitos para o tipo Data.  
     Lembramos que para criar esse processo torna-se necessário conhecimento mínimo em como criar um Projeto de Metadados.

**1º Passo - Tipo de Dados:**

     Pata este exemplo foram criados os tipos de dados: Inteiro e Data

Clique para expandir

* Inteiro - Tipo de dados da linguagem: System.Int32 | Tipo de dados SQL: int | Tipo de Dados Oracle: number(10,0)
* Data2 - Tipo de dados da linguagem: System.DateTime | Tipo de dados SQL: datetime2 | Tipo de Dados Oracle: date

**2º Passo - Tabela:**

     Foi criada uma tabela com dois campos: ID e Data\_Teste.

Clique para expandir

* ID - Tipo: Inteiro
* Data\_teste - Tipo: Data2

******3****º Passo - Modelo de Negócio:**

     Foi adicionada a tabela criada no passo anterior em um novo modelo de negócio, na aba Estrutura de Dados.

     Na aba Controles, o campo Data\_Teste foi configurado com o Tipo de Controle 'Caixa de edição' e o formato: {0:d' de 'MMMM' de 'yyyy HH:mm:ss}:

Informações:

* Lembrando que o tipo de Controle deve ser o tipo Caixa de edição, obrigatoriamente.

     Ao clicar nas opções do campo Formato, é possível ver todos os formatos disponíveis para Moeda e Data/Hora. No rodapé é exibido um exemplo do formato selecionado:

Clique para expandir

******4****º Passo - Criar o Formulário:**

     Basta criar um novo formulário com o objeto de negócio criado no passo anterior. Certifique-se que na aba Apresentação, o campo Data está com o Formato preenchido e o Tipo de Controle é Caixa de edição.

******5****º Passo - Criar e gerar o Projeto de Metadados:**

     Após criar o novo projeto de metadados, gere-o. Neste exemplo, a tela ficou assim:

Informações:

* Devido a funcionalidade estar em desenvolvimento, o campo Data não possui máscara. O formato será aplicado depois que o usuário preencher o campo data e clicar em outra parte da tela do sistema, mudando o foco do campo.
Informações:

* A formatação dos campos em Data e Hora e Decimal está disponível apenas para as edições.
falsefalse

**Produto:** Framework

false

**Versão:** 12.1.21

false

**Processo:** Formatar campos do tipo Data ou Moeda

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
