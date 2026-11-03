---
article_id: 35174492360215
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: bc574f8085553adcdf4d9c5bfe6f3b10d5e835629501e7dd2e6c377117630532
fetched_at: '2026-06-28T22:37:22.718880+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Envio de e-mail para
  o evento 040 (Limite saldo na planilha) Eventviewer
type: support-article
updated_at: '2025-09-26T11:47:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35174492360215-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Envio-de-e-mail-para-o-evento-040-Limite-saldo-na-planilha-Eventviewer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35174492344087) Tempo aproximado para leitura: **00:05:SS min**  
  
**Dúvida**  
Envio de e-mail para o evento 040 **(Limite saldo na planilha)** do Eventviewer.

**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Gestão de Contratos - Todas as versões  
  
**Solução**

**1.**Incluir o Cadastro do "Evento 040" em Miscelânea>Insc.Eventviewer no cadastro do usuário que irá receber o email , veja mais detalhes no link [Eventviewer](https://tdn.totvs.com/display/public/PROT/Configurar+Event+Viewer).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35175503563159)

2.É necessário que o usuário que irá receber o email tenha o e-mail cadastrado no cadastro de usuários do configurador do sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35175514319255)

3.No cadastro do tipo de planilha, informar o campo Perc Aviso (CNL\_LMTAVS).

![](https://tdn.totvs.com/download/attachments/663613194/image2022-2-1_9-59-35.png?version=1&modificationDate=1643721285433&api=v2)

**Exemplo:**

O e-mail será enviado no encerramento da medição, caso o saldo da planilha esteja dentro do percentual configurado.

* Contrato no valor total de 100.000, com 80% definido no campo CNL\_LMTAVS.
* Ao realizar uma medição de 10.000, o saldo da planilha ficará em 90.000. Nesse momento não será disparado o e-mail , pois ainda não atingiu o limite de 80.000 (80% do valor do contrato).
* Em seguida, ao realizar mais uma medição de 20.000, o saldo da planilha passará para 70.000. Nesse caso, o e-mail será isparado, pois o saldo atingiu o limite configurado.
* Dessa forma, sempre que o saldo ultrapassar o limite definido conforme exemplo, o sistema enviará automaticamente o e-mail no encerramento da medição.

  4.Exemplo do Disparo de e-mail:
* ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35175503568919)

***Saiba Mais:***

[GCT0020\_Configuração para utilização dos eventos 040(Limite saldo na planilha) e 041(log execução medição automática)](https://tdn.totvs.com/pages/releaseview.action?pageId=663613194)

[GCT0028\_MV\_ATUGCT\_Eventos\_038\_e\_039](http://tdn.totvs.com/display/PROT/GCT0028_MV_ATUGCT_Eventos_038_e_039)

[GCT0127\_Eventos\_038\_e\_039\_Configuração\_via\_Schedule](https://tdn.totvs.com/pages/releaseview.action?pageId=402071753)

[GCT0125 - Ativando e-mails de avisos automáticos do módulo GCT](https://tdn.totvs.com/pages/releaseview.action?pageId=393363398)

[GCT0032\_Aviso\_de\_Vencimento](https://tdn.totvs.com/display/public/PROT/GCT0032_Aviso_de_Vencimento)

[GCT0158\_Cadastrando eventos no EventViewer do GCT](https://tdn.totvs.com/x/Nyz2MQ)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)

[GCT0028\_MV\_ATUGCT\_Eventos\_038\_e\_039](https://tdn.totvs.com/display/public/PROT/GCT0028_MV_ATUGCT_Eventos_038_e_039)
