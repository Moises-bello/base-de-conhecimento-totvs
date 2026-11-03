---
content_hash: 3b2ec3ee01977a5e10cfb1793e3b27522615fcea5f5ea3785383f46f41db9bb8
fetched_at: '2026-06-29T00:10:07.901185+00:00'
page_id: '452719467'
product: rm
source: tdn-rm
title: Aprovação Global de Requisições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719467
version: 3
---

**Aprovação Global de Requisições**

A Aprovação Global de Requisições, localizada no RM Portal pelo menu Recursos Humanos| Requisições| Aprovação Global, permite que os chefes possam Aprovar/Reprovar várias requisições do mesmo tipo e na mesma etapa do fluxo de aprovação.

**Observações:**

- Esta ferramenta será disponibilizada somente no RM Portal.

- Se o usuário selecionar duas requisições que estejam em etapas diferentes do fluxo de aprovação, o sistema apresentará uma mensagem para que o usuário selecione um status válido para a etapa atual das requisições selecionadas.

- Uma vez Aprovada/Reprovada a requisição não será mais visualizada na tela de aprovação global.

- Para a consulta de pareceres e edição da requisição, deve ser selecionado somente um registro.

- Para o devido funcionamento o chefe/supervisor deve ter o seu cadastro de usuário ativo (GUSUARIO.STATUS = 1 e ter permissão de acesso à tela de Requisições do RM Portal. Para tal, no Perfil de acesso do usuário, deverá ser verificada a permissão no RM Portal | Requisições.

**Atenção:**

Para a utilização desta funcionalidade é preciso que as seguintes parametrizações sejam realizadas no Totvs Gestão de Pessoas:

- Em Gestão Organizacional| Chefes e Supervisores, os chefes devem estar definidos corretamente.

- Em Configurações| Tipo de Requisição, todos os tipos cadastrados devem conter o fluxo de etapas e o mapeamento definidos.

- Em Configurações| Parametrizador| Requisições, a Configuração de E-mails deve estar preenchida e o parâmetro "Envio automático de e-mail" deve estar marcado.

- Em Ambiente| Parâmetros| Globais, os campos de envio de e-mail devem estar preenchidos, além do campo "URL de acesso ao RM Portal."

**Funcionamento:**

Após a criação da Requisição, a mesma segue o seu fluxo e o aprovador atual recebe o e-mail automático para realizar a Aprovação/Reprovação da Requisição.

Sistema disponibiliza no e-mail o link do parecer específico da Requisição em questão, juntamente com o link da tela de Aprovação Global de Requisições, sendo apresentado também o histórico dos pareceres da Requisição.

Clicando no 1º link disponibilizado no e-mail:

Sistema direciona para o parecer específico da Requisição em questão para que o usuário informe todos os dados necessários e Aprova/Reprova a Requisição.

**OBS.:** Usuário com acesso somente a tela específica da Requisição, não sendo liberado acesso aos demais recursos do RM Portal.

Clicando no 2º link disponibilizado no e-mail:

Sistema direciona para a tela de Aprovação Global de Requisições. Usuário seleciona o tipo de Requisição desejada para aprovação, visualiza todas as Requisições pendentes e seleciona todas as Requisições que deseja Aprovar/Reprovar, informando todos os dados necessários.

**OBS.:** Usuário com acesso somente a tela de "Aprovação Global de Requisições", não sendo liberado acesso aos demais recursos do RM Portal. A utilização dos links deste e-mail vai depender da utilização de dois parâmetros:

- Dispensar login no RM Portal para interação na requisição

- Utiliza parecer padrão na requisição Marcando o parâmetro "**Dispensar login no RM Portal para interação na requisição**", quando o aprovador receber o e-mail para realizar a aprovação, o acesso ao RM Portal será automático ao clicar no link. Caso contrário, o acesso ao RM Portal será por meio do seu login/senha. Marcando o parâmetro "**Utiliza parecer padrão na requisição**", quando o aprovador acessar a tela do parecer da Requisição, automaticamente será preenchido o campo "parecer" da tela, conforme texto informado no campo "**Texto padrão do parecer**". Caso contrário, o aprovador terá que preencher o campo "parecer" da tela.

**Exemplo de mensagem de e-mail:**

*Requisições - TOTVS Gestão de Pessoas* *A requisição de transferência, número 248, está sob sua responsabilidade.* *Para emitir o seu parecer da requisição número 248, acesse o link abaixo:*

*[http://localhost/corpore.net/Source/Rhu-RecHumanos/RM.Rhu.Req/RM.Rhu.ReqGlobal/RhuReqExecPage.html?ActionID=RhuReqGlobalParecerActionWeb&FINAL=5&Col=1&Tprv=1&Req=\B9O\19\3C\F6\CEB\85\24\D3\3D\28\BC\3C3\D76\1B\DA\3E\23\CD\88\92\8Ei\F6\C2\E5\B2\B9\CD\F1\03L\9Ft\3D8\D4\EA\1Fs\BA\21\0BGD\_](http://localhost/corpore.net/Source/Rhu-RecHumanos/RM.Rhu.Req/RM.Rhu.ReqGlobal/RhuReqExecPage.html?ActionID=RhuReqGlobalParecerActionWeb&FINAL=5&Col=1&Tprv=1&Req=B9O193CF6CEB8524D33D28BC3C3D761BDA3E23CD88928EiF6C2E5B2B9CDF103L9Ft3D8D4EA1FsBA210BGD_) \_Para acessar a tela de aprovação global (TOTVS SA), acesse o link abaixo:* *[http://localhost/corpore.net/Source/Rhu-RecHumanos/RM.Rhu.Req/RM.Rhu.ReqGlobal/RhuReqExecPage.html?ActionID=RhuReqGlobalPainelControleActionWeb&Col=1&Tprv=2&Req=\B9O\19\3C\F6\CEB\85\95\F2\C4c\E2\0C\E1Q\18E\F3\EC\CA\E57\BB\9B\2DrM\DD4\F1\BB\_](http://localhost/corpore.net/Source/Rhu-RecHumanos/RM.Rhu.Req/RM.Rhu.ReqGlobal/RhuReqExecPage.html?ActionID=RhuReqGlobalPainelControleActionWeb&Col=1&Tprv=2&Req=B9O193CF6CEB8595F2C4cE20CE1Q18EF3ECCAE57BB9B2DrMDD4F1BB_)*

*\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_Pareceres emitidos:* *Emitido em: 28/02/2013 11:03:43* *Responsável: ABGAIL DE OLIVEIRA CARVALHO NEVES* *Filial / Função: Filial Belo Horizonte / Representante Técnico* *Parecer Emitido: teste* \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
