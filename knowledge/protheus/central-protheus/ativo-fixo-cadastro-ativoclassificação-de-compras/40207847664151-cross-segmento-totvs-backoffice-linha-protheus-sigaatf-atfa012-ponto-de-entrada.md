---
article_id: 40207847664151
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 16d21ac725b5eb5318a19bf36dd263df50201eaa04d0fa4f0a0eba30ac06cf38
fetched_at: '2026-06-28T22:41:48.493703+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAATF - ATFA012 - Ponto
  de Entrada no Cadastro de Ativos
type: support-article
updated_at: '2026-05-04T13:28:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40207847664151-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Ponto-de-Entrada-no-Cadastro-de-Ativos
---

A rotina de Cadastro de Ativos (ATFA012) do módulo de Ativo Fixo no TOTVS Protheus utiliza um único Ponto de Entrada no padrão MVC, diferente dos pontos convencionais que possuem vários nomes. A programação segue o conceito MVC comum a todas as rotinas do sistema, com documentação disponível para consulta e uma lista específica de pontos de entrada para o Ativo Fixo.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40207866534679) Tempo aproximado para leitura: **5 min**  
  
**Dúvida**  
Existe algum ponto de entrada para o módulo de Ativo Fixo, especificamente na rotina de Cadastro de Ativos (ATFA012)?  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo (SIGAATF) - a partir da versão 12  
  
  
**Solução**  
A rotina do cadastro via ATFA012 utiliza o Ponto de Entrada MVC.   
  
A programação do Ponto de Entrada em MVC é a mesma para todas as rotinas do sistema que utilizam esse padrão, podendo usar como base a documentação abaixo:

* [Pontos de entrada com conceito em MVC](https://tdn.totvs.com/display/framework/Pontos+de+Entrada+para+fontes+Advpl+desenvolvidos+utilizando+o+conceito+MVC)

Nos fontes convencionais temos um "nome" para cada ponto de entrada criado, por exemplo, na rotina MATA010 – Cadastro de Produtos temos os pontos de entrada: MT010BRW, MTA010OK, MT010CAN, etc. Em MVC, não é desta forma.   
  
Em MVC criamos um único ponto de entrada, e este é chamado em vários momentos dentro do fonte desenvolvido.

Para verificar os pontos de chamada do MVC, verificar a documentação:

* [Pontos de Entrada para fontes Advpl desenvolvidos utilizando o conceito MVC](https://tdn.totvs.com/display/public/framework/Pontos+de+Entrada+para+fontes+Advpl+desenvolvidos+utilizando+o+conceito+MVC)

**Saiba mais:**  
[ALGUNS PONTOS DE ENTRADA DO ATIVO FIXO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020956992-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ALGUNS-PONTOS-DE-ENTRADA-DO-ATIVO-FIXO?source=search)  
[Ponto de entrada Ativo Fixo](https://tdn.totvs.com/display/public/PROT/Ponto+de+entrada+-+Ativo+Fixo)
