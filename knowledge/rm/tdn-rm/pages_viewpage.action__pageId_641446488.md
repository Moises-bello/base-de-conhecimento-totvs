---
content_hash: 51bbd47029a3d860e90038f3775ddacd6c41e27e0f67490796f5b062197887fe
fetched_at: '2026-06-29T00:11:10.101703+00:00'
page_id: '641446488'
product: rm
source: tdn-rm
title: Órgão Público
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=641446488
version: 55
---

false

**A partir das Versões:**

* 12.1.31.261
* 12.1.32.206
* 12.1.33.128
* e Superiores.

# Objetivo:

---

Apresentar as adequações no produto para atender a legislação do eSocial referente a Órgão Público, leiaute S-1.0.

Para atender a geração dos eventos periódicos: S-2200, S-2300, S-2400, S-2405, S-2410, S-2416, S-2418 e S-2420 foi necessário criação de campos e anexos, que serão detalhados abaixo.

Outras informações acesse:

falseImportante!

As adequações realizadas no produto são exclusivamente para atender ao eSocial, demais rotinas não foram afetadas.

11ParametrizaçãoParametrização

1) Para a liberação dos novos campos nos cadastros é necessário a execução do script pelo aplicativo  RM.Script.Executor.exe

2) No parametrizador deverá selecionar o leiaute S-1.0 e:

2.1) Para o caso onde a empresa se enquadra no grupo 4 deverá preencher o campo "Não Periódicos" com a data 22/11/2021 e não marcar o parâmetro "Economia Mista".

2.2.) Quando a empresa não se enquadrar no grupo 4, ou seja, já envia funcionários em outro grupo (1, 2 ou 3), porém possui funcionários com regime próprio, o campo "Não Periódicos" deverá permanecer com a data do grupo a qual a empresa se enquadra (1, 2 ou 3), porém deverá marcar o parâmetro "Economia Mista" e preencher o campo "Não Periódicos" informando a data de "22/11/2021", assim o sistema irá considerar essa data na tratativa dos eventos não periódicos dos funcionários com categoria (3XX).

Veja exemplo na tela abaixo:

**ATENÇÃO:**

As alterações e os novos eventos citados nesse documento só serão gerados quando selecionado o leiaute S-1.0 NT 03/2021 ou superior.

3Eventos eSocialEventos eSocial

Acesse o link abaixo para entendimento sobre cada evento:

# Tabelas/Eventos Iniciais

* [S-1000 - Informações do Empregador/Contribuinte/Órgão Público](https://tdn.totvs.com/pages/viewpage.action?pageId=645258288)
* [S-1010 - Tabela de Rubricas](https://tdn.totvs.com/pages/viewpage.action?pageId=644964073)

# Eventos Periódicos

* [S-1202 - Remuneração de servidor vinculado a Regime Próprio de Previdência Social – RPP](https://tdn.totvs.com/pages/viewpage.action?pageId=404916475)
* [S-1207 – Benefícios – Entes públicos](https://tdn.totvs.com/pages/viewpage.action?pageId=673801865)

# Eventos Não Periódicos

* [S-2200 - Cadastramento Inicia do Vinculo e Admissão/ingresso e Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=643310836)
* [S-2206 - Alteração de Contrato e Trabalho](https://tdn.totvs.com/pages/viewpage.action?pageId=643313989)
* [S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário Início](https://tdn.totvs.com/pages/viewpage.action?pageId=645248465)
* [S-2306 - Trabalhador Sem Vínculo de Emprego/Estatutário Alteração Contratual](https://tdn.totvs.com/pages/viewpage.action?pageId=645248487)

# Beneficiário e Benefícios - Órgãos Públicos

Abaixo estão descrito os eventos para envio das informações dos beneficiários, previdenciários ou não, de todo e qualquer benefício pago pelos entes federativos, diretamente com recursos do tesouro, ou por seus RPPS, incluindo os beneficiários das complementações de benefícios do RGPS, das aposentadorias e pensões graciosas, reserva, reforma e pensões de militares e aposentadorias e pensões dos parlamentares.

**Estão obrigados a enviar**: empregadores de órgãos públicos que administrem benefícios, previdenciário ou não, no mês de referência, exceto aos efetuados pelo INSS.

### **Produto de Folha de Pagamento**

Após estudos realizados com alguns clientes Órgão Público que utilizam a folha de pagamento do RM, verificamos que existem três tipos de beneficiários, sendo eles:

1) Quando o funcionário recebe o salário normalmente e além disso recebe algum tipo de benefício;

**Exemplo:**

O funcionário esta ativo recebendo seu vencimento normalmente, porém recebe algum beneficio, como aposentadoria.

2) Quando o funcionário é cadastrado apenas para receber algum tipo de benefício, ou somente para seu dependente receber algum tipo de beneficio.

**Exemplos:**

O funcionário faleceu e sua esposa irá receber seu vencimento;

O funcionário está aposentado e recebe somente algum beneficio;

O funcionário esta demitido e recebe algum benefício.

3) Quando o beneficiário não é o funcionário, porém é cadastrado no produto para receber algum tipo de benefício.

**Exemplo:**

A empresa é responsável pelo pagamento de algum beneficio para uma pessoa que não é funcionário na base de dados.

Para tratamento dessas situações foi necessário alteração no produto, para que seja possível identificar quem são esses beneficiários na folha de pagamento e gerar os eventos de "Beneficiário e Benefício", ficando da seguinte maneira:

Para identificar a **situação 1)**, como o funcionário estará ativo na base de dados, criamos o parâmetro **"Beneficiário Entes Públicos"**, que ao selecioná-lo será habilitada a aba **"Informações do beneficiário"**para preenchimento das informações necessárias;

Para identificação das **situações 2)** e **3)**, criamos o tipo de funcionário **"W-Beneficiário"**, que ao preencher o funcionário com essa situação será habilitada a aba **"Informações do beneficiário"**para preenchimento das informações necessárias;

Ao acessar o link dos eventos abaixo mencionado, irá verificar que descrevemos alguns exemplos para que fiquei mais completo o entendimento.

As informações do beneficiário serão enviadas ao eSocial através de dois leiautes:

* [S-2400 - Cadastro de Beneficiário - Entes Públicos - Início](https://tdn.totvs.com/pages/viewpage.action?pageId=639197620)
* [S-2405 - Cadastro de Beneficiário - Entes Públicos - Alteração](https://tdn.totvs.com/pages/viewpage.action?pageId=641446580)

As informações do benefício serão enviadas ao eSocial através de quatro leiautes:

* [S-2410 - Cadastro de Benefício - Entes Públicos - Início](https://tdn.totvs.com/pages/viewpage.action?pageId=641666488)
* [S-2418 - Reativação de Benefícios](https://tdn.totvs.com/pages/viewpage.action?pageId=644307614)
* [S-2420 – Cadastro de Benefícios – Entes Públicos - Término](https://tdn.totvs.com/pages/viewpage.action?pageId=644307505)
