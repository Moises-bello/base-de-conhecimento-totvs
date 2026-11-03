---
article_id: 22879075438487
category: Rescisão
content_hash: 839d2d1e78882ae7f2280a7d61c111233365a46de7c1ebdb5175fe89745973ce
fetched_at: '2026-06-28T22:46:54.184603+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - TRCT - Erro: O dado informado para a fórmula não é considerado
  valor'
type: support-article
updated_at: '2025-02-12T18:04:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22879075438487-RH-RM-FOP-TRCT-Erro-O-dado-informado-para-a-f%C3%B3rmula-n%C3%A3o-%C3%A9-considerado-valor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22879075393431) Tempo aproximado para leitura: **00:01:42 min****Ocorrência**Ao gerar o TRCT, o sistema retorna o seguinte erro: **Funcionário XXXXX: O dado informado para a fórmula não é considerado valor, favor verificar o retorno da fórmula.**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois a fórmula utilizada no campo 50 está retornando um valor zerado.    
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o cadastro da fórmula utilizada no campo 50 e ajuste a estrutura da fórmula para que retorne o valor do saldo salário do funcionário. Como sugestão, a empresa poderá utilizar a fórmula que se encontra na seguinte documentação: [RH - RM - FOP - TRCT: Saldo de Salário (Campo 50)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028914491-RH-RM-FOP-TRCT-Saldo-de-Sal%C3%A1rio-Campo-50)

**Importante:  O suporte padrão não presta auxílio na criação ou manutenção de fórmulas. Para estes casos, verifique a possibilidade de contratar nossa equipe de consultoria tarifada;**

2. Caso a empresa opte por gerar o campo 50 com o valor zerado, é necessário marcar as flags: **Imprimir verbas rescisórias pré-definidas** e **Zeradas**, conforme o exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22879075395095)

3. Feito isso, o sistema irá gerar o TRCT com o campo 50 zerado e não emitirá a mensagem de erro.

**Saiba Mais**

**[RH - RM - FOP - Parametrização Folha de Pagamento - Emissão TRCT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411690878103-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-Folha-de-Pagamento-Emiss%C3%A3o-TRCT#:~:text=F%C3%B3rmula%20para%20Saldo%20de%20Sal%C3%A1rio,Sal%C3%A1rio%20L%C3%ADquido%20pago%20na%20rescis%C3%A3o.)**
