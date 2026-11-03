---
article_id: 38671937195159
category: Financeiro - Smart View
content_hash: 33943a086202cb3e511241e9857d2d4c9ee906c7aca45e0ee285bd42405dfb8f
fetched_at: '2026-06-28T22:37:44.786876+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Smart View - FINSV014
  Relatório de Extrato bancário sendo emitido com a data do dia anterior
type: support-article
updated_at: '2026-02-26T21:22:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38671937195159-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Smart-View-FINSV014-Relat%C3%B3rio-de-Extrato-banc%C3%A1rio-sendo-emitido-com-a-data-do-dia-anterior
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38671937186583) Tempo aproximado para leitura: 00**:05;00 min**  
  
**Dúvida**  
Ao gerar o relatório de Extrato Bancário no Smart View, o sistema apresenta a data do dia anterior ao invés da data atual.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução:**

Esse comportamento ocorre devido à configuração desatualizada do fuso horário no sistema. Com a suspensão do horário de verão no Brasil, é necessário desativar o parâmetro MV\_HVERAO para evitar divergências de datas ao utilizar a função `FwTimeStamp` e prevenir outros possíveis problemas decorrentes dessa ativação.

**Passos:**

1. Acesse o módulo **Configurador (SIGACFG)**;
2. Navegue até o menu **Ambiente > Cadastros > Parâmetros**;
3. Localize o parâmetro **MV\_HVERAO**;
4. Altere seu conteúdo para desativar o uso do horário de verão (ajustando conforme a documentação oficial da versão);
5. Salve as alterações.
6. Gere o relatório de Extrato Bancário no Smart View para validar a correção da data.

Saiba mais:

[Função FWTimeStamp - TDN](https://tdn.totvs.com/display/public/framework/FWTimeStamp)

[Parâmetros de Horário de Verão - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=772806491)
