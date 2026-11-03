---
article_id: 360035250554
category: Integrações Nativas
content_hash: 9f43bb4cd2b32690c0e65e100721df9cac052d72291fc2ccde8bcdf13eb1f6b1
fetched_at: '2026-06-28T22:42:35.415356+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Habilitar Campo Estoque
type: support-article
updated_at: '2021-09-02T20:21:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035250554-Manufatura-Linha-Protheus-MNT-Habilitar-Campo-Estoque
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:00:45 min**  
**Dúvida**Como é realizada a habilitação do campo **Estoque - T9\_CODESTO**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Todas as versões  
  
**Solução**O campo **Estoque - T9\_CODESTO** está fechado para edição no **Cadastro de Pneus - MNTA083**.  
Para habilitá-lo, verifique os seguintes itens:

1. Os parâmetros **MV\_NGSTAEU - Estoque Usado**, **MV\_NGSTAER - Estoque Reformado**, **MV\_NGSTARS - Removido de Serviço**, **MV\_NGSTAEN - Estoque Novo** e **MV\_NGSTEST - Estoque Filial**, devem ser informados com seus respectivos status cadastrados no Sistema, na rotina de **Status - MNTA710**.
2. Os parâmetros **MV\_NGMNTES** **- Integração com Estoque** e **MV\_NGPNEST - Identificação do Bem** no **Controle de Estoque** devem estar habilitados.
