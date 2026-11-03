---
article_id: 360028449411
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: a49e40f93d71e77fac27d9bbd77449d14d688e02a18ffeb3b0de550006b6282d
fetched_at: '2026-06-28T22:42:05.342845+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  Código de Natureza na Gravação dos títulos da Apuração '
type: support-article
updated_at: '2022-08-31T12:57:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028449411-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-C%C3%B3digo-de-Natureza-na-Grava%C3%A7%C3%A3o-dos-t%C3%ADtulos-da-Apura%C3%A7%C3%A3o
---

**Dúvida**  
Quais parâmetros devo configurar para configuração da gravação dos títulos da apuração EFD Contribuições?  
  
**Ambiente**  
Protheus – Livros Fiscias – A partir da versão 11.80]  
  
**Solução**

**Código de Natureza na Gravação dos títulos da Apuração**  
  
O código da Natureza Financeira (SED) a ser gravada nos títulos no Contas a Pagar, poderão ser informados através dos parâmetros:  
  
**MV\_PISAPC** - Informe a natureza a ser considerada para o título do PIS no regime cumulativo. Se o parâmetro estiver em branco, é considerado o conteúdo do parâmetro MV\_PISNAT.  
  
**MV\_PISAPNC** - Informe a natureza a ser considerada para o título do PIS no regime não cumulativo. Se o parâmetro estiver em branco, é considerado o conteúdo do parâmetro MV\_PISNAT.  
  
**MV\_COFAPC** - Informe a natureza a ser considerada para o título da COFINS no regime cumulativo. Se o parâmetro estiver em branco, é considerado o conteúdo do parâmetro MV\_COFINS  
  
**MV\_COFAPNC** - Informe a natureza a ser considerada para o título da COFINS no regime não cumulativo. Se o parâmetro estiver em branco, é considerado o conteúdo do parâmetro MV\_COFINS  
  
Casos estes parâmetros acima não estejam preenchidos, a rotina irá considerar então os parâmetros MV\_PISNAT e MV\_COFINS para obter a Natureza Financeira para PIS e COFINS respectivamente.

**Exclusão dos Títulos gerados no Financeiro através da apuração da rotina FISA001 - EFD Contribuições:**

Para excluir os títulos gerados no Financeiro através da rotina FISA001 - EFD Contribuições, basta refazer a apuração com a pergunta "Gera Titulo?" = "Não".
