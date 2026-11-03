---
article_id: 4403595715351
category: GPE - eSocial - Carga Inicial
content_hash: 0a88ae646decb7ff9fa64ac5b98e9da0bbea6bc3a5f1772ac4034a5043e43762
fetched_at: '2026-06-28T22:45:03.002430+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - Ao tentar entrar no cadastro de funcionários aparece
  mensagem de erro - Usuário ou módulo sem acesso aos campos necessários ao eSocial
type: support-article
updated_at: '2025-09-18T19:47:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403595715351-RH-Linha-Protheus-GPE-Ao-tentar-entrar-no-cadastro-de-funcion%C3%A1rios-aparece-mensagem-de-erro-Usu%C3%A1rio-ou-m%C3%B3dulo-sem-acesso-aos-campos-necess%C3%A1rios-ao-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25857104754711)** Tempo aproximado para leitura: **00:01:00 min** **Ocorrência**Ao tentar entrar no cadastro de funcionários aparece mensagem de erro informando "**Usuário ou módulo sem acesso aos campos necessários ao eSocial.** **A informação será utilizada somente na base do GPE, sem integração do evento**"  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**A mensagem ocorre devido a validações dos fontes em relação a campos criados ou modificados para atender a versão atual do leiaute em relação a versão anterior  
Para que seu ambiente esteja de acordo com o esperado para envio correto dos eventos eSocial é necessário que esteja com os pacotes Expedição Continua ( RH e TAF) liberados a partir de **18/11/2024** aplicados, inclusive as **atualizações de dicionários.** Também é necessário que os parâmetros **MV\_VLESOC** e **MV\_TAFVLES** estejam com a versão **S\_01\_03\_00.**  
**Solução**1 - Para correção do problema será necessário efetuar atualização do ambiente com o pacote de expedição continua, conforme link abaixo:  
1. [Pacote e Dicionário Correções Expedição Continua RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
2. [Pacote e Dicionário Correções Expedição Continua TAF](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/TAF_EXPEDICAO)  
3. [Pacote e Dicionário Correções Expedição Continua MDT](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/MDT_EXPEDICAO)  
  
Verifique também se o sistema está adequado ao novo leiaute: [RH - Linha Protheus - GPE - eSocial - Como se adequar ao eSocial leiaute S-1.3](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26092480826007-RH-Linha-Protheus-GPE-eSocial-Como-se-adequar-ao-leiaute-S-1-3-eSocial-e-para-quais-releases-est%C3%A1-dispon%C3%ADvel-as-atualiza%C3%A7%C3%B5es)  
  
2- Também é possível que usuário do sistema não possua acesso a todos os campos do cadastro de funcionário que são obrigatórios para o eSocial.   
Por exemplo, se o usuário está tentando incluir um cadastro de funcionário, mas não possui acesso ao campo RA\_SALARIO, o sistema não permitirá a inclusão.  
Esse tipo de configuração é feita pelo nível de acesso ao campo: [RH - Linha Protheus - GPE - Como definir nível de acesso dos usuários para um determinado campo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055770993-RH-Linha-Protheus-GPE-Como-definir-n%C3%ADvel-de-acesso-dos-usu%C3%A1rios-para-um-determinado-campo)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Para conhecimento dos **eventos futuros**, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/rh/?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-#) selecione em categorias a área e pesquise por "**Eventos**".  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade** **WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
