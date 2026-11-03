---
article_id: 37541406086295
category: Folha Mensal
content_hash: 0e40e22d4ca45c1b17deb966cfe4f1c334160d27f11d9320a03de231673cba7a
fetched_at: '2026-06-28T22:46:57.992996+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Crédito do Trabalhador - Campo Competência Atual
type: support-article
updated_at: '2026-01-12T18:56:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37541406086295-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Campo-Compet%C3%AAncia-Atual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37541406063767) Tempo aproximado para leitura: **00:05:15 min**  
  
**Dúvida**  
Qual é o funcionamento do novo campo Competência Atual implementado na tabela de Importação do Crédito do Trabalhador? Como o sistema valida a competência informada nesse campo para aplicar ou não o desconto do empréstimo na folha de pagamento, na rescisão e no cálculo de férias?  
  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

12.1.2410.319

12.1.2502.229

12.1.2506.179

12.1.2510.112

12.1.2602 e superiores

**Solução**  
Foi implementado um novo campo denominado Competência Atual na tabela de Importação do Crédito do Trabalhador, com o objetivo de controlar em qual competência o desconto do empréstimo deve ser aplicado.

A partir dessa alteração, o cálculo da folha de pagamento e da rescisão passa a considerar obrigatoriamente o valor informado nesse campo. O desconto do empréstimo somente será efetuado quando a competência preenchida corresponder exatamente à competência da folha que está sendo processada. Caso o campo não esteja preenchido ou a competência seja diferente da competência da folha, o desconto não será aplicado.

No cálculo de rescisão, o mesmo critério é utilizado: o desconto ocorrerá apenas se a competência informada no campo Competência Atual coincidir com a competência da rescisão.

Como exceção, no caso de férias, o sistema permite a aplicação do desconto quando a competência informada no novo campo corresponder ao mês de gozo das férias ou ao mês imediatamente anterior.  
  
➡️ EXEMPLO DE UTILIZAÇÃO:  
  
Dados Fictícios:

Validação dos campos da tabela de empréstimos:

PFEMPRT.MESCOMPATUAL

PFEMPRT.ANOCOMPATUAL

O campo será preenchido na base de dados e apresentado na tela do anexo Empréstimo do cadastro de funcionários

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37541406064535)

Neste mesmo funcionário tem outro empréstimo que deixarei com o campo Nulo na base de dados:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37541406072087)

Estando a base de dados também no mês 03/2025: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37541406074263)

Lançando o empréstimo pelo grupo de eventos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37541422311959)

No envelope foi lançado apenas o empréstimo considerando os campos de mês/ano competência do credito do trabalhador igual a competência atual da base de dados:  
  
  
![image-2025-10-31_15-44-42.png](https://tdn.totvs.com/download/attachments/1010818273/image-2025-10-31_15-44-42.png?version=1&modificationDate=1761936312383&api=v2)

⚠️ IMPORTANTE:

1.  Ao executar o script para a criação do campo deve-se importar o arquivo para o correto preenchimento dessa competência.

Se este campo estiver nulo na base de dados e apresentando valor zerado na visão do cadastro de empréstimo, este valor do empréstimo não será lançado.

Exemplo:

No mês de Outubro de 2025 o funcionário quitou o empréstimo.

No inicio do mês de Novembro de 2025 foi executado o atualizador na base de dados criando os campos com valor NULL

PFEMPRT.MESCOMPATUAL

PFEMPRT.ANOCOMPATUAL

Ao importar o arquivo disponibilizado no Emprega Brasil e o nome desse funcionário não estará no arquivo de Novembro de 2025, então o campo continuará nulo para este funcionário.

Quando executado o lançamento do desconto do empréstimo, então este funcionário não terá o desconto em folha porque não estava presente no arquivo e com isso este campo não foi atualizado.

* ⚠️ ATENÇÃO:

Caso importar o arquivo do Emprega Brasil antes de atualizar a base de dados no mês que deve ter o desconto do empréstimo consignado deve-se importar novamente o arquivo para preenchimento correto destes campos mês e ano da competência atual, sob risco de não ser descontado nenhum dos empréstimos por estarem com o campo Nulo.

2. Estes campos de mês/ano competência do credito do trabalhador foram tratados no lançamento do desconto pelo Grupo de Eventos e na Rescisão, e também no provisionamento no Adiantamento e no cálculo do recibo de Férias. Se o evento de desconto for lançado diretamente no envelope de pagamento do funcionário será feito o cálculo sem considerar os campos de mês/ano competência do credito do trabalhador, ficando o controle por conta do usuário.
