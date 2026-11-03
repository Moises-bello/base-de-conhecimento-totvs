---
article_id: 360058323594
category: Gestão de Frotas
content_hash: bd75a825fb725bd003275c0fdec667806911f2bee740b253f81e6b2c67247bf1
fetched_at: '2026-06-28T22:42:39.563406+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: 'Manufatura - Linha Protheus - MNT - Pneus não aparecem para aplicação na estrutura
  de pneus '
type: support-article
updated_at: '2024-02-14T17:25:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058323594-Manufatura-Linha-Protheus-MNT-Pneus-n%C3%A3o-aparecem-para-aplica%C3%A7%C3%A3o-na-estrutura-de-pneus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:20 min**  
**Dúvida**Por que os **pneus** não aparecem para aplicação na estrutura de pneus no botão **Rodados**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas – Versão 12  
  
**Solução**Ao utilizar o botão de **Rodados** presente na rotina **O.S. Corretiva - MNTA420**, que possibilita a aplicação de **pneus** em uma estrutura ou removê-los, é necessário que algumas configurações prévias sejam realizadas.

* O **pneu** a ser aplicado precisa ser da mesma **Família de bens** conforme definida na rotina **Esquema padrão - MNTA220/MNTA221**;
* O **pneu** a ser aplicado precisa estar com o mesmo **Status** relacionado a algum dos parâmetros:  
  **MV\_NGSTAEU - Código do status para Estoque Usado**  
  **MV\_NGSTAER - Código do status para Estoque Reformado**  
  **MV\_NGSTAEN - Código do status para Estoque Novo**  
  **MV\_NGSTEST - Indica o status para o pneu no estoque da filial**
* O **pneu** a ser aplicado não pode estar com o mesmo **Status** relacionado a algum dos parâmetros:  
  **MV\_NGSTAGR - Código do status para Aguardando Reforma**  
  **MV\_NGSTAGC - Código do status para Aguardando Conserto**  
  **MV\_NGSTAAT - Código do status para Aguardando Analise Técnica**

**Saiba mais**Para que o botão **Rodados** seja apresentado, verifique a parametrização disponível no *link* [Configuração botão Rodados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028080352)  
Para informações complementares a respeito da rotina de **Esquema padrão**, verifique o *link* [Esquema Mod 2 (MNTA221 - SIGAMNT)](https://tdn.totvs.com/pages/viewpage.action?pageId=555285702)
