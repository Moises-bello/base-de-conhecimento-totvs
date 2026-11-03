---
content_hash: e2d62b572f05da92f0b6686cfcbb81259b4a2ccc3317a54619854219e622d462
fetched_at: '2026-06-29T00:11:49.576667+00:00'
page_id: '835359157'
product: rm
source: tdn-rm
title: 11- URL's externas
type: documentation
url: https://tdn.totvs.com/display/LRM/11-+URL%27s+externas
version: 19
---

As URL's externas são os links que a instituição pode disponibilizar para o professor acessar.

Essa funcionalidade está disponível a partir da versão 12.1.2406

Permissão de acesso a funcionalidade

Para acessar a funcionalidade, o perfil do professor deverá ter a permissão em: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | URL's externas**

Cadastro de URL's externas

Para realizar a inclusão de uma nova URL's externa, deve-se acessar a tela de:  **Serviços Globais | Serviços | Url's Externas | Url's Externa**

Ao selecionar a **Categoria de URL Externa**, será necessário definir quais perfis estarão autorizados a exibir a URL que estiver cadastrando.

Caso o parâmetro **"Envia Contexto"**estiver marcado, será enviado o contexto do professor via queryString concatenado na própria URL Externa.

**Exemplo de contexto a ser adicionado a URL:**

Context=[**CodSistema=S;Environment=PortalWeb;CodUsuario=JoaoSantana**;CodUsuarioServico=-1;**CodColigada=1;CodFilial=1**;**DataSistema=03/04/2024%2000:00:00**;IdPrj=-1;  
**CodTipoCurso=1**;CodUnidadeBib=-1;CodLocPrt=-1;EduTipoUsr=-1;RhTipoUsr=-1;ChapaFuncionario=-1;CodigoExterno=-1;ExercicioFiscal=-1]

Informações válidas

Apenas as informações de **CodSistema, Environment, CodUsuario, CodColigada, CodFilial, DataSistema, CodTipoCurso** **são válidos** para o portal do professor

Exibição

Exibição no novo Portal do Professor:
