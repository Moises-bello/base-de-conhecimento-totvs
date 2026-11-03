---
article_id: 360025728073
category: RH - Relatórios Folha
content_hash: 56d374b3b0ebe67a6bf069721f0ecf035ff7b4e56c6652dc53da2bb769e2606b
fetched_at: '2026-06-28T22:43:17.539810+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - O relatório de folha está quebrando a página e
  imprimindo em duas páginas
type: support-article
updated_at: '2025-08-01T20:32:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025728073-RH-Linha-Protheus-GPE-O-relat%C3%B3rio-de-folha-est%C3%A1-quebrando-a-p%C3%A1gina-e-imprimindo-em-duas-p%C3%A1ginas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25971319081879) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**O relatório de folha está quebrando a página e imprimindo em duas páginas, o que fazer para ajustar?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Deverá verificar o parâmetro **MV\_QBIMPFO** se está parametrizado de forma correta.  
  
**Conteúdo recomendável:**Impressoras Matriciais: Valor padrão = 58  
Impressoras Laser ou Jato de Tinta:  
Papel A4 – Retrato: Valor = 75  
Papel A4 – Paisagem: Valor = 62  
  
Os valores podem variar de acordo com o modelo de impressora, tamanhos de fonte e papel utilizados.

**1.** Acesse o C**onfigurador SIGACFG > Cadastros > Parâmetros (CFGX017)** e pesquise pelo parâmetro  **MV\_QBIMPFO:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25971340238871)  
**2.** Em Gestão de Pessoal (SIGAGPE)  acesse **Relatório > Periódicos > Folha de Pagamento (GPER040)**. Emita o relatório da Folha de Pagamento verificando se está ok.

**Saiba mais:**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
