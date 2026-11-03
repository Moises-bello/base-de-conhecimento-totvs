---
article_id: 360033898193
category: Ativo Fixo - Transferência
content_hash: 8462d52d7efc14e8ae9a4c3deb29907fae2bf125077f1911a1f425689cc9121d
fetched_at: '2026-06-28T22:41:52.222895+00:00'
product: protheus
section_id: 1500001536061
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF -ATFA060 TRANSFERÊNCIA
  CIAP COMO FAZER
type: support-article
updated_at: '2024-11-01T11:43:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033898193-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA060-TRANSFER%C3%8ANCIA-CIAP-COMO-FAZER
---

**Dúvida**

O sistema realiza a transferência do CIAP ?  
  
**Ambiente**  
Microsiga Protheus – Ativo Fixo – A partir da versão P11  
  
**Solução**

**Versão P11**ao realizar a transferência do bem através da rotina "Transferência do ativo ATFA060" o sistema **não** possui a funcionalidade de  transferir automaticamente o CIAP para a filial destino.

* A partir da versão P11 os campos [N1\_CODCIAP e N1\_ICMSAPR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011054291-MP-SIGATF-CAMPOS-DO-ATIVO-BLOQUEADOS-N1-CODCIAP-N1-ICMSAPR-?source=search)foram bloqueados a pedido do time do modulo fiscal
* Para cliente com contrato de garantia estendida foi liberado [Ponto de Entrada AT010SN1 Permitir Alterar Campos do Ativo](http://tdn.totvs.com/display/public/PROT/2527405+DSERCTR1-10639+DT+Ponto+de+Entrada+AT010SN1+Permitir+Alterar+Campos+do+Ativo). Para obter o  pacote clique [DSERCTR1-10639](https://suporte.totvs.com/portal/p/10098/download?e=696169)
* Com isso após habilitar o Ponto de entrada para edição dos campos realize:

**1 Passo** : Através da rotina "Transferência do ativo ATFA060" realize a transferência do bem para a filial destino

**2 Passo:** Vincule o CIAP através dos campos N1\_CODCIAP e N1\_ICMSAPR

Obs: Em caso de duvida para criar código do CIAP na filial destino  entre em contato com time do modulo fiscal

**Versão P12** ao realizar a transferência do bem através da rotina "Transferência do ativo ATFA060" o sistema baixa automaticamente o  CIAP na filial origem e gera/transfere o código de CIAP na filial destino

* O bem é baixado automaticamente na filial origem
* Na filial Origem o sistema  transfere o bem e  relaciona automaticamente no campo N1\_CODCIAP o código do CIAP na filial destino
* Para que o sistema gere um código de CIAP para a filial Destino se faz necessário informar "Gera NF =Sim" ,"TES de Saida " e TES Entrada". preencher esse dados o sistema :  
    
  1º Baixa o CIAP da Filial Origem  
  2º Criar um novo codigo de CIAP automaticamente na Filial Destino

![](https://totvssuporte.zendesk.com/attachments/token/MzupfslUsKoiujieyWYGdddS3/?name=inline470159824.png)

Issue [DSERCTR1-18057](https://tdn.totvs.com/pages/releaseview.action?pageId=235337625) de solicitação de documentação, onde o desenvolvimento descreveu  mais detalhe quanto ao procedimento

Veja mais :[Conceito TRANSFERÊNCIA DE BENS COM CIAP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021375172-MP-SIGAATF-ATFA060-TRANSFER%C3%8ANCIA-DE-BENS-COM-CIAP?source=search)
