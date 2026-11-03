---
article_id: 360041427034
category: MDFe - Manifesto de Carga
content_hash: d5705ecc8b1c2da01b461c708d1747f0a93ed279cd5aa022d2d0ffabf6de5dfe
fetched_at: '2026-06-28T22:40:08.067559+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - Implantação
  MDF-e
type: support-article
updated_at: '2025-06-17T17:11:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041427034-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Implanta%C3%A7%C3%A3o-MDF-e
---

**Dúvida**Qual o processo para implantação e como gerar o MDFe de nota fiscal ?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

1. Preencher no pedido de vendas o ***campo Veiculo  C5\_VEÍCULO;***

***![veiculo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/10575744347927)***

ou poderá ir em ***Faturamento > Atualizações > Faturamento > Expedição > Após entrar na rotina clique sobre o documento desejado e depois em  Manutenção e vincule o veículo no documento e depois clique em confirmar.***

*![expedicao.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/10576011805463)*

2. Acessar em ***Faturamento > Atualizações > NF-e e NFs-e > MDF-e***

***![mdfe.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/10576250419735)***

3. Selecionar a nota  e preencha o município de acordo com a ***UF de descarregamento***

***![mdfe_rotina.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/10576522318231)***

4. Acessar a segunda aba e preencha o ***município de carregamento (Obrigatório), preencha o percurso*** somente se for diferente das UF’s do cabeçalho ***Observação: Aba Outros é opcional***

***![percurso.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/10576608588439)***

5. Clicar ***em Confirmar***

6. Antes de transmitir o MDFe entre em Outras Ações - Parâmetro e defina o ambiente que deseja transmitir o MDFe. Salve com o grupo Administrador: Salvar e depois OK.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21789531594391)

8. Acessar > ***Outras ações > Gerenciar MDFe > Transmitir***

![gerenciar_mdfe.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/10576735304599)

9. Acessar > ***Outras ações > Gerenciar MDFe > Monitorar***

## **CONTEÚDO**

1. **[Visão Geral](https://tdn.totvs.com/pages/releaseview.action?pageId=727912921#Novofluxodesele%C3%A7%C3%A3odeNFesnarotinadeMDFe(SPEDMDFE)-VISAO)**
2. **[Exemplo de utilização](https://tdn.totvs.com/pages/releaseview.action?pageId=727912921#Novofluxodesele%C3%A7%C3%A3odeNFesnarotinadeMDFe(SPEDMDFE)-EXEMPLO)**
   1. **[Novo Fluxo de Seleção de NF-e no MDF-e](https://tdn.totvs.com/pages/releaseview.action?pageId=727912921#Novofluxodesele%C3%A7%C3%A3odeNFesnarotinadeMDFe(SPEDMDFE)-EXEMPLO)**
   2. **[Marca/Desmarca Todas NF-e](https://tdn.totvs.com/pages/releaseview.action?pageId=727912921#Novofluxodesele%C3%A7%C3%A3odeNFesnarotinadeMDFe(SPEDMDFE)-MARCA)**
   3. **[Selecionar NF-e Vinculada à Outro MDF-e](https://tdn.totvs.com/pages/releaseview.action?pageId=727912921#Novofluxodesele%C3%A7%C3%A3odeNFesnarotinadeMDFe(SPEDMDFE)-SELECIONAR)**
3. **[Tabelas utilizadas](https://tdn.totvs.com/pages/releaseview.action?pageId=727912921#Novofluxodesele%C3%A7%C3%A3odeNFesnarotinadeMDFe(SPEDMDFE)-TABELA)**

## **01. VISÃO GERAL**

Disponibilizado para as releases 12.1.33 e superiores, melhoria no fluxo de apresentação e seleção de documentos eletrônicos na rotina de MDF-e do módulo de Faturamento do ERP Protheus (rotina SPEDMDFE).

Esta mudança implica na otimização das operações de manutenção, visualização e exclusão do MDF-e, deixando-as mais rápidas e práticas para modificar um dado no MDF-e ou até mesmo incluir uma NF-e aos documentos vinculados ao MDF-e.

Também foram realizadas melhorias de performance na rotina.

## **02.EXEMPLO DE UTILIZAÇÃO**

## **Novo Fluxo de seleção de NF-e no MDF-e.**

Aqui, será detalhado passo a passo do novo fluxo de vinculação e desvinculação de uma NF-e na rotina de MDF-e (SPEDMDFE), presente no módulo Faturamento (SIGAFAT) do ERP Protheus.

Será utilizada a opção de **Incluir** para exemplificar o novo fluxo, porém o mesmo se aplica as manutenções do MDF-e: INCLUIR, ALTERAR, VISUALIZAR, EXCLUIR, claro que respeitando seus comportamentos específicos de manutenção.

Começamos clicando no botão "**Incluir**".

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_18-13-38.png?version=1&modificationDate=1671657218307&api=v2&effects=drop-shadow)

Serão apresentados os campos vazios em tela, preencher os campos conforme desejado.

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_18-15-37.png?version=1&modificationDate=1671657338080&api=v2&effects=drop-shadow)

Note que as Notas Fiscais Eletrônicas (NF-e) que possuem o veículo, neste caso "TSS00000", ainda não foram apresentadas para marcação e vínculo ao MDF-e.

Este é o novo comportamento da rotina de manutenção do MDF-e.

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_18-17-18.png?version=1&modificationDate=1671657438347&api=v2&effects=drop-shadow)

Para que as NF-e sejam apresentadas para seleção e vínculo ao MDF-e, basta preencher ou não os campos presentes no espaço de "**Filtro para exibição de NF-e para seleção**" e clicar no botão "**Listar NF-e**".

Pronto!

As NF-e serão listadas para seleção.

O filtro pode ser realizado por alguns campos disponibilizados:

* **Emissão De/Até:** Aqui pode-se filtrar pela emissão da NF-e.
* **NF-e De/Até**: Aqui pode-se filtrar um range ou número específico de NF-e.
* **Series:** Aqui pode-se informar nenhuma ou até 4 séries (dependendo do tamanho da série utilizada) separadas por ponto e virgula (";"). Exemplo de preenchimento: "848;55;1"

Serão listadas as NF-e que se enquadram no filtro informado, respeitando o veículo informado e se filtrar por filial ou não. Abaixo, o exemplo de uso do filtro para exibição de NF-e.

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_18-26-38.png?version=1&modificationDate=1671657998800&api=v2&effects=drop-shadow)

Caso nenhuma nota seja contemplada pelo filtro informado, o sistema irá informar.

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_18-28-0.png?version=1&modificationDate=1671658080903&api=v2&effects=drop-shadow)

IMPORTANTE

Quando clicado no botão "Listar NF-e", todas as NF-e **não** selecionadas no grid serão removidas para que novas NF-e que contemplem o novo filtro realizado sejam apresentadas para seleção.

Para marcação basta dar duplo clique na NF-e desejada e realizar o processo habitual de seleção/vinculação de NF-e.

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_18-52-58.png?version=1&modificationDate=1671659578727&api=v2&effects=drop-shadow)

Ficando apenas uma NF-e selecionada e vinculada.

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_18-53-33.png?version=1&modificationDate=1671659613833&api=v2&effects=drop-shadow)

Caso seja necessário selecionar mais de uma NF-e entre as notas apresentadas, no próximo capitulo será mostrado como selecionar todos os estes documentos disponíveis em tela.

## **Marca/Desmarca todas NF-e**

Uma nova funcionalidade disponibilizada foi a possibilidade: Marcar/desmarcar todas NF-e apresentadas no grid.

#### Marcação/Seleção

Para isso, com as NF-e já apresentadas e prontas para seleção, basta clicar no cabeçalho do campo "Seleção".

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_18-55-59.png?version=1&modificationDate=1671659759903&api=v2&effects=drop-shadow)

Após, clique no campo "Seleção", será apresentada tela de confirmação, clique em "**Sim**".

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_18-36-5.png?version=1&modificationDate=1671658565793&api=v2&effects=drop-shadow)

Em seguida será apresentada a tela de preenchimento do "**Código de Município de Descarregamento da NF-e**", que neste caso deverá ser igual à todas as NF-e apresentadas pendentes de seleção.

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_18-56-27.png?version=1&modificationDate=1671659787333&api=v2&effects=drop-shadow)

Clicar em "Salvar" para que o **código** e **descrição do município** seja aplicada a todas as NF-e elegíveis (não selecionadas). Note que a NF-e previamente selecionada não foi alterada, desta forma sendo selecionadas e preenchidas com o município de descarregamento somente as NF-e não marcadas anteriormente.

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_18-57-7.png?version=1&modificationDate=1671659827670&api=v2&effects=drop-shadow)

IMPORTANTE

A opção marca e desmarca todos irá sempre realizar a marcação dos registros desmarcados caso haja algum (ao menos um). Caso contrário, onde todos os registros estiverem marcados, o sistema assumirá que deseja-se desmarcar todos os registros selecionados.

#### Desmarcação

Para desmarcar todas as NF-e já marcadas, basta clicar novamente no cabeçalho do campo "**Seleção**" e confirmar a operação.

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_19-4-27.png?version=1&modificationDate=1671660267277&api=v2&effects=drop-shadow)

As NF-e são apresentadas desmarcadas, desta forma possibilitando nova seleção e vínculo ao MDF-e.

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_19-5-47.png?version=1&modificationDate=1671660348030&api=v2&effects=drop-shadow)

## **Selecionar NF-e vinculada à outro MDF-e**

Outra característica implementada nesta melhoria foi a possibilidade de selecionar uma NF-e específica que esteja já vinculada à outro MDF-e.

Alguns pontos importante são:

* Somente serão mostrada(s) NF-e(s) vinculadas à outros MDF-e quando forem preenchidos os campos do filtro: **NF-e De** ou **NF-e Até** ou **Series;**
* A NF-e buscada deve ter o mesmo veículo do MDF-e em manutenção; e
* A NF-e buscada não poderá estar vinculada a um MDF-e autorizado (o sistema irá alertar, caso necessário).

A seguir será mostrado um exemplo de como buscar.

Note que os campos **NF-e De** e **NF-e  Até** foram preenchidos com o número da NF-e desejada.

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_19-12-44.png?version=1&modificationDate=1671660764357&api=v2&effects=drop-shadow)

Ao clicar para seleção esta NF-e, é apresentada mensagem:

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_19-18-57.png?version=1&modificationDate=1671661137357&api=v2&effects=drop-shadow)

Ao clicar em "Sim" o sistema irá marcar a NF-e e ao finalizar a manutenção (neste caso a inclusão) do MDF-e, o sistema irá desvincular a NF-e selecionada  do MDF-e original, neste caso o

Filial: x TSS01

Numero: 000000216

Série: 849

E será vinculado ao documento que esta realizando a vinculação.

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_19-22-33.png?version=1&modificationDate=1671661353373&api=v2&effects=drop-shadow)

Documento recém ingressado e vinculado NF-e:

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_19-23-25.png?version=1&modificationDate=1671661405997&api=v2&effects=drop-shadow)

MDF-e original que teve a NF-e desvinculada:

![](https://tdn.totvs.com/download/attachments/727912921/image2022-12-21_19-24-17.png?version=1&modificationDate=1671661457317&api=v2&effects=drop-shadow)

* **Saiba mais**Para verificar as **correções realizadas pelo desenvolvimento**  e baixar o pacote atualizado dos fontes a **expedição** continua dos **documentos eletrônicos MDFe**  será liberado através do link abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=525010692>

**Caso o link acima não abra copie e cole em outra aba do Navegador.**

* Neste **link acima** para baixar clique na versão.
* Para aplicar o **RDMAKE da rotina do MDF-e deve estar compilado,  *MDFesefaz e o DAMDFe* baixar o fonte pelo link abaixo:**

[Clique Aqui](https://suporte.totvs.com/portal/p/10098/download?e=1083729)
