---
article_id: 5346117132439
category: Folha Mensal
content_hash: ccca9179eb081fdb5dff3dc27bb24105de97cb722e8d3ead560cb1042ccb076a
fetched_at: '2026-06-28T22:46:59.210687+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Analítica: geração de funcionários transferidos'
type: support-article
updated_at: '2024-06-17T14:13:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5346117132439-RH-RM-FOP-Folha-Anal%C3%ADtica-gera%C3%A7%C3%A3o-de-funcion%C3%A1rios-transferidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24229723084823)Tempo aproximado para leitura: **00:02:51 min****Dúvida**Como gerar a folha analítica para funcionários que tiveram transferência?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Atualmente a folha analítica não valida as informações contidas no histórico de seções, o relatório valida a seção atual do período onde o relatório será gerado.   
  
Para uma melhor compreensão do comportamento da geração da folha analítica de funcionários transferidos, segue evidências:  
  
Funcionário Marcelo está alocado na seção 01.09.  
  
**![](https://totvssuporte.zendesk.com/attachments/token/SUkEsQFDy2CezZa0yZ9QBT5GE/?name=inline-1529918890.png)**Após realizada a transferência do funcionário entre seções, por exemplo, o funcionário foi para seção 01.10.  
  
**![](https://totvssuporte.zendesk.com/attachments/token/uYsbyPgrNsZAJqB4de9mCelgY/?name=inline897279533.png)**Após realizado o processo de transferência de funcionário com sucesso, automaticamente o histórico de seção fora alimentado.  
 **![](https://totvssuporte.zendesk.com/attachments/token/T6KQetgkWV2ZRR2lkaC9Xa7GP/?name=inline416253652.png)**Ao gerar a folha analítica por seção e especificamente buscando a seção 01.09 por um filtro criado, o funcionário Marcelo não foi apresentado.​ Assim, apresentado apenas quem consta na seção 01.09, na qual seria o funcionário Edmilson.  
  
**![](https://totvssuporte.zendesk.com/attachments/token/OpW2Dj5UUoROvVmEiE23i2ieg/?name=inline1227056105.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/CvPH5WgMlvrsgT2j9BREDVMp2/?name=inline1470501081.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/eaK44vouOvCGDQjp3ahQhaKFj/?name=inline-410125332.png)​**Ao gerar a folha analítica por um filtro criada puxado a chapa do funcionário Marcelo, esse que transferiu de seção, é apresentado na seção atual.  
  
**![](https://totvssuporte.zendesk.com/attachments/token/pgaylyN7YjwvZWKENxly2UGPU/?name=inline-1668595173.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/HM9UQUIHGASr7MZZrxI35vL4G/?name=inline-1625624083.png)**Portanto, fica claro que, ao selecionar a opção **Parâmetros específicos** e selecionar a chapa atual do funcionário, serão impressos somente os dados daquela chapa específica e na coligada atual, ou seja, caso a chapa tenha sido alterada e a transferência tenha ocorrido entre coligadas, as informações da coligada/chapa antiga não serão apresentadas.   
  
**Importante**Além da folha analítica não validar as informações contidas no histórico de seções, mas sim o relatório validar a seção atual do período onde o relatório será gerado, a Folha Analítica terá os valores corretos somente na competência atual, pois leva as informações atuais do funcionário. Ou seja, caso exista algum funcionário com qualquer tipo de alteração, como por exemplo, Férias, Retorno de Férias, Afastamentos, Transferências e etc, que seja diferente de competências anteriores, o valor será alterado pois não existia a configuração atual do funcionário em competência passada. Portanto é importante gerar a Folha Analítica e salvar de todas as competências geradas para consultas posteriores. **Saiba Mais**[RM - FOP - Relatórios: Nenhum funcionário atende à seleção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009848672-RM-FOP-Relat%C3%B3rios-Nenhum-funcion%C3%A1rio-atende-%C3%A0-sele%C3%A7%C3%A3o?source=search)  
[RH - RM - FOP - Folha Analítica: cadastro e parametrização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416042752151-RH-RM-FOP-Folha-Anal%C3%ADtica-cadastro-e-parametriza%C3%A7%C3%A3o)
