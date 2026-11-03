---
content_hash: 24665c46baf7ad925dbc0251ac7eed07b3b550446e79393a049c7c330ecb252a
fetched_at: '2026-06-29T00:09:33.789790+00:00'
page_id: '425459054'
product: rm
source: tdn-rm
title: Agendamento/Envio de mensagens de notificações temporais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459054
version: 15
---

O processo de agendamento/Envio de mensagens de notificações temporais tem como finalidade executar as mensagens de notificações que são classificadas como temporais.   
São elas:

* Pendências financeiras do aluno;
* Frequência do aluno próximas do limite ou excedido;
* Pendências de matrícula.

Envio de e-mails por pacotes

É possível parametrizar no **RM** o envio de e-mails em lotes utilizando a mesma conexão SMTP, reduzindo a sobrecarga causada pela reabertura da conexão a cada mensagem enviada.  
Essa opção pode melhorar o desempenho em ambientes com alto volume de envios.

Para mais informações, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=1021200817).

Filtros do público alvo

O público alvo e definido pelos seletores, no caso em que tipo de consulta for pelo padrão do sistema os seletores são:

* Período letivo;
* Código do curso;
* Código da habilitação;
* Código da turma.

## 

No filtro de **público-alvo**, será possível enviar a notificação **apenas para um grupo de usuários ou para um único usuário**, não sendo permitido **selecionar ambas as opções simultaneamente**.

Além disso, **somente será possível prosseguir** após preencher **todas as informações referentes aos públicos-alvo selecionados**.  
Por exemplo, seguindo o caso acima, o envio só poderá continuar após o preenchimento dos dados para os grupos **“Alunos, Pais e Responsáveis Acadêmicos e Financeiros”, “Coordenadores” e “Professores”**.

Parâmetro: Considerar situações de matrícula que não definem 'aluno ativo' no período letivo

**Descrição:**  
Permite incluir, nos filtros e envios de notificação, alunos cuja situação de matrícula não é classificada como “ativa” no período letivo.

**Uso recomendado:**  
Ative este parâmetro apenas quando for necessário considerar alunos em outras situações (por exemplo, trancado ou transferido) nos processos de envio da notificação.

Parâmetro: Incluir somente alunos com matricula em disciplina(s) em curso na turma

Quando este parâmetro estiver habilitado, os usuários receberão notificações apenas se o aluno possuir **ao menos uma matrícula ativa** em alguma disciplina vinculada à turma selecionada.

O exemplo acima mostra onde define o aluno como matriculado/cursando uma disciplina

**Observações:**  
Este parâmetro **somente poderá ser ativado** caso o usuário **selecione uma turma**.

Este parâmetro **somente estará disponível** no publico alvo **"Alunos, Pais e Responsáveis acadêmicos e financeiros"**

Este parâmetro **somente estará disponível** no ensino básico

Se o tipo de consulta for por sentença sql e o tipo de saída for por e-mail então a consulta necessita do campo e-mail. Caso a saída seja por notificação fluig será necessário informar os campos: codcoligada, idhabilitacaofilial, codcurso, nomecurso, codhabilitacao, email, codusuario e rh.   
Quando a seleção é de um ou mais tipos de notificação e a mensagem estiver parametrizada para envio por e-mail a todos os destinatários , os que não possuírem e-mail cadastrados serão ignorados.  
Quando a seleção é de um ou mais tipos de notificação e a mensagem estiver parametrizada para notificação no fluig, todos os destinatários que não estiverem cadastrados no fluig serão ignorados.

## Consulta SQL

A partir das versões 12.1.29.283, 12.1.31.199 e 12.1.32.136 foi disponibilizado na seleção do público alvo por consulta SQL a opção para visualizar os resultados gerados pela consulta.

Esta opção permite ao usuário validar corretamente o total de pessoas e também quais são as pessoas que atendem as definições da consulta SQL.

Importante

Caso a consulta utilize parâmetros, estes devem ser preenchidos para que a visualização ocorra.

Após a visualização da consulta, é possível retornar para a sentença, para selecionar outra consulta ou até mesmo fazer uma alteração na consulta e validar seu resultado antes da execução do processo. 

 Veja Também

---

[Documento Técnico - Central de Notificação II](http://tdn.totvs.com/display/LRM/DT_Central_Notificacao)
