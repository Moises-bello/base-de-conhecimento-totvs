---
content_hash: 003bba4f469fcafff1d05d5656cbc3ea5971c622577a40f0f7703f93a4cb8316
fetched_at: '2026-06-28T21:35:23.067333+00:00'
page_id: '243649873'
product: fluig
source: tdn-fluig
title: Identity | Por que o Chrome não abre aplicativos do tipo Desktop?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243649873
version: 10
---

**Ocorrência**

Foi criado um aplicativo no Identity que executa um programa *desktop*, que fica instalado na estação de trabalho do usuário. Contudo, ao tentar abrir este aplicativo a partir do Launchpad utilizando o navegador Google Chrome, o programa não é executado.

**Causa**

Não foi concedida permissão no navegador Google Chrome para que o aplicativo seja executado.

**Solução**

Ao tentar executar um aplicativo do tipo Desktop, o Chrome irá solicitar a autorização do usuário, conforme a mensagem exibida abaixo. A opção **Iniciar aplicativo** deve ser selecionada para que o aplicativo seja executado.

Caso tenha sido marcada a opção **Lembre-me da minha opção para todos os links deste tipo** e acionado o botão **Não fazer nada**, o Chrome não irá armazenar esta preferência e jamais executará os aplicativos tipo Desktop a partir do Identity. Para reverter esta configuração será necessário reinstalar o Google Chrome na estação de trabalho do usuário.
