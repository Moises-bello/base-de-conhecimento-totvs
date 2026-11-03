---
content_hash: bda13abb9a1eaa38974f1868854bfb75850e4620eec6bb31c02cdc377d4a3ee7
fetched_at: '2026-06-29T00:09:21.384426+00:00'
page_id: '422545876'
product: rm
source: tdn-rm
title: Especificação Técnica da Conversão da Natureza
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545876
version: 13
---

**Pré-Condições para execução da funcionalidade**

O parâmetro "Natureza Global" deve ter sido alterado no parametrizador TOTVS Gestão Fiscal, o mesmo deve ter sido **Habilitado** ou **Desabilitado**

**Descrição da Funcionalidade**

* Quando o parâmetro for **Desabilitado** o usuário deve converter as **Naturezas Globais** que eram utilizadas no sistema para as **Naturezas Não Globais** que devem ser cadastradas para cada Filial da coligada no qual o parâmetro foi desabilitado.
* Quando o parâmetro for **Habilitado** o usuário deve converter as **Naturezas Não Globais** que eram utilizadas no sistema para as **Naturezas Globais** que devem ser cadastradas para a coligada no qual o parâmetro foi habilitado.

O objetivo de se relacionar/converter um natureza de operação é atualizar todos os cadastros relacionados à Natureza de Operação que não será mais utilizada (Global quando o parâmetro for desabilitado e Não Global quando o parâmetro for habilitado) para uma nova Natureza de Operação que poderá ser utilizada no sistema.  
  
**Exemplo quando o parâmetro for desabilitado:**

* Um lançamento "00001" estava relacionado com a natureza de operação 1.101.01 (idnat = 1) que foi cadastrada no sistema enquanto o parâmetro Natureza Global estava habilitado.
* Após o parâmetro ser desabilitado é criado uma nova natureza de operação (1.101.01 – idnat = 2) para a filial no qual o lançamento foi gerado. Essa nova natureza deve ter as mesmas características da natureza global 1.101.01 (idnat = 1).
* A natureza de operação global (1.101.01 – idnat = 1) é convertida na nova natureza de operação não global (1.101.01 idnat = 2).
* O lançamento fiscal passa a ter relacionamento com a nova natureza de operação (1.101.01 idnat = 2).

***Observações:**Após o parâmetro ser desabilitado o lançamento "00001" continua relacionado com a natureza **global** 1.101.01 (idnat = 1).*  
*Ao se abrir um lançamento, por exemplo, o sistema não conseguirá apresentar a natureza corretamente pois, quando o parâmetro está desabilitado, o sistema filtra somente naturezas cadastradas para uma determinada filial o que não é o caso das naturezas globais, que são cadastradas para a coligada.*  
*A conversão é necessária para que, o lançamento, por exemplo, passe a ser relacionado à uma natureza cadastrada para uma filial.*  
*É de suma importância que a natureza cadastrada para a filial e a natureza global tenham as mesmas características, isso evitará que haja inconsistências fiscais no lançamento quando a conversão for realizada.*  
Este exemplo também se aplica quando o parâmetro for **habilitado**, porém a conversão é feita de uma natureza não global para uma natureza global.

*****Importante!!!***Para cadastro de novas Naturezas de Operações com as mesmas características da Natureza Global ou Não Global ver rotina "Duplicação de Natureza".**

**Impacto no Sistema**  
 Ao se converter uma Natureza de Operação o sistema deve atualizar todos os registros existentes na base de dados que estiverem relacionados à Natureza que não será mais utilizada, isso inclui as seguintes tabelas.

* **DATIVO** (Lançamentos – Manutenção Lançamentos Ativo Imobilizado CIAP)
* **DITMEVCTRB (**Item tributário do evento Tributário**)**
* **DLAF** (Lançamentos – Manutenção de Lançamentos de Entrada / Saída)
* **DLAFHISTORICO** (Tabela de Histórico do Lançamento Fiscal)
* **TMOV** (Movimentos)
* **TITMMOV** (Itens de Movimento)
* **TCNT** (Contratos)
* **TITMCNT** (Itens de Contrato)
* **TTRIBUTACAOECFNAT** (Natureza por Tributação de Cupom Fiscal)
* **TPONTOVENDA (**Ponto de Venda**)**

**Regras de Conversão de Natureza**

Ao se iniciar o processo de conversão de natureza, os seguintes dados serão requisitados do usuário.

* **Filial** – informação que permite o filtro das naturezas não globais que serão utilizadas para o processo de conversão de natureza.
* **Exercício Origem** – informação que permite o filtro de Naturezas Globais ou Não Globais. Só serão apresentadas para conversão as naturezas globais cadastradas para este exercício fiscal.

**Quando Parâmetro for desabilitado:**

1 NG pode ser **convertida** em **1 única** NNG

1 NNG pode **converter N** NG

**Quando Parâmetro for habilitado:**

**1** NNG pode ser **convertida** em **1** **única** NG

**1** NG pode **converter** **N** NNG

**Alertas ao usuário**

O sistema verificará se a Natureza Global está sendo convertida para uma Natureza não Global compatível, por exemplo. O ideal seria que todos os elementos que compõe uma natureza de operação fossem comparados, porém para não tornar o processo oneroso serão testados somente as regras de dependência (regras de ICMS e IPI) e será feito consistência se as naturezas relacionadas são do mesmo tipo (entrada/saída).  
É importante que o usuário saiba que se a conversão for feita para naturezas que possuem características diferentes os lançamentos criados e inicialmente relacionados com a Natureza Global terão inconsistências fiscais e isso poderá provocar diversos problemas no momento de apuração dos tributos ou na geração de alguma rotina, seja ela municipal, estadual ou federal.
