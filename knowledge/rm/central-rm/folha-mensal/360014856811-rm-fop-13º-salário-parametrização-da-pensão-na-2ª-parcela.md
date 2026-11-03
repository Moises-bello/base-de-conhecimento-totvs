---
article_id: 360014856811
category: Folha Mensal
content_hash: 8e133dadbaf043a50d6418f067f2d4e0178a87cd5941bf37a6e3d5cf3e8d9cf0
fetched_at: '2026-06-28T22:47:00.265876+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RM - FOP - 13º Salário: Parametrização da Pensão na 2ª parcela'
type: support-article
updated_at: '2025-03-07T14:54:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014856811-RM-FOP-13%C2%BA-Sal%C3%A1rio-Parametriza%C3%A7%C3%A3o-da-Pens%C3%A3o-na-2%C2%AA-parcela
---

**Dúvida**Como parametrizar o desconto da Pensão Alimentícia na 2ª parcela do 13º salário?  
  
**Ambiente**RM - Totvs Folha de Pagamento - Todas as versões  
  
**Solução**Para configurar a parametrização da pensão alimentícia para o cálculo do 13º Salário, veja os passos abaixo:  
  
**01.** Acessar **Administração de Pessoal | Administração de Pessoal | Eventos** e inserir o evento de Pensão Alimentícia Código de Calculo 120, evento de **Desconto** do tipo **Valor** e **Dedutível IRRF 13º Salário**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000144741/mceclip0.png)  
  
Aba incidências:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101239733/mceclip1.png)  
  
**02.** Acesse **Administração de Pessoal | Funcionários** e localize o funcionário que terá o desconto de Pensão Alimentícia. Acesse **Dependentes | Incidências** e marque a opção **Pensão.****![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000144881/mceclip2.png)****3.** Acesse a aba **Dados da Pensão** e realize toda a parametrização (normalmente essa parametrização já existe, devido ao desconto em folha de pagamento). Caso já esteja parametrizado, não há necessidade de uma nova parametrização.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000144901/mceclip3.png)  
  
**04.** Ainda no cadastro do funcionário, acesse **códigos fixos** e informe o evento criado no passo 01 (PENSÃO ALIMENTÍCIA 13º SALÁRIO) no campo **Código do Evento**.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099020714/mceclip4.png)
