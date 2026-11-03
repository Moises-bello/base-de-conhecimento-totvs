---
article_id: 37507151388311
category: Financeiro - Contas a Pagar
content_hash: 31448e599924e99ee8da7646f61ec444c1ede83ef8fadd562923b8081949fe6c
fetched_at: '2026-06-28T22:38:06.912048+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA050/FINA040 - Contabilização
  de valores e acessórios
type: support-article
updated_at: '2026-01-07T17:30:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37507151388311-Cross-Segmento-Backoffice-Linha-Protheus-FINA050-FINA040-Contabiliza%C3%A7%C3%A3o-de-valores-e-acess%C3%B3rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37507151362711) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como realizar a contabilização de valores e acessórios no módulo financeiro?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Quando você cria um **título a receber**, o sistema **não faz automaticamente a contabilização dos valores acessórios** (como juros, multa, desconto etc.).

Para que esses valores sejam contabilizados corretamente, é preciso:

Ir até o **cadastro de tipos de valores acessórios** e preencher o campo **“Variável CTB”** com um nome que identifique aquele valor, por exemplo, “JUROSVA ”;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37507193799447)

Depois, usar essa **mesma variável** na configuração dos **Lançamentos Padronizados**, conforme as regras contábeis adotadas pela empresa.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37507193802519)

Ou seja, é um processo manual de **vincular os valores acessórios à contabilidade**, criando uma referência (a variável) que o sistema usará para saber **como contabilizar cada tipo de valor**.

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37507193803287)

**Saiba mais**

[Valores Acessórios no Contas a Receber](https://tdn.totvs.com/pages/releaseview.action?pageId=311631483)

[REGRA PARA CADASTRO VALORES ACESSÓRIOS](https://tdn.totvs.com/pages/releaseview.action?pageId=490636586#FINA050ContasaPagar(Revitaliza%C3%A7%C3%A3o)-11.REGRAPARACADASTROVALORESACESS%C3%93RIOS)

[Variáveis de contabilização da compensação a receber (online e off-line)](https://tdn.totvs.com/pages/releaseview.action?pageId=233747403)
