---
article_id: 4412242005783
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 7ef460f585ead712a1d13bf6fe9d9d8486e7e6708d950473b833812840cc3765
fetched_at: '2026-06-28T22:38:45.295748+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) -SIGAFAT - Help Esta nota
  está sem substituta. Confirmar a exclusão?
type: support-article
updated_at: '2025-01-10T20:17:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412242005783-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-Esta-nota-est%C3%A1-sem-substituta-Confirmar-a-exclus%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Ao excluir a nota fiscal de serviço apresenta o help, "esta nota está sem substituta. Confirmar a exclusão?"

![pesquisa.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412252611863/pesquisa.png)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Todas as versões  
  
**Causa**Ao realizar a exclusão da nota de serviços, pode ocorrer algumas situações como:

* Já ultrapassou a data limite de exclusão;
* Está dentro do prazo, porém, o título de ISS já está com vencimento expirado;
* O ISS não está expirado, o parâmetro MV\_VLDSBT = .T. e a nota esta sem substituta.

**Solução**O sistema pode apresentar a tela abaixo, indicando que a nota não possui substituta:

![exc.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4412235857815/exc.jpg)

Também pode apresentar a tela abaixo, solicitando o preenchimento do Processo Administrativo:

![01.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4412235854231/01.PNG)  

A nota substituta e/ou o processo administrativo é exigido por algumas prefeituras em casos de cancelamento de notas que geraram ISS e este já está vencido.

Caso o ISS seja devido, é necessário a emissão da nota substituta ou verificar com sua Assessoria Contábil a forma de emissão do Processo Administrativo.

Caso o ISS seja indevido, é necessário alterar a data de vencimento (**E2\_VENCREA**) no Contas a Pagar (**FINA750**) para uma data igual ou superior à data base (data atual).

**Saiba Mais**  
[Processo Administrativo na Exclusão de Notas Fiscais de Serviço](https://tdn.totvs.com/pages/releaseview.action?pageId=267797581)
