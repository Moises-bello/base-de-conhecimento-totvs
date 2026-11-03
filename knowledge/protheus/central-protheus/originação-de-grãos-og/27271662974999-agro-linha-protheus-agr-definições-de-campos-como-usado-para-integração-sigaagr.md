---
article_id: 27271662974999
category: Originação de Grãos (OG)
content_hash: e56722bae90bbde77d3dc0446d1c61c43aef4ca5b9b79606f718cbd82cbb1324
fetched_at: '2026-06-28T22:45:39.004660+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Definições de campos como USADO para integração
  SIGAAGR X SIGACOM
type: support-article
updated_at: '2025-06-26T11:18:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27271662974999-Agro-Linha-Protheus-AGR-Defini%C3%A7%C3%B5es-de-campos-como-USADO-para-integra%C3%A7%C3%A3o-SIGAAGR-X-SIGACOM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27272613886743) Tempo aproximado para leitura: **00:02:45 min** **Dúvida**Quais os campos que devem estar definidos como USADO para integração SIGAAGR X SIGACOM?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Para as rotinas que realizam a movimentação do contrato de compra funcionar corretamente e vincular o romaneio de entrada **SIGAAGR** com documento de entrada **SIGACOM** é necessário que os campos abaixo estejam como **USADO**.

**D1\_CODROM**

**D1\_CODSAF**

**D1\_CTROG**

**D1\_ITEROM**

**D1\_NFPNUM**

**D1\_NFPSER**

Para verificar se o campo está marcado como **USADO** para o módulo do **SIGAAGR**, faça os seguintes passos:

**1.** Acesse o módulo Configurador **SIGACFG**;

**2.** Abra o menu **Base de Dados / Dicionário / Base de Dados**;

**3.** Selecione a opção **Dicionário de Dados** para a empresa que será atualizada;

![USA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27272531118871)

**4.** Clique na ![USA1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27272531120791), digite **SD1** e clique em **Buscar**;

![USA2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27272507364887)

**5.** Clique no ícone ![USA9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27272531127191) para abrir a tabela em modo de edição

**6.** Na opção **Itens das Nf de Entrada**, clique em **Campos**;

![USA3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27272531128855)

**7.** Clique no ícone![USA1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27272531120791), digite o nome do campo e clique em Buscar

**8.** Informar **D1\_CODSAF**;

![USA4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27272531130647)

**9.** Clique no ícone ![](https://tdn.totvs.com/download/thumbnails/756453348/image2023-1-20_16-24-59.png?version=1&modificationDate=1682668933920&api=v2)para abrir o Campo em modo de edição

10. Clique na Pasta **Uso**;

![USA5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27272507373463)

11. Confirme que o **Campo** está marcado como **Usado**;

![USA6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27272531134359)

12. Clique na Pasta **Módulos** e confirme que o campo está marcado como **Utilizado por todos os módulos** ou que o mesmo está marcado para o módulo **SIGAAGR**;

![USA7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27272507376791)

13. Caso ambos estejam em branco, deve ser marcado de forma manual o módulo do **SIGAAGR**;

14. Salve as alterações.

![USA8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27272531137047)
