---
article_id: 360013711431
category: RH - Relatórios Cadastros/Funcionários
content_hash: 7c0b4bb4e5d08d460482b6dfdb103ca3c37d76c1d820c4f7ce7ea523f3cd950f
fetched_at: '2026-06-28T22:43:18.514877+00:00'
product: protheus
section_id: 360010843654
source: central-protheus
title: RH - Linha Protheus - GPE -  Relatórios gerando folha em branco no início/
  fim do arquivo
type: support-article
updated_at: '2025-07-29T13:40:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013711431-RH-Linha-Protheus-GPE-Relat%C3%B3rios-gerando-folha-em-branco-no-in%C3%ADcio-fim-do-arquivo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33790837946903) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**Ao realizar impressão de relatórios, seja encaminhando para impressora ou exportando-o para arquivo PDF, sistema **gera folha em branco** no início ou no final do arquivo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12  
  
**Causa**   
Esse situação ocorre, pois a configuração dos parâmetros **MV\_CANSALT**e **MV\_SALTPAG**constam ativados para criação de folhas em branco.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse ambiente **SIGACFG** (Configurador);  
2. Acesse **Parâmetros**através do menu **Base de Dados > Dicionário > Base de Dados**;  
3. Clique em **Parâmetros**e localize **MV\_CANSALT** e coloque seu conteúdo = **.F..****Observações:**Caso queira a impressão dessa folha, é necessário ajustar o conteúdo dos parâmetros **MV\_CANSALT**e **MV\_SALTPAG**.

**MV\_CANSALT** - Define se permite ou não o envio de uma página em branco após a impressão. Caso afirmativo será considerado o parâmetro MV\_SALTPAG. **Conteúdo**: .T. = Sim; .F. = Não

**MV\_SALTPAG** - Indica se o salto de pagina deverá ser dado antes ou depois da impressão do relatório. Saltar pagina no início da impressão? **Conteúdo**: S = Salta no início da impressão; N= Salta depois da impressão
