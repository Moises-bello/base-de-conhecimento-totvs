---
article_id: 28118514210839
category: Financeiro
content_hash: 218a64d8be5690386c153c8d6b8de120abc2cec3b839d0525630725a7b499904
fetched_at: '2026-06-28T22:38:00.936306+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como realizar o rastreio
  das tabelas?
type: support-article
updated_at: '2024-11-27T21:02:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28118514210839-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-realizar-o-rastreio-das-tabelas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28118482938263) Tempo aproximado para leitura: **00****:10:00 min**

**Dúvida**  
Como realizar o rastreio das tabelas?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

A **tabela SE5** - Movimentações bancárias ao longo do ciclo de vida das versões do Microsiga Protheus influenciou o processo de evolução do produto.

Para que fosse possível manter um processo contínuo de evolução do produto, foi elaborado um projeto para reestruturação da tabela de movimentações bancárias, criando uma nova família de tabelas para normalização da tabela SE5. Essa nova família de tabelas, com o prefixo FK, possui 11 tabelas, sendo:

| Tabela | Descrição | Função |
| --- | --- | --- |
| FK1 | Baixas a receber | Registrar as baixas de títulos a receber |
| FK2 | Baixas a pagar | Registrar as baixas de títulos a pagar |
| FK3 | Impostos calculados | Armazenar os valores de impostos calculados para títulos a receber ou pagar |
| FK4 | Impostos retidos | Armazenar os valores de impostos retidos para títulos a receber ou pagar |
| FK5 | Movimentos bancários | Registra as movimentações bancárias de títulos a receber, a pagar e individuais |
| FK6 | Valores acessórios | Registra os valores de juros, multas, descontos, acréscimos e etc. de títulos a receber e pagar |
| FK7 | Tabela auxiliar | A tabela FK7 é um de DE/PARA entre a chave atual do título e chave futura do título. Aqui são armazenadas as chaves de amarração entre as tabelas SE1 e SE2. |
| FK8 | Dados contábeis | Gravação de dados complementares da tabela FK5, exclusivamente com dados contábeis |
| FK9 | Complemento de movimento | Gravação de dados complementares da tabela FK5, com dados de origem de módulos que integram ao Financeiro |
| FKA | Rastreio de movimento | Reúne em um único processo as informações referentes às baixas (FK1/FK2), movimento bancário (FK5) e cheques (SEF) e suas operações de estorno |
| FKB | Tipos de movimentos | Uso interno |

**Observação:** O compartilhamento das tabelas a seguir deve ser idêntica à da **tabela SE5**, com exceção das tabelas **FK7** e **FKB**.

Aqui estão alguns exemplos de como a nova família de tabelas se comporta nas situações listadas a seguir:

* [Baixa de títulos a Pagar](https://tdn.totvs.com.br/pages/releaseview.action?pageId=183730409)
* [Baixa de títulos a Receber](https://tdn.totvs.com.br/pages/releaseview.action?pageId=183730400)
* [Inclusão de título a receber com valores acessórios](https://tdn.totvs.com.br/pages/releaseview.action?pageId=652409315)
* [Inclusão de título a pagar com valores acessórios](https://tdn.totvs.com.br/pages/releaseview.action?pageId=652576938)
* [Movimentos Bancários](https://tdn.totvs.com.br/pages/releaseview.action?pageId=183730412)
* [Contabilização da nova estrutura de gravação do processo de movimento bancário e baixas](https://tdn.totvs.com.br/pages/releaseview.action?pageId=184779769)
* [Apropriação de variação cambial](https://tdn.totvs.com/pages/releaseview.action?pageId=569481610)
* [Padrão de gravação dos movimentos de títulos do tipo PA (Pagamento Antecipado).](https://tdn.totvs.com.br/pages/releaseview.action?pageId=606100372#Padr%C3%A3odegrava%C3%A7%C3%A3odosmovimentosdet%C3%ADtulosdotipoPA(PagamentoAntecipado).-02.PADR%C3%83ODETRATAMENTODOSIMPOSTOS)

Para informações sobre a  utilização de ponto de entrada para gravação de dados complementares das tabelas FK´s no modelo MVC acessar o link abaixo:

[Ponto de entrada para gravação de dados complementares nas tabelas FK´s e SE5](https://tdn.totvs.com.br/pages/releaseview.action?pageId=284859148)

Para informações adicionais e maiores esclarecimentos, acesse as perguntas mais frequentes no link abaixo:

[Reestruturação Financeiro - Baixas e Movimento Bancário](https://tdn.totvs.com.br/pages/releaseview.action?pageId=181965434)

**Saiba mais**

[Compartilhamento de tabelas do módulo Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=307830478)
