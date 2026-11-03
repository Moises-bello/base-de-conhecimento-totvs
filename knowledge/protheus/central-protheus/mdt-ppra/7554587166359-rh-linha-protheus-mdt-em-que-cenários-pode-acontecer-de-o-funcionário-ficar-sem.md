---
article_id: 7554587166359
category: MDT - PPRA
content_hash: 0da61da32c79fb27496ab0119f8ea630fdea4553abfab328b78a3683fad16f22
fetched_at: '2026-06-28T22:44:27.215709+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: "RH - Linha Protheus - MDT - \t Em que cenários pode acontecer de o funcionário\
  \ ficar sem tarefa na integração com o SIGATAF/Middleware e o que fazer nesses casos"
type: support-article
updated_at: '2025-10-10T11:15:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7554587166359-RH-Linha-Protheus-MDT-Em-que-cen%C3%A1rios-pode-acontecer-de-o-funcion%C3%A1rio-ficar-sem-tarefa-na-integra%C3%A7%C3%A3o-com-o-SIGATAF-Middleware-e-o-que-fazer-nesses-casos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19996620712087) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Em que cenários pode acontecer de o funcionário ficar sem tarefa na integração com o SIGATAF/Middleware e o que fazer nesses casos?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução** Na integração do evento S-2240 ao SIGATAF/Middleware deve ser configurado o parâmetro **MV\_NG2TDES** que é responsável por definir qual a descrição das atividades exercidas pelo funcionário será enviada na tag <dscAtivDes> (para saber mais sobre o parâmetro MV\_NG2TDES acesse: <https://tdn.totvs.com/x/liWJJQ>).   
  
Caso o parâmetro esteja definido como "1" (sem aspas) o sistema irá considerar as tarefas do funcionário para saber qual descrição enviar na tag <dscAtivDes>. Porém, podem ocorrer situações em que o funcionário que está sendo enviado ao SIGATAF/Middleware esteja sem nenhuma tarefa vinculada e esse é um comportamento esperado. As rotinas que podem gerar o evento S-2240 nessa situação, ou seja, sem nenhum conteúdo na tag <dscAtivDes> são: cadastro de funcionário (GPEA010), transferência de funcionário (GPEA180), tarefas por funcionário (MDTA090) e cadastro de ambiente físico (MDTA165).

**Cadastro de funcionário (GPEA010):**

Ao realizar o cadastro de um novo funcionário ou alterar um funcionário existente (desde que ele não tenha um evento S-2240 comunicado ao SIGATAF/Middleware) é gerado o evento S-2240, porém caso o parâmetro **MV\_NG2TDES** esteja definido como "1" (sem aspas) não existe como vincular uma tarefa ao funcionário antes de finalizar esse cadastro. Dessa forma ao finalizar o cadastro de um funcionário na rotina GPEA010 o evento S-2240 será gerado com a tag <dscAtivDes> em branco. Nesse caso, após realizar o cadastro do funcionário e ser gerado o evento S-2240 com a tag vazia, deve-se vincular o funcionário cadastrado/alterado a alguma tarefa para que o sistema saiba que descrição enviar na tag <dscAtivDes>. Após vincular o funcionário a alguma tarefa o sistema irá retificar automaticamente o evento S-2240 ao SIGATAF/Middleware e dessa forma irá enviar o conteúdo da tag <dscAtivDes> preenchida.

**Transferência de funcionário (GPEA180):**

Ao realizar a transferência de empresa ou filial de um funcionário é gerado o evento S-2240, porém caso o parâmetro **MV\_NG2TDES** esteja definido como "1" (sem aspas) não existe como vincular uma tarefa ao funcionário na empresa ou filial destino antes de realizar a transferência da filial origem. Dessa forma ao finalizar a transferência do funcionário para a empresa ou filial destino através da rotina GPEA180 o evento S-2240 será gerado com a tag <dscAtivDes> em branco. Nesse caso, após realizar a transferência do funcionário e ser gerado o evento S-2240 com a tag vazia, deve-se entrar na empresa ou filial destino e vincular o funcionário transferido a alguma tarefa para que o sistema saiba que descrição enviar na tag <dscAtivDes>. Após vincular o funcionário a alguma tarefa na empresa ou filial destino o sistema irá retificar automaticamente o evento S-2240 ao SIGATAF/Middleware e dessa forma irá enviar o conteúdo da tag <dscAtivDes> preenchida.

**Tarefas por funcionário (MDTA090):**

Ao realizar a inclusão, alteração ou exclusão de uma tarefa a um funcionário pela rotina MDTA090 é gerado o evento S-2240, porém caso o parâmetro **MV\_NG2TDES** esteja definido como "1" (sem aspas) pode ocorrer de que ao finalizar a exclusão de alguma tarefa o funcionário fique sem nenhuma outra tarefa vinculada e envie o evento com a tag <dscAtivDes> em branco. Um exemplo é o seguinte, caso o funcionário esteja sendo excluído da única tarefa que realiza, após salvar o cadastro, ficará sem nenhuma tarefa vinculada e por esse motivo a tag será enviada vazia. O sistema permite concluir o cadastro pois aceita que o funcionário seja excluído de uma tarefa antes de ser vinculado a outra. Dessa forma, após excluir o funcionário da única tarefa que realiza e enviar a tag <dscAtivDes> vazia no evento S-2240, deve-se vinculá-lo a alguma outra tarefa para que o sistema saiba que nova descrição enviar. Após vincular o funcionário à nova tarefa exercida o sistema irá retificar automaticamente o evento S-2240 ao SIGATAF/Middleware e dessa forma irá enviar o conteúdo da tag <dscAtivDes> preenchida.

**Cadastro de ambiente físico (MDTA165):**

Ao realizar o cadastro de um um funcionário a um ambiente pela rotina MDTA165 é gerado o evento S-2240, porém caso o parâmetro **MV\_NG2TDES** esteja definido como "1" (sem aspas) e não haja nenhuma tarefa vinculada ao funcionário através da rotina de tarefas por funcionário (MDTA090) pode ocorrer de que o evento S-2240 seja enviado com a tag <dscAtivDes> em branco. Dessa forma, após cadastrar o funcionário ao ambiente e enviar a tag <dscAtivDes> em branco no evento S-2240, deve-se vincular o funcionário a uma tarefa através da rotina MDTA090 para que o sistema saiba que descrição de atividades enviar para o funcionário. Após vincular o funcionário a uma tarefa o sistema irá retificar automaticamente o evento S-2240 ao SIGATAF/Middleware e dessa forma irá enviar o conteúdo da tag <dscAtivDes> preenchida.  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
