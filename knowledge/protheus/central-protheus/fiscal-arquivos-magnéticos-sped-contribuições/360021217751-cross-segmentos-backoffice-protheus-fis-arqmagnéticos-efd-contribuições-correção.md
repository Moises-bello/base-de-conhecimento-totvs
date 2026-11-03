---
article_id: 360021217751
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: e0c33a8004c261eade0673b05c57fbcde6a0cab72ff942b0f89543e8c08e70e5
fetched_at: '2026-06-28T22:42:05.154012+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Correção do errorlog "invalid field name in Alias SCGN000024->F1_SUBSERI on PROCD500
  (FISA007.PRW)"
type: support-article
updated_at: '2023-01-04T13:21:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021217751-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Corre%C3%A7%C3%A3o-do-errorlog-invalid-field-name-in-Alias-SCGN000024-F1-SUBSERI-on-PROCD500-FISA007-PRW
---

**Dúvida**Como corrigir o errorlog invalid field name in Alias SCGN000024->F1\_SUBSERI on PROCD500(FISA007.PRW)?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

 1. Atualize a rotina **FISA007.PRW** com o pacote de atualização abaixo:  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049615333-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Atualiza%C3%A7%C3%A3o-do-Ambiente-Fiscal-M%C3%B3dulo-09-para-a-correta-gera%C3%A7%C3%A3o-dos-Arquivos-Magn%C3%A9ticos-fiscais-?source=search>

2. Crie o parâmetro **MV\_SUBSERI**no configurador com as características abaixo:  
Nome da Variável: **MV\_SUBSERI**  
Tipo: **Lógico**  
Descrição: **Habilita o campo F1\_SUBSERI no cabeçalho da nota**  
**fiscal de entrada.**  
Valor Padrão: .**F.**3. Crie o campo **F1\_SUBSERI** no configurador com as características abaixo:   
Campo: **F1\_SUBSERI**  
Tipo: **C**  
Tamanho: **3**  
Decimal: **0**  
Formato: **!!!**  
Título: **Subserie**  
Descrição: **Subserie do documento**  
Nível: **1**  
Usado: **Sim**  
Obrigatório: **Não**  
Browse: **Não**  
Help: **Subsérie do documento fiscal**.  
  
4. Processe a rotina para gerar o arquivo referente ao **EFD Contribuições**, o erro não será apresentado.
