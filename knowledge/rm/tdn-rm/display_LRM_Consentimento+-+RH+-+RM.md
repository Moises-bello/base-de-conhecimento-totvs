---
content_hash: f8456bce5ac9b281e0f7f8b65629f17a00caf9609c1875977ac874bce50e7a9b
fetched_at: '2026-06-29T00:10:47.977292+00:00'
page_id: '561633820'
product: rm
source: tdn-rm
title: Consentimento - RH - RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Consentimento+-+RH+-+RM
version: 21
---

Neste artigo será descrito o passo a passo para a parametrização do consentimento para o Banco de Talentos e o Processo Seletivo.

## **Introdução**

Devido as necessidades criadas pela Lei Geral de Proteção de Dados (LGPD) foi preciso a inclusão do consentimento nos cadastros externos da empresa.

#### Requisitos:

* Versão: 12.1.29
* Possuir acesso à Internet.
* Estrutura de rede estável, para que haja trafego de dados sem interrupção.
* RM devidamente configurado e serviço Rest habilitado em seu host.

## **Configurações inicias TOTVS Gestão de Pessoas (RM)**

Para habilitar o cadastro do Consentimento é necessário configurar o sistema.

##### **Parametrizador**

Acesse o Parametrizador do TOTVS Gestão de Pessoas (RM). No item 07.00 - Configurações → 07.00.00.00 - Preferências → 07.00.00.00.01 - LGPD será encontrado a opção para habilitar a utilização do consentimento no sistema.

**Observação:** **Após marcar o parâmetro é necessário dar permissão nos novos menus para o usuário.**

## **Cadastro do consentimento**

Na aba de Planejamento e Captação se encontra o novo menu **Consentimento LGPD**onde é feito o cadastro do consentimento.

Ao clicar para incluir um novo consentimento uma tela é apresentada perguntado se o usuário quer ou não criar um consentimento com base em outro já cadastrado. Se for o primeiro consentimento basta clicar em OK.

Se for selecionado algum consentimento, os campos de Descrição do Consentimento, Texto do Consentimento e Orientação de menor, serão preenchidos de acordo com o consentimento selecionado, caso contrário os campos ficarão em branco.

### Primeira Aba Identificação:

Dados Gerais do Consentimento.

**1 - Código Identificador do Consentimento**.

**2 - Data início da validade do Consentimento**.

**3 - Data de término da validade do Consentimento.**

**4 - Descrição do Consentimento.**

### Segunda Aba Consentimento:

Aqui deve ser redigido o texto do consentimento que será apresentado no Banco de Talentos para ser aceito pelos usuários.

É possível utilizar a funcionalidade **Abrir** para buscar e importar arquivos do tipo RTF e Word.

**Observação:** **Não é permitido a inclusão de imagens no texto.**

### Terceira Aba Orientação para menores de Idade:

Aqui deve ser redigido o texto que será apresentado para o menor de idade, para que ele possa comprovar o aceite do consentimento pelos seus responsáveis.

Importante: **Ao finalizar o cadastro não será possível modificar a Data Inicio e o Texto do Consentimento. Além disso, se a data atual estiver entre as datas início e fim da** **vigência****do consentimento, este já será considerado ativo e será apresentado no Banco de Talentos para ser aceito. Então não faça o cadastro de consentimento sem que tenha certeza que este está correto, pois não será possível modificá-lo após ser salvo e não será possível excluí-lo caso alguém o aceite.**

## **Enviar E-mail para Candidatos**

Este processo tem o intuito de enviar um e-mail para todos os candidatos que não estão consentidos com o consentimento selecionado.

A mensagem deve ser redigida pelo usuário utilizando a funcionalidade de Mensagem Customizada encontrada na Aba de Configuração. Esta mensagem deve conter o que o candidato deve fazer para aceitar ou rejeitar o novo consentimento e não deve conter um Relatório.

**Observação:** Este processo só pode ser executado para consentimentos vigentes.

## **Consentimento no Banco de Talentos:**

A partir do momento que um consentimento fica Ativo, ou seja, a data início é anterior ou igual a data atual, este consentimento é apresentado no Banco de Talentos para que seja aceito pelos usuários. Desta forma qualquer candidato que se cadastre no período do consentimento (imagem abaixo), será apresentado o consentimento na tela para que ele analise e clique em aceitar ou recursar antes que ele possa finalizar o cadastro. Com o aceite do candidato, o cadastro será finalizado. Caso ele recuse, a tela do consentimento é fechada e o cadastro não é concluído.

**Consentimento para menor de idade:**Quando o usuário é menor de idade, a mesma tela do consentimento é apresentada com a adição das orientações de como prosseguir (imagem abaixo), e o botão que diz "Li e concordo com os termos" é substituído por um "OK". Ao clicar em "OK" pessoa é redirecionada para a página inicial, pois é necessário que ela faça o que foi instruído na página para liberar seu acesso ao restante do cadastro e funcionalidades do portal. Sempre que o candidato menor de idade logar no Banco de Talentos, será apresentado novamente uma mensagem de consentimento, até que faça o procedimento apresentado na mensagem ou fale que não concorda com os termos.

O consentimento do menor de idade é registrado no Totvs Gestão de Pessoas, através da tela "Insere consentimento do candidato" que é um Anexo da tela Candidatos.

No caso de candidatos já cadastrados ao logar ou recarregar a página(F5) o novo consentimento será apresentado igual no momento do cadastro. Ao realizar o aceite a tela do consentimento será fechada e o usuário poderá prosseguir normalmente dentro do Banco de Talentos.

Caso não seja realizado o aceite do consentimento será apresentada uma mensagem informando que os dados dele serão excluídos e não será possível mais fazer parte do processo seletivo da empresa.

Clicando em **Não** a tela volta para o consentimento para que seja aceito, clicando em **Sim** o sistema tenta fazer a exclusão de todos os dados daquele candidato, caso este candidato possua vínculos dentro da empresa fora do processo seletivo não será possível fazer a exclusão, sendo necessário o candidato entrar em contado para resolver o problema, caso contrario é feita a exclusão sem problemas.

## **Consentimento no Processo Seletivo:**

No processo seletivo o consentimento é considerado em dois pontos, sendo estes a Execução da Triagem e a Aprovação de um candidato para a próxima etapa, em ambas é dada a opção de não selecionar candidatos não consentidos.

### Triagem

No processo de triagem antes de executá-lo uma mensagem é apresentada perguntado se quer ou não excluir os candidatos não consentidos.

### Aprovar Candidato

Ao selecionar os candidatos para aprovação para a próxima etapa caso algum deles não esteja consentido, uma mensagem é apresentada com os devidos códigos perguntando se aceita ou não prosseguir com o processo. Em caso negativo o processo é abortado em caso positivo outra mensagem é apresentada perguntado se deseja excluir estes candidatos do processo, que ao clicar em Sim eles serão desconsiderados e ao clicar no Não eles serão aprovados.

## **Consentimento Tela de Candidatos:**

No cadastro de candidato foi incluída uma coluna na visão principal que mostra se um candidato está consentido ou não. Além disso, foi criado um processo para conceder o consentimento para candidatos selecionados na visão.

### Insere Consentimento Candidato

Este processo permite selecionar vários candidatos para conceder o consentimento Atual. Após a seleção é apresentada uma tela para que seja informado a data que o candidato foi consentido e a justificativa da execução deste processo que é obrigatória.

Caso algum menor de idade seja selecionado, uma mensagem é apresentada ao clicar em executar para que o usuário confirme que a justificativa inserida é adequada para estes registros.

Você também pode usar painéis visuais para comunicar informações relacionadas, dicas ou recomendações de alerta ao usuário.

## Artigos relacionados

# [DT - Exclusão de candidatos (Banco de talentos)](https://tdn.totvs.com/pages/viewpage.action?pageId=527003893)

true
