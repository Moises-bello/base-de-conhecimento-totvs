---
article_id: 1500004355022
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 22b2f231519c8fb69a8954d463bc26973db61dde95425e77c8b1393aa14087ab
fetched_at: '2026-06-28T22:39:57.356873+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - E243: ESTA
  NFS-E NAO DEVERA TER O ISSQN RETIDO PELO TOMADOR DO SERVICO'
type: support-article
updated_at: '2021-10-04T19:23:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004355022-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-E243-ESTA-NFS-E-NAO-DEVERA-TER-O-ISSQN-RETIDO-PELO-TOMADOR-DO-SERVICO
---

**Dúvida**Como resolver a rejeição abaixo, ao transmitir rps para as prefeituras atendidas pelo Provedor COPLAN?  
E243: Esta nfs-e nao devera ter o issqn retido pelo tomador do servico.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005410501/mceclip1.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para as prefeituras que utilizam o provedor **COPLAN** para transmissão de nfse web service, ao transmitir rps onde o iss é retido pelo Tomador do serviço, tag <IssRetido> igual a 1, ela retorna esta rejeição **E243**.

Trecho do xml:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005445841/mceclip2.png)

Para solucionar esta rejeição, basta ajustar o campo **C5\_RECISS**e/ou **A1\_RECISS** para **Não** no **Pedidos de** **Venda**, excluir o rps e fazer um novo para uma nova transmissão.

Existe uma regra do sistema para criação da tag de retenção de iss, IssRetido no xml:  
-Tag no xml <IssRetido> 1-Tomador, 2-Prestador.

Cadastros no Protheus:  
-A1\_RECISS/C5\_RECISS= 1 ou S - retenção pelo Tomador.  
-A1\_RECISS/C5\_RECISS= branco, 2 ou N - retenção pelo Prestador.

**\*Importante:** O sistema prioriza o conteúdo do campo C5\_RECISS, ignorando a configuração do cadastro do Cliente. Caso o campo no pedido esteja em branco, o cadastro do Cliente será considerado.

**Glossário:**  
**ISS - Imposto sobre serviço**  
**NFSE - Nota Fiscal de serviço eletrônica**  
**RPS - Recibo provisório de serviço**
