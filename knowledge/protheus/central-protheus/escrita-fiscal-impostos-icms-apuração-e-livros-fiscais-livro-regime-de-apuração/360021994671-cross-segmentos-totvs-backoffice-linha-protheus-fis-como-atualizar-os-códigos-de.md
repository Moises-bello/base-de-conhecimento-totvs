---
article_id: 360021994671
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 491017d5cac666cc74d3af6a200d2d827260a57c04c5b1e6b36174b00256a09e
fetched_at: '2026-06-28T22:39:22.151881+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como atualizar os
  códigos de ajuste/lançamentos manuais da apuração de ICMS (tabelas 51 "CDO" e 53
  "CC6")? '
type: support-article
updated_at: '2024-10-08T21:29:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021994671-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-atualizar-os-c%C3%B3digos-de-ajuste-lan%C3%A7amentos-manuais-da-apura%C3%A7%C3%A3o-de-ICMS-tabelas-51-CDO-e-53-CC6
---

**Dúvida**

Como atualizar os códigos de ajuste/lançamentos manuais da apuração de ICMS (tabelas CDO e CC6)?   
  
**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Para alimentar ou atualizar a tabela de Ajustes manuais de apuração de ICMS é necessário seguir os seguintes passos.

1. Acesse site da receita:   
<http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>

* **PACOTE** = Selecione o estado desejado;
* **TABELA** = Selecione a tabela desejada baixar;

Tabela 5.1 é pertinente ao código de 8 caracteres.

Tabela 5.3 é pertinente ao código de 10 caracteres.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15908819511063)

2. Selecionar a tabela desejada com a UF desejada e clique em Baixar tabela

3. Renomear tabela 5.1 para TABELA51 e tabela 5.3 para TABELA53

4. Coloque o Arquivo TXT dentro da pasta System do Protheus

**Importante**:

**\***Caso seu servidor for **Linux** o arquivo deve ser em letra minúscula "tabela51.txt"  ou "tabela53.txt"  e o caminho interno deve ser em minúsculo da pasta por exemplo: protheus\_data/system/...

**\*** Na pasta systemload é importante que contenha os arquivos do dicionário completo para não ocorrer o erro **"File\systemload\ SXSBRA.TXT not found"** no momento de rodar o U\_IMPSPED.

5. Execute o compatilizador U\_IMPSPED

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15908975395735)

6. Clique em procurar e seleciona a pasta System do Protheus e depois clique em Ok

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15909025409431)

7. Após conclusão clique em OK

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15909156257303)

Assim será gravado os códigos da tabela 5.1 na tabela do Protheus CDO com 8 caracteres e tabela 5.3 na tabela do Protheus CC6 com 10 caracteres.

Abaixo GIF demonstrativo

**TABELA51 e TABELA53**

![TABELA51 E TABELA 53 IMPORTAÇ~~AO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19035785535639)

Códigos de Lançamento e Reflexos da Apuração:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=640907320>
