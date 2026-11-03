---
article_id: 360036515853
category: RH - CNAB
content_hash: 2367ef0551d7aa1408c949f538cc1960c50a9d2c107243b7a4855236c1396fcb
fetched_at: '2026-06-28T22:43:39.265704+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Geração de arquivo CNAB Múltiplos Lotes (Modelo
  CNAB 2)
type: support-article
updated_at: '2025-06-16T14:41:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036515853-RH-Linha-Protheus-GPE-Gera%C3%A7%C3%A3o-de-arquivo-CNAB-M%C3%BAltiplos-Lotes-Modelo-CNAB-2
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32844016548247)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida:**Geração arquivo CNAB de Múltiplos Lotes  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução:**A opção "Ambos" no parâmetro "Gerar conta tipo?", permite a geração de registros para contas corrente e poupança.

Para utilizar essa funcionalidade é necessário atentar-se à alguns pontos:  
  
1. Quando a opção "Ambos" for selecionada o sistema irá processar todos os funcionários que respeitem os filtros informados e baseado no campo RA\_TPCTSAL ( Tipo da Conta Salário ) e no campo RA\_BCDEPSA ( Banco Conta Salário ) ele fará uma "quebra";  
  
2. Cada "quebra" será feita pela conjunção do Código do Banco + Tipo da Conta Salário para funcionários cujo o campo RA\_BCDEPSA **sejam iguais** ao informado no parâmetro "Processar Banco?". Os demais funcionários, ou seja, os que tiverem o campo RA\_BCDEPSA **diferente** do banco informado no parâmetro "Processar Banco?", a "quebra" será feita pela conjunção da palavra "DOC" + Tipo da Conta Salário. Essa conjunção, responsável pela "quebra" é armazenada numa variável chamada **cLote** que pode ser usada pelo usuário dentro de fórmulas e funções de usuário para determinar a forma de lançamento. Para melhor compreensão, vamos verificar um exemplo:   
  
**A)** O layout do *CNAB Padrão 240 - Folha de Pagamento* de determinado banco estabelece a seguinte regra no cabeçalho do lote:  
**I)** Entre as posições 012 e 013 deve constar a forma de lançamento do Lote, seguindo a numeração: 01 - Crédito em Conta Corrente, 03 - Transferências para outros Bancos(Doc ou Ted), 05 - Crédito em Conta Poupança e 10 - Ordem de Pagamento, baseado nessa numeração e na nossa variável **cLote**, podemos montar uma função de usuário com a estrutura abaixo:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047079614)**

3. Os funcionários cujo campo RA\_TPCTSAL ( Tipo da Conta Salário ) estiver vazio são considerados um lote à parte. No nosso exemplo do item 2 os funcionários cujo RA\_TPCTSAL ( Tipo da Conta Salário ) estão vazios são tratados dentro do lote de Ordem de Pagamento;

4. A estrutura de chamada do LayOut é a seguinte:

**A)** Cabeçalho do Arquivo  
**I.** Cabeçalho do Lote (1 ou N)  
**II.** Rodapé Lote (1 ou N)

**B)** Rodapé Arquivo  
  
5. O sistema disponibiliza algumas novas variáveis que podem ser utilizadas livremente dentro das funções de usuário e das fórmulas do layout:  
  
**nLoteSeq**, armazena a sequência do lote, sendo incrementado toda vez que ocorre uma "quebra", ou seja, toda vez que **cLote** se modifica;  
B) **nLoteQtd**, armazena a quantidade de registros dentro do lote atual.  
C) **nLoteTotal**,armazena o valor dos lançamentos contidos no lote atual.  
D) **nQtdLinLote**, armazena a quantidade de linhas detalhe dentro do lote atual, ou seja, desconsiderando as linhas do cabeçalho e do rodapé.

6. Algumas variáveis que já existiam mantiveram seu comportamento normal:

**nTotal**, guarda o valor total do arquivo como um todo;  
**nTotFunc**, guarda a quantidade de registros processados no arquivo como um todo;

7. Lembrando que a rotina processa os beneficiários dos funcionários também, nesse caso evite utilizar o alias da tabela de funcionários(SRA) no seu layout, por exemplo, ao invés de usar SRA->RA\_NOME, utilize a variável **cNome**.

8. O layout utilizado para múltiplos lotes também funciona quando selecionada as opções separadas(Conta Corrente ou Conta Poupança), só que nesse caso a variável **cLote** fica imutável

Exemplo de arquivos gerados com essa nova funcionalidade:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047963313)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047080294)  
  
*O parâmetro **"Processar banco ?"** deve ser informado com o banco da empresa(no nosso exemplo, 033). O parâmetro **"Gerar conta tipo ?"** deve estar configurado como "Ambos"*

*![](https://tdn.totvs.com/download/attachments/239035368/2.JPG?version=1&modificationDate=1465995402000&api=v2)*

*O parâmetro **"Layout ?"** deve ser necessariamente "CNAB Modelo 2"*

*![](https://tdn.totvs.com/download/attachments/239035368/1.JPG?version=1&modificationDate=1465995401000&api=v2)*

**IMPORTANTE:   
 Verifique se sua tabela S052 está configurada também com a quebra de conta conforme print abaixo:**

**![](https://totvssuporte.zendesk.com/attachments/token/AgUz5kmsqovOCKP8V3C1EtvWo/?name=image.png)  
  
Obs.:** Essa funcionalidade só está disponível para CNAB modelo 2.  Anexo um arquivo configurado com as funções descritas na documentação. 

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Passo a passo para geração do Arquivo CNAB (GPEM080)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8420406092951-RH-Linha-Protheus-GPE-Passo-a-passo-para-gera%C3%A7%C3%A3o-do-Arquivo-CNAB-GPEM080-)

[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
