---
article_id: 360011965651
category: esocial - Processos
content_hash: 604560c8b8a31a3fa20927013cc4196b706cb6783c0ab32fa4c77ffa5daa8b2d
fetched_at: '2026-06-28T22:47:08.396940+00:00'
product: rm
section_id: 1500000834441
source: central-rm
title: RH - RM - FOP - eSocial - Limpeza da base de dados do ambiente de produção
  restrita
type: support-article
updated_at: '2024-06-27T18:08:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011965651-RH-RM-FOP-eSocial-Limpeza-da-base-de-dados-do-ambiente-de-produ%C3%A7%C3%A3o-restrita
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24481841304343) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Quais processos realizar após limpeza da base de dados no ambiente de produção restrita do governo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da versão 12.1.22  
  
**Solução**As empresas que enviaram eventos no ambiente de produção restrita deverão reenviá-los após a limpeza da base de dados feita pelo governo. Para isso deveremos executar alguns processos no RM e no TAF conforme abaixo:  
1. Para fazer a limpeza da fila de eventos no RM e assim ser possível o reenvio das informações para o governo, é imprescindível que o ambiente utilizado seja de homologação. Assim, verifique em **Configurações | Parametrizador | eSocial | Configurações Gerais 1/5** se o campo **Tipo de Ambiente** está preenchido com **2- Produção restrita**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040234073)

2. Após conferência do tipo de ambiente, selecione o menu **Outros Processos | Limpar Fila de Eventos**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039393594)

2.1. É muito importante ficar atento a todas as mensagens apresentadas pelo processo. Em caso de dúvidas, acesse os nossos canais de atendimento antes de proceder com a exclusão;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008597191)

2.2. Selecione os eventos a serem excluídos e clique no botão **Avançar**;

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008597531)

2.3. Selecione a coligada e clique no botão **Avançar.** Será exibida mensagem de alerta relacionada ao processo **Atualizar Status Integração TAF**. Ao selecionar a opção **Sim**, basta executar o processo clicando no botão **Executar;**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008597791)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008597931)

3. Após a execução do procedimento no RM, é necessário executar o procedimento de Limpeza no TAF. Certifique-se então se o tipo de ambiente do TAF está preenchido como **2** (produção restrita);  
4. Após conferência do tipo de ambiente, acesse o menu **Miscelanea | Funcionalidades | Exclusão por Período Fiscal**;

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008565092)

 4.1 No campo **Excluir movimento eSocial** informe **Sim** e execute o processo.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008565252)

Após execução desse processo, tanto o RM quando o TAF estão prontos para o reenvio das informações para a produção restrita.  
  
**Importante**  
O ambiente de produção do governo não sofre limpeza de dados. Desta forma, nunca realize a limpeza da fila de eventos se o **Tipo de Ambiente** estiver como **1 - Produção**.  
  
**Saiba mais**  
[Como realizar a alteração do Tipo de Ambiente (MV\_TAFAMBE) no TAF?](http://tdn.totvs.com/pages/releaseview.action?pageId=334334200)
