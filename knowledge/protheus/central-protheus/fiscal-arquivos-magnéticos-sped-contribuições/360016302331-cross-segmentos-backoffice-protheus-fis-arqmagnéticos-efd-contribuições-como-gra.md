---
article_id: 360016302331
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: ccc79f3d63ce284602f522014e52e39618bea8d77f7e69d6cf14f9192eea91a6
fetched_at: '2026-06-28T22:42:05.136193+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Como Gravar os Dados do Contabilista
type: support-article
updated_at: '2023-01-04T13:00:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016302331-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Como-Gravar-os-Dados-do-Contabilista
---

**Ocorrência**Os parâmetros utilizados na Geração do arquivo com os dados do Contabilista não ficam salvos nas Wizards da EFD Contribuições.   
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Causa**   
Esse incidente ocorre, pois a parametrização do sistema está incorreta para os parâmetros do Contabilista permanecerem salvos na wizard.  
  
**Solução**1. Acesse a **APSDU** na **Tabela SX1**;  
2. Realize o filtro pelo campo **X1\_GRUPO** digitando as opções conforme abaixo para alteração:

**FSA004 (Dados do Contabilista)**

3. Na coluna **X1\_GSC** altere os campos de C para G. Dessa forma o conteúdo dos campos de todas as perguntas do contabilista devem ficar **X1\_GSC** = G;  
4. Realize a geração do arquivo **EFD Contribuições** e verifique a gravação das informações referentes aos dados do contabilista.  
  
**Observação:** Após o procedimento acima, preencha os respectivos dados, processe a apuração e gere o arquivo da **EFD Contribuição,** entre novamente na Wizard da geração do arquivo e verifique se os dados do contabilista foram salvos. A partir daí os dados ficarão salvos.

![dados_contabilista.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360012031592/dados_contabilista.gif)
