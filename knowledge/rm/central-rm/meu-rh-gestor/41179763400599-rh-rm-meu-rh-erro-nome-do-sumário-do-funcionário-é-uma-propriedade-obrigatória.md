---
article_id: 41179763400599
category: Meu RH - Gestor
content_hash: 5f6494f8aec9833c5c3ecf463ea4af74c0ad9636a1003dda5bed075e46c9f441
fetched_at: '2026-06-28T22:47:32.330614+00:00'
product: rm
section_id: 1500000861742
source: central-rm
title: RH - RM - Meu RH - Erro nome do sumário do funcionário é uma propriedade obrigatória
type: support-article
updated_at: '2026-06-12T17:55:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41179763400599-RH-RM-Meu-RH-Erro-nome-do-sum%C3%A1rio-do-funcion%C3%A1rio-%C3%A9-uma-propriedade-obrigat%C3%B3ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41179776672663) Tempo aproximado para leitura: **00:03:40 min**  
  
**Ocorrência**  
Ao acessar o Meu RH com um Gestor e acessar alguma tela que irá trazer seus subordinados, como Gestão de Férias, Minha Equipe e outros, é exibida a mensagem de erro: *"Nome do sumário do funcionário é uma propriedade obrigatória."*  
*![](https://centraldeatendimento.totvs.com/hc/article_attachments/41179776673815)*  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
Esse erro acontece quando o sistema está parametrizado para "Exibir o nome social" e o campo de Nome Social está com o valor em BRANCO no banco de dados.  
  
**Solução**  
Para solucionar essa ocorrência existem duas possibilidades:

1- O campo NOMESOCIAL da tabela PPESSOA deve estar com o valor NULL ou possuir de fato o NOME SOCIAL do colaborador.

2- Desabilitar a opção para Exibir o nome social conforme a documentação: [**RH - RM - Meu RH - Como apresentar o nome social**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8928320110103)

**Exemplo:**  
1. Utilizando a pessoa de código 3 - MARIACONCEICEO ASSIS conseguimos identificar que o campo NOMESOCIAL está em branco, um espaço por exemplo, mas possui algum preenchimento por não estar como NULL.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41179763382295)

2. Acessando o menu MINHA EQUIPE, o erro é apresentado pois o sistema está parametrizado para exibir o NOME SOCIAL.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41179776681111)

3. Após preencher o campo do NOME SOCIAL ou alterá-lo para NULL, realizamos um novo acesso a tela com erro;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41179763386519)

4. O erro deixou de ser apresentado;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41179763387415)

**Importante**  
Caso o erro ocorra apenas para determinados gestores ou para um gestor específico, isso indica que o colaborador que possui a inconsistência cadastral mencionada anteriormente não está vinculado a esses gestores como subordinado, ou não é um subordinado direto deles.

Dessa forma, como o colaborador com a inconsistência não é carregado na consulta realizada por esses gestores, o erro não é apresentado nesses casos.
