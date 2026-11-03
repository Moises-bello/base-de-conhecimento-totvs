---
content_hash: 180564a1f1d221dc33c5704c6a0dd76416280dd989f47523f94e4a425209428c
fetched_at: '2026-06-29T00:12:03.619611+00:00'
page_id: '911867483'
product: rm
source: tdn-rm
title: PI - Proposta - Clientes
type: documentation
url: https://tdn.totvs.com/display/LRM/PI+-+Proposta+-+Clientes
version: 21
---

Nesta etapa, é necessário preencher os dados dos proponentes da proposta, juntamente com suas informações adicionais e outros dados importantes.

**Cliente Principal:** Essa opção permite definir um dos compradores como o principal, o que significa que os lançamentos relacionados à proposta serão gerados em nome desse comprador específico.

**Adicionar Cliente:** Caso haja outros clientes envolvidos na elaboração da proposta, você pode adicioná-los usando essa opção no menu. Isso permite incluir todos os proponentes relevantes na proposta, garantindo uma representação precisa de todas as partes envolvidas.

Ao preencher corretamente os dados dos proponentes e utilizar as opções de cliente principal, adicionar cliente ou remover cliente, você garantirá que todos os envolvidos na proposta estejam devidamente representados e que suas informações sejam registradas com precisão.

Nesta tela é possível de buscar o Cliente através dos campos abaixo, que apresentam o seguinte comportamento:

* **Busca (com a Lupa):** A busca neste campo é realizada à medida que o usuário digita mais de 3 letras. Ao fazer isso, o sistema irá pesquisar pelos caracteres digitados apenas na Tabela XPIPESSOA e apresentar todos os clientes que contenham essa sequência de caracteres em seu nome. Por exemplo, se o usuário digitar "ria", o sistema irá apresentar a lista com todos os clientes que contenham essa sequência de letras em sua composição, como "Aria", "Faria", "Maria", "Mariana", "Marmoraria", etc.;
* **Nome:** A busca neste campo será realizada exatamente pelo termo digitado e ocorrerá quando o usuário retirar o foco do cursor dele. Ao realizar esta ação, o sistema irá pesquisar apenas na Tabela XPIPESSOA. Por exemplo, se o usuário digitar apenas "Maria Aparecida", o sistema não irá apresentar o cliente "Maria Aparecida Martins", porque o termo pesquisado não corresponde ao cadastro deste cliente. É preciso ficar atento ao cadastro dos nomes em bases que utilizem cadastros com caracteres ***case-sensitive*** ativados.;
* **CPF/CNPJ:** A busca neste campo será realizada nas Tabelas XPIPESSOA e/ou FCFO pelo número do CPF/CNPJ digitado, quando o usuário retirar o foco do cursor dele. Ao realizar esta ação, o sistema irá pesquisar primeiramente na Tabela XPIPESSOA e, caso o CPF/CNPJ informado não seja encontrado nesta tabela, o sistema irá buscar na Tabela FCFO. Caso a pesquisa nessas tabelas não retorne nenhum resultado, o PI exibirá uma mensagem informando que não foi encontrado nenhum cliente cadastrado; e
* **E-Mail:** A busca neste campo será realizada exatamente pelo termo digitado e ocorrerá quando o usuário retirar o foco do cursor dele. Ao fazer isso, o sistema irá pesquisar apenas na Tabela XPIPESSOA. Por exemplo, se o usuário digitar apenas "teste@[hotmail.com](http://hotmail.com)", o sistema não irá apresentar o cliente que possui o e-mail "teste@[hotmail.com.br](http://hotmail.com.br)", porque o termo pesquisado não corresponde ao cadastro deste cliente.

Adicionar

Para incluir as informações adicionais, você precisa clicar e expandir o menu "Dados Adicionais", localizado abaixo da tela de inclusão e seleção dos proponentes.

Remover

Se for necessário remover um cliente da proposta ao editar suas informações, basta clicar no botão "Remover Cliente". Isso possibilita ajustar a composição dos proponentes, caso haja alterações ao longo do processo.

Remover

Caso precise descartar as informações inseridas e começar de novo, utilize o botão 'Limpar'. O sistema removerá os dados dos campos e exibirá novamente o indicativo de Inclusão, pronto para um novo cadastro.

Dados Adicionais

Dados adicionais do cliente

Pessoas adicionais tem o propósito de disponibilizar o vínculo de pessoas que virão a participar da proposta/contrato de venda, sendo definido papeis de participação para as pessoas adicionais.  
Onde o sistema disponibiliza papeis controlados internamente, os papeis existentes hoje são: **Fiador, Procurador, Conjuge.  
Saiba mais: [Pré-Venda - Pessoas (Nova Visão 12.1.2302 e Superiores)](https://tdn.totvs.com/pages/viewpage.action?pageId=701668855)**

Na proposta ao adicionar o cliente principal e as pessoas adicionais a este cliente para serem utilizadas na proposta é considerado os dados pre existentes no cadastro do prospect para gerar as pessoas adicionais com o papel definido anteriormente, se a pessoa com o papel já existir não será criada novamente.

Ao criar a proposta e a pessoa adicional que foi criada no momento não possui o cadastro em prospect será criada a pessoa adicional somente com os dados inputados na criação da proposta, caso deseje colocar mais informações deverá editar o prospect da pessoa adicional para que todos os papeis sejam atualizados.
