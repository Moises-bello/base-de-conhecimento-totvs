---
article_id: 37730714161943
category: Financeiro - Contas a Receber
content_hash: 6e200e62676ac3f9190914f5468e9990b10336815393e9421c96b42a84d83689
fetched_at: '2026-06-28T22:38:12.480736+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - O PR não volta para o status de
  aberto quando excluído o PA ou  RA gerado por substituição do PR
type: support-article
updated_at: '2026-03-16T11:54:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37730714161943-Cross-Segmento-Backoffice-Linha-Protheus-O-PR-n%C3%A3o-volta-para-o-status-de-aberto-quando-exclu%C3%ADdo-o-PA-ou-RA-gerado-por-substitui%C3%A7%C3%A3o-do-PR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37730750941847) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Foi realizada a substituição de um PR por um PA; entretanto, após a exclusão do PA, o PR não retornou ao status **Aberto**.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
O processo de substituição de títulos provisórios (PR) gera movimentações de amarração nas tabelas FIH (Contas a Receber) e FII (Contas a Pagar).

Como essas tabelas são responsáveis por manter o relacionamento entre o título provisório e o título gerado no processo de substituição, é imprescindível que o mesmo modo de compartilhamento aplicado às tabelas SE1 e SE2 seja igualmente replicado para as tabelas FIH e FII. Dessa forma, assegura-se a preservação do vínculo entre os títulos, garantindo que, em operações posteriores à substituição, ambos sejam corretamente atualizados.

**Exemplo:**

A tabela SE2 está configurada com os modos de compartilhamento **Compartilhado**, **Exclusivo** e **Exclusivo**, enquanto as tabelas FIH e FII encontram-se configuradas integralmente como **Exclusivo**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37730714148503)

Ao criar um título provisório (PR) e substituí-lo por um título a pagar (PA), quando o compartilhamento estiver configurado de forma incorreta, conforme ilustrado no exemplo abaixo, ocorre o seguinte comportamento:

Ao excluir o PA, o título retorna para PR; entretanto, o status não é atualizado para **Aberto**, permanecendo indevidamente com o status **Encerrado**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37730750943127)

**Saiba mais**

[Compartilhamento de tabela para substituição de títulos](https://tdn.totvs.com/pages/releaseview.action?pageId=510501648)
