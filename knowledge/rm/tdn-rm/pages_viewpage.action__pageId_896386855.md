---
content_hash: 32c3d3f1b99948f9a1d60a29102eceba723e995240960e7bd0263e447baa974b
fetched_at: '2026-06-29T00:12:01.628756+00:00'
page_id: '896386855'
product: rm
source: tdn-rm
title: 9 – Como criar seu primeiro teste automatizado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=896386855
version: 6
---

Antes de começar a criar uma automação, certifique-se que todos os pontos abaixo estão claros e entendidos:

**[Obedeça a Pirâmide de Teste](https://tdn.totvs.com/pages/viewpage.action?pageId=896383405):** Vamos sempre priorizar testes de integração (WebService, API´s) antes de partir para testes de interface gráfica (link).

**[Conheça o que irá testar:](https://tdn.totvs.com/pages/viewpage.action?pageId=896383809)** Antes de automatizar, compreenda completamente a funcionalidade e os requisitos antes de criar a automação (Link)

**[Documentação](https://tdn.totvs.com/pages/viewpage.action?pageId=896383866):** Mantenha os testes bem documentados, descrevendo claramente as pré-condições, passos e resultados esperados (link)

**[Defina a arquitetura do seu teste](https://tdn.totvs.com/pages/viewpage.action?pageId=896384883):** Defina se o teste será individual, de jornada ou sistêmico e se será dependente ou independente de base de dados ou outros testes (link)

## 9.1 - Criando um teste de Cadastro no RM

1 – Defina o objetivo do seu teste. Se o seu objetivo é testar somente o cadastro ou se você quer testar uma rotina completa e for necessário começar pelo cadastro. Se for somente testar o cadastro, conseguirá criar um teste que seja independente de outros testes, mas se for testar uma funcionalidade, lembre-se que os dados deste cadastro serão utilizados nos próximos testes.

2 - O segundo passo é fazer o cadastro manualmente e entender como ele funciona, quais são suas pré-condições, os dados necessários e qual resultado esperar.

3 - Existe a possibilidade de deletar este registro cadastrado e criá-lo novamente? Se sim, ótimo, conseguiremos refazer o processo quantas vezes precisar, fazendo manualmente, criando o teste, validando o teste e testando a automação para ver se deu tudo certo. Se não for possível excluir o registro cadastrado, será necessário restaurar a base novamente para conseguir criar o teste e fazer a validação. Para testar o projeto, também teremos que restaurar o backup da base fixa de automação novamente.

4 – Depois de fazer o cadastro manualmente, crie o Caso de Teste do mesmo, informando detalhadamente as pré-condições, passos e resultados esperados

5 – Escolha qual tipo de Atividade do TOTVS Automação de Testes melhor se encaixa para criar a automação. Vamos sempre olhar para a Pirâmide de Teste e dar preferência para testes de integrações (API´s, WebServices).

6 – Defina a arquitetura do seu teste. Este cadastro será atômico (Não depende de nada) ou se dependerá de dados da base. Se será um teste dependente ou independente de outros testes. Escolha se terá testes individuais, Jornada ou Sistêmico.

7 – Crie o seu teste automatizado com o TOTVS Automação de Testes. Verifique os exemplos de uso no help de cada atividade.

8 – Valide o seu teste. Todo teste automatizado deve ter uma validação detalhada do resultado. Utilize as atividades do TOTVS Automação de Testes para validar se o seu teste executou com sucesso (Comparação de Banco, arquivos, diretório, API´s, Código C#). Você consegue validar inclusive as integrações que este cadastro possui.

9 – Limpe o ambiente para que o próximo teste seja executado com o ambiente íntegro. Este processo já é feito automaticamente pelo TOTVS Automação de Testes.

## 9.2 - Criando um teste de processos do RM

* O teste de processo segue o mesmo fluxo de um teste de cadastro.
* Avalie se o processo pode ser re-executado para facilitar a criação do teste. Caso não seja possível, terá que restaurar a base caso necessite executar o processo novamente.
* Se o processo que for automatizar existir muitas pré-condições, opte por criar testes dependentes de base pegando os dados já existentes. Desta forma, você focará seus objetivos no processo que quer testar, mas será um teste dependente de base. Exemplo: Cálculo da folha de pagamento.

## 9.3 - Criando um teste de uma funcionalidade completa (Jornada)

* Para testes de Jornada, o mesmo dado seguirá durante toda a jornada da funcionalidade e criaremos testes que são dependentes.
* Faça o uso da criação de Sub-Projetos para facilitar a execução dos testes de Jornada.
* Sub-Projetos é quando usamos um projeto como se fosse uma atividade (Nodo) dentro de outro projeto. Exemplo: Tenho um projeto de Jornada de internação de paciente (Projeto Pai) e dentro dele tenho todos os projetos relacionados aos cadastro e processos que fazem parte da jornada de internação de paciente (Projetos filhos).

## 9.4 - Dicas importantes na criação dos testes automatizados:

* Criando um teste de cadastro, avalie qual o comportamento do código (chave primária) do mesmo. Se for digitável, opte por colocar um código maior. Ex: 9999.
* Se o código do cadastro for AutoIncremento (O sistema é que informa), avalie a necessidade de alterar a GAUTOINC deste campo para colocar um código maior.
* Colocar um código maior se faz necessário para que seus testes automatizados tenham menos manutenções caso a sua base fixa de automação tenha sofrido alterações com novos registros, impactando testes que são dependentes de base.
* Na base de dados de Automação, dê nome para os dados de forma que você consiga identificar que é utilizado na automação. Se for usar algum dado da base para a automação ou for criar um dado novo, informe claramente caso tenha uma descrição que é utilizada na automação. Desta forma, facilitará a identificação e análise dos mesmos.
* Exemplo de nome do cadastro de escola: Escola Teste Automatizado TOTVS Automação de Testes.
* Se for necessário alterar dados na criação dos testes automatizados, lembre-se de que esta mesma alteração deve ser realizada na base fixa de automação para que o seu teste funcione ou automatize esta alteração.

[← Anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=896384883) | [Próximo →](https://tdn.totvs.com/display/LRM/10+-+Validando+seus+testes%3A+Como+garantir+que+eles+funcionam)
