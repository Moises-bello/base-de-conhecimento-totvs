---
article_id: 27866535256087
category: esocial - Periódicos
content_hash: 78ce3d7165123a96b8b7d6b2d587dc8038cc1f437c256603739ebb32ebddba66
fetched_at: '2026-06-28T22:47:09.244321+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - eConsignado: Grupo descFolha (S-1.3)'
type: support-article
updated_at: '2026-05-26T20:01:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27866535256087-RH-RM-FOP-eSocial-eConsignado-Grupo-descFolha-S-1-3
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27866535249815)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
Como gerar o grupo ***descFolha*** nos eventos do eSocial, com informações de desconto do empréstimo consignado em folha?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir dos Patches 12.1.2406.254, 12.1.2410.197, 12.1.2502.117 e superiores  
  
**Solução**

O grupo ***descFolha*** será preenchido automaticamente sempre que o evento lançado e vinculado ao cadastro de empréstimo tiver a rubrica **9253 - Empréstimos ECONSIGNADO - Desconto**. 

As informações necessárias serão extraídas diretamente do cadastro de empréstimos, acessível no menu **Administração de Pessoal | Funcionários | Anexos | Folha de Pagamento | Empréstimos**. Necessário marcar o parâmetro **Funcionário firmou contrato de empréstimo consignado com garantia de FGTS** para correta geração do XML.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27866510138775)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27866510144407)

O grupo será gerado nos eventos: S-1200, S-1202, S-1207, S-2299 e S-2399.

**Importante**  
Os esclarecimentos sobre o fluxo e processo do **eConsignado**só poderão ser fornecidos **após a publicação da normatização legal e infralegal correspondente.** Como já ocorreram vários adiamentos desta publicação, o eSocial decidiu antecipar as informações no Leiaute através na [Nota Técnica 04/2024](https://informa.totvs.com/rh/protheus/esocial-nota-tecnica-03-2024-e-04-2024-entrega/) apenas para **preparação do Leiaute**.

Ainda que o sistema já esteja preparado para configuração da rubrica **9253**- Empréstimos eConsignado - Desconto, o envio através do evento S-1010 está condicionada à tag *iniValid (deve ser **igual ou posterior ao mês de início do eConsignado**no eSocial)*. Portanto, mesmo que as informações do eConsignado estejam previstas na solução da NT 04/2024 e as parametrizações realizadas no sistema, elas **só serão enviadas após a oficialização da normatização supracitada.**

**Saiba mais**  
Para mais informações, acesse:  
     - [Nota Técnica V. S-1.2 03/2024 e 04/2024](https://tdn.totvs.com/pages/viewpage.action?pageId=853920910)  
     -  [Leiaute Versão S-1.3 e NT 01/2024](https://tdn.totvs.com/pages/releaseview.action?pageId=862114556)
