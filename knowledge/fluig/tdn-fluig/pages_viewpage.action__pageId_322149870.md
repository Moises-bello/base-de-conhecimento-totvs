---
content_hash: c149c96caa064aaf538c2dbb56211dd21f2c12d83f69c2c5ed7948404c55213d
fetched_at: '2026-06-28T21:35:25.945611+00:00'
page_id: '322149870'
product: fluig
source: tdn-fluig
title: Solução de problemas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=322149870
version: 16
---

true.\*ndicenone

Nesta página reunimos algumas situações comuns que podem ocorrer durante a utilização da autenticação multifator do TOTVS Identity (ou outros serviços) com o My Safe id e que procedimentos podem ser realizados para solucioná-las.

#### O token do My Safe id é inválido

Aguarde a geração de um novo token pelo My Safe id (isso demora no máximo 30 segundos) e tente novamente.

#### O novo token também é inválido

Nas configurações de Data e Hora do *smartphone* em que o My Safe id está instalado, habilitar a opção **Automaticamente** (iPhone) ou **Data e hora automáticas** e **Fuso horário automático** (Android).

#### Desinstalei o My Safe id do aparelho

Solicite ao administrador do contexto da sua empresa no Identity redefinir a configuração MFA da sua conta. O procedimento está descrito no manual [Gerenciar Usuário](http://tdn.totvs.com/pages/viewpage.action?pageId=317306108#GerenciarUsuário-RedefiniracessocomMFAdousu%C3%A1rio).

Após a redefinição, basta acessar novamente o menu **Segurança** → **Multi-Factor Authentication** para escanear um novo QR Code e habilitar o My Safe id novamente no aparelho.

#### Troquei de aparelho

Solicite ao administrador do contexto da sua empresa no Identity redefinir a configuração MFA da sua conta. O procedimento está descrito no manual [Gerenciar Usuário](http://tdn.totvs.com/pages/viewpage.action?pageId=317306108#GerenciarUsuário-RedefiniracessocomMFAdousu%C3%A1rio).

Após a redefinição, basta acessar novamente o menu **Segurança** → **Multi-Factor Authentication** para escanear um novo QR Code e habilitar o My Safe id novamente no aparelho.

#### Sou o administrador do contexto e preciso redefinir o MFA na minha própria conta

Caso você seja o único administrador do contexto, abra um ticket para o [Suporte do TOTVS Fluig](http://suporte.fluig.com) que faremos a redefinição da MFA da sua conta para você.
