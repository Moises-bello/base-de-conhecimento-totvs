---
article_id: 360035413994
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 79ae2f9d5616ecbbdf2e09e95ba618a1319d7ed1c08fcce26722672d2aedd188
fetched_at: '2026-06-28T22:39:41.191256+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Mensagem: A120RSPED'
type: support-article
updated_at: '2022-06-02T13:18:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035413994-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Mensagem-A120RSPED
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como corrigir a mensagem A120RSPED?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control - Todas as versões  
  
**Solução**Neste caso, trata-se de uma verificação da rotina MATA120 - SIGACOM. Por gentileza, siga as orientações do módulo SIGACOM conforme abaixo, caso persistir estaremos direcionando para análise dos mesmos.  
  
\_ Verificar se o campo C7\_GRUPCOM está preenchido  
  |\_ Se o campo está preenchido, verificar se o usuário atual pertence ao grupo de compras do C7\_GRUPCOM  
  |  |\_ Se o usuário pertencer ao grupo de compras permitirá a modificação  
  |  |\_ Se não pertencer retorna o help "A120RSPED"  
  |  
  |\_ Se o campo não está preenchido verifica se o usuário atual é o mesmo do campo C7\_USER  
    |\_ Se é o mesmo usuário permite a modificação.  
    |\_ Se não é o mesmo usuário retorna o help "A120RSPED"  
  
Com base neste tratamento, recomendo que realize os seguintes passos para que o o seu usuário possa alterar também o pedido de compra:  
• Via MPSDU abrir a tabela SC7 e localizar o pedido de compra que o usuário não tem acesso.  
• Verificar o valor do campo C7\_GRUPCOM.  
• Via Client, no módulo de compras, acessar a rotina Atualizações>Adm.Compras>Compradores e cadastrar o usuário desejado como comprador.  
• Acessar a rotina Atualizações>Adm.Compras>Grupo de Compras, e com o valor encontrado anteriormente no campo C7\_GRUPCOM localizar o grupo de compras e altera-lo, incluindo o comprador cadastrado anteriormente. Dessa forma o usuário conseguirá alterar os pedidos de compra incluídos pelos usuários deste grupo de compras.  
  
OBSERVAÇÕES:  
• O campo C7\_GRUPCOM só é gravado quando se utiliza a configuração completa para o controle de alçada, utilizando grupo de solicitantes amarrados aos grupos de compra. Para que o campo C7\_GRUPCOM seja gravado, o processo deve seguir exatamente este caminho: Inclusão de SC (por um solicitante cadastrado) |--> Geração de Cotação |--> Analise da Cotação |--> Geração do PC. Neste processo serão gravados os campos: C1\_GRUPCOM, C8\_GRUPCOM e C7\_GRUPCOM. Se o processo utilizado for diferente deste, será necessário a utilização de ponto de entrada para gravar C7\_GRUPCOM.  
  
• Caso o campo C7\_GRUPCOM esteja em branco a única forma de os outros usuários terem acesso aos pedidos de compra será desativando o parâmetro MV\_RESTPED=N.
