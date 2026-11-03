---
article_id: 18076929597207
category: CRM - Dúvidas Gerais
content_hash: 450561cbfd95de75b8d33645079185b4abd597dc866ce9bc39bc302cb08b42ab
fetched_at: '2026-06-28T22:40:27.625778+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACRM - Log de Transferência
  de Contas (CRMA030)
type: support-article
updated_at: '2023-10-06T16:40:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18076929597207-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACRM-Log-de-Transfer%C3%AAncia-de-Contas-CRMA030
---

**Dúvida:**

Log Transferência de Contas (CRMA030)  
  
**Ambiente:**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACRM - Todas as versões.  
  
**Solução:**

Esta funcionalidade possibilita consultar o log de transferência realizada para contas contendo as principais informações das contas como:

* Vendedor anterior e atual;
* Unidade de Negócio;
* Observações anotadas no decorrer da transferência;
* Vendedor que decidiu a transferência, a data e a hora que foi realizada a transferência;

```
![Help_button](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/help_button.zoom40.gif) Importante:  
  
Configure os conteúdos dos parâmetros conforme descrevemos: MV_FATPROP, conteúdo com P e MV_FATMNTP, conteúdo com 1.  
  
Configure o parâmetro MV_PAPEL com o conteúdo, uma lista de código de cargos utilizados como papel no time de vendas da oportunidade.
```

Gera consulta de **Previsão de Vendas** tanto na área de trabalho do vendedor como no menu consulta do Faturamento, o que permite projetar a receita de vendas baseada no histórico das oportunidades com o objetivo de construir um **Plano de Vendas** eficaz e produtivo.

A consulta é feita em MVC e exibe a lista de oportunidades filtradas por período, permitindo visualizar a receita deste período além de outras informações da **Oportunidade de Vendas** pela exibição de seus campos na lista da consulta e o cálculo de totalizadores de receita por *status*.

A lista das oportunidades na consulta exibir um semáforo indicativo da atual situação da oportunidade. O primeiro semáforo exibe o status da oportunidade:

![](https://tdn.totvs.com/download/thumbnails/345540790/br_verde.png?version=1&modificationDate=1555953240887&api=v2)*Status* = Aberta

**![](https://tdn.totvs.com/download/thumbnails/345540790/br_amarelo.png?version=1&modificationDate=1555953249633&api=v2)***Status* = Suspensa

**![](https://tdn.totvs.com/download/thumbnails/345540790/br_vermelho.png?version=1&modificationDate=1555953257567&api=v2)***Status* = Ganha

*![](https://tdn.totvs.com/download/thumbnails/345540790/br_preto.png?version=1&modificationDate=1555953265830&api=v2)Status* = Perdida

O segundo semáforo exibirá a situação da oportunidade. Para as oportunidades abertas, a situação pode ser:

**![](https://tdn.totvs.com/download/thumbnails/345540790/br_verde.png?version=1&modificationDate=1555953240887&api=v2)**Significa que o tempo de duração do processo de vendas da oportunidade está **em dia.**

**![](https://tdn.totvs.com/download/thumbnails/345540790/br_amarelo.png?version=1&modificationDate=1555953249633&api=v2)**Significa que o tempo de duração do processo de vendas da oportunidade está **em alerta**, ou seja, o tempo de duração do estágio atual e dos próximos estágios somado com a data atual ultrapassa a data prevista para o encerramento da oportunidade.

**![](https://tdn.totvs.com/download/thumbnails/345540790/br_vermelho.png?version=1&modificationDate=1555953257567&api=v2)**Significa que a oportunidade está em atraso, ou seja, a data atual ultrapassa a data prevista para o encerramento da oportunidade.

---

**Especificação do Projeto**

Para as oportunidades fechadas, a situação pode ser:

![](https://tdn.totvs.com/download/thumbnails/345540790/br_branco.png?version=1&modificationDate=1555953358540&api=v2) Significa que a oportunidade de venda foi finalizada sem atraso no processo de vendas.

*![](https://tdn.totvs.com/download/thumbnails/345540790/br_preto.png?version=1&modificationDate=1555953265830&api=v2)* Significa que a oportunidade de venda foi finalizada com atraso no processo de vendas.

---

**A consulta deve apresentar também os seguintes totalizadores:**

\_ Total de **Receita Estimada** das oportunidades abertas.

\_ Total de **Receita Real** das oportunidades perdidas.

\_ Total de **Receita Estimada** das oportunidades suspensas.

\_ Total de **Receita Real** das oportunidades ganhas.

\_ Total de **Receita Estimada** das oportunidades previstas para fechar que não foram fechadas, ou seja, das oportunidades em atraso.

\_ Total de **Receita Estimada** das oportunidades previstas para fechar na semana.

\_ Total de **Receita Real** das oportunidades ganhas, encerradas na semana.

\_ Total de **Receita Estimada** das oportunidades previstas para fechar no mês.

\_ Total de **Receita Real** das oportunidades ganhas no mês.

\_ Total de **Receita Real** das oportunidades perdidas no mês.

Os valores de**Receita Real** e **Receita Estimada** respeitam a porcentagem de cada vendedor do time de vendas. Calcula-se o valor de acordo com a porcentagem de participação para cada vendedor do time.

Esta consulta está disponível na área de trabalho do vendedor e no menu de consulta do Faturamento.

Ao acessar a área de trabalho, exibem-se as informações já filtradas de acordo com os parâmetros selecionados. Quando o acesso é pelo menu consulta, o usuário informa as **Unidades de negócio** ou **Vendedores** que compõe a consulta, lembrando que as exibições dos filtros respeitam o nível de acesso do usuário, de acordo com a **Estrutura de Venda**.

A consulta deve permitir a exportação para arquivo em planilha (Excel).

---

**Procedimentos:**

**Transferência de conta direta**

1. Faça o logoff e acesse o sistema como o usuário que recebeu a conta da rotina [Transferência de Contas](https://tdn.totvs.com/x/R4iYF).
2. Acesse **Log de Transferência de Contas**e verifique na **Aba de Clientes**se a conta está disponível.

**Transferência de conta por solicitação**

1. Faça o logoff e acesse o sistema como o superior do vendedor que recebeu a conta pela rotina [Transferência de Contas](https://tdn.totvs.com/x/R4iYF).
2. Acesse **Log de Transferência de Contas**e na Aba **Liberação de Contas**está disponível a solicitação efetuada.
3. Selecione a solicitação e clique em **Decisão.**Visualize a abertura de uma tela com as informações do proprietário atual da conta do solicitante dessa conta (vendedor destino) e as descrições do motivo da solicitação.
4. No item **Decisão** na parte inferior da tela, preencha a observação decisão no campo **Obs.Decisão.**
5. Escolha a ação realizada nas oportunidades das contas a transferir, selecione **SIM** no campo **Liberar?**e clique em **Confirmar.**

**Veja também:**

* [Proposta Comercial](https://tdn.totvs.com/x/q56aFQ)
* [Transferência de Contas](https://tdn.totvs.com/x/R4iYF)
* [Log de Transferência de Contas](https://tdn.totvs.com/x/SA2LFQ)
* [Log de Transferência de Contas (CRMA030 - SIGACRM)](https://tdn.totvs.com/pages/releaseview.action?pageId=345540790)
