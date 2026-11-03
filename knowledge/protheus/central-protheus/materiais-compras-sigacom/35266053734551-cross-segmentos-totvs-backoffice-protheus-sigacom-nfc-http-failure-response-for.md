---
article_id: 35266053734551
category: Materiais - Compras (SIGACOM)
content_hash: 0e00c0e7f234d322b4df10e6a0a335427af75ea93fd0f3dc24832d8b10a4711d
fetched_at: '2026-06-28T22:41:21.823590+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Http failure
  response for http://linknfc 500 Internal Server Error ao anexar arquivo
type: support-article
updated_at: '2026-01-27T19:50:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35266053734551-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Http-failure-response-for-http-linknfc-500-Internal-Server-Error-ao-anexar-arquivo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35266053721879) Tempo aproximado para leitura: **03:00:00 min**

**Ocorrência**  
Ao adicionar anexo no envio do email do formulário do Workflow da cotação ao fornecedor, é gerado o erro ***Http failure response for http://linknfc 500 Internal Server Error***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35267126352791)

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310

**Causa**  
Esse erro costuma ocorrer devido a ocorrência de chave duplicada na tabela ACB, a chave única dessa tabela é o ACB\_CODOBJ. Desse modo para correção desse erro deve se ajustar o controle de numeração da tabela ACB, para isso acesse a tabela ACB valide qual foi o ACB\_CODOBJ do último item incluído e ajuste o controle de numeração.

**Solução**  
Desse modo, para correção desse erro deve se ajustar o controle de numeração da tabela ACB. Para isso, realize o procedimento abaixo:

1. Acesse a tabela ACB.
2. Valide qual foi o conteúdo do campo ACB\_CODOBJ do último item/registro incluído nessa tabela.
3. Ajuste o controle de numeração. Dúvidas no ajuste do controle de numeração , seguir o passo 3 da documentação:[FAT0046 Ajuste de Numeração automática dos Formulários (Tabelas / ALIAS) no Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=235570751)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35267126354583)

**Saiba Mais:**

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[FAT0046 Ajuste de Numeração automática dos Formulários (Tabelas / ALIAS) no Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=235570751)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)
