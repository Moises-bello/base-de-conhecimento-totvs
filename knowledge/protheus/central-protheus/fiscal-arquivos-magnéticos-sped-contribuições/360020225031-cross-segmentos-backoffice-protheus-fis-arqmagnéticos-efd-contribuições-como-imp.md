---
article_id: 360020225031
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: a9d9bfac5c599cd17770dc35da0dc83c5d4c84803c612868cbee56a389c62532
fetched_at: '2026-06-28T22:42:05.144188+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Como importar no sistema as tabelas da Natureza da Receita  (4.3.9, 4.3.10, 4.3.11,
  4.3.12, 4.3.13, 4.3.14, 4.3.15, 4.3.16, 4.3.17, 7.1.1, 7.1.2, 7.1.3* e 7.1.4*)
type: support-article
updated_at: '2023-01-04T13:05:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020225031-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Como-importar-no-sistema-as-tabelas-da-Natureza-da-Receita-4-3-9-4-3-10-4-3-11-4-3-12-4-3-13-4-3-14-4-3-15-4-3-16-4-3-17-7-1-1-7-1-2-7-1-3-e-7-1-4
---

**Dúvida**Como importar no sistema as Tabelas da Natureza da Receita (4.3.9, 4.3.10, 4.3.11, 4.3.12, 4.3.13, 4.3.14, 4.3.15, 4.3.16, 4.3.17, 7.1.1, 7.1.2, 7.1.3\* e 7.1.4\*)?  
  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1. Realize o download das tabelas de Natureza da Receita em: <http://sped.rfb.gov.br/pasta/show/1545>

![receit.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015949532/receit.png)  
  
  
![receita2.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015993311/receita2.JPG)  
  
  
  
2. Após baixar o arquivo .\*txt é necessário renomear para a seguinte estrutura (exatamente com os nomes abaixo):  
  
Arquivo txt da tabela 4.3.10 para “**TABELA4310.TXT**”  
Arquivo txt da tabela 4.3.11 para “**TABELA4311.TXT**”  
Arquivo txt da tabela 4.3.12 para “**TABELA4312.TXT**”  
Arquivo txt da tabela 4.3.13 para “**TABELA4313.TXT**”  
Arquivo txt da tabela 4.3.14 para “**TABELA4314.TXT**”  
Arquivo txt da tabela 4.3.15 para “**TABELA4315.TXT**”  
Arquivo txt da tabela 4.3.16 para “**TABELA4316.TXT**”  
Arquivo txt da tabela 4.3.17 para “**TABELA4317.TXT**”  
Arquivo txt da tabela 4.3.9   para “**TABELA439.TXT**”  
Arquivo txt da tabela 5.1.1   para “**TABELA511.TXT**”  
Arquivo txt da tabela 7.1.1   para “**TABELA711.TXT**”  
Arquivo txt da tabela 7.1.2   para “**TABELA712.TXT**”  
  
Devido as tabelas 7.1.3 e 7.1.4 serem dividas por grupos deverão ser renomeadas da seguinte maneira:  
  
Arquivo txt da tabela 7.1.3 para “**TABELA713GRXXX.TXT**”\*, onde **XXX** refere-se ao Grupo a ser importado. Ex.: **TABELA713GR100.TXT / TABELA713GR200.TXT ... etc.**Arquivo txt da tabela 7.1.4 para 7.1.4 para “**TABELA714GRXXX.TXT**”\*,onde **XXX** refere-se ao Grupo a ser importado. Ex.: **TABELA714GR000.TXT / TABELA714GR100.TXT ... etc.****Depois, salve o arquivo na pasta ARQSPED, que deve ser criada manualmente dentro da pasta PROTHEUS\_DATA\SYSTEM;**3. Entre na rotina Apuração EFD Contribuições(FISA001) >> Importação Código EFD(FISA005) >> Opção 1. Natureza Rec. >> Outras Ações >> Importar TXT.

Obs.: A importação através da execução do Update (IMPSPED) - este processo foi **DESCONTINUADO**.

Obs.: A tabela que será atualizada no sistema recebendo os códigos de atividade é a **tabela CCZ**.
