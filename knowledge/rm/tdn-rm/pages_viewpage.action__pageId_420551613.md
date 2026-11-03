---
content_hash: 749579473e2e255019e66db64305e2da751988fdd88b502c059f34d004ed891b
fetched_at: '2026-06-29T00:09:13.485347+00:00'
page_id: '420551613'
product: rm
source: tdn-rm
title: Vincular Família de Produtos ao Insumo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=420551613
version: 7
---

No Sistema Totvs Obras e Projetos, existe um processo de vinculação de mais de Produto de Suprimento/ Faturamento ao insumo através da abstração de família de Produtos, que pode ser acessado através do Menu Orçamento | Insumos | Cadastro (ou atalho F8) | Processos | Vincular Família de Produtos ao Insumo, com uma representação gráfica através de ícone, ou ainda na edição do Insumo, para executa-lo deve-se obrigatoriamente selecionar ao menos um Insumo.

Este Processo **NÃO** estará disponível caso a base em questão esteja integrada com Protheus pois as Tabelas de Classificações utilizadas no Produto não são integradas.

São verificados as seguintes regras para execução em Insumos Locais/ Globais:

* Em Projetos Globais, onde somente Insumos Globais são visualizados, o processo está disponível normalmente para execução.
* Em Projetos Locais, o processo somente está disponível para Insumos Locais. Caso o usuário selecione um Insumo Global em um Projeto Local e tente executar o processo, apresentará uma mensagem de erro informando a validação.

Ao Executar o processo, a primeira tela apresentada (tela padrão de processos) é apresentado para o usuário informar opcionalmente a descrição do processo.

Após esta etapa, são exibidas as cinco Tabelas de Classificação de Produtos existentes no Totvs Gestão de Estoque, Compras e Faturamento, sendo que caso alguma das Tabelas não esteja sendo utilizada ou seja incompatível, a mesma é exibida de forma desabilitada.

As tabelas de classificação são configuradas a partir da tela de Parâmetros no Totvs Gestão de Estoque, Compras e Faturamento:

Após selecionar a Classificação será exibido ao usuário um componente de *grid* de visão com todas as famílias de produtos pertencentes à coligada corrente, conforme a tabela de classificação escolhida pelo usuário na tela anterior. O usuário deve escolher um ou mais registros. A confirmação da escolha é feita através do botão “Confirmar”. **Esta implementação foi necessária porque o *grid* não persiste os valores escolhidos ao mudar de tela**. Se o usuário não selecionar nenhum registro e clicar no botão “Confirmar”, uma mensagem de erro será exibida informando ao usuário que o mesmo deve selecionar pelo menos um registro do *grid.*

No próximo passo está disponível duas opções para definir como o processo irá disponibilizas a informação na tela de seleção de Produtos sendo estas:

* **Manter o vínculo atual de Produtos ao Insumo:**nesta opção, os produtos atualmente vinculados ao insumo são exibidos na próxima tela e o usuário tem a opção de adicionar novos produtos, como por exemplo no caso de ter havido cadastro de novos produtos desde a última execução do processo (sincronização).
* **Excluir o vínculo atual de Produto ao Insumo:**nesta opção, a próxima tela desconsidera qualquer vínculo atual de produtos ao insumo. Neste caso, portanto, o usuário além de selecionar produtos a serem associados, deve obrigatoriamente definir um dos produtos para ser o produto principal da associação.

Após a escolha da(s) família(s) de produto(s), a próxima tela exibirá ao usuário todos os produtos retornados pelo filtro no *grid* para que o mesmo defina quais produtos deseja associar ao insumo. Esta tela também possui o botão “Confirmar”.

Esta tela possui inteligência para auxiliar o usuário na escolha dos produtos. Para isso são aplicadas as seguintes funcionalidades:

* Ordenação, agrupamento, filtros e persistência das configurações do *grid*.
* Botão para escolha de todos os produtos compatíveis.
* Botão para escolha de todos os produtos compatíveis de uma mesma família.
* Botão para selecionar apenas **um registro** como ativo, desmarcando, portanto, todos os demais.
* *Checkbox* para definir se serão excluídas todas as associações já existentes no insumo selecionado.
* Diferenciação de registros já vinculados a outros insumos através de mudanças nas cores das fontes.

**Observação:** Quando um registro possui vínculo com outro insumo, o texto é destacado em vermelho, e o usuário tem a opção de visualizar o insumo vinculado (Código + descrição) passando o mouse sobre o *checkbox*. Se o vínculo é com o próprio insumo do processo, a fonte é definida como azul-marinho, sendo que esta opção só é possível caso o usuário escolha a opção de manter o vínculo atual, na tela anterior. A imagem abaixo ilustra melhor a tela com os vínculos em destaque.

Se o usuário passar o *mouse* na coluna [Compatível?] dos registros, é exibido um *hint* (dica) informando as unidades-base tanto do insumo selecionado quanto do registro (produto) em questão, conforme a imagem abaixo:

Se o usuário passar o *mouse* na coluna [Vinculado?] dos registros e o mesmo estiver marcado, é exibido um *hint* (dica) informando a qual insumo o registro (produto) em questão está vinculado, conforme a imagem abaixo:

Botão para a seleção de todos os produtos compatíveis, destacado na imagem abaixo, permite que todos os produtos compatíveis para associação sejam marcados.

Botão para a seleção de todos os produtos compatíveis de uma mesma família, destacado na imagem abaixo, permite que todos os produtos compatíveis para associação, pertencentes à mesma família do registro atualmente selecionado, sejam marcados.

Botão para cancelar a seleção atual, este botão desmarca todos os registros selecionados. O botão pode ser visualizado na imagem abaixo.

Botão para definição do Produto principal, este botão marca o registro atual como principal, desmarcando todos os outros, pois apenas um registro pode ser definido como principal.

Ao final do processo apresentará uma tela com o resumo das definições do usuário, com  a opção de executar o processo. Após a execução do processo, é exibida ao usuário uma tela informando do sucesso ou não na execução do processo, com o texto de *log.* O *log* contém todos os detalhes da execução do processo, informando data/hora de cada instrução e documentando as etapas executadas com sucesso ou não.
