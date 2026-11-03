---
content_hash: d2154d6e49f07ab5d3298e4f062989eb158e1d4066f21445386079757a5998d7
fetched_at: '2026-06-29T00:10:10.723220+00:00'
page_id: '452719919'
product: rm
source: tdn-rm
title: RNT
type: documentation
url: https://tdn.totvs.com/display/LRM/RNT
version: 2
---

**RNT**

Por este cadastro é possível incluir, editar e excluir o Registro das Necessidades de Treinamento da pessoa.

**Observações**

Os status do RNT poderão ser controlados da seguinte forma:

1) Quando a demanda for criada então o status será Pendente;

2) Quando a demanda for treinada por meio da Turma e houver o fechamento da avaliação de conhecimento então o status será Atendida;

3) Quando for preenchido o campo "Justificativa para não atender a demanda" então o status será Cancelada.

* Somente RNT´s com status de "Pendente" e "Cancelada" podem ser excluídas.
* O campo "Tipo do RNT" contém informações da tabela dinâmica de código RNTTPDEMAN.
* Se o RNT definido for treinado por meio de uma Turma, após o fechamento da mesma os dados serão atualizados no cadastro do RNT.
* O campo "Data de Registro" não pode ser maior do que a data do dia.
* No campo "Pessoa que detectou demanda" será exibido somente funcionários.

Será possível também realizar a "Importação de RNT" por um arquivo XML, para isto é necessário acessar o sistema "Integração" | Integração | Conceito, criar um novo conceito que tenha como origem um arquivo XML, dentro do formato exigido por um arquivo XSD.

Feito isso, informe o arquivo XML a ser importado, e execute o processo: "Processar Conceito" para que as informações do RNT sejam importadas.

**Atenção**

Para qualquer ícone desabilitado, verifique com o Supervisor as permissões do usuário em questão em Cadastros| Seguranças| Perfis| pasta Acesso a menus.

|  |  |
| --- | --- |
|  | Como Fazer |

---

Importação de RNT - Modelo de Arquivo XML  
Importação de RNT - Modelo de Arquivo XSD
