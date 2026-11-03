---
content_hash: 415327d0b4dc500e003564c7d72861c96318769b122282938a6ccb7c2f3928bf
fetched_at: '2026-06-29T00:09:32.545145+00:00'
page_id: '425458870'
product: rm
source: tdn-rm
title: Provas
type: documentation
url: https://tdn.totvs.com/display/LRM/Provas
version: 27
---

O Cadastro de Provas tem como objetivo definir as provas/pesquisas que serão aplicadas à candidatos para consultas gerais e/ou avaliação de conhecimento. As provas são divididas em dois tipos: **Avaliação de conhecimento** ou **Pesquisa de opinião**.

A prova poderá ter questões previamente definas ou questões geradas aleatoriamente para cada candidato a partir de uma pré-configuração. Este recurso  estará disponível se no momento do cadastro da prova o parâmetro **Prova dinâmica** for habilitado.

A configuração da prova dinâmica é feita quando é definido a quantidade de questões por área de conhecimento, matéria e grau de dificuldade.

Na prova existe algumas configurações básicas e de execução da prova que são definidas para os dois tipos de prova como:

**Prova ativa -**Parâmetro que define que a prova está ativa, podendo ser utilizado para criar filtros de prova.

**Disponível para execução -**  Caso a prova tenha um idioma definido este parâmetro habilita a versão original da prova para execução.

**A partir da versão: 12.1.2209.194.**

O nome do checkBox: **Disponível para execução** foi alterado para: **Disponível para execução no idioma informado,** com o objetivo em ficar mais intuitivo para o usuário, para as provas que possui Idioma vinculado em em seu cadastro.

OBS: O checkBox so é ativo caso o idioma da avaliação seja selecionado e o usuário for editar a avaliação, no momento da criação o checkBox permanece **DESATIVADO**.

**Idioma -** Define o idioma da prova.

**Instruções –**este recurso foi implementado com o intuito de permitir que seja cadastrado as informações pertinentes as instruções da prova. Neste campo, será permitido usar quebras de linhas e se por acaso o texto for extenso será exibido uma barra de rolagem tanto no cadastro quanto no Executor Web. Este recurso está disponível somente a partir da versão 12.1.27.

**Classificação -**É possível inserir nenhuma ou quantas classificações desejar para uma prova. E somente usuário conseguirá incluir a classificação na prova se o mesmo caso tiver permissão no perfil do usuário. Importante: O usuário só poderá visualizar as provas quando as mesmas não possuírem classificações vinculadas ou se tiverem classificações que possuem permissões de perfil de usuário.

***Configurações***

* **Permite mudança de tela durante a avaliação -** Se este parâmetro estiver habilitado, o usuário não consegue sair da tela do RM Executor. A tela fica travada até a prova ser finalizada. Isto é feito por medida de segurança, impossibilitando o usuário de acessar informações de outro local para se na execução da prova. Este recurso está disponível apenas para o RM Executor.

* **Desabilita o uso da calculadora -** Com esta opção marcada, na execução de provas o ícone da calculadora se encontrará desabilitado. Recurso disponível apenas para o RM Executor.

* **Exibir resultado -** Habilitando essa opção, o sistema emitirá o resultado da prova na tela assim que o candidato concluir sua prova via RM Executor. Caso contrário o resultado não aparecerá na tela, podendo ser pesquisado via TOTVS Avaliação e Pesquisa.

* **Permite imprimir -** Marcando esta opção, o candidato pode imprimir sua prova durante a execução no RM Executor.

* **Desabilita o uso do comentário -** Habilitando esta opção, não será possível inserir comentários nas questões durante a execução da prova.

* **Impede a reabertura da avaliação após ter iniciado a execução** - Define que a avaliação só poderá ser iniciada uma única vez, ou seja, ao clicar no botão iniciar nas instruções iniciais da avaliação através do executor web, a avaliação em hipótese alguma poderá ser iniciada novamente, esta funcionalidade implica que se o candidato tiver algum problema na internet, o navegador ou computador travar, ou até mesmo se fechar o navegador com ou sem intenção, ao acessar a avaliação novamente, a mesma não estará disponível para execução. Caso a instituição queira conceder novamente o acesso a avaliação para o candidato (), a avaliação deve ser alterada para "Pendente" ou deverá ser executado o processo  . Caso a instituição não queria conceder acesso novamente a instituição e deseje concluir a avaliação do candidato, é necessário executar o processo  .
  + **Permite salvar o andamento da prova** - Caso este parâmetro esteja ativado, ele bloqueia o parâmetro que impede a reabertura da avaliação e assim vice e versa, este parâmetro faz com que o usuário possa salvar o andamento da avaliação a qualquer momento.

Informações

Este parâmetro está disponível somente para o  à partir da execução do script TS.2020.10\_01 disponível nos patchs 12.1.27.282, 12.1.28.196 e 12.1.29.118.

Já para as provas de pesquisa de opinião é possível habilitar o parâmetro **Confidencial** que permite a execução de uma pesquisa sem identificação do pesquisado.  
Além das configurações descritas acima é possível também definir o tempo da prova que será executada. Informando as seguintes informações:

* **Duração:** informe o período de duração da prova. Exemplo: 60 minutos.
* **Aviso de Encerramento:** informe em quantos minutos após o início da prova, o candidato receberá o aviso do tempo que lhe resta para finalizar a atividade.
* **Repetir Aviso a cada:** informe de quanto em quanto tempo o aviso de encerramento deverá ser repetido.

 Informações complementares

---

[Questões da Prova](http://tdn.totvs.com/x/7f9bGQ)

[Candidatos](http://tdn.totvs.com/x/Z-1bGQ)

[Grupo](http://tdn.totvs.com/x/y-xbGQ)

[Período](http://tdn.totvs.com/x/EPxbGQ)

[Características pessoais](http://tdn.totvs.com/x/JgBjGQ)

[Ranking](http://tdn.totvs.com/x/6f9bGQ)

[Provas em outros idiomas](http://tdn.totvs.com/x/--9bGQ)

 Como fazer

---

[Ordenar questões](http://tdn.totvs.com/x/MwBjGQ)

[Adicionar questões](http://tdn.totvs.com/x/BABjGQ)

[Incluir funcionários como candidatos na prova](http://tdn.totvs.com/x/5v9bGQ)

[Gerar versão de prova em outro idioma](http://tdn.totvs.com/x/MQBjGQ)

[Gerar prova local (Off line)](http://tdn.totvs.com/x/6v9bGQ)

[Recuperar prova local (Off line)](http://tdn.totvs.com/x/mf5bGQ)

[Relatório de pesquisa de opinião confidencial](http://tdn.totvs.com/x/R-pbGQ)

[Relatório de relação de candidatos](http://tdn.totvs.com/x/KwBjGQ)

[Relatório de ranking de candidatos](http://tdn.totvs.com/x/KgBjGQ)

[Importação de candidato a partir da seleção RM Vitae](http://tdn.totvs.com/x/CABjGQ)

[Importar candidatos a partir de arquivos texto](http://tdn.totvs.com/x/0PxbGQ)

[Copiar provas entre coligadas](http://tdn.totvs.com/x/wP1bGQ)

[Integração da Prova de Etapa da Turma/Disciplina com a Prova do Totvs Avaliação e Pesquisa](http://tdn.totvs.com/x/w-1bGQ)

[Executor Web](https://tdn.totvs.com/display/LRM/Executor+Web)
