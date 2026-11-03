---
article_id: 38962290368791
category: SIGAEST - PROCESSAMENTOS
content_hash: 6007e906e3e9b11994b5d8d2cd26b551d69f5b5b1d25a711ee08069bc8d0eb77
fetched_at: '2026-06-28T22:39:04.889198+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Contabilização de
  Impostos do Configurador de Tributos
type: support-article
updated_at: '2026-03-24T14:05:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38962290368791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Contabiliza%C3%A7%C3%A3o-de-Impostos-do-Configurador-de-Tributos
---

O artigo explica como contabilizar impostos calculados pelo Configurador de Tributos (FISA170) no módulo SIGAEST, usando funções para buscar valores na tabela F2D. Destaca duas funções principais: CTBVLTRIB, que busca tributo pelo nome, e Posicione, que utiliza o ID do tributo. Ambas são usadas em Lançamentos Padronizados para integrar valores tributários ao processo contábil.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38962326702743) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como realizar a contabilização de impostos calculados através do **Configurador de Tributos (FISA170)** no módulo **SIGAEST**, utilizando as funções de busca de valores na tabela **F2D**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões]  
  
**Solução**  
Os impostos calculados pelo Configurador de Tributos não utilizam os campos padrões das tabelas de itens (**SD1/SD2**). Eles são gravados na tabela **F2D (Tributos por Item de Documento)**. Para contabilizar esses valores através de **Lançamentos Padronizados (LP)**, é necessário utilizar funções que busquem o valor específico do tributo desejado, filtrando pelo seu ID ou Nome.

Existem duas formas principais de realizar essa busca no LP:

1. **Função** `CTBVLTRIB`: Desenvolvida especificamente pelo time contábil para facilitar a leitura da tabela **F2D**. Ela permite buscar o valor total de um tributo independentemente do código da regra, utilizando o nome do imposto.
2. **Função** `Posicione`: Utilizada para buscar o valor gravado na **F2D** com base no índice e na chave de ligação (ID do tributo gravado nos campos `D1_IDTRIB` ou `D2_IDTRIB`).

Abaixo temos um vídeo demonstrando o processo de contabilização com as duas funções:

[![Capa.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38962326704663)](https://youtu.be/I0BcKLL1iRs?si=KDVuVXoJWQG1Gf1b)

#### Opção 1: Utilizando a função CTB VL Trib (Recomendado)

* Acesse o módulo CTB (Contabilidade Gerencial);
* Vá em Atualizações > Cadastros > Lançamentos Padronizados;
* No campo Valor (Sintaxe em AdvPL), utilize a função CTBVLTRIB
* Exemplo: [**Contabilização com Base na Classificação do Tributo**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37097599152663-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Contabiliza%C3%A7%C3%A3o-com-Base-na-Classifica%C3%A7%C3%A3o-do-Tributo)

O sistema buscará automaticamente o valor correspondente na tabela F2D vinculado ao item da nota que está sendo processado.

#### Opção 2: Utilizando a função Posicione

* Acesse o módulo CTB (Contabilidade Gerencial);
* Vá em Atualizações > Cadastros > Lançamentos Padronizados;
* No campo Sintaxe configure a função [**Posicione**](https://tdn.totvs.com/x/Hv1n)
* Exemplo: Posicione("F2D", 6, xFilial("F2D")+SD1->D1\_IDTRIB+"NOME\_DO\_IMPOSTO", "F2D\_VALOR")

Certifique-se de que o campo D1\_IDTRIB (para entradas) ou D2\_IDTRIB (para saídas) esteja preenchido no documento fiscal, pois ele é a chave de ligação com a regra do configurador.

***Saiba mais:***

[SIGAEST - Como configurar o custo de entrada com impostos na TES?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19509172274455-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-configurar-o-custo-de-entrada-com-impostos-na-TES)

[Configurador de Tributos - Regras de Custo (MATA041)](https://tdn.totvs.com/x/ZM-HNg)
