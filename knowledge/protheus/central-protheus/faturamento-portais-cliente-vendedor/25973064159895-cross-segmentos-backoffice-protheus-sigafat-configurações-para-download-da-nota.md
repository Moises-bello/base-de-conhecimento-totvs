---
article_id: 25973064159895
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: e0ebe7bc223f38b9b8a55f8454f56b73068c2c18a4859e62623ad92cd14501a8
fetched_at: '2026-06-28T22:38:23.917521+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Configurações para Download
  da Nota Fiscal - PGV
type: support-article
updated_at: '2026-05-22T12:54:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25973064159895-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Configura%C3%A7%C3%B5es-para-Download-da-Nota-Fiscal-PGV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25973064134935) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar o Download da Nota Fiscal no Portal gestão de Vendas?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12.1.2310  
  
**Solução**  
Para utilizar o recurso de download de DANFE e XML das notas fiscais através do Portal Gestão de Vendas, é necessário que algumas premissas sejam atendidas.

Estas configurações devem ser realizadas previamente pelo administrador do ambiente.

**A seguir estão os requisitos para o Protheus e para o TSS:**

**0. Portal gestão de Vendas versão** **1.9.1.**

1. **REST do Protheus**:

   * Deve estar ativo
2. **Integração com o TSS**:

   * Deve estar devidamente configurada. (Para mais informações, consulte as [Configurações Gerais do TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=590613669))
3. **Parâmetro MV\_FNPCTSS**:

   * Deve conter o endereço do servidor REST do TSS (exemplo:`[seuip]:[suaporta]/``[caminhorest]``/`)
4. **Parâmetro MV\_SPEDGRV**:

   * Deve estar configurado com o valor `2`. (Para mais informações, consulte a [Criação do parâmetro MV\_SPEDGRV](https://tdn.totvs.com/pages/viewpage.action?pageId=814528388)).
5. **Para Protheus 12.1.2310 ou inferior**:

   * Atualize com o pacote de expedição contínua do BackOffice com data superior a 15/01/2024 para funcionar com o TSS 12.1.2310 e 15/09/2024 para o TSS 12.1.2410.
   * A autenticação (segurança do socket) deve estar habilitada (`Security = 1`). (Para mais informações, consulte [WebServices REST/Server - Configuração](https://tdn.totvs.com/pages/viewpage.action?pageId=185747842)).

**Parâmetros:**

1. **MV\_FNPCTSS**
2. **MV\_SPEDGRV**
3. **MV\_XMLSIZE**
4. **MV\_SPEDURL**
5. **MV\_ESPECIE**
6. **MV\_ESTADO**
7. **MV\_CODREG**

**Saiba mais:**

[**TSS - Como configurar e utilizar tabela SPED059 (Rotina Portal)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22847223925399-Cross-Segmentos-Backoffice-Protheus-TSS-Como-configurar-e-utilizar-tabela-SPED059-Rotina-Portal-do-cliente)

[DR - Meus Pedidos - Download Nota Fiscal](https://tdn.totvs.com/display/public/PROT/DR+-+Meus+Pedidos#DRMeusPedidos-ACESSAR_NOTA)
