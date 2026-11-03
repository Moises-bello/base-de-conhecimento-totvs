---
content_hash: 017a01e8bb22d9e3c6e7f15dd182102afa6f6baafc5a29391466f1e86d8094b6
fetched_at: '2026-06-29T00:10:07.923349+00:00'
page_id: '452719473'
product: rm
source: tdn-rm
title: Exames Realizados
type: documentation
url: https://tdn.totvs.com/display/LRM/Exames+Realizados
version: 3
---

**Exames Realizados**

**Atenção**

- Se o parâmetro "Entidade padrão para inclusão de exames no Prontuário", localizado em Opções| Parâmetros| RM Vitae| Geral, pasta Seg e Med Trab| Exames, tiver uma entidade informada, esta entidade será exibida como padrão na inclusão de exames realizados, caso o exame tenha mais de uma entidade conveniada.

- O parâmetro "Exame audiométrico" deve conter o exame de audiometria utilizado na empresa, para que quando incluído como exame realizado, o sistema apresente a pasta Audiometria para preenchimento do resultado deste exame.

- Para qualquer ícone desabilitado, verifique com o Supervisor as permissões do usuário em questão em Cadastros| Seguranças| Perfis| pasta Acesso a menus.

**Observações**

- No campo "Cód. da entidade" serão visualizadas todas as entidades conveniadas ao exame selecionado, que foram previamente cadastradas no menu SMT| SMT| PCMSO| Exames| Convênios.

- Os tipos de exames disponíveis são: Admissional, Demissional, Periódico, Retorno ao trabalho e Mudança de função.  
   
**Considerações para o eSocial (S-2220)**

* A "Ordem do Exame" será definida de acordo com a marcação da flag "Exame Referencial", retornando Referencial caso marcada ou Sequencial, caso desmarcada.
* O campo "Interpretação Exame" deverá ser preenchido obrigatoriamente para o eSocial, onde estará disponíveis as opções EE, SC e SC+ conforme NR7.

O resultado do exame será definido de acordo com as seguintes "combinações":

|  |  |
| --- | --- |
| **Cadastro do SSO** | **Valor a ser informado no XML** |
| Campo "Normal" marcado. | 1 - Normal |
| Campo "Anormal" marcado e campo "Tipo anormalidade" em branco. | 2 – Alterado |
| Campo "Anormal" marcado e campo "Estável" marcado. | 3 – Estável |
| Campo "Anormal" marcado e campo "Agravamento" marcado. | 4 – Agravamento |

Por este cadastro é possível controlar:

**Informações Clínicas**

- Nesta pasta são visualizadas as informações clínicas que foram previamente cadastradas no menu SMT| SMT| PCMSO| Exames| Itens de informação clínica e vinculadas aos exames.  
Os Itens de Informação Clínica podem ter os Tipos de Valor abaixo:

* - Numérico
* - Opções
* - Texto (linha única ou múltiplas linhas)

Para os tipos "Numérico" e "Opções", no lançamento de resultado de exames, poderá ser exibida uma legenda, contendo uma caixa de cor e nome, que são atualizadas de acordo com o valor informado pelo usuário.

**Atenção:**

Essa parametrização é realizada nos anexos "Faixas de Item de Informação Clínica" e "Opções de Item de Informação Clínica".

**Observações para o Tipo de Valor-Numérico:**

- Se nenhuma faixa for encontrada, nenhuma legenda será exibida.

- Se apenas uma faixa for encontrada, será exibida legenda com a cor e o nome da faixa.

- Se mais de uma faixa for encontrada, a faixa que tiver uma Consulta SQL será identificada e a sentença da consulta SQL será executada, passando ao parâmetro CODPESSOA o valor do código da pessoa a que pertence o exame selecionado. Se a consulta retornar um ou mais registros, será exibida legenda com a cor e o nome da faixa em questão, senão será exibida legenda com a cor e nome da faixa que não contém a consulta SQL.

- Nos casos em que existirem mais de uma faixa com Consulta SQL, será exibida legenda com a cor e nome da primeira faixa em que a consulta SQL retornar um ou mais registros.

- Se forem identificadas apenas faixas com Consulta SQL e nenhuma das consultas retornar um ou mais registros, nenhuma legenda será exibida.

**Observação para o Tipo de Valor-Opções:**

- Se existir para o item uma Opção cadastrada será exibida a legenda com a cor e nome cadastrados.

**Atenção**

- Os itens de informação clínica podem ser associados a uma tabela dinâmica que tenha a finalidade 2 e que estejam cadastradas no menu Cadastros| Tabelas Dinâmicas.

**Audiometria**

Esta pasta destina-se ao preenchimento dos valores definidos durante o exame audiométrico e ainda é possível representar por meio de gráficos o resultado da audiometria do funcionário, considerando ouvido esquerdo e ouvido direito.

**Avaliação Física**

Neste módulo será possível realizar um controle específico de avaliação física. Além dos controles pertinentes de uma avaliação física, serão calculados automaticamente valores como: "IMC", "RCQ", "Percentual de Gordura", "Flexão de Braço" e "Flexibilidade".

**Observação**

- Os valores possíveis de serem selecionados na frequência constam da tabela dinâmica INTAUDIO possível de ser editada pelo menu Cadastros| Tabelas dinâmicas.

- O gráfico será gerado corretamente apenas quando existirem os dados informados na pasta Audiometria| Dados.
