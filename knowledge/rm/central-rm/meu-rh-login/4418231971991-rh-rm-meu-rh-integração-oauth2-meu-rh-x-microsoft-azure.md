---
article_id: 4418231971991
category: Meu RH - Login
content_hash: df1f8855c26fa83f42cbc4c2f2a64b207f87739081e95f59399efa41ec01e91f
fetched_at: '2026-06-28T22:47:27.307415+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Integração OAuth2, Meu RH X Microsoft Azure
type: support-article
updated_at: '2026-01-16T15:27:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418231971991-RH-RM-Meu-RH-Integra%C3%A7%C3%A3o-OAuth2-Meu-RH-X-Microsoft-Azure
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24077812898071) Tempo aproximado para leitura: **00:03:12 min**  
  
**Dúvida**  
Como configurar o o Meu RH para autenticar com Oauth2 Microsoft Azure Active Directory?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir do release 12.1.33.158  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1.  Realizar configurações já previstas para linha RM na  documentação <https://tdn.totvs.com/pages/releaseview.action?pageId=651942057>

2.  Habilitar o TOKEN  no Meu RH. No diretório **\FrameHTML\web\app\RH\PortalMeuRH** edite o arquivo "**properties.json**" e atribua o valor  "**true**" à propriedade "**USE\_TOKEN**".

|  |
| --- |
| `"USE_TOKEN": true` |

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418220243479)

3. Acessar <https://portal.azure.com/>

3.1 Todos os Serviços

![](https://tdn.totvs.com/download/attachments/654103174/image2021-12-6_17-29-57.png?version=1&modificationDate=1638822597397&api=v2)

 3.2 Em seguida selecionar, identidade no menu lateral esquerdo e clicar em “**Active Directory do Azure**”

![](https://tdn.totvs.com/download/attachments/654103174/image2021-12-6_17-31-28.png?version=1&modificationDate=1638822688363&api=v2)

3.3 Considerando as configurações previas realizadas, utilizaremos o mesmo Registro de Aplicativo já criado.

![](https://tdn.totvs.com/download/attachments/654103174/image2021-12-6_17-31-52.png?version=1&modificationDate=1638822712917&api=v2)

3.4 Em seguida clique no aplicativo já existente.

![](https://tdn.totvs.com/download/attachments/654103174/image2021-12-6_17-32-19.png?version=1&modificationDate=1638822739697&api=v2)

3.5 A seguinte tela será exibida, clicamos então no menu “Autenticação”.

![](https://tdn.totvs.com/download/attachments/654103174/image2021-12-6_17-32-45.png?version=1&modificationDate=1638822765230&api=v2)

3.6 Em seguida clicar em “Adicionar uma plataforma” e selecionar a configuração “Aplicativo de pagina única”

![](https://tdn.totvs.com/download/attachments/654103174/image2021-12-6_17-33-5.png?version=1&modificationDate=1638822785747&api=v2)

3.7 Nesta etapa será necessário definir o URI de redirecionamento.

Exemplo .:

MeuRh:  <http://localhost:8089/web/app/RH/PortalMeuRH>

\*\* http://{servidor}:{porta}/web/app/RH/PortalMeuRH

![](https://tdn.totvs.com/download/attachments/654103174/image2021-12-6_17-34-6.png?version=1&modificationDate=1638822846420&api=v2)

**Importante:**A URL de Redirecionamento é case sensitive, para acessar o Meu RH com sucesso deverá utilizar a mesma URL que está sendo informada. Poderá inserir mais de uma URL de redirecionamento.

4. Usuário de RM deve estar com o mesmo e-mail utilizado para login Azure.

**RM**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418239306903)

**Azure**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418227169431)

5. Realize o login no Meu RH através da integração com Azure Active Directory

![](https://tdn.totvs.com/download/attachments/654103174/image2021-12-6_17-59-0.png?version=1&modificationDate=1638824341933&api=v2)

**Saiba Mais**

 [CLIQUE AQUI para acessar a documentação completa sobre a integração  OAuth2](https://tdn.totvs.com/pages/viewpage.action?pageId=654103174)
