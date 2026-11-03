---
content_hash: db9b7fb42540138e27271abe9b176c9bac592e3c7186a42b91e765d63bd16c4e
fetched_at: '2026-06-29T00:10:03.119256+00:00'
page_id: '452719015'
product: rm
source: tdn-rm
title: Validação da Base de Dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719015
version: 3
---

Neste módulo será possível realizar a verificação da base de dados no que diz respeito ao cadastro de funcionários, gerando logs de inconsistências.   
Para realizar a verificação da base de dados acesse: Folha Mensal | Validações | Validação da Base de Dados.  
Após acessar o módulo, o usuário deverá informar a seleção de funcionários para os quais deseja fazer a verificação.  
O sistema permite que escolher algumas verificações a serem realizadas:

* Duplicidade de CPF;
* Duplicidade de CTPS;
* Opção de não verificar funcionários demitidos até determinada data e de não verificar funcionários que serão admitidos no próximo mês;
* Desconsidera campos complementares.

**Observação:**

* Ao ser solicitada a verificação da base de dados, o sistema irá verificar também eventuais inconsistências no histórico de afastamento, como, por exemplo, afastamento sem informação do "tipo".
* Caso dois eventos do mesmo período de cálculo da folha tenham os seus Códigos de cálculo repetidos o arquivo de "Log" irá conter mensagens de alerta, já que no mesmo período isto não é permitido.
* Ao fazer a verificação da base o sistema irá conferir se o funcionário tem idade maior ou igual à 65 anos e apresentará um aviso que após a liberação da competência será acertado o campo TEM MAIS 65 ANOS (controle interno do sistema) preenchendo o mesmo com valor 1. Se o funcionário tem menos de 65 anos o sistema apresentará um aviso que após a liberação da competência será acertado o campo TEM MAIS 65 ANOS (controle interno do sistema) preenchendo o mesmo com valor 0. Vale lembrar que este aviso só será apresentado caso o campo referente esteja preenchido incorretamente.
* Para fazer a verificação da base é necessário, quando inserimos um dependente para o funcionário inserimos pelo menos um valor para os campos complementares dos DEPENDENTES, o sistema não insere nenhuma linha na tabela onde guarda os campos complementares dos dependentes se não tiver nenhum valor inserido. A verificação é feita cima desses campos complementares dos dependentes e não do funcionário.
* Para o parâmetro "Desconsidera campos complementares", o sistema não fará a consistência de erros nos campos complementares de todos os cadastros (Funcionários, Dependentes, etc.).  Marcando este parâmetro pode implicar em acumulo de inconsistências, principalmente quando da utilização de fórmulas nos campos complementares.
