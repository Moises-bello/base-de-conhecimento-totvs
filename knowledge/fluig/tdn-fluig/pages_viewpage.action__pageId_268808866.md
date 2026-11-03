---
content_hash: 5315866319b3a57bf50a0c7b44044e48487cffc5d69e144464b558f7e852be01
fetched_at: '2026-06-28T21:35:24.043347+00:00'
page_id: '268808866'
product: fluig
source: tdn-fluig
title: Identity | O Protheus não está sendo iniciado através do aplicativo no Identity.
  Como resolver?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268808866
version: 6
---

---

**Ocorrência**

Foi realizada a configuração do aplicativo Protheus no Identity e o mesmo deveria abrir o smartclient.exe que está instalado na máquina ao ser acionado. Porém, nada acontece quando o aplicativo é acionado e não é exibido nenhum erro em tela.

**Causa**

O caminho do executável (smartclient.exe) informado nas configurações do aplicativo Protheus está errado.

**Solução**

**01.** Acessar as configurações do aplicativo Protheus no Identity (**Aplicativos** → pesquisar pelo aplicativo do Protheus).

**02.** Nas configurações do aplicativo, selecionar a aba **Entrar**.

**03.** Ajustar o caminho de instalação do smartcliente.exe no campo **Nome do Executável ou Atalho**.

**04.** Salvar as alterações.
