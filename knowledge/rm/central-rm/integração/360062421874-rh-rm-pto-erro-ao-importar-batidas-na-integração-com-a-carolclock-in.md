---
article_id: 360062421874
category: Integração
content_hash: f0f372fbe99f43125b50dd6e74ae8def6c3155e9f55f0c31c42b0a5ce556118c
fetched_at: '2026-06-28T22:46:34.655995+00:00'
product: rm
section_id: 6045439793431
source: central-rm
title: RH - RM - PTO - Erro ao importar batidas na integração com a Carol/Clock In.
type: support-article
updated_at: '2025-09-16T16:28:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062421874-RH-RM-PTO-Erro-ao-importar-batidas-na-integra%C3%A7%C3%A3o-com-a-Carol-Clock-In
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19408900750999) Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**  
Ao executar o processo de importação automática de batidas utilizando a integração com a Carol é apresentado no log técnico Carol o erro :

*\*\*\*\*\*\*\* Início do processo de autenticação \*\*\*\*\*\*\**

*Recuperando dados de tenant para autenticação.*  
*Dados de tenant recuperados com sucesso.*  
*- grant\_type: password*  
*- connectorId: clockinmobile*  
*- subdomain: nomeempresa*  
*- orgSubdomain: nomeempresa*  
*Definindo parametros para autenticação.*  
*- urlBase: https://nomeempresa.carol.ai/api/v2/*  
*- urlRequisicao: oauth2/token*  
*Iniciando geração de token de autenticação.*  
*Iniciando requisição http assíncrona.*  
*Aguardando execução da requisição http.*  
*e.Message: One or more errors occurred.*  
*e.InnerException: An error occurred while sending the request.*

*\*\*\*\*\*\*\* Fim do processo de autenticação \*\*\*\*\*\*\**

**Ambiente**RH - RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.1.28  
  
**Causa**Esse incidente ocorre, quando não é possivel efetuar a autenticação na plataforma Carol, devido ao usuário e senha ter sofrido alterações ou quando existe bloqueio de rede.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.** Efetuar o login na URL apresentada no log (*https://nomeempresa.carol.ai/*)  com o mesmo usuário e senha configurado no parametrizador e validar se ele consegue visualizar as  batidas no Clock In.  O acesso pode ser efetuado direto pelo navegador.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103285774)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004615821)

**2**. Se existir alguma configuração de proxy definida no menu : Ambiente | parâmetros | parâmetros globais etapa Google,  nas regras do proxy deve ser liberada a conexão com a Url da Carol.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103286534)

**3.** Acesse os servidores/maquinas envolvidos no ambiente Totvs RM, exemplo: servidor que tem o banco de dados instalado, servidor de Job, servidor de app.   
Estes servidores também devem ter o acesso a URL. Acesse os servidores e tente conectar na URL da Carol direto pelo navegador.

Para verificar se o ambiente da empresa é Local ou N camadas acesse: [RM - Frame - Diferença entre instalação local e 3/N camadas.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019802571-RM-Frame-Diferen%C3%A7a-entre-instala%C3%A7%C3%A3o-local-e-3-N-camadas)

**4.** Avalie se houve alterações de Firewall em sua infra, ou mesmo se o Antivírus está bloqueando o acesso. Pois pode haver impacto na integração. Efetue os ajustes se necessário.

**5.** Verifique se as URL's e portas contidas no artigo abaixo estão liberadas para a integração:

[Requisitos de Infraestrutura](https://tdn.totvs.com/display/public/TCI/Requisitos+de+infraestrutura)

**Saiba Mais:**

Para mais informações da configuração integração RM X Carol acesse : [Integração RM X Carol - Importação de Batidas.](https://tdn.totvs.com/pages/releaseview.action?pageId=441821303)
