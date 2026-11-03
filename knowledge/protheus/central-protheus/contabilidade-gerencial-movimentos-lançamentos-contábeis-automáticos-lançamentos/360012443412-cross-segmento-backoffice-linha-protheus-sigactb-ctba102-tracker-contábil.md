---
article_id: 360012443412
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 7a19f5454275d85c5e3d9809448c3bc66cbf883289e13ef443f632056231786c
fetched_at: '2026-06-28T22:40:32.469096+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 TRACKER CONTÁBIL
type: support-article
updated_at: '2021-11-10T12:32:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012443412-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-TRACKER-CONT%C3%81BIL
---

**Dúvida**COMO FUNCIONA TRACKER CONTÁBIL?   
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**

O objetivo é localizar e exibir os lançamentos contábeis a partir do documento que os originou.  
  
A rotina utiliza as tabelas CV3 e CT2.  
Recebe o Alias da tabela onde o documento original esta gravado e o numero do registro (RECNO) do documento da tabela original.  
  
A localização dos registro é feita pela tabela CV3, que é o elo entre origem e tabela CT2.  
Na CV3 contém o registro da tabela de origem (CV3\_RECORI) e o registro do destino CT2 no campo (CV3\_RECDES).

Os campos da chave de busca (CTL\_KEY). determinam o que aparecerá no tracker contábil   
Na tabela CV3 tem o código do LP (CV3\_LP), com base nesse código localiza-se o registro na tabela CTL do registro da tabela CTL .

Os lançamentos são apresentados em **moeda 1**ordenados por data  
Se não localizar o registro na CV3 a rotina não exibe dados.

Para validar a funcionalidade do processo segue um exemplo do LP 500 (pode ser feito com outros LP):  
Obs.: importante validar em ambiente teste atualizado conforme portal do cliente

- Confirmar se o LP esta cadastrado na rotina Cadastro de Relacionamentos (CTBA090)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055521214/mceclip0.png)

- Incluir um titulo a receber contabilizando.  
- Através da rotina de inclusão de títulos a receber, posicionar sobre o registro, clicar em outras ações, Tracker Contábil.  
Exibirá o lançamento contábil gerado.

**Informações técnicas**

A contabilização irá gerar o lançamento na tabela CV3 com LP = 500, campo CV3\_RECDES = R\_E\_C\_N\_O da tabela CT2, campo CV3\_RECORI = R\_E\_C\_N\_O da tabela SE1, campo CV3\_KEY = CT2\_KEY.

Importante: A tabela **CV3-Rastreamento Contábil** é utilizada para o rastreamento do registro de origem a partir do lançamento contábil nas rotinas **Lançamento Contábil (CTBA101)**, **Lançamento Contábil Automático (CTBA102)** e **Lançamento Contábil Parametrizado (CTBA103)**. Em hipótese alguma deve-se executar a exclusão dos registros desta tabela, pois, sua exclusão inviabiliza este processo.

A função que faz a localização é a CTBC662

**Disponibilizado nos módulos:**

* Compras;
* Faturamento;
* Financeiro;
* Ativo fixo;
* Estoque/custos.
