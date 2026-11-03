---
article_id: 39544478522519
category: Materiais - Compras (SIGACOM)
content_hash: b66d6c76f9585afa2d844c118857a4105f0e04277e449275f5cdcf34da1eba50
fetched_at: '2026-06-28T22:41:24.002411+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - PORTAL FORNECEDOR
  - AUTHENTICATION: USER NOT AUTHORIZE'
type: support-article
updated_at: '2026-04-06T14:21:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39544478522519-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-PORTAL-FORNECEDOR-AUTHENTICATION-USER-NOT-AUTHORIZE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39544493712663) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Ao efetuar o Login no Portal do Fornecedor, gera a mensagem de acesso negado : AUTHENTICATION: USER NOT AUTHORIZED"

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39544478500375)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12

**Solução :**

Para o correto funcionamento do Portal, valide os pontos a seguir:

1.  Configuração do Portal, conforme o Artigo: [PORTAL FORNECEDOR - Configuração básica e demais ocorrências](https://totvssuporte.zendesk.com/knowledge/editor/01HE58P3Z8XB6VBMNG3YDAS3E9/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F360027708192)

OBS: ***A chave SECURITY = 1 se tornou obrigatória na configuração do Ini, a partir da release 12.1.2310***

2. Inserir no Menu a rotina AUTHWSRH, acessar a rotina citada no Protheus | Autenticação :  [Função para Usuário e Senha para portal](https://tdn.totvs.com/pages/releaseview.action?pageId=563435668).

Nessa rotina o sistema solicitará que sejam informados o usuário e a senha (para validação dos dados – senha mascarada em tela) e caso os dados estejam corretos, o sistema gravará o conteúdo criptografado no parâmetro **MV\_AUTHWS**. Caso o usuário altere a senha no configurador, ele deverá refazer a autenticação por essa rotina.

**O usuário e senha a serem informados são os mesmos utilizados no acesso ao Protheus**.

Apenas os usuários pertencentes ao grupo de administradores do sistema podem acessar esta rotina. O usuário e senha a serem utilizados na autenticação também devem pertencer ao grupo de administradores.

2. Acessar a rotina citada no Protheus | Autenticação WS.

***Saiba Mais:***

[Como alterar logo da tela de login e superior esquerdo do portal do fornecedor?](.com/hc/pt-br/articles/21633342931095-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-alterar-logo-da-tela-de-login-e-superior-esquerdo-do-portal-do-fornecedor)

[PÁGINA CENTRALIZADORA DO COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigo Materiais - COMPRAS ( SIGACOM )](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual Funcionamento dos parâmetros MV\_PORTAL1 / MV\_PORTAL2 / MV\_PORTAL3 e MV\_PORTAL4 no Portal do Fornecedor ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6044175266967-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-Funcionamento-dos-par%C3%A2metros-MV-PORTAL1-MV-PORTAL2-MV-PORTAL3-e-MV-PORTAL4-no-Portal-do-Fornecedor)
