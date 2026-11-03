---
article_id: 360053715433
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: e3730f4da8306f4bc767f0635c1993111a3590b7854ea12935f18b54a85689c7
fetched_at: '2026-06-28T22:38:44.153380+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Preenchimento dos campos
  D2_ESPECIE e F2_ESPECIE ao faturar
type: support-article
updated_at: '2026-03-26T14:24:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053715433-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Preenchimento-dos-campos-D2-ESPECIE-e-F2-ESPECIE-ao-faturar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39311114923031) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**

Como configurar para que, ao faturar uma nota de saída, os campos **D2\_ESPECIE** e **F2\_ESPECIE** sejam preenchidos?

**Ambiente**

Cross Segmentos - BackOffice Protheus - SIGAFAT - Todas as versões

**Solução**

O campo **F2\_ESPECIE** é preenchido quando a série da nota está preenchida no parâmetro **MV\_ESPECIE**.  Exemplo: **MV\_ESPECIE: 1=SPED** - Com esta configuração, sempre que a nota for emitida com a série 1, o campo **F2\_ESPECIE** será preenchido como **SPED**. Porém, isso depende do parâmetro **MV\_ESPNFX5:**

Caso o parâmetro **MV\_ESPNFX5** esteja como ".T.", a série para o **F2\_ESPECIE** não será levada do parâmetro **MV\_ESPECIE** e, sim da tabela genérica "**42**":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16759839662615)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16759832084247)

Caso o **F2\_ESPECIE** não esteja preenchido e o **MV\_ESPNFX5** = .T., verifique se a nomenclatura (exemplo: SPED) existe na tabela genérica "**42**" e se possui o vínculo entre série e espécie na tabela genérica "**SN - Cadastro Série/Espécie da NF. de Saída**".

A rotina Geração de Documento de Saída (**MATA460A**) irá considerar os dados da nova tabela "**SN**", junto com as informações já existentes no parâmetro **MV\_ESPECIE**, funcionará assim:

* **Tabela 00 - Chave 01:** Nesta tabela, devem ser cadastradas as **séries das Notas Fiscais**.
* **Tabela 42:** Aqui, você deve cadastrar as **espécies dos Documentos Fiscais** (***F2\_ESPECIE***).
* **Tabela SN:** Esta tabela faz o vínculo entre **série e espécie (semelhante ao MV\_ESPECIE)**. Por exemplo, inclua a série no campo *Chave = **1*** e no campo *Descrição = **1=SPED*** para indicar o vínculo da Série 1 com a espécie “**SPED**”.

Caso o **F2\_ESPECIE** não esteja preenchido e o **MV\_ESPNFX5** = .F., verifique se a série do parâmetro **MV\_ESPECIE** existe, na tabela genérica "01":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16759880831639)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16759911913239)

Verifique se as séries e parâmetros não estejam separados por filial, onde por exemplo na filial "X" é: "1=SPED" e na filial "Y" é: "1=NFE" e por isso não esteja sendo levado/está errado.

**OBSERVAÇÃO:** O campo **D2\_ESPECIE** somente é utilizado em operações específicas, como notas ficais de países localizados (**MATA467N**) ou notas de crédito e débito de países localizados, como Argentina e Equador.

Não é utilizado para o preenchimento de uma geração de nota pela rotina **MATA461**, por isso, que o campo sempre ficará vazio.

**Saiba mais:**

* [TVGGTJ\_DT\_Utilização da tabela SN (SX5) para cadastro de série/espécie de Nota Fiscal Saída (MV\_ESPECIE)](https://tdn.totvs.com/pages/viewpage.action?pageId=237382095)
