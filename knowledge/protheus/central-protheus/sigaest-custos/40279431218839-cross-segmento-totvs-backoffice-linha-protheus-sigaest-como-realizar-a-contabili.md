---
article_id: 40279431218839
category: SIGAEST - CUSTOS
content_hash: 7dc6f9828e370c2f3aa0040fd9df2e29747789d3ae4c55710306a98c04b97724
fetched_at: '2026-06-28T22:39:02.427886+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Como realizar
  a contabilização de um documento de entrada no módulo do estoque?
type: support-article
updated_at: '2026-06-17T13:05:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40279431218839-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Como-realizar-a-contabiliza%C3%A7%C3%A3o-de-um-documento-de-entrada-no-m%C3%B3dulo-do-estoque
---

A contabilização de documentos de entrada no módulo SIGAEST depende da correta configuração do Lançamento Padrão 681, do parâmetro MV\_CUSMED="M" e da execução do recálculo do custo médio. Esses passos garantem que os valores sejam adequadamente transferidos para a contabilidade, gerando os lançamentos contábeis esperados.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40279431203863) Tempo aproximado para leitura: 00**:**01:00 **min**  
  
**Dúvida**  
Como realizar a contabilização de documentos de entrada no módulo de Estoque e Custos utilizando o **Lançamento Padrão 681**, garantindo que os valores sejam corretamente levados para a contabilidade?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões.

**Solução**

A contabilização dos documentos de entrada no SIGAEST está diretamente vinculada ao **custo do item**.

Caso o **Lançamento Padrão (LP 681)** não esteja configurado corretamente ou o **recálculo do custo médio** não seja executado, o sistema não gera os lançamentos contábeis esperados.

Para que a contabilização ocorra corretamente, é necessário:

* Configurar o **Lançamento Padrão 681**;
* Garantir que o parâmetro **MV\_CUSMED = "M"**;
* Executar o **Recálculo do Custo Médio**, pois é nesse momento que os lançamentos contábeis são gerados.

**Passos**

* Acessar cadastro do Lançamento Padrão
* No módulo de Estoque/Custos acesse: **Atualizações > Cadastros > Contábil -> Lançamentos Padrões**;
* Localize ou inclua o código **681**;

![Captura de tela 2026-05-06 144346.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40279402638999)

* Na aba Valores, utilize a sintaxe correta para buscar o custo da nota (Exemplo: `SD1->D1_CUSTO`);

![Captura de tela 2026-05-06 144717.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40279402641047)

* Após configurar o LP, acesse Miscelânea > Cálculos > Recálculo do Custo Médio;
* Nos Parâmetros da rotina, certifique-se de que a opção **Gera Lançamento Contábil** esteja definida como **Sim**;
* Execute o processamento. Ao final, o sistema apresentará a tela de lançamentos contábeis gerados com base nos documentos de entrada processados no período.

![Captura de tela 2026-05-06 145122.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40279402642199)

**Saiba mais:**

[SIGAEST - Como Contabilizar as Movimentações Internas do Estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405082704791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-Contabilizar-as-Movimenta%C3%A7%C3%B5es-Internas-do-Estoque)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
