---
article_id: 360038007153
category: esocial - Periódicos
content_hash: 306cdb33342c8ed0ca7b9b36410e862d2b3ea1aab7bb38f91ebfb78203b78406
fetched_at: '2026-06-28T22:47:09.519680+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Verbas de natureza salarial ou não salarial devidas
  após o desligamento
type: support-article
updated_at: '2026-02-02T17:42:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038007153-RH-RM-FOP-eSocial-Verbas-de-natureza-salarial-ou-n%C3%A3o-salarial-devidas-ap%C3%B3s-o-desligamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20860714258967)**  Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**  
Como informar ao eSocial o pagamento de **Verbas de natureza salarial ou não salarial devidas após o desligamento**, como por exemplo, Participação nos Lucros, comissão e Resultados (PLR) de funcionários demitidos?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.2302.160, 12.1.2306.104, 12.1.2310.100 e superiores.

**Solução**  
As **Verbas de natureza salarial ou não salarial devidas após o desligamento** são enviadas para o eSocial através do dissídio do **Tipo F** . Siga os passos abaixo para a correta geração do XML S-1200:

1. Acesse **Folha de Pagamento | eSocial | Acordo Coletivo/Reajuste por Lei**;  
1.1. Cadastre um acordo com**Tipo do acordo** sendo **F - Outras Verbas de natureza salarial ou não salarial devidas após o desligamento**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29526864260503)​

2. Acesse **Folha de Pagamento | Rescisão | Complementar**;   
2.1. No parâmetro **Dissídio/Convenção/Acordo Coletivo** selecione a opção **Não;**  
2.2. Selecione os parâmetros **Calcular Somente Eventos Informados** e **Pagamento de verbas de natureza salarial ou não salarial devidas após o desligamento**;  
2.3. Informe no campo **Dados do dissídio/convenção/acordo coletivo** o acordo cadastrado conforme passo 1.1 e avance o processo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29526847527959)

2.4. Em **Eventos Adicionais**, insira o evento correspondente ao pagamento da verba devida ao funcionário demitido, com o valor específico e execute o processo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29526847529623)

3.. Uma vez executada a rotina, basta gerar o evento **S-1200**em **eSocial | Gerar XML** (Eventos Periódicos). Dentro do grupo **infoPerAnt**, as informações do acordo e o valor serão gerados no grupo **ideADC** conforme exemplo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29526892177815)

**Importante**  
Conforme Manual de Orientações do eSocial, só poderão ser informados no tipo **F - Verbas de natureza salarial ou não salarial devidas após o desligamento** parcelas que legalmente não poderiam ser apuradas em competência igual ou anterior ao período de apuração (**perApur**) informado neste evento. Para os demais casos, deve ser feita a retificação do evento remuneratório correspondente: **S-1200**, **S-1202**, **S-2299** ou **S-2399**.  
  
**Saiba mais**  
Para mais informações acesse:  
      • [Diferença Processo de Rescisão Complementar - Retificação de Rescisão e Acordo Coletivo](https://tdn.totvs.com.br/pages/releaseview.action?pageId=419535691)  
      • [Código de Cálculo 126 - Participação nos Lucros](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718798)  
      • [Rescisão Complementar (Tipo F) - Campo dissídio para eventos de IRRF](https://tdn.totvs.com/pages/releaseview.action?pageId=770958493)
