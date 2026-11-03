---
content_hash: e01529684b6f24d85adc15bf03db4abd0f73cd3ba15c7eb838952ab484d0814c
fetched_at: '2026-06-29T00:12:03.392222+00:00'
page_id: '908339712'
product: rm
source: tdn-rm
title: 5- Customização para utilizar apenas o login unificado dos portais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=908339712
version: 3
---

O login unificado dos portais, permite que a instituição realize a configuração para que seja utilizado apenas o login unificado dos portais nos portais **Aluno**, **Professor**e **Gestão Educacional.** Para isso, acesse é necessário acessar configurar cada portal de forma independente.

As customizações **devem ser realizadas em cada servidor web existente.**

Desta forma é **altamente necessário sempre** que tiver uma atualização de patch o cliente **salve as informações antes da atualização, e após a mesma, faça as modificações anteriormente realizadas**.

Portal do aluno

Deve ser configurado **para ativo** a tag "**EDU\_CONST\_GLOBAL\_USAR\_LOGINPORTAIS**", caso deseja **utlizar apenas o** **login unificado dos portais**, ao **invés da tela de login do portal do aluno**. Desta forma, ao usuário tentar acessar a tela de login do portal do aluno, **será redirecionado automaticamente** para a tela de **login unificado dos portais.**

**Arquivo:** C:\totvs\CorporeRM\FrameHTML\Web\App\Edu\web\app\Edu\portaleducacional\js\edu-contantes.global.config.js

Portal do professor

Deve ser configurado **para ativo** a tag "unifiedLogin", caso deseja **utlizar apenas o** **login unificado dos portais**, ao **invés da tela de login do portal do professor**. Desta forma, ao usuário tentar acessar a tela de login do portal do professor, **será redirecionado automaticamente** para a tela de **login unificado dos portais.**

**Arquivo:** C:\totvs\CorporeRM\FrameHTML\Web\App\Edu\web\app\Edu\portaldoprofessor\config\config.json

Portal do gestão educacional

Deve ser configurado **para ativo** a tag "unifiedLogin", caso deseja **utlizar apenas o** **login unificado dos portais**, ao **invés da tela de login do portal do gestão educacional**. Desta forma, ao usuário tentar acessar a tela de login do portal gestão educacional, **será redirecionado automaticamente** para a tela de **login unificado dos portais.**

**Arquivo:** C:\totvs\CorporeRM\FrameHTML\Web\App\Edu\web\app\Edu\portalgestaoeducacional\config\config.json
