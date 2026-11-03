---
content_hash: b38eee3867367812fca21a4432f209fd6fb1ec95c043ac5810312ee77ba9b11d
fetched_at: '2026-06-29T00:11:50.657737+00:00'
page_id: '844260671'
product: rm
source: tdn-rm
title: FAQ - Integração Aplicativos Externos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=844260671
version: 2
---

# FAQ - Integração Aplicativos Externos

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 12.1.XX ou Superiores |
| **Ocorrência:** | Dúvidas frequentes na integração dos Aplicativos Externo |
| **Ambiente:** | Aplicativos Externo |
| **Passo a passo:** | **Pergunta 1**  É possível no RM a utilização do SAML via ADFS para autenticação dos portais em conjunto com o LDAP para autenticação na MDI do RM.  **Solução**  Atualmente não é possível configurar a integração/autenticação LDAP no RM juntamente com o integração SAML.  **Pergunta 2**  Após a configuração do SAML via ADFS foi apresentado erro sendo necessário liberação para o usuário Sysdb  GRANT SELECT ON GSESSAOFLUIG TO sysdba GRANT DELETE ON GSESSAOFLUIG TO sysdba   **Solução**  Essa permissão não é específica para essa integração pois, já estão presentes no script **Acerta Usuário** padrão da base do RM, que pode ser obtido neste "[Link](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007385351-Framework-Framework-RM-BD-Acerta-usu%C3%A1rio-SQL)". Obs.: Avalie a necessidade de executar esse script nas mudanças de release.    **Pergunta 3**  É possível utilizar o RM com o LDAP habilitado em conjunto com o Oauth2 configurado com a Azure.  **Solução**  O sistema funciona corretamente usando os dois métodos de autenticação LDAP e Oauth2.    **Pergunta 4**  É possível forçar o login do usuário somente através da autenticação Oauth?  **Solução**  Atualmente não têm configuração específica para isso. Uma sugestão é, se o usuário não conhecer as informações para login (usuário e senha), ele obrigatoriamente terá apenas a opção do Oauth2 para realizar o acesso ao sistema, contudo, ele ainda terá acesso a tela inicial de login caso ele clique para fechar a tela de autenticação do Oauth2.  O login automático também é uma possibilidade, pois, quando o usuário salva a sessão do login ao acessar o RM naquela máquina clicando no RM.exe, ele já acessa sem visualizar a tela de login. O parâmetro /Admin garante que a tela de login será aberta sem o carregamento automático.    **Pergunta 5**  Como realizar o login automático usando Oauth?  **Solução**  Basta informar nos parâmetros Globais para Ativar o carregamento automático |
| **Observações:** |  |
