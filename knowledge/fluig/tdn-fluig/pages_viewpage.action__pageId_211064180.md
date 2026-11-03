---
content_hash: f3cbdc8928c42a61a529c493cfb7083d47cd3405dd8c2911702a881548d8b774
fetched_at: '2026-06-28T21:35:19.537434+00:00'
page_id: '211064180'
product: fluig
source: tdn-fluig
title: LMS 006 - Como permitir que os alunos visualizem o catálogo e se matriculem
  em trilhas e treinamentos?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=211064180
version: 25
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

***Card*:** LMS

# Ocorrência

Como liberar o catálogo para todos os usuários e também permitir que eles visualizem e se matriculem nos treinamentos e trilhas?

# Solução

Para permitir tais ações, é necessário liberar algumas permissões. Para isso, siga os passos abaixo:

0.5falsesamplesfadetrue1Passo 1

* Faça o *login* com um usuário administrador e, no menu principal, acesse o **Painel de Controle**.
* No agrupador **Pessoas**, acione **Permissões**.

2Passo 2

* Selecione a categoria de permissão **Papel** e acione **Próxima etapa**.

3Passo 3

* No quadro Papéis, selecione o papel **user** e acione **Próxima etapa**.

4Passo 4

* Acione **Adicionar** e localize e selecione os seguintes recursos: **Trilhas e treinamentos**, **Aprendizado - Catálogo de trilhas e treinamentos** e **Aprendizado - Matrículas**.

5Passo 5

* Ative as permissões de cada recurso conforme descrito abaixo:
  + [Trilhas e treinamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=274850166#Plataforma%E2%9D%99Recursosdeaprendizadoeavalia%C3%A7%C3%B5es-Trilhasetreinamentos): opção **Visualizar página** deve ser ativada.
  + [Aprendizado - Catálogo de trilhas e treinamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=274850166#Plataforma%E2%9D%99Recursosdeaprendizadoeavalia%C3%A7%C3%B5es-Trilhasetreinamentos): opção **Ler** deve ser ativada.
  + A opção **Cancelar matrícula em treinamento/trilhas** do recurso [Aprendizado - Matrículas](https://tdn.totvs.com/pages/viewpage.action?pageId=274850166#Plataforma%E2%9D%99Recursosdeaprendizadoeavalia%C3%A7%C3%B5es-Matr%C3%ADculas) permite que o aluno cancele sua própria matrícula nos itens do catálogo. Se desejado, ativar essa opção também.

    Atualizações anteriores à 1.6.1

    Obrigatoriamente é necessário ativar a opção **Matricular em treinamento/trilhas** do recurso **Aprendizado - Matrículas**.
* Depois de ativar todas as opções, acione **Aplicar permissões**.

6Passo 6

* Agora, é necessário que o catálogo e todas as trilhas e treinamentos tenham a permissão de **Execução** definida para **Todos**. Para isso, no menu principal posicione o *mouse* sobre **Aprendizado** e, em seguida, clique em **Trilhas e treinamentos** e edite a segurança da pasta raiz do catálogo.  
  Você pode conferir o passo a passo da edição da pasta raiz do catálogo em [Editar catálogo](https://tdn.totvs.com/pages/viewpage.action?pageId=233765960#Plataforma%E2%9D%99Trilhasetreinamentos-Editarcat%C3%A1logo).

Entenda:

Todas as trilhas e treinamentos também precisam estar com essa mesma permissão configurada. Para isso, existem duas opções:

* definir essa mesma permissão (**Execução** para **Todos**) na segurança do cadastro de cada item (trilha ou treinamento);
* ou definir na segurança do cadastro de cada item abaixo da pasta raiz que ele deve herdar as permissões definidas para ela.

Mais informações e o passo a passo para definir essas permissões podem ser obtidas em , ,  e [*Link*](http://tdn.totvs.com/display/HF/Link#Link-seguranca).

Saiba mais...

Confira as opções de permissão dos demais catálogos e recursos de aprendizado em .

Importante!

A partir da atualização **[1.6.5-190219](http://tdn.totvs.com/pages/viewpage.action?pageId=442961412#Atualiza%C3%A7%C3%B5es(1.6.5)-190219)**, o **LMS** não faz mais parte da plataforma para **novas instalações**.

Mas, não se preocupe: se você adquiriu a plataforma com o **LMS incluso**, entre em contato com o [Suporte Fluig](https://suporte.fluig.com/) para que você consiga utiliza-lo normalmente – mesmo após a atualização **1.6.5-190219**. Se você não lembra se o LMS está incluso ou não no seu pacote, consulte sua proposta comercial ou entre em contato com o seu ESN.
