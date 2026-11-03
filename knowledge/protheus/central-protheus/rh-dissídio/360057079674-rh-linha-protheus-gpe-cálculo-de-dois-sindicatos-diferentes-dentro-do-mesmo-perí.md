---
article_id: 360057079674
category: RH - Dissídio
content_hash: 706fbd79e3df8c942ab52ff829271b1f39583b63e160be0b26ba0322b17e8d48
fetched_at: '2026-06-28T22:43:43.505933+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: 'RH - Linha Protheus - GPE - Cálculo de dois sindicatos diferentes dentro do
  mesmo período sistema gera mensagem: Período Selecionado já foi integrado'
type: support-article
updated_at: '2025-08-20T15:21:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057079674-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-dois-sindicatos-diferentes-dentro-do-mesmo-per%C3%ADodo-sistema-gera-mensagem-Per%C3%ADodo-Selecionado-j%C3%A1-foi-integrado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34318873400215) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Ao realizar o cálculo de dissídio para dois sindicatos diferentes, dentro do mesmo mês o sistema gera a mensagem: Período Selecionado já foi integrado. Dentro desse cenário, um sindicato foi calculado e integrado com folha de pagamento e em seguida houve a tentativa de calcular outro sindicato.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**A mensagem é gerada quando, ao calcular funcionários do primeiro sindicato, a **pergunta 'Sindicato'** - localizada dentro dos parâmetros de cálculo **não é preenchida**. Por esse motivo, dentro da tabela RHH - que armazena valores de dissídio a verba 000 não está com a coluna RHH\_SINDIC preenchida.  
O sistema faz a validação de função, sindicato, categoria e situação desde que os mesmos sejam informados nos parâmetros de cálculo.

A seguir, um exemplo de cálculo de dois sindicatos diferentes dentro do mesmo período:

1. Calcular funcionário X vinculado ao sindicado X:![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099220833)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099220913)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096906174)  
  
2. Visualizar cálculo da matricula X por meio da rotina de dissídio retroativo/ outras ações/ manutenção:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099221173)

3. Realizar a geração dos lançamentos e confirmar envio dos valores em lançamentos/ por funcionário:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096906674)  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099221473)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096906754)

4. Cálculo via tabela:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099221613)

5. Calcular dissídio para Funcionário Y – Sindicato Y: Mesmo parâmetros utilizados anteriormente, apenas com alteração de matricula e sindicato.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096906854)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099221673)

6. Visualizar cálculo da matricula Y por meio da rotina de dissídio retroativo/ outras ações/ manutenção:

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096907134)

7. Realizar a geração dos lançamentos e confirmar envio dos valores em lançamentos/ por funcionário:

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096907274)  
![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099221953)

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099222013)

**Saiba mais**: <https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio>
