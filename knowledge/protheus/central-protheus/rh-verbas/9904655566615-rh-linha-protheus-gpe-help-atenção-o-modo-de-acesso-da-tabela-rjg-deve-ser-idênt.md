---
article_id: 9904655566615
category: 'RH - Verbas '
content_hash: fb65bf5dc8d3e5447342a0cc477b5942e58c52cbd002362d3f477565d0db662d
fetched_at: '2026-06-28T22:43:20.117233+00:00'
product: protheus
section_id: 360010838314
source: central-protheus
title: 'RH - Linha Protheus - GPE - HELP: Atenção: O modo de acesso da tabela RJG
  deve ser idêntico ao da tabela SRV'
type: support-article
updated_at: '2025-02-18T14:20:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9904655566615-RH-Linha-Protheus-GPE-HELP-Aten%C3%A7%C3%A3o-O-modo-de-acesso-da-tabela-RJG-deve-ser-id%C3%AAntico-ao-da-tabela-SRV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30061354923159) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**HELP: Atenção: O modo de acesso da tabela RJG deve ser idêntico ao da tabela SRV  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Compartilhamento divergente entre as tabelas SRV e RJG  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o Configurador / Base de dados / Dicionário  e busque a tabela SRV;  
   
2. Verifique o compartilhamento da tabela SRV  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9905033189655)  
  
3. Depois , pelo mesmo caminho acesse a tabela RJG, altere deixando igual a SRV.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9905126730007)   
  
4. Após alterar os compartilhamentos, grave as alterações, atualize a base de dados para que os compartilhamentos estejam corretos no relacionamento entre as tabelas: 

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9905492865943)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9905696176151)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Verbas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010838314-RH-Verbas)
