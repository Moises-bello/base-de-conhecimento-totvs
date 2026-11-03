---
content_hash: 75b5d44718be4b1278e307588fe47f0161d251df59042168be27f93dbe6b7bb0
fetched_at: '2026-06-29T00:11:26.469459+00:00'
page_id: '717706755'
product: rm
source: tdn-rm
title: COCKPIT 360 - Sentença SQL de Interesses para Base PVI Externa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=717706755
version: 5
---

### Sentença SQL de Interesses para Base PVI Externa

Para que o card de [Interesses](https://tdn.totvs.com/display/LRM/COCKPIT+360+-+Interesses) exiba essas informações de uma base do [*Portal de Imóveis*](https://tdn.totvs.com/pages/viewpage.action?pageId=435105077), que é externa à base do RM, é preciso seguir as orientações abaixo:

**1° -** Siga as orientações do documento [TOTVS Compartilhamento](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento), para habilitar a barra de ferramentas de mesmo nome, que dá acesso ao repositório dos Objetos Gerenciais da TOTVS;

**2° -** Após realizar os procedimentos acima, acessando pelo contexto do TCGI, clique no menu TOTVS Compartilhamento, na lateral direita da tela e pesquise pela palavra ***interesse***. Caso não encontre clique no link "*Não Encontrou? Pesquise na TOTVS!*" e refaça a pesquisa:

**3º -** Baixe a Consulta  ***( para baixá-la)*,***que após realizado o download, é alterado para um link para instalá-la. Neste caso, execute as orientações abaixo a partir da etapa **4°- d***;

**4º -** No momento da importação, é preciso seguir as orientações abaixo, para garantir que a busca dos *Interesses* no PI funcione corretamente:

**a)** Importe a Consulta *SQL\_PI\_INTERESSE - COCKPIT - INTERESSE PI  - CONSULTA SQL.TotvsSQL*, a partir do contexto do TCGI, ou seja, quando em acesso a esse módulo.

**b)** Acesse o menu Gestão, agrupador Ferramentas de Análise e acione o ícone da Lupa com as palavras SQL para abrir a visão das Consultas SQL:

**c)** Acesse o Processo para Importação de Consulta SQL e aponte para o arquivo da consulta baixada, acima;

**d)** Na tela de *Importação de Consulta SQL*, que se abre, configure a *Seleção de Coligadas* desta consulta, para ***Todas as Coligadas***:

**e)** Marque a *Seleção de Sistemas*, como ***Sistema Atual***, sendo obrigatório estar no contexto do TCGI, como dito anteriormente:

**f)** Não é necessário nenhuma alteração na aba de *Parâmetros*, que deve estar idêntico ao da imagem abaixo:

**g)** Finalize a importação desta consulta.

**5° -** Ao término do processo de importação desta consulta SQL, localize a mesma no agrupador *TOTVS Incorporação Coligada 0, Global* e edite-a e:

**a)** Conforme se essa Consulta SQL está ***Visível a Todas as Coligadas*** e veja o comentário que **alerta** para não se alterar nenhuma informação nesta consulta, sendo necessário apenas configurar o acesso ao banco de dados externo do PI. Clique na opção para informar o ***Banco de Dados Externo***:

**b)** Caso ainda não tenha o acesso externo ao banco de dados do PI configurado, acione o botão para adicionar:

**c)** Na opção ***Choose Data Source***, selecione o tipo do **Data Source** seu respectivo **Data Provider**:

**d)** Na tela seguinte, informe o ***Server Name***, o ***Logon*** e a ***Database*** de acesso ao PI. Sugerimos que a conexão seja validada nesta tela mesmo, através do botão destinado a esse fim:

**e)** Na tela seguinte, defina o nome de ***Identificação*** e o ***Provedor de Segurança***, se necessário e salve:

**f)** Na tela da consulta, pode ser que o sistema apresente uma mensagem de erro informando que o object name PESSOAINTERESSE é inválido, caso essa mensagem seja apresentada, ignore-a, porque essa validação deve ser considerada apenas para as bases RM:

Após realizar as ações acima, o sistema estará apto a apresentar as informações dos [Interesses](https://tdn.totvs.com/display/LRM/COCKPIT+360+-+Interesses) dos Cliente, no ***Cockpit 360***.
