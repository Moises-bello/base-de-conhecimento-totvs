---
content_hash: 7b83bc9bd27ef6581a892b6ac61af604c55f82b1ed936f70e45dc2bdaf60b1b6
fetched_at: '2026-06-29T00:09:30.836801+00:00'
page_id: '425458544'
product: rm
source: tdn-rm
title: Questões condicionais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458544
version: 15
---

Questão condicional, é a configuração onde uma ou mais questões na prova sejam habilitadas ou desabilitadas dependendo da resposta que o candidato marca para uma questão anterior.

10.101 - Conceitofade

## **01. Conceito**

A Instituição de Ensino pode parametrizar a Questão condicionais em três momentos:

**1°-** Opção condicional: é a opção de resposta da questão da prova que desencadeia uma ação condicional.

**2°-**Ação condicional: é a ação que será realizada caso o candidato marque uma opção condicional. Esta ação pode ser habilitar uma ou mais questões e desabilitar uma ou mais questões.

**3°-**Questão condicional: são as questões que foram adicionadas a prova pela configuração de ação "habilitar questão". Estas questões permanecerão ocultas na execução da prova e somente serão habilitadas se a opção condicional correspondente for marcada.

Ao configurar uma questão cujas opções de respostas encadeiam uma opção condicional (habilitar ou desabilitar), é possível relacionar uma opção de resposta a uma ação, seja ela habilitar uma nova questão do banco de questões ou desabilitar uma questão já existente na prova.

Ao habilitar uma nova questão é possível definir a ordem em que a questão aparecerá na prova.

Ao vincular as ações desejadas para uma opção de resposta, é possível voltar ao primeiro step do processo e configurar outra opção da mesma questão para que também seja condicional. O sistema guardará todas as configurações ao executar o processo.

O log de execução será apresentado ao final do processo com o estado atual de configurações de questões condicionais para a questão. Mesmo que não se faça nada no processo, o log mostrará se há ou não ações condicionais definidas para as opções de resposta daquela questão.

0.102 - Parametrizaçãofade

## **02. Parametrização**

A parametrização da Questão Condicional, só é possível se:

* A prova ser do tipo: Pesquisa de opinião;

* A Questão da prova deverá ser do tipo: Pesquisa

* Somente poderá ser habilitada uma questão em uma ordem posterior a questão cuja opção condicional correspondente foi marcada;
* Não é possível configurar ações condicionais que habilitem ou desabilitem questões a partir de respostas de questões abertas.
* Só será possivel alterar uma questão condicional , caso a prova não tenha sido executada por nenhum aluno.
0.103 - Execução do processofade

## **03. Parametrização da Questão Condicional**

Após cadastrar as [Questões](https://tdn.totvs.com/x/7f9bGQ) e vincular as mesmas na [Prova](https://tdn.totvs.com/x/tvxbGQ), executar o processo abaixo:

**03.1 -** Selecionar uma ou mais questões (que serão condicionais)  - Acessar a Prova | "Anexo" - Questões | "Processo" - Definir Questões Condicionais.

**03.2 -** Em seguida, selecionar qual é a resposta que será aplicada a questão condicional e clicar em: Avançar.

**03.3 -** Em seguida, o usuário será redirecionado para a lista de questões que foram adicionadas à Prova, a Instituição de Ensino deverá selecionar qual (quais) questão (ões) será (ão) desabilitadas, caso o Candidato/Aluno selecione a opção 'A' da pergunta XXXX.

**03.4 -** Caso necessário, a Instituição poderá adicionar uma nova questão que será habilitada, caso o Candidato/Aluno selecione a resposta 'A' da Questão XXXX.

Observação: A questão a ser incluída, não pode estar associada a Prova.

Para adicionar uma nova questão, a Instituição de Ensino deverá informar a Área e a Matéria. Após informar, o sistema irá exibir a questão no campo: Enunciado.

false

A partir da versão 12.1.31.229 será exibido apenas as Matérias e Questões da coligada logada.

Para incluir a nova questão, a instituição deverá clicar em: Adicionar.

Ao clicar em:  Adicionar, a Questão será adicionada a prova e será habilitada caso o Candidato/Aluno responda a opção 'A' da  questão XXXX.

Ao executar o processo, o sistema irá exibir um log, contendo a descrição do processo que foram realizados na configuração da Questão Condicional.

  

## **Execução da prova no Executor Web**

Ao executar a prova no RM Executor ou Executor Web as ações condicionais definidas devem ser ativadas no momento em que o candidato marcar a questão.

Caso o candidato retorne na questão e marque outra opção, aquelas ações desencadeadas anteriormente devem ser desfeitas e passará a habilitar e/ou desabilitar as ações (se houver) da nova opção marcada. Após a finalização da prova, na consulta ao ranking, somente serão exibidas as questões que estiverem habilitadas para o candidato no momento de sua finalização.
