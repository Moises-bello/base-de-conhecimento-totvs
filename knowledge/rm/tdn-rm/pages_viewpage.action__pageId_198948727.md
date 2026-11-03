---
content_hash: 716496dee952ece72557c4a07ab35cf616ebc928152397faa6dd96fb74477ff5
fetched_at: '2026-06-29T00:06:02.700831+00:00'
page_id: '198948727'
product: rm
source: tdn-rm
title: Facebook (Aplicativo)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198948727
version: 10
---

# Pré-requisitos

---

2
complete
Linha RM atualizada até a versão 12.1.5

# Objetivos

---

Para que um sistema (RM) possa se integrar às redes sociais, é necessário a criação de um aplicativo nos provedores e gerar uma chave de acesso para a comunicação com a rede.

# Criando o App

---

1. Acessar <https://developers.facebook.com>
2. Selecione Meus Aplicativos -> Adicionar um novo aplicativo
3. Preencher os dados necessários ao cadastro
4. Importante:

   Na aba Configurações -> Avançado

   * Aplicativo nativo ou para desktop ? Sim.
   * Descoberta social ? Sim.
5. Na Opção Produtos acesse "+Adicionar Produto"
   * Selecione a opção "Login do Facebook e clique em Começar"
6. Acesse a Opção Login do Facebook | Configurações  

   Na aba Configurações

   * Login no OAuth do cliente ? Sim.
   * Login do OAuth na Web ? Sim.
   * Login do Oauth no navegador incorporado ? Sim.

Importante

Para o Facebook, somente o usuário administrador da aplicação pode fazer atualizações na rede social usando o RM, devido a restrições do próprio Facebook. Vide links abaixo:

<https://developers.facebook.com/policy/>

<https://developers.facebook.com/docs/apps/review>

1. Para verificar o ID do Aplicativo e Chave Secreta do Aplicativo do Facebook, acesse <https://developers.facebook.com>
2. Selecione Meus Aplicativos -> <Nome do Aplicativo>
3. Aba Painel:

   * ID do Aplicativo
   * Chave Secreta do Aplicativo
4. Dentro do RM, Parâmetros Globais, aba Redes Sociais informar os dados dos respectivos aplicativos:

Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)

|  |  |
| --- | --- |
| **Produto** | Framework |
| **Versão** | 12.1.5 |
| **Processo** | Gestão |
| **Subprocesso** | Comunicação |

|  |  |
| --- | --- |
| **Status do documento** | Produção |
| **Data** | 18/08/2015 |
| **Versão** | 1.0 |
| **Versão anterior** | 1.0 |
| **Autores** |  |

| Índice |
| --- |
| truenone |
