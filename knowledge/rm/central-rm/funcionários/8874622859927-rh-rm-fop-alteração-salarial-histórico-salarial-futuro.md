---
article_id: 8874622859927
category: Funcionários
content_hash: 471a8a253c8868fc534cf9c0a4c6c13fabca012f953e5e714f739e4ba227ad0f
fetched_at: '2026-06-28T22:47:03.217339+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: 'RH - RM - FOP - Alteração Salarial: Histórico Salarial Futuro'
type: support-article
updated_at: '2024-10-23T22:14:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8874622859927-RH-RM-FOP-Altera%C3%A7%C3%A3o-Salarial-Hist%C3%B3rico-Salarial-Futuro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:03:40 min  
  
Dúvida**  
Como realizar alteração salarial futura?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - 12.1.2205.131 e superiores  
  
**Solução**Possibilitar realizar alteração salarial para competências futuras, sem alterar o salário diretamente no cadastro do funcionário (PFUNC), para isso disponibilizamos o parâmetro "**Utiliza controle de alteração salarial futura**", onde o sistema passa a armazenar as alterações salariais futuras em um novo cadastro.   
  
Para atualizar o cadastro do funcionário com esse novo salário, o usuário poderá parametrizar a atualização na liberação de competência ou executar o processo **Efetivar Alteração Salarial**.

**Observação**  
Lembrando que, nenhuma rotina do produto irá buscar o salário desse novo cadastro, continuará buscando o salário do cadastro do funcionário.  
  
1.Para atender essa demanda foi necessário a criação do anexo "Histórico Salarial Futuro", e para a liberação desse anexo é necessário a execução do script pelo aplicativo RM.Atualizador.exe.

![](https://tdn.totvs.com/download/attachments/687158765/image2021-9-8_9-20-29.png?version=1&modificationDate=1652970707523&api=v2)

2.Acesse o menuRH | Funcionário | Restrições Cadastrais e marque o parâmetro "**Utiliza controle de alteração salarial futura**".

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8874323293207/mceclip0.png)  
  
3.Para realizar a alteração salarial global para competência futura, deverá acessar o menu RH | Folha de Pagamento | Administração de Pessoal l Alteração de Salário.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8874379469335/mceclip1.png)  
  
4.Ao preencher o campo "**Data da Mudança**" com uma data posterior a competência atual, será apresentada a mensagem abaixo:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8874422826519/mceclip2.png)  
  
5.Ao avançar poderá realizar a alteração utilizando "Percentual | Fórmula ou Tabelas Salariais":   
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8874459899543/mceclip3.png)  
  
6.Ao finalizar o processo será apresentada a mensagem abaixo:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8874477946647/mceclip4.png)  
  
**ATENÇÃO**  
Alteração salarial realizada para próxima competência.   
Para visualizar os dados deverá acessar o anexo Histórico Salarial Futuro.  
Para atualizar o salário do funcionário e o histórico salarial é necessário   
liberar a competência ou executar o processo Efetivar Alteração Salarial.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8874562064663/mceclip5.png)  
  
**Saiba Mais**  
[Histórico Salarial Futuro](https://tdn.totvs.com/pages/viewpage.action?pageId=687158765#1-1)
