---
article_id: 38585621995287
category: Escrita Fiscal - Impostos - ICMS
content_hash: 6bd67cbcc83fa5c2b950e03260c21f22a2b4a8f6e3a087e35f6f09db5c3d466a
fetched_at: '2026-06-28T22:39:24.072168+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  FIS - Como configurar o cBenef por grupo cliente / produto para o estado de SP?
type: support-article
updated_at: '2026-02-23T19:30:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38585621995287-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-FIS-Como-configurar-o-cBenef-por-grupo-cliente-produto-para-o-estado-de-SP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38585621977367) Tempo aproximado para leitura: 05:10m  
  
**Dúvida**  
 Como configurar o cBenef por grupo cliente / produto para o estado de SP?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Inserir os codigos da tabela52 seja através do U\_IMPSPED ou na rotina fisa156

<http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>

MV\_estado = SP

MV\_GIAEFD = .F.

MV\_MTCLF3K = 1

Cliente = SP

Grp clientes = 100

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38585630728727)

Cadastro de Produtos = 000039

Grupo trib = 001

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38585630730391)

TES

CFOP = 5102

Calcula icms = não

L fiscal icms = isento

CST = 40

Mot desone = outros

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38585630731287)

Fisa156

Codigo = SP010140

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38585630731927)

Fisa140

Grupo de cliente = 100

Grupo do prouto = 001

CFOP = 5102 = CST = 40 Codigo SP010140 = reflexo para produto isento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38585630732951)

Reflexo 0000173

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38585630734231)

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38585630735127)

Val. Declaratório

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38585630736279)

Dessa forma a tabela CDV é gerada.

Deve ser verificado o parametro MV\_CODCST para a geração do XML

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017974352-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-cBenef>
