---
article_id: 4409699320343
category: eSocial - Middleware
content_hash: fcec0efb7881a8b4e3dc6bd823f7f2b6a7590ba5a2a202f445ae8752f2d335c2
fetched_at: '2026-06-28T22:47:05.587549+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Middleware: evento sem retorno do governo'
type: support-article
updated_at: '2026-05-27T14:11:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409699320343-RH-RM-FOP-eSocial-Middleware-evento-sem-retorno-do-governo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17089888030871) Tempo aproximado para leitura: **00:02:00 mim****Dúvida**O que fazer quando o evento enviado através do Middleware não é retornado pelo governo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões

**Solução**O objetivo deste documento é orientar como proceder caso tenha transmitido algum evento ao governo através do Middleware, porém, ao realizar a atualização do status, não existe retorno por parte do governo (continua com status **3 - Enviado**).

Para avaliar o motivo da falta de retorno. siga os passos abaixo:

1. Verifique se o ambiente do governo está estável. É possível fazer um acompanhamento através do [semáforo](https://www.gov.br/esocial/pt-br/acesso-ao-sistema/semaforo) do Portal eSocial;  
2. Verifique se não existem bloqueios internos através de firewall ou políticas de proxy na rede da empresa. Para consultar os eventos, é necessário possuir permissão para acesso às url's:

- **Ambiente Produção**:   
https://webservices.consulta.esocial.gov.br/servicos/empregador/consultarloteeventos/WsConsultarLoteEventos.svc  
- **Ambiente Produção Restrita**:   
https://webservices.producaorestrita.esocial.gov.br/servicos/empregador/consultarloteeventos/WsConsultarLoteEventos.svc

3. Para esta situação dos eventos que estão com status **3 - Enviado**, pode ser necessário a atualização do TSS. Acesse as documentações abaixo para atualização do binário, do arquivo RPO e dos *schemas* na pasta de instalação do TSS:

- [Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)  
- [Atualização do Appserver (binário) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062416694)  
- [Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

3.1. O próximo passo é a atualização da *URL* do TSS;

- [Atualizando URL TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025394911-TSS-Atualiza%C3%A7%C3%A3o-das-URLs-do-TSS)

3.2. Acesse o diretório de instalação do TSS e na pasta **[...]TSS\bin\appserver**, edite o arquivo **appserver.ini**. Na seção [**General**], ajuste a chave **MaxStringSize** para o valor **20**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410080007959)
