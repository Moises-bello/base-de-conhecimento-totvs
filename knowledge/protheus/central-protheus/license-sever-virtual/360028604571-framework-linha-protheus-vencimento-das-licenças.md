---
article_id: 360028604571
category: License Sever Virtual
content_hash: 317f42cc135b9de6e0e0f26661557bb2784bdb28a9c4159a25c73ce2ca1e600a
fetched_at: '2026-06-28T22:42:20.086929+00:00'
product: protheus
section_id: 360000075428
source: central-protheus
title: Framework - Linha Protheus - Vencimento das Licenças
type: support-article
updated_at: '2026-01-27T17:22:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028604571-Framework-Linha-Protheus-Vencimento-das-Licen%C3%A7as
---

**Dúvida**

O que fazer quando receber a mensagem de expiração das licenças?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27639189594519)

**Ambiente**

Protheus - LSVirtual - Todas as versões

**Solução**

**Para versões do License Server virtual inferiores à 3.6.2, é imprescindível que a empresa** [**atualize**](https://tdn.totvs.com/display/public/framework/TOTVS+License+Server+Virtual#TOTVSLicenseServerVirtual-Atualiza%C3%A7%C3%A3odoLicenseServer.:~:text=15%20minutos-,Atualiza%C3%A7%C3%A3o%20do%20License%20Server%C2%A0,-Caso%20seja%20necess%C3%A1ria) **para a versão mais recente para garantir o funcionamento correto e ininterrupto do sistema.**  
**Caso a atualização não seja realizada, a mensagem continuará a ser exibida e nenhuma outra ação será capaz de solucionar a mensagem apresentada.**

Para manter o License Server Virtual ativo e com as licenças atualizadas, é necessário que o servidor tenha acesso à internet. O Acesso é realizado através do protocolo HTTPS e toda a comunicação é feita pela porta 443. Caso a sua empresa possua Firewall e/ou restrições de acesso à internet, é necessário que o administrador da rede libere o endereço <https://licenseservercloud.totvs.com.br>, para comunicação.

O tráfego ocorrerá uma vez por dia no horário estabelecido pela TOTVS e caso a conexão seja interrompida por mais de 3 dias, a autorização de uso do sistema expirará e os usuários e/ou administradores dos software TOTVS serão notificados no Login do sistema, permanecendo por mais 4 dias, totalizando 7 dias na modalidade off-line. Após este prazo, o sistema não estará mais disponível.

**Importante:**  
Para o correto funcionamento, é imprescindível que mantenha o License Server com a versão atualizada.

**Abaixo link com o procedimento para atualização:**

[https://tdn.totvs.com/display/public/framework/TOTVS+License+Server+Virtual#TOTVSLicenseServerVirtual-Atualiza%C3%A7%C3%A3odoLicenseServer.](https://tdn.totvs.com/display/public/framework/TOTVS+License+Server+Virtual#TOTVSLicenseServerVirtual-Atualiza%C3%A7%C3%A3odoLicenseServer)

Ao aparecer a mensagem de Vencimento de Licenças e utilizando a versão mais recente do License Server, poderá realizar o sincronismo manual através do Monitor do License Server, para isso, basta utilizar o ícone com o símbolo de antena (canto superior direito).

Neste processo, caso gere algum erro, recomendamos avaliar os itens listados na documentação [https://tdn.totvs.com/pages/releaseview.action?pageId=715829897.](https://tdn.totvs.com/pages/releaseview.action?pageId=715829897)

Segue abaixo o procedimento de sincronização manual do License Server Virtual:

- Abra o Monitor do LS Virtual

- Clique no ícone com o símbolo de antena (canto superior direito);

- Aguarde a sincronização;

- Verifique se foi atualizado clicando no ícone com o símbolo de um balão de informação (canto superior direito);

- O campo Data de Geração da Autorização de Uso deverá mostrar a data atual

Em caso de dúvidas, o suporte poderá ser acionado.

Links úteis para leitura:

<https://tdn.totvs.com/pages/releaseview.action?pageId=715829897>

[Atualização](https://tdn.totvs.com/display/public/framework/TOTVS+License+Server+Virtual#TOTVSLicenseServerVirtual-Atualiza%C3%A7%C3%A3odoLicenseServer.:~:text=15%20minutos-,Atualiza%C3%A7%C3%A3o%20do%20License%20Server%C2%A0,-Caso%20seja%20necess%C3%A1ria)
