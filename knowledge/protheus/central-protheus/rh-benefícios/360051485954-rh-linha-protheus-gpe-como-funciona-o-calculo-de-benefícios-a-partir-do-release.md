---
article_id: 360051485954
category: RH - Benefícios
content_hash: 2a56f14b107e0f212fd816d1b969811562e44b087a10ef573bfc669e50c5f59d
fetched_at: '2026-06-28T22:44:04.863349+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona o calculo de benefícios a partir
  do release 12.1.27
type: support-article
updated_at: '2025-01-30T02:44:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051485954-RH-Linha-Protheus-GPE-Como-funciona-o-calculo-de-benef%C3%ADcios-a-partir-do-release-12-1-27
---

**Dúvida**Como funciona o calculo de benefícios a partir do release 12.1.27  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**

Foi desenvolvida uma nova tela para a atualização dos benefícios, a rotina GPEA133.  
A rotina foi construída seguindo a arquitetura de desenvolvimento **MVC** o que possibilita a implementação dos [Pontos de Entrada Padrão](https://tdn.totvs.com/x/cBtrD) e a execução sem interface, [Rotina Automática (ExecAuto)](https://tdn.totvs.com/x/evxn).

Após alterar o parâmetro MV\_CALCBEN para .T. e acessar a rotina de Atualização de Benefícios (*SIGAGPE > Atualizações > Benefícios > VT / VR / VA > Atualização*) pela primeira vez, será apresentada uma mensagem questionando se deseja realizar a conversão para a nova rotina de benefícios.

![](https://tdn.totvs.com/download/attachments/536708194/image2020-2-11_20-46-34.png?version=1&modificationDate=1581464794403&api=v2) 

Ao clicar em Sim o sistema irá transferir as informações da tabela SR0 para a nova tabela SM7 e excluir os registros da SR0, esse processo será executado apenas uma vez e é irreversível. 

**Alterar o parâmetro MV\_CALCBEN para .F. não irá retornar os registros para a tabela SR0**.

Assim que a conversão dos dados é concluída a nova tela é apresentada

Veja mais detalhes sobre a tela:

Temos na parte superior (1) as informações do funcionário, Matrícula, Nome e data de Admissão.

Agora os Benefícios são organizados em abas (2), possibilitando a navegação entre eles na mesma tela, facilitando a manutenção.

Em cada aba temos os vales vinculados ao funcionário (3) e os pedidos calculados no período atual (4) demonstrando a quantidade de dias e valores calculados, assim como dias de afastamento e quantidade de faltas consideradas para o cálculo.

![](https://tdn.totvs.com/download/attachments/536708194/image2020-2-11_21-11-4.png?version=1&modificationDate=1581466264693&api=v2)

O Histórico dos benefícios pode ser consultado acessando o menu *Outras Ações > Histórico*

![](https://tdn.totvs.com/download/attachments/536708194/image2020-2-11_21-15-48.png?version=1&modificationDate=1581466548250&api=v2)

A tela de histórico também está organizada por abas e para consultar os vales pagos basta informar o período que deseja consultar na seção Pesquisa e o *grid*da parte inferior será atualizado com as informações daquele período.

![](https://tdn.totvs.com/download/attachments/536708194/image2020-2-11_21-18-56.png?version=1&modificationDate=1581466736983&api=v2)

**Acesse os *links* abaixo para mais informações:**

* [Atualização de Benefícios](https://tdn.totvs.com/pages/viewpage.action?pageId=536708194#tabs-tela)
* [Cálculo](https://tdn.totvs.com/pages/viewpage.action?pageId=536708194#tabs-calculo)
* [Integração com o Ponto Eletrônico](https://tdn.totvs.com/pages/viewpage.action?pageId=536708194#tabs-sigapon)
* [Informações Técnicas](https://tdn.totvs.com/pages/viewpage.action?pageId=536708194#tabs-infotec)
