---
article_id: 29247830586263
category: Financeiro - Manutenção de Extratos
content_hash: 7da43255d046c16e93b50f306695627cada2684bbe3d895ed27f565db37c11fb
fetched_at: '2026-06-28T22:37:31.147055+00:00'
product: protheus
section_id: 35057672519319
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA474 - Falha na
  importação do Arquivo do Extrato - Conta com Hífen - Banco, Agência e Conta não
  existem
type: support-article
updated_at: '2026-01-07T14:07:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29247830586263-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA474-Falha-na-importa%C3%A7%C3%A3o-do-Arquivo-do-Extrato-Conta-com-H%C3%ADfen-Banco-Ag%C3%AAncia-e-Conta-n%C3%A3o-existem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29247830560919) Tempo aproximado para leitura: **03:00 min**  
  
**Dúvida**  
Ao realizar a importação do arquivo na FINA474, gerou a mensagem que a Banco, Agência e Conta não existem. Como proceder?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões.   
  
**Solução**  
A conta foi registrada com hífen, o que causa um problema de posicionamento, já que o banco não envia o hífen e o Protheus não grava dessa forma através do INSERT no banco de dados.

Para corrigir, é preciso criar uma nova conta, cadastrando sem hífen e digitando o digito da conta no campo correto ou utilizando o ponto de entrada **F474CTA** .

**Documentação sobre o Ponto de Entrada**

[F474CTA](https://tdn.totvs.com/pages/viewpage.action?pageId=776531933)

**Saiba Mais**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Conciliador Financeiro Pontos de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29000337545751-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Conciliador-Financeiro-Pontos-de-Entrada)
