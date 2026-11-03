---
article_id: 23081588769815
category: eSocial - Gerar XML/ Integração Evento
content_hash: 88d76eba6922166223c0e69a7456b09b3215979e8ac74fa5fb50f55106226aa0
fetched_at: '2026-06-28T22:47:13.121471+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - S-1200 e S-1210 - Unificação de períodos mediante
  retificação
type: support-article
updated_at: '2026-05-27T21:57:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23081588769815-RH-RM-FOP-eSocial-S-1200-e-S-1210-Unifica%C3%A7%C3%A3o-de-per%C3%ADodos-mediante-retifica%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23081601704471) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como realizar a unificação de períodos na realização de retificação nos eventos S-1200 e S-1210?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir da versão 12.1.23.  
  
**Solução**  
Seguindo o parecer SEI Nº16120/2020, é preciso unificar a geração dos arquivos XML no eSocial. Isso ocorre porque não podemos enviar uma restituição de INSS sem incluir o desconto correspondente na mesma tag <ideDmDev>.

Para isso, realizamos uma tratativa no produto incluindo o parâmetro **Unificar período na retificação**. Quando ativado, o sistema passa a unificar a geração dos XMLs de retificação, o que significa que os eventos registrados nos períodos de retificação são agora consolidados no período original.  
  
Vale ressaltar que, por enquanto, essa atualização não abrange rescisões. Assim que essa funcionalidade estiver disponível, será registrada por meio de nossas documentações.

1) Aplique o patch mencionado no campo ambiente, após a liberação da versão será necessário executar os script's de adequação da tabela e dos campos do sistema através do sistema [RM.Atualizador.exe.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5893403025687-RH-RM-FOP-RM-Atualizador)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23081601706007)

2) Ative o parâmetro criado acessando o caminho: **RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 5/7.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23081588741783)**

3) Proceda com o lançamento das retificações. O sistema irá registrar a qual período original a retificação está relacionada.![](https://centraldeatendimento.totvs.com/hc/article_attachments/23081601712535)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23081712519831)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23081727628695)

4) No XML S-1200, somente o <ideDmDev> original foi gerado. Os eventos do período de retificação 10000, conforme mencionado anteriormente no item 3, foram registrados no <ideDmDev>1, correspondente ao período original.  
![image-2023-12-15_8-23-12.png](https://tdn.totvs.com/download/attachments/811714715/image-2023-12-15_8-23-12.png?version=1&modificationDate=1702639392980&api=v2)

5) No XML S-1210, apenas o <ideDmDev>1 foi gerado, referente ao período original.  
![image-2023-12-15_8-25-9.png](https://tdn.totvs.com/download/attachments/811714715/image-2023-12-15_8-25-9.png?version=1&modificationDate=1702639509227&api=v2)

**Saiba mais**  
[Configurações Gerais 5/7](https://tdn.totvs.com/pages/releaseview.action?pageId=452719597)

[DT - Retificação Folha - Parecer SEI Nº16120/2020](https://tdn.totvs.com/pages/releaseview.action?pageId=814541129)
