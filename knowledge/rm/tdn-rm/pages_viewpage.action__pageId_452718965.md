---
content_hash: 1fe67f0a376a6f9b903aebcf8129b3825c9eb7b7814634f3831d8d01ed668875
fetched_at: '2026-06-29T00:10:02.575680+00:00'
page_id: '452718965'
product: rm
source: tdn-rm
title: RNT (Registro das Necessidades de Treinamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718965
version: 2
---

**RNT (Registro das Necessidades de Treinamento)**

Por este cadastro é possível incluir, editar e excluir o Registro das Necessidades de Treinamento da pessoa.

**Observações**

-  O status do RNT poderá ser controlado da seguinte forma:

* Quando a demanda for criada então o status será Pendente;
* Quando a demanda for treinada por Turma e houver o fechamento da avaliação de conhecimento então o status será Atendida;
* Quando for preenchido o campo "Justificativa para não atender a demanda" então o status será Cancelada.

- Somente RNT´s com status de "Pendente" e "Cancelada" podem ser excluídas.

- O campo "Tipo do RNT" contém informações da tabela dinâmica de código RNTTPDEMAN.

- Se o RNT definido for treinado por uma Turma, após o fechamento da mesma os dados serão atualizados no cadastro do RNT.

- O campo "Data de Registro" não pode ser maior do que a data do dia.

- No campo "Pessoa que detectou demanda" será exibido somente funcionários.

Será possível também realizar a "Importação de RNT" por um arquivo XML, para isto é necessário:  
   
Acessar o sistema "Integração" | Integração | Conceito, criar um novo conceito que tenha como origem um arquivo XML, dentro do formato exigido por um arquivo XSD. Feito isso, informe o arquivo XML a ser importado, e execute o processo: "Processar Conceito" para que as informações do RNT sejam importadas.

**Atenção**

Para qualquer ícone desabilitado, verifique com o Supervisor as permissões do usuário em questão em Cadastros| Seguranças| Perfis| pasta Acesso a menus.

|  |  |
| --- | --- |
|  | Como Fazer |

---

Importação de RNT - Modelo de Arquivo XML  
Importação de RNT - Modelo de Arquivo XSD
