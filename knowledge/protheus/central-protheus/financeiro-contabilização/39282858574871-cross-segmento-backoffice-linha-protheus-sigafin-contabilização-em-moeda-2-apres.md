---
article_id: 39282858574871
category: Financeiro - Contabilização
content_hash: 053e185db7bb100bae3f1d5fed4520a25299e419349e94ad1ddcf88ecc8fa7da
fetched_at: '2026-06-28T22:38:05.250171+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Contabilização em moeda
  2 apresenta valores no contábil na moeda 1
type: support-article
updated_at: '2026-03-26T18:26:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39282858574871-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Contabiliza%C3%A7%C3%A3o-em-moeda-2-apresenta-valores-no-cont%C3%A1bil-na-moeda-1
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39282911748887)***Tempo aproximado para leitura: **00:08:00 min**

**Ocorrência:**  
Por que ao realizar uma contabilização offline de títulos com Moeda 2 e taxa de conversão, o sistema apresenta os valores na Moeda 1(R$) no Contábil?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**  
Este comportamento ocorre devido à arquitetura de integração entre os módulos de origem (Financeiro, Compras, Ativo e Faturamento) e o módulo Contabilidade Gerencial (SIGACTB).

Enquanto os módulos de origem utilizam a rotina **MATA090** (Cadastro de Moedas) para cálculos diários, o módulo Contábil possui uma estrutura própria baseada no relacionamento entre calendário, moeda e câmbio. No padrão da localização Brasil, a **Moeda Forte (Moeda 1)** da Contabilidade é o Real.

Dessa forma, no momento da integração (contabilização), o sistema prioriza a geração do lançamento na moeda principal do contábil. Esta é uma característica nativa do sistema e não é passível de alteração para que a Moeda 1 seja ignorada em favor da Moeda 2 no ato do lançamento.

Como alternativa para incluir ou converter os valores para a Moeda 2, o usuário pode seguir as seguintes recomendações:

1. **Câmbio Contábil:** Certifique-se de que a taxa de câmbio da moeda desejada (ex: Dólar) esteja devidamente cadastrada e vinculada ao calendário vigente no módulo **SIGACTB**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39282911752215)
2. **Campo CT2\_CONVER:** Utilize o campo **CT2\_CONVER** durante a contabilização para realizar a conversão manual para a posição correspondente à Moeda 2.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39282858552087)
3. **Critério de Conversão no Plano de Contas:** É possível definir o critério de conversão diretamente no Cadastro de Contas Contábeis. Isso permite a conversão automática, embora o sistema continue gerando obrigatoriamente os valores na Moeda 1 (Real).  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39282911757463)

**Saiba Mais:**

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Lançamentos em outras moedas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044528493)
