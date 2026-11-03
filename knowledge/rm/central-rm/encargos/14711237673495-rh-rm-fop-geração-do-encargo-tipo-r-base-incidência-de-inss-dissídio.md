---
article_id: 14711237673495
category: Encargos
content_hash: ad6e1f01e871817bbf699aa1c2a294b9993827118ad62348267d5aaace1f82fb
fetched_at: '2026-06-28T22:46:52.293859+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - Geração do encargo TIPO R - Base: incidência de INSS Dissídio'
type: support-article
updated_at: '2024-10-09T20:10:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14711237673495-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-encargo-TIPO-R-Base-incid%C3%AAncia-de-INSS-Diss%C3%ADdio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:15 min****Dúvida**Como gerar o encargo TIPO R - Base: incidência de INSS Dissídio  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de pagamento - Todas as versões  
  
**Solução**Para geração do encargo TIPO R - Base: incidência de INSS Dissídio, é necessário que anteriormente já tenha sido realizado a alteração salarial e lançamento da diferença salarial. Segue documentação de ambos os processos.

[RH - RM - FOP - Alteração Global de Salários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007539911-RH-RM-FOP-Altera%C3%A7%C3%A3o-Global-de-Sal%C3%A1rios)

[RH - RM - FOP - Diferença Salarial Cálculo e Lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419368388887-RH-RM-FOP-Diferen%C3%A7a-Salarial-C%C3%A1lculo-e-Lan%C3%A7amento)

Para o lançamento do encargo do tipo R - Base: incidência de INSS Dissídio e S - Base: incidência de INSS de 13o. salário Dissídio é necessário que os eventos de CC415 e CC416 estejam lançado no aba Verbas de Diferença, na ficha financeira. Caso contrário o encargo deverá ser calculado por fórmula customizado pelo usuário.

**Para cadastrar os eventos acesse: Administração de pessoal | Eventos:**  
Mais detalhes: [RH - RM - FOP - Cadastro de Eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412771329815-RH-RM-FOP-Cadastro-de-Eventos)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/14710468120343)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/14712359599127)**

Com esses eventos cadastrados ao fazer o lançamento da diferença salarial, dentro da ficha financeira do funcionário aba verbas geradas por diferença, mês a mês será levado o evento :

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/14710599651863)**

Em **Encargos | Cadastros | Encargos**deverá realizar o cadastro do encargo conforme a necessidade especifica da empresa:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14710627292567)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14710660360727)

**Importante:** Verificar o código ativo associado ao cadastro do encargo, pois no momento da geração do encargo será necessário selecionar o mesmo código ativo. Caso precise de apoio para criar o código ativo para vincular no encargo, utilize a documentação abaixo, após criar o código ativo, vincule o mesmo no cadastro do encargo.

[RH - RM - FOP - Encargos: Criação de códigos ativos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021841391-RH-RM-FOP-Encargos-Cria%C3%A7%C3%A3o-de-c%C3%B3digos-ativos)

Geração do encargo em **Encargos | Geração dos encargos**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14710702550423)

Log da geração do encargo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14711016590999)

**Saiba mais**  
[Encargos - Folha de Pagamento](https://tdn.totvs.com/display/public/LRM/Encargos+-+Folha+de+Pagamento)
