---
article_id: 18034893177111
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: fa628970b7c209883cbecbf49bc0fedb716f3c2a69721c3f5b8e245e71cdfb06
fetched_at: '2026-06-28T22:39:22.053209+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Relatórios gerando
  folha em branco no início/fim do arquivo
type: support-article
updated_at: '2023-10-04T22:50:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18034893177111-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Relat%C3%B3rios-gerando-folha-em-branco-no-in%C3%ADcio-fim-do-arquivo
---

**Dúvida**No módulo **Fiscal**, ao realizar impressão de relatórios no modo personalizado, ao encaminhar para a impressora ou exportando-o para arquivo PDF, o sistema gera folha em branco no início ou no final do arquivo. Como fazer para não gerar página em branco?  
  
**Ambiente**Protheus - Livros Fiscais - A partir da versão 12 "Todas as Versões"  
  
**Solução**

Esse situação ocorre, pois a configuração dos parâmetros **MV\_CANSALT**e **MV\_SALTPAG**constam ativados para criação de folhas em branco.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse ambiente **SIGACFG** (Configurador);  
2. Acesse **Parâmetros**através do menu **Base de Dados > Dicionário > Base de Dados**;  
3. Clique em **Parâmetros**e localize **MV\_CANSALT** e coloque seu conteúdo = **.F.****Observações:**Caso queira a impressão dessa folha, é necessário ajustar o conteúdo dos parâmetros **MV\_CANSALT**e **MV\_SALTPAG**.

**Para saber mais:**

**MV\_CANSALT** - Define se permite ou não o envio de uma página em branco após a impressão. Caso afirmativo será considerado o parâmetro MV\_SALTPAG

Seu conteúdo é lógico, podendo ser  **.T.**  ou **.F.**

 

**MV\_SALTPAG** - Indica se o salto de página deverá ser dado antes ou depois da impressão do relatório. Saltar página no início da impressão? 

Seu conteúdo é caractere, podendo ser  **S** ou **N**

**S** = Salta no início da impressão

**N**= Salta depois da impressão
