---
content_hash: 9251cd89687b7b1191ba2daccbd16085eaf667646b41d7be01aa8f0e5445d510
fetched_at: '2026-06-29T00:08:24.594481+00:00'
page_id: '270898632'
product: rm
source: tdn-rm
title: Lookup Metadados
type: documentation
url: https://tdn.totvs.com/display/LRM/Lookup+Metadados
version: 29
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é mostrar que para utilizar o lookup do Metadados, é necessário realizar algumas configurações.

Veja exemplo de como criar ;

Veja exemplo de como criar ;

# Configuração:

---

       Ao utilizar o lookup no metadados, o campo que o usuário deseja realizar a pesquisa deve ser o último da lista de chaves informadas.

Importante

Não é possível utilizar um campo Imagem no relacionamento do Lookup.  
Por este motivo, a partir da versão 12.1.26, no cadastro da Tabela do metadados, não é possível marcar a opção "Descrição para Lookup" em campos do tipo 'image' (SQL) ou 'blob' (Oracle).

Em versões anteriores, caso o projeto de metadados tenha sido gerado com o campo Imagem em um lookup, é necessário alterar o cadastro da Tabela, desmarcando a opção "Descrição para Lookup". Depois, ajustar o Modelo de Negócio e Apresentação de Formulários, removendo o relacionamento para o campo do tipo imagem. Em seguida, regerar o Projeto de Metadados. Se o campo do tipo Imagem permanecer no relacionamento, um erro será apresentado na tela.

Nas versões superiores a 12.1.24.168 e 12.1.25.109, quando o projeto já foi gerado com o campo Imagem em um lookup, é necessário reabrir o cadastro da Tabela, Modelo de Negócio e Apresentação de Formulários, refazer as associações do lookup, salvar os registros, garantindo que o relacionamento foi ajustado e regerar o Projeto de Metadados.

**Exemplo:** Ao utilizar a action do Cliente/Fornecedor e o usuário deseja realizar uma pesquisa pelo CPF/CNPJ do cliente, é necessário as seguintes configurações:

* Adicionar a action FinCFOAction
* Adicionar a Coligada como primeira chave da pesquisa
* Adicionar o Código Cliente/Fornecedor como segunda chave da pesquisa

falseObservação:

Os campos adicionados acima fazem parte da **chave primária**. Agora deve-se adicionar o campo que será utilizado para pesquisa.

O Comportamento de cadastro de Action anexa é diferente ao de criar um LookUP em metadados.

Ao criar um LookUp em metadados o mesmo utiliza do método DoReadLookUpView do DataServer correspondente da action informada no LookUP. Estes campos são configurados pela equipe responsável por cada DataServer.

Caso o seja necessário adicionar algum campo no LookUp a demanda deve ser direcionada para equipe responsável avaliar se o campo será adicionado ou não no LookUp.

* Adicionar o campo CPF/CNPJ da action (Campo em que o usuário deseja realizar a pesquisa)

|  |
| --- |

       Ao gerar o projeto metadados o campo de CPF/CNPJ será utilizado como campo de pesquisa para o cliente fornecedor.

|  |
| --- |

Atenção

Caso uma das chaves do LookUp possua relacionamento em algum dos itens da visão , o LookUp filtrará os dados automaticamente, respeitando o valor do campo.

Exemplo:

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Lookup Metadados

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
