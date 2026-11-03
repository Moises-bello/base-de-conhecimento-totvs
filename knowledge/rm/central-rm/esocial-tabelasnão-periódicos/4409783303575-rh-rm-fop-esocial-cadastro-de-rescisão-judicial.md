---
article_id: 4409783303575
category: eSocial - Tabelas/Não Periódicos
content_hash: 3e146e103d8bc47ef6864afd8b9777707ea563d1ad4ee580fbd6cb6aa156e44b
fetched_at: '2026-06-28T22:47:10.264533+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Cadastro de rescisão judicial
type: support-article
updated_at: '2021-10-04T15:02:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409783303575-RH-RM-FOP-eSocial-Cadastro-de-rescis%C3%A3o-judicial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:00 min  
  
Dúvida**Como informar rescisão judicial para o eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Não existe na **Tabela 19** do leiaute do eSocial um motivo específico para rescisão judicial. Deve-se informar no S-2299 um motivo que melhor se enquadre na ocorrência registrada pela empresa. Para que o sistema considere o motivo escolhido na geração do S-2299, deve-se então parametrizar o de/para de desligamento. Siga os passos abaixo:

1. Acesse o menu **Configurações | Parametrizador | eSocial**, e avance até a etapa**De/Para de Desligamento**;  
2. Clique no botão **Incluir** e preencha os campos que serão apresentados;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409997593367/mceclip0.png)

3. Salve o cadastro e avance ate concluir o *wizard* de parametrização;  
4. Cadastre a rescisão com o tipo informado no campo **Cód. Tipo Folha de Pagamento** no parametrizador, gere o S-2299 e transmita ao governo.

**Importante**Todas as rescisões geradas com o **Cod. Tipo Folha de Pagamento** informado no parametrizador, terão a *tag* **mtvDeslig** gerada conforme o **Cod. Tipo eSocial** informado.

O TOTVS Folha de Pagamento não realiza o cálculo de rescisão retroativa,. Assim, o usuário deve preencher manualmente os valores na ficha financeira ou realizar a importação do movimento.

****Saiba mais****Para mais informações acesse:  
     - [Mapeamento evento S-2299](https://tdn.totvs.com/display/public/LRM/Evento+S-2299)  
     - [Contato com o Portal eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004050432-RH-RM-FOP-eSocial-Contato-com-o-Governo-para-d%C3%BAvidas-sobre-os-eventos-do-eSocial)
