---
article_id: 38510244316055
category: Contabilidade Gerencial - Relatórios Diários
content_hash: 6a6f28131521e90e0aad95cb7390a7dfc064f6c482b94466b4183904af41498e
fetched_at: '2026-06-28T22:40:39.542855+00:00'
product: protheus
section_id: 1500001548862
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR110 - Erro de limite
  de linhas no relatório Diário Contábil
type: support-article
updated_at: '2026-02-20T10:53:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38510244316055-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR110-Erro-de-limite-de-linhas-no-relat%C3%B3rio-Di%C3%A1rio-Cont%C3%A1bil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38510244289687) Tempo aproximado para leitura: 00**:**10 min  
  
**Dúvida**  
Ao tentar executar o relatório Diário Contábil (CTBR110), o sistema não prossegue com a emissão e apresenta a seguinte mensagem de erro: "Para esta versão do relatório o número de linhas não pode ser maior que 65 linhas".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38510244290839)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial (SIGACTB) - A partir da Versão 12.

**Solução**  
Esta ocorrência é um comportamento padrão do sistema e é apresentada devido ao limite estrutural de linhas do relatório. Esse conceito é utilizado no momento da impressão para garantir que a montagem do relatório no componente **TReport** ocorra corretamente e sem erros de quebra de página.

Os limites máximos de linhas definidos para os relatórios padrão são:

* Máximo de **65 linhas** para a impressão no modo **Retrato**.
* Máximo de **58 linhas** para a impressão no modo **Paisagem**.

Para corrigir o incidente e prosseguir com a emissão, será necessário adequar os parâmetros de impressão.

**Passos**

1. Acesse a rotina de emissão do relatório Diário Contábil (CTBR110).
2. Na tela de **Parâmetros**, localize a opção ou pergunta referente à quantidade de linhas por página.
3. Ajuste a quantidade informada para não ultrapassar os limites do layout de impressão selecionado (máximo de 65 para o modo retrato ou máximo de 58 para o modo paisagem).
4. Confirme as configurações e inicie a emissão do relatório novamente.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38510260840215)

**Saiba Mais**

[Diário Contábil (CTBR110 - SIGACTB)](https://tdn.totvs.com/pages/viewpage.action?pageId=347440203)
