---
article_id: 40724704176407
category: Folha Mensal
content_hash: d647b3520f99e00af5d31a52124132c9ebbbb5b67df336417da8b85ade9427b7
fetched_at: '2026-06-28T22:46:57.893521+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Parametrização da dedução de dependentes no cálculo de IRRF
  sobre PLR
type: support-article
updated_at: '2026-05-25T19:08:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40724704176407-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-da-dedu%C3%A7%C3%A3o-de-dependentes-no-c%C3%A1lculo-de-IRRF-sobre-PLR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40724704164247) Tempo aproximado para leitura: **00:01:11 min**  
  
**Dúvida**  
Como funciona a dedução de dependentes no cálculo do IRRF sobre PLR e qual parametrização controla esse comportamento no sistema?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Com este parâmetro marcado será deduzido da base de cálculo do evento de Código de Cálculo 126 - Participação nos Lucros, o valor referente a dedução de Imposto de Renda por dependente, cadastrado em Administração Pessoal | Cadastros | Cálculos | Valores Fixos, registro com a finalidade “Valor deduzir de IRRF por dependente” e com a vigência dentro da competência de cálculo da folha.

Caso este parâmetro esteja desmarcado, não será considerado o valor da tabela cálculo de valores fixos na dedução para Imposto de Renda.

**Observação**

* Para que a dedução ocorra, é necessário que o funcionário tenha dependente cadastrado em Administração de Pessoal | Cadastros | Funcionários | Anexo | Folha de Pagamento | Dependentes, com o parâmetro marcado “IRRF” na aba incidências do cadastro do dependente e que o mesmo seja elegível pela receita federal, como menores de 21 anos, filho inválido, etc.
* Esse parâmetro também será considerado no cálculo do imposto de renda da pensão que incide na participação dos lucros, sendo que terá o mesmo comportamento feito no cálculo do imposto de renda sobre a participação dos lucros.

O sistema RM possui um parâmetro específico que determina se o valor por dependente deve ou não ser deduzido da base de cálculo do IRRF sobre a Participação nos Lucros e Resultados (PLR). Se o sistema está deduzindo os dependentes e a orientação da empresa é para não deduzir, é necessário desmarcar essa opção na parametrização do sistema.

1. Acesse a aba: **Configurações | Parametrizador | Folha normal | Cálculo 2/2** e valide o parâmetro: **Deduz valor por dependente na base de IRRF PL**, conforme a imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40724678092183)

2. Avance até o final do assistente e clique em Salvar para consolidar a alteração;
3. Recalcule a folha e valide os valores.

**Saiba Mais:**

[RH - RM - FOP - Folha: Lançamento de PLR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12548712757015-RH-RM-FOP-Folha-Lan%C3%A7amento-de-PLR)
