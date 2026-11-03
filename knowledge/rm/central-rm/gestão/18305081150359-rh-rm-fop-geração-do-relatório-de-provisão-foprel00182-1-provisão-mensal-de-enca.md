---
article_id: 18305081150359
category: Gestão
content_hash: 64f0f76fccf7840756f6fb63a0defe55e82abc992014f12e0cd72c67ae14f17e
fetched_at: '2026-06-28T22:46:48.261614+00:00'
product: rm
section_id: 1500000861162
source: central-rm
title: RH - RM - FOP - Geração do relatório de provisão FOPREL00182. 1 -  Provisão
  Mensal de Encargos de Férias
type: support-article
updated_at: '2026-05-27T14:11:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18305081150359-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-relat%C3%B3rio-de-provis%C3%A3o-FOPREL00182-1-Provis%C3%A3o-Mensal-de-Encargos-de-F%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18305065452951) Tempo aproximado para leitura: **00:02:10min**  
  
**Dúvida**  
No módulo **Folha de Pagamento, c**omo gerar o relatório padrão de provisão **FOPREL00182. 1 - Provisão mensal férias** disponível no TOTVS Compartilhamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões.  
  
**Solução**  
Após realizar a importação do relatório padrão através do TOTVS Compartilhamento:  
  
[RH - RM - FOP- Importação de relatórios e layouts através do Totvs Compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7781155867543-RH-RM-FOP-Importa%C3%A7%C3%A3o-de-relat%C3%B3rios-e-layouts-atrav%C3%A9s-do-Totvs-Compartilhamento)  
  
Acesse: **Gestão | RM Reports**

Em seguida, localize o relatório:

**FOPREL00182.1 - Provisão Mensal de Encargos de Férias**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40768782888855)

Após localizar o relatório:

1. clique em **Processos**;

2. selecione **Geração do Relatório**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40768782890263)

3. Será apresentada a tela para definição dos filtros. Para editar os filtros desejados, clique nos três pontos conforme demonstrado abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18301241111575)

4. O relatório padrão possui filtro de **mês** e **ano**, permitindo a geração apenas de um período por vez.  
Não é possível realizar a geração de múltiplos meses simultaneamente nesse modelo de relatório.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18301410250135)

5. Após definir os filtros, avance e execute o processo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18301462417943)

## **Importante:**

As informações apresentadas no relatório são buscadas através do caminho:

**Encargos | Histórico de Provisão**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18301819494423)

Para os cálculos de encargos:

* o percentual de terceiros será considerado conforme parametrização da seção centralizadora do funcionário;
* para FGTS, o relatório considera percentual fixo de 8%.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18301850474519)

O cálculo interno do relatório considera:

**Valor do mês atual - valor do mês anterior**

Dessa forma, caso não exista histórico de provisão no mês anterior, os valores poderão não ser apresentados no relatório.

**Saiba mais**  
[RH - RM - FOP - Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019748711-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o)
