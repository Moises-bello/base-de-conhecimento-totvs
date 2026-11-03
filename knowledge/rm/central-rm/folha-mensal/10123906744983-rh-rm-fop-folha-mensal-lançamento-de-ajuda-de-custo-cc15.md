---
article_id: 10123906744983
category: Folha Mensal
content_hash: fa8a3cd71001f8541f718a1f2c1d4c67ee47a065d90fecf151a6b9e4384e1e87
fetched_at: '2026-06-28T22:46:58.325713+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Mensal: lançamento de ajuda de custo cc15'
type: support-article
updated_at: '2024-09-16T18:27:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10123906744983-RH-RM-FOP-Folha-Mensal-lan%C3%A7amento-de-ajuda-de-custo-cc15
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15577123248663)**Tempo aproximado para leitura:**00:02:52 min  
  
Dúvida**  
Como realizar o lançamento de ajuda de custo (cc15) no envelope?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**1. Realize o cadastro do evento com o seguinte [Código de Cálculo 15 - Ajuda de Custo](https://tdn.totvs.com/pages/viewpage.action?pageId=452719784), abaixo caminho para processo:

[RH - RM - FOP - Cadastro de Eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412771329815-RH-RM-FOP-Cadastro-de-Eventos)  
  
Exemplo evento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15577120472343)  
  
2. Acesse o cadastro do **Funcionário | aba Parâmetros  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15577152212631)**  
  
O sistema irá lançar neste evento conforme informado no campo Ajuda de Custo do cadastro de Funcionários, pasta Base de Cálculo e fará proporcionalidade em relação a horas trabalhadas (Códigos de cálculo 01, 02 e 08).

O cálculo será feito da seguinte forma:

(CAMPO AJUDA DE CUSTO \* No. HORAS NORMAIS) / Nº. DE HORAS

O sistema buscará o valor informado no campo Ajuda de Custo, multiplicado pelo número de horas normais, e dividirá pelo número de horas informado para o evento com código de cálculo 01 (Horas Normais).

**Exemplo**

Ajuda de custo = 100,00

O funcionário trabalhou 220 horas, logo, o valor calculado será igual a 100,00.

Se o mesmo funcionário trabalhasse somente 110 horas, a ajuda de custo seria igual a 50,00.

É importante que o mesmo número de horas normais (código de cálculo 01) seja informado na movimentação do funcionário, antes ou simultaneamente com a ajuda de custo e que o evento de ajuda de custo tenha a prioridade maior.
