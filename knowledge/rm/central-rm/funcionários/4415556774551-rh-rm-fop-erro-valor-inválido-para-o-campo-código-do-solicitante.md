---
article_id: 4415556774551
category: Funcionários
content_hash: 0bcfda6ec235c54ced1b540b6af0bd639e021209f322dbf9fa09e4ad4590a388
fetched_at: '2026-06-28T22:47:03.365846+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: 'RH - RM - FOP - Erro: Valor inválido para o campo Código do Solicitante'
type: support-article
updated_at: '2025-03-06T18:27:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415556774551-RH-RM-FOP-Erro-Valor-inv%C3%A1lido-para-o-campo-C%C3%B3digo-do-Solicitante
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:15 min**  
**Dúvida**Ao realizar o Cadastro do Funcionário em: **Anotação Pessoal | Código do Solicitante** não exibe o código e apresenta o seguinte erro: **Valor inválido para o campo Código do Solicitante**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10754327640599)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O campo Código do Solicitante serve para documentar o responsável pela anotação pessoal no cadastro do funcionário. Sendo assim, para correção do erro, deve validar a parametrização, acessando através do módulo **Gestão de Pessoas | Configurações | Parametrizador | Validações** e validar em **Anotações Pessoais**, marcando o parâmetro: **Somente Chefes podem aprovar Anotações Pessoais**. Desta forma, será exibido no cadastro de anotações o código do solicitante do funcionário que são classificados como **Chefe**.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10754439497623)  
  
**Saiba mais**[Anotação Pessoal](https://tdn.totvs.com/pages/releaseview.action?pageId=452720033)
