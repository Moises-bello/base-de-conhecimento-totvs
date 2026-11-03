---
article_id: 360039953813
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: ecd888db9c0512d15e5156904f2bf79cff5132f2f87f05578dd1e78fe75672c8
fetched_at: '2026-06-28T22:38:31.221859+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-Help: QuantSerie'
type: support-article
updated_at: '2022-01-12T11:57:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039953813-MP-FAT-Help-QuantSerie
---

**Ocorrência**

Ao incluir pedido de venda (**MATA410**) com endereçamento, ocorre help: 

**Help "QUANTSERIE: Problema: Quando utilizamos número de série a quantidade deve ser igual a 1."**  
   
 **Ambiente**

Microsiga Protheus - a partir da release 12.1.17.  
   
 **Causa**

O problema ocorria na validação da função **MtVlQtSe** que era chamada no momento em que o endereçamento do produto era preenchido no pedido, acionando o help de forma indevida.

**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download do **SIGACUSB** ,mais atual, conforme a release de sistema:

12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=790405> ;

12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=790404> ;

12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=790403> ;

2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;

3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
