---
article_id: 360016084112
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 5f0772750ab777a7dd1970fff500553353b092996f322c345c0f4b33cee492f4
fetched_at: '2026-06-28T22:42:05.139505+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Como Gravar os Dados do Contabilista - Como gravar os parâmetros do Contabilista
  na wizard da geração do arquivo do EFD Contribuições
type: support-article
updated_at: '2023-01-04T13:02:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016084112-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Como-Gravar-os-Dados-do-Contabilista-Como-gravar-os-par%C3%A2metros-do-Contabilista-na-wizard-da-gera%C3%A7%C3%A3o-do-arquivo-do-EFD-Contribui%C3%A7%C3%B5es
---

**Ocorrência**Os parâmetros do Contabilista não ficam salvos na Wizard da geração do arquivo do EFD Contribuições.  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Causa**   
 Esse incidente ocorre, pois a parametrização do sistema está incorreta para os parâmetros do Contabilista permanecer salvo na wizard.  
  
**Solução**1. Acesse a **APSDU** na **Tabela SX1**;  
2. Realize o filtro pelo campo **X1\_GRUPO**, será apresentado as perguntas da **FSA004**;  
3. Na coluna **X1\_GSC** altere os campos de C para G. Dessa forma o conteúdo dos campos de todas as perguntas de contabilista devem dicar **X1\_GSC** = G;  
4. Realize a geração do arquivo **EFD Contribuições** e verifique a gravação das informações do contabilista.  
Observação: Após o procedimento acima, processe a apuração do **EFD Contribuição** e preencha os dados do Contabilista, gere o arquivo. Entre novamente na Wizard da geração do arquivo e verifique se os dados do contabilista foram salvos. A partir daí os dados ficarão salvos.

![dados_contabilista.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360012031592/dados_contabilista.gif)
