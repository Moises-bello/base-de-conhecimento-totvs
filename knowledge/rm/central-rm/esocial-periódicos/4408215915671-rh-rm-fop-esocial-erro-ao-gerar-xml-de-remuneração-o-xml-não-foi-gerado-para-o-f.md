---
article_id: 4408215915671
category: esocial - Periódicos
content_hash: 7a92e717639c41696b9ed64b8de3ab42494cd788c53df07f91e58a6b75535b81
fetched_at: '2026-06-28T22:47:09.076795+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: ' RH - RM - FOP - eSocial - Erro ao gerar XML de remuneração: O XML não foi
  gerado para o funcionário ''xxxxx''. Verifique se a distribuição por tomador foi
  realizada'
type: support-article
updated_at: '2021-09-22T13:15:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408215915671--RH-RM-FOP-eSocial-Erro-ao-gerar-XML-de-remunera%C3%A7%C3%A3o-O-XML-n%C3%A3o-foi-gerado-para-o-funcion%C3%A1rio-xxxxx-Verifique-se-a-distribui%C3%A7%C3%A3o-por-tomador-foi-realizada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao gerar o XML de remuneração (S-1200, S-2299, etc), é apresentada mensagem de erro: **O XML não foi gerado para o funcionário 'xxxxx'. Verifique se a distribuição por tomador foi realizada**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409189838231/mceclip0.png)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Quando a coligada está configurada para utilizar tomadores de serviço, para a correta geração do XML é necessário que seja feito, previamente, a distribuição do SEFIP. Isso ocorre pois, neste caso, o evento de remuneração será gerado considerando a distribuição realizada e não a movimentação presente no envelope de pagamento.  
  
**Solução**Para distribuição , siga os passos abaixo:

1. Acesse **Encargos** | **SEFIP** | **Distribuir Sefip** e selecione a competência a ser distribuída;  
2. Selecione quais os períodos da folha de pagamento serão distribuídos;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408215749527/mceclip1.png)

3. Após distribuição, o XML poderá ser gerado novamente.

**Saiba mais**   
Para mais informações acesse:  
     - [RM - eSocial - Distribuição de SEFIP de meses anteriores para tomadores de serviços em retificação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028703594)
