---
article_id: 360016515752
category: RH - Rescisão
content_hash: 4fe0e820c4e1107e02165022b38ffeaa42c8f842778a358f7008cdc923af348a
fetched_at: '2026-06-28T22:43:48.631544+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar e conferir a indenização coletiva
  na rescisão
type: support-article
updated_at: '2025-09-12T17:28:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016515752-RH-Linha-Protheus-GPE-Como-configurar-e-conferir-a-indeniza%C3%A7%C3%A3o-coletiva-na-rescis%C3%A3o
---

**Dúvida**Como configurar e conferir a indenização coletiva na rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Em **Atualizações\Definições de cálculo\Verbas**, cadastre uma verba com identificador **0158**:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012758771)

2. Em **Atualizações\Definições de cálculo\Manutenção tabelas**, cadastre a tabela S040:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012757132)  
Os campos Inicio faixa e Fim faixa servem para determinar quantos meses o funcionário precisa ter trabalhado para se enquadrar na parametrização dessa linha. Utilizando esse print como exemplo, os que estiverem vinculados no sindicato 10 e tiver de 12 a 24 meses trabalhados terão uma indenização de 10%.  
  
**Observação:** Quando o campo Data base estiver em branco o sistema irá contar os meses pré-determinados no inicio e fim de faixa a partir da data de admissão do funcionário.

3. Em **Atualizações\Definições de cálculo\Manutenção tabelas**\**tabela S043**. No tipo de rescisão utilizado você deve deixar a coluna I**ndenização** com o conteúdo S.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012759291)

4. Vincule o funcionário (em **Atualizações\Funcionários\Funcionários**) ao Sindicato informado na tabela S040.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012757872)

5. Conferencia do valor na rescisão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012757952)

**Fórmula de cálculo:** Salário do funcionário + adicionais padrões (insalubridade, periculosidade, adicional por tempo de serviço, adicional de confiança e transferência) / dias de cálculo definidos no cadastro de período \* os dias de férias vencidos + proporcionais = base de cálculo \* percentual definido na S040 = **Valor da Indenização**  
  
O funcionário de exemplo não tem nenhum adicional, então: salário 2.000,00/ 30 dias \* férias vencidas de 30 dias + férias proporcionais 22,55 dias (total 52,5) = base de calculo de 3.500,00 \* 10% definido na tabela S040 = 350,00.

**Saiba mais**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

<https://tdn.totvs.com/pages/viewpage.action?pageId=329038342>
