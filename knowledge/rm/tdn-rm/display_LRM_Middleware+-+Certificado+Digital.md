---
content_hash: e059dbf5988418d99c662fc02a53d80e6065246f3418f03e938257acac4d9e86
fetched_at: '2026-06-29T00:10:50.682144+00:00'
page_id: '562955566'
product: rm
source: tdn-rm
title: Middleware - Certificado Digital
type: documentation
url: https://tdn.totvs.com/display/LRM/Middleware+-+Certificado+Digital
version: 11
---

false

**A partir das Versões:**

* 12.1.27.288
* 12.1.28.200
* 12.1.29.125
* 12.1.31.000

# Objetivo:

---

       O objetivo deste documento é apresentar como deverá registrar o Certificado Digital para o Middleware.

0trueCertificado Digital A1Certificado Digital A1

Acesse o menu Serviços Globais| Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em acesso aos menus e permita o acesso 09.01.19 Certificado Digital

Realize a importação do certificado através do menu: RH | Folha de Pagamento | eSocial | Certificado Digital 

Clique em Processos | Importar Certificado digital

Selecione o certificado que deseja realizar a importação, digite a senha e cadastre uma descrição e clique em <executar>.

Após a finalização desse processo o certificado estará disponível para utilização.

Ativação do MiddlewareAtivação do Middleware

Para ativação do middleware acesse o menu: RH | Folha de Pagamento | eSocial | Outro Processos | Ativar Integração com Middleware

Cadastre os dados de conexão com o Web Service Middleware, sendo eles: dados de conexão com o Web Service TSS, dados do Certificado digital (opção de seleção do certificado ao marcar tipo do Certificado Digital A1 - Formato PFX(.pfx ou .p12)) e Identificador da tabela de rubricas utilizado pelo TAF.

Ao clicar , será apresentada a lista de certificados importados/cadastrados.

Mais detalhes da ativação do middleware [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=519722143).

**Observação:** Caso a seleção do tipo do certificado seja A3 - HSM (Hardware Security Module) será habilitado os campos para cadastro das informações e deverá ser apontando o diretório do certificado.

Alteração do certificado no middlewareAlteração do certificado no middleware

Caso tenha realizar a alteração do certificado.

Acesse o menu RH | Folha de Pagamento | Configurações| Parametrizador, clique no item 06.07 - esocial | 06.07.01 - Configurações Gerais | Integração com Middleware

Ao clicar , será apresentada a lista de certificados importados/cadastrados.

Selecione o certificado desejado e clique em <Atualiza Certificado>.

**Observação:** Caso a seleção do tipo do certificado seja A3 - HSM (Hardware Security Module) será habilitado os campos para cadastro das informações e deverá ser apontando o diretório do certificado.
