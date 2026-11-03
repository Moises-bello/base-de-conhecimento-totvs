---
article_id: 37453495738135
category: Financeiro - Configurador de Tributos
content_hash: 1eadf350627da6fde5be4d02294d1175110e8b6ffe27a275b91c0c458da095e8
fetched_at: '2026-06-28T22:37:46.239931+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Qual o cadastro
  da Regra Financeira para gera o titulo TX DIFAL?
type: support-article
updated_at: '2026-01-05T19:31:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37453495738135-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Qual-o-cadastro-da-Regra-Financeira-para-gera-o-titulo-TX-DIFAL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37453525111319) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como gerar um titulo TX DIFAL com a regra financeira?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução**  
  
**1.1** Para esse cenário, crie a **regra de título** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* O **Tipo de Movimento (Tp. Movto)**, selecionando a opção *Impostos*
* **O****código do participante** (fornecedor ou cliente) para o qual será gerado o título;
* A **carteira**, que neste caso deve ser definida como *Pagar*;
* A **natureza** previamente criada para vinculação do tributo;
* O **tipo de título**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37453525112727)

**1.2 Regra Financeira**  
Este cadastro tem como função definir a regra de retenção do tributo aplicado a títulos gerados diretamente no módulo Financeiro, consolidando outras regras como vencimento, cumulatividade, retenção, cálculo, etc.

Outra função deste cadastro é definir a qual tributo a regra se refere, ou seja, relacionar a regra financeira a um tributo definido por legislações federais, estaduais ou municipais.

Para este cenário, é necessário criar a regra financeira correspondente ao imposto na aba**Dados Gerais**, preenchendo os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Início de Vigência**: data inicial
* **Fim da Vigência**: data final
* **Fato Gerador:** 1 – Competência (emissão) | 2 – Caixa (baixa)
* **Aplica-se à Carteira**: (1 – Pagar ou 2 – Receber; neste caso, selecionar a opção *Pagar*)
* **Valor do Título**: (1 – Subtrair, 2 – Somar ou 3 – Sem ação. Neste caso, selecionar a opção Sem ação)
* **Parcelamento**: opcional, conforme a necessidade.
* **Tributo**: imposto a ser cadastrado.
* **Classificação do tipo de imposto** (Principal)  
    
  Exemplo de um cadastro para o **DIFAL**  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37453495714071)

**1.3** Na aba Regras Gerais, vincule as regras criadas anteriormente nas **regras financeiras**, considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Regra de Título**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37453495715863)

**1.4** após configurar a regra Financeira, necessário vincular a Regra Fiscal cadastrada, exemplo abaixo  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37453525116311)  
  
**1.5** Demonstração de um processo onde esta vinculado a Regra Financeira a uma Regra Fiscal e geração de um documento de saida e ao ser finalizado é gerado o titulo TX do DIFAL no contas a pagar   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37453525125271)

**Obs.** Caso não queira que o titulo seja gerado com a sigla TG, a regra financeira deve possuir uma regra de retenção cadastrada e vinculada na regra Financeira. Com isso, o sistema irá gerar o título do tributo com a numeração da nota ou título conforme artigo: [Cross Segmentos Backoffice Linha Protheus - SIGAFIN - FISA170 - Regra financeira - Título com a Sigla TG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34520371038871-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Regra-financeira-T%C3%ADtulo-com-a-Sigla-TG)  
  
⚠️ Importante

Para o cadastro da Regra Fiscal em notas de entrada e saída, por meio do Configurador de Tributos, favor consultar as documentações

* [Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como Configurar Difal da EC/87 com Base dupla no fisa170?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14193357628823-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-Configurar-Difal-da-EC-87-com-Base-dupla-no-fisa170)  
  [Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar o DIFAL EC/87 com FECP no FISA170 base simples?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33254267433751-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-DIFAL-EC-87-com-FECP-no-FISA170-base-simples)  
  [Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como calcular Difal EC/87 com redução de base calculo Conv 52/91?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15478798420247-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-Difal-EC-87-com-redu%C3%A7%C3%A3o-de-base-calculo-Conv-52-91)  
  [Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como calcular o Difal EC/87 com base dupla?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26081448258071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-o-Difal-EC-87-com-base-dupla)
