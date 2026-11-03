---
article_id: 34539886822295
category: MIDDLEWARE eSocial
content_hash: 2e0dd695e873136e3900ef30a0e3841bcb39906342a46179c44b2033ccc2ebb3
fetched_at: '2026-06-28T22:43:04.927030+00:00'
product: protheus
section_id: 360005445753
source: central-protheus
title: RH - Linha Protheus - TAF - ATUALIZAÇÕES - TAF e TSS para clientes MIDDLEWARE
type: support-article
updated_at: '2026-06-19T21:29:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34539886822295-RH-Linha-Protheus-TAF-ATUALIZA%C3%87%C3%95ES-TAF-e-TSS-para-clientes-MIDDLEWARE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34539893354903) Tempo aproximado para leitura: **00:15:00 min**  
  
**Dúvida**  
Utilizo o middleware, e preciso atualizar o TAF e TSS, como deve ser realizado?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Atualizações - Middleware - Todas as versões  
  
**Solução**

**1º Pare todos os serviços referentes ao TAF/Protheus e TSS, para execução do processo:**

DBAccess

TAFWS

TSS

**2º Atualize do DBAccess:**  
[RH - Linha Protheus - TAF - eSocial - ATUALIZAÇÃO - Como atualizar o DBACCESS do TAF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18504207190039)  
   
**3º Atualize o RPO do TAFWS 12.1.2310, abaixe o arquivo RPO e cole-o na sua pasta APO do TAFWS:**

Link para o download do RPO:

[REPOSITORIO DE OBJETOS 12.1.2310 TAFWS](https://suporte.totvs.com/portal/p/10098/download#detail/1122630)  
   
**4º Atualize os arquivos Binário para o TAFWS, baixe os arquivos e cole-os na sua pasta APP do TAFWS:**

Link para o download do Binário TAFWS:

[APPSERVER HARPIA TAFWS](https://suporte.totvs.com/portal/p/10098/download?e=1112215)  
   
**5º Abra o arquivo appserver.ini da pasta APP e edite as linhas TAF\_CFGJOB e ONSTART como seguem abaixo, salve as alterações:**  
  
**;[TAF\_CFGJOB]**  
MAIN=TAF\_CFGJOB  
Instances=2,2  
Environment=TAF\_WS  
preparein=all  
RefreshRate=120

**[Onstart]**  
Jobs=HTTPJOB  
;TAF\_CFGJOB  
RefreshRate=120  
    
**6º Atualização completa do TSS, baixe os arquivos dos links 12.1.2410, basta substituir os arquivos em suas** **devidas pastas:**  
[RH - Linha Protheus - TAF - eSocial - ATUALIZAÇÃO -  Links para atualizar o TSS - Transmissão de Documentos Eletrônicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7658806742679)  
  
**7º Após as manutenções descritas acima, suba os serviços novamente:**  
DBAccess, TAFWS e TSS

**Saiba Mais**

Para saber mais consulte os links abaixo:   
[Centralizadora TAF](https://tdn.totvs.com/display/public/TAF/Centralizadora+TAF)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos"

Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
