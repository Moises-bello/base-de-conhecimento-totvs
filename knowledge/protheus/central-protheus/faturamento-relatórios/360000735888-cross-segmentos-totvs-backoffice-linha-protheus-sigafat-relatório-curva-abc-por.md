---
article_id: 360000735888
category: FATURAMENTO - RELATÓRIOS
content_hash: 956eee0f275f32838c63697f0cc81b32af59338abedb7d0af5f51035c8ddf3e4
fetched_at: '2026-06-28T22:38:22.969275+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Relatório Curva
  ABC (Por Cliente [MATR765] ou Por Região [MATR755]
type: support-article
updated_at: '2023-10-17T20:50:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000735888-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Relat%C3%B3rio-Curva-ABC-Por-Cliente-MATR765-ou-Por-Regi%C3%A3o-MATR755
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18344298959767) Tempo aproximado para leitura: 00:02:30 min**

**Dúvida**

Os relatórios MATR755 e MATR765 estão sendo gerados sem registro, o que fazer?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - A partir da versão 11.80

**Solução**  
Para gerar o relatório em questão é necessário que seja seguido os quatro passos abaixo, analisando as três observações descritas:

1. Os parâmetros **MV\_CFOFAT e MV\_CFODEV devem ter** o CFOP utilizado no **pedido de venda** (**MATA410**), no campo C6\_CF.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12044627349015)

2.As **CFOP's** devem estar em **ordem crescente**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18344280680471)

3. O campo "Região (A1\_REGIAO)" do cliente do pedido de vendas (C5\_CLIENTE) deve estar preenchido.

4. A rotina **Atualização de Consumo de Vendas** (**MATA560**) deve ser rodada para que haja a criação de registros na tabela SJ3 (**A rotina de atualização de consumo deve ser processada de forma exclusiva no sistema, ou seja, sem interferência de usuários).**

5. O TES do pedido de venda (C6\_TS) deve atualizar estoque e ter saldo em estoque (F4\_ESTOQUE == Sim)

**OSBERVAÇÃO 1:** Os relatórios MATR765 e MATR755 são um espelho da tabela SJ3, tabela essa populada pela rotina A**tualização de Consumo de Vendas (MATA560), caso contrário ela pode vir vazia.**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087313774)**

**OSBERVAÇÃO 2:** No preenchimento dos parâmetros **MV\_CFOFAT e MV\_CFODEV os CFOPs devem estar em ordem crescente (do menor ao maior)** e com sempre cinco dígitos antes da barra, mesmo que sejam espaços em branco.

**(Exemplo A)**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12044402649879)

**(Exemplo B) MV\_CFOFAT** ou **MV\_CFODEV = 5101  /5111**

**((Exemplo C)**Exemplo 2: **<número><número><número><número><espaço><espaço><barra>**

**(Exemplo D)** Exemplo 3: **<5><1><0><1><espaço><espaço></>**

**OSBERVAÇÃO 3: Certifique-se que o filtro do relatório esteja correto para obter resultados**

**MATR755**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088460493)

**MATR765**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088460633)

**Saiba mais:**

[Relatório Curva ABC (MATR765 Por Cliente / MATR755 - Por Região)](https://tdn.totvs.com/x/d7p3DQ)
