---
article_id: 360035997054
category: RH - Contabilização
content_hash: 9985ea0fb7a06aba7cbc188ec3136f55c6be864d32308a65ce82b344a4fa4f2a
fetched_at: '2026-06-28T22:43:45.999197+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - O arquivo de contabilização (TXT) é gerado sem
  os pontos das contas contábeis
type: support-article
updated_at: '2025-07-30T20:48:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035997054-RH-Linha-Protheus-GPE-O-arquivo-de-contabiliza%C3%A7%C3%A3o-TXT-%C3%A9-gerado-sem-os-pontos-das-contas-cont%C3%A1beis
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33832502928535)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**O arquivo de contabilização (TXT) é gerado sem os pontos das contas contábeis.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Ao gerar o processo de contabilização, o arquivo TXT não apresenta pontos da conta contábil:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047942013)

Verifique os procedimentos abaixo:   
1.Foi configurado os parâmetros para geração do arquivo conforme o padrão do Logix?<https://tdn.totvs.com/pages/releaseview.action?pageId=281260962>

2. Para que gere os pontos na conta contábil é necessário que o de/para das contas contábeis entre Logix x Protheus esteja corretamente na tabela XXF, pois no Protheus não existem pontos na conta contábil.  
Obs: após configuração da conta contábil , a tabela XXF será apresentada da seguinte forma:   
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047058954)  
  
Para mais detalhes verificar a orientação da FAQ no item 9 :   
<https://tdn.totvs.com/pages/releaseview.action?pageId=268816283>  
3. Refaça o processo de geração do arquivo e verifique a conta contábil no arquivo TXT:   
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047059954)

* Caso não haja nenhuma informação na tabela XXF, para realizar a carga inicial do Plano de contas execute via FIN0000, conforme o item 7 da FAQ acima;
* Caso necessite de auxílio para parametrizar esta integração do plano de contas, abra um ticket com a equipe Contábil Logix.

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como configurar Lançamento Padrão para Folha de Pagamento do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021101152-RH-Linha-Protheus-GPE-Como-configurar-Lan%C3%A7amento-Padr%C3%A3o-para-Folha-de-Pagamento-do-Protheus-)
