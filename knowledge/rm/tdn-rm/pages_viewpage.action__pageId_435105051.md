---
content_hash: fe54503f8113b35cd19a71e3476bd9477a81d7fa3898a5309c98c284e59b567d
fetched_at: '2026-06-29T00:09:47.708334+00:00'
page_id: '435105051'
product: rm
source: tdn-rm
title: EFD - PIS/Cofins - Log do SPED F200
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105051
version: 5
---

Foi criado um novo log para o EFD contribuições, este log será responsável por descrever os valores de cada venda que possui parcelas consideradas no SPED no período gerado. Este log trará informações do arquivo F200 do EFD.

A geração do arquivo ficará na **localização padrão na pasta RM.Net**.  
Exemplo: `C:\totvs\CorporeRM\RM.Net\Arquivos\LOG_SPED`.

Este caminho pode ser alterado através da inclusão da seguinte tag no arquivo **RM.Host.exe.config**:

`<add key="FileServerPath" value="\\ServidorExemplo\Compartilhamento\LOG_SPED" />`

Em ambientes **TCloud**, o caminho do Share pode ser consultado em **“Informações do Ambiente”**, no campo **“Caminho do Share (Files/Processos/LOG\_SPED)”**.  
Esse caminho corresponde ao **diretório do compartilhamento de arquivos do ambiente**, onde são armazenados os arquivos gerados pelo sistema, como os logs do SPED.

O log será dividido por contrato e em cada contrato serão detalhados os lançamentos financeiros e seus somatórios que serão enviados para o SPED.  
Para cada contrato serão mostrados as seguintes colunas e o somatório ao final:

* **IDLAN** - Identificador do lançamento no contrato.
* **VL\_TOT\_VEND** - Valor total da unidade imobiliária atualizada.
* **VL\_TOT\_REC** - Valor total no período da escrituração.
* **VL\_REC\_ACUM** - Valor Total Recebido no período anterior da Escrituração.
* **Valor a desconsiderar** - Valor desconsiderado na parcela pelo uso do parâmetro no cadastro de componentes (Desconsiderar valor na exportação para SPED/IMOB).

Ao final do contrato será mostrado também a soma dos valores das parcelas e multiplicados pelo percentual de participação do empreendimento. Este valor será compatível com o valor do arquivo EFD gerado.  
**Observação**: Dentro do cadastro de Empreendimento, na aba EFD-PIS/COFINS existe o campo marcável "Aplicar Juros e Muta (Financeiro), este campo pode interferir nos valores a serem enviados pelo SPED. Quando marcado ele aparecerá neste log para indicar o cálculo dos valores.

Veja Também

---

Para conferir a parametrização do EFD no Empreendimento, veja:   
Para mais informações sobre as atividades imobiliárias fiscais, acesse: [Atividades Imobiliárias](http://tdn.totvs.com/pages/viewpage.action?pageId=422545902)
