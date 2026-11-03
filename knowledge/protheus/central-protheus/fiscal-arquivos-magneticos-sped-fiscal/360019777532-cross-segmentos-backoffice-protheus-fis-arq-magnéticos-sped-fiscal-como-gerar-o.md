---
article_id: 360019777532
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 077ae848127f0fd114526c6ab2e9c65cbd0963a704465399509bb8fe477ce9de
fetched_at: '2026-06-28T22:42:01.187640+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o registro C110
type: support-article
updated_at: '2025-02-11T21:04:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019777532-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-C110
---

**Dúvida**Como gerar o registro C110: Complemento de Documento - Operações de Importação (Códigos 01 e 55) do Sped Fiscal.  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**

Este registro é gerado a partir do Livro Fiscal, fazendo o relacionamento do documento com a informação complementar lançada no registro 0450.

**Configuração**:

Para o preenchimento automático da tabela (**CDT - Informações Complementares NF**) ao finalizar um pedido de venda ou documento de entrada siga os procedimentos abaixo:

**1. Parâmetros**:

* **MV\_ATUCOMP = .T.**

**2. TES** de entrada/saída:

* Campo (**F4\_CODINFC** - "Cod.Inf.") = Informe o código da tabela (**CCE** - Informações Complementares) que será utilizado para gravar o código no campo (**CDT\_IFCOMP** - "Inf. Compl") da tabela (**CDT** - Informações Complementares NF).
* Campo (**F4\_FORINFC** - "Cod.Inf.") = Informe a formula cadastrada na tabela (**SM4** - Formulas) que retornará o conteúdo da descrição para o campo (**CDT\_DCCOMP** - "Desc. Compl") da tabela CDT - Informações Complementares NF).

**3.** Geração do registro **C110** do **SPEDFISCAL**:

* O registro **C110** será gerado seguindo as seguintes regras nesta ordem;

* Ponto de entrada: **SPDPISIC;**
* Situação do Documento: Caso o documento esteja com a situação de cancelamento fora do prazo, o registro C110 será gerado com código de cancelamento e descrição padrão do cancelamento.
* Parâmetro: **MV\_SPDIFC**;
* **MV\_SPDIFC = 0** : O sistema irá realizar uma busca na tabela **CCE**, utilizando o **CDT\_IFCOMP**, caso encontre o registro, então o registro **C110** será preenchido com o código do campo **CDT\_IFCOMP** da tabela **CDT** e com a descrição do campo **CCE\_DESCR**;
* **MV\_SPDIFC = 1** : O sistema irá preencher o registro C110 com o código do campo CDT\_IFCOMP e para a descrição irá verificar o campo CDT\_DCCOMP, caso esteja preenchido então será utilizado como descrição se não o sistema irá realizar uma busca na tabela CDC e caso o campo CDC\_DCCOMP esteja preenchido então utilizará como descrição do registro C110;
* **MV\_SPDIFC = 2** : O sistema irá preencher o registro C110 com o código do campo CDT\_IFCOMP e para a descrição irá utilizar os campos F1\_MENNOTA ou F2\_MENNOTA dependendo do tipo da NF;
* **MV\_SPDIFC = 3** : O sistema irá preencher o registro C110 com o código do campo CDT\_IFCOMP e para a descrição irá executar a formula do campo F4\_FORINFC, o retorno da formula será utilizado para descrição;

Exemplo para uso da formula: Caso queira que o descrição complementar do registro C110, seja o campo **(C5\_MENPAD + C5\_MENNOTA)** para as Notas de Saídas e **F1\_MENNOTA e F1\_MENPAD** para Notas de Entrada, basta criar uma formula concatenando essas informações e então preencher a formula no campo **F4\_FORINFC** da TES.

Se estiver usando o parâmetro **(****MV\_ATUCOMP = .T.)** no momento da geração do documento de entrada ou finalização do pedido, a tabela CDT já será preenchido e desta forma no momento da geração do arquivo magnético SPEDFISCAL se o parâmetro **(MV\_SPDIFC = 1)** então o sistema irá buscar do campo **CDC\_DCCOMP** a descrição para o registro.

Caso o parâmetro **(MV\_SPDIFC = 3)** no momento da geração do SPEDFISCAL, o sistema irá executar a formula cadastrada no campo **F4\_FORINFC**, para retornar a descrição do registro.
