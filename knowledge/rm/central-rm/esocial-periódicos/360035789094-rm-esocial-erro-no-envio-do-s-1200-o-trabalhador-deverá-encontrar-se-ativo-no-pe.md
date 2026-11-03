---
article_id: 360035789094
category: esocial - Periódicos
content_hash: 0b7cdd00d564f5455216ccb2882c10e09337253fa47a0145f10482e37d1489c8
fetched_at: '2026-06-28T22:47:09.534205+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RM - eSocial - Erro no envio do S-1200: O trabalhador deverá encontrar-se
  ativo no período'
type: support-article
updated_at: '2024-11-13T12:27:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035789094-RM-eSocial-Erro-no-envio-do-S-1200-O-trabalhador-dever%C3%A1-encontrar-se-ativo-no-per%C3%ADodo
---

**Ocorrência**Ao enviar o evento S-1200 é apresentado o erro 317: **O trabalhador do CPF xxxxxxxxxxx, matricula xxxxxxx, deverá encontrar-se ativo no periodo aaaa-mm**.  
  
**Causa**  
Este erro ocorre pois no evento **S-1200** de rescisão complementar foi gerada a tag **infoPerApur**. Esta tag indica que o funcionário está recebendo remuneração referente ao período apurado porém, como o funcionário se encontra demitido, só poderá receber verbas referentes à períodos anteriores. Para funcionários demitidos o XML S-1200 de rescisão complementar deverá gerar as verbas somente dentro da tag **infoPerAnt**, indicando os períodos de referência das verbas geradas.  
  
                  Exemplo **i****nfoPerApur**                |                  Exemplo **infoPerAnt**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046973934/mceclip0.png)      ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046974234/mceclip2.png)

**Ambiente**RM - eSocial - Todas as versões  
  
**Solução**   
Para solucionar este incidente, siga os passos abaixo:  
1. Cancele a movimentação para o funcionário em **Folha de Pagamento | Folha Mensal | Cancelamento** e cancele tudo que foi lançado para o funcionário:  
2. Gere novamente a [rescisão complementar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004806532) indicando o acordo coletivo associado;  
3. Gere o XML e verifique a geração. Não poderá existir a tag **infoPerApur**. **Importante**A geração incorreta se deve por alguma alteração ou inclusão de verbas diretamente no envelope ou ficha financeira do funcionário. Para funcionários demitidos só é permitido o lançamento de verbas através das rotinas de Rescisão Complementar associando à um acordo coletivo cadastrado.  
  
**Saiba Mais**Para mais informações, acesse:  
• [RM - eSocial - Informar verbas geradas por dissídio no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004806532-RM-eSocial-Informar-verbas-geradas-por-diss%C3%ADdio-no-eSocial?source=search)
