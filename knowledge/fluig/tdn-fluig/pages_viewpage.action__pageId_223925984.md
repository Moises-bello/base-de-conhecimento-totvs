---
content_hash: b585926beb5ac6f519cc4f8ad2b8a0c12fabeba09569c9d713f026a980f8102f
fetched_at: '2026-06-28T21:35:19.831068+00:00'
page_id: '223925984'
product: fluig
source: tdn-fluig
title: WCM - Por que minha página pública está solicitando credenciais?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223925984
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Mesmo após configurar uma determinada página como pública, o Fluig Plataforma continua solicitando login e senha na hora de acessá-la.

# Causa

Os usuários estão tentando a acessar a página com o endereço em modo privado: http://[endereço\_fluig]/portal**/p**/empresa/[nome\_pagina\_publica]. O "/p" na URL indica "Privado" e por isso exige as credenciais para acesso;

# Solução

Retirar o "/p" no endereço, assim o Fluig acessará a página em modo público.

# Observações

Configurar uma página como pública não significa que ela será sempre acessada sem pedir credencias, mas simplesmente que foi habilitado um "Modo Público" de acesso a ela.

O "Modo Privado" continua funcionando normalmente. Esse recurso foi pensado dessa forma para que possam ser feitas validações e, se necessário, modificar o comportamento da página dependendo da forma como ela é acessada.

Vale notar que a página em modo público pode apresentar erros que não apresenta quando é acessada em modo privado. Isso vai depender de quais *widgets* foram configuradas nessa página e da forma como elas se comportam em uma página em modo público.
