---
article_id: 360063881573
category: Financeiro - Contas a Receber - LCDPR
content_hash: 5667fd4576f1c7e7b481ba7b17ce63970da85e09dfff2057f5fb7e298bc5c043
fetched_at: '2026-06-28T22:38:15.786236+00:00'
product: protheus
section_id: 1500001539361
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - LCDPR - Atualização
  para o correto funcionamento do lcdpr
type: support-article
updated_at: '2022-04-14T01:01:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063881573-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-LCDPR-Atualiza%C3%A7%C3%A3o-para-o-correto-funcionamento-do-lcdpr
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:02 min**

**Dúvida**Qual as atualizações necessárias para o correto funcionamento do LCDPR?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 12  
  
**Solução**Para o correto funcionamento do **LCDPR**, será necessário realizar as atualizações e processos abaixo:

Aplicar o acumulado do financeiro de acordo com seu ambiente:

12.1.23 - <https://suporte.totvs.com/portal/p/10098/download?e=749845>

12.1.25 - <https://suporte.totvs.com/portal/p/10098/download#detail/817562>

12.1.27 - <https://suporte.totvs.com/portal/p/10098/download#detail/954746>

12.1.33 - <https://suporte.totvs.com/portal/p/10098/download#detail/1039087>

Atualizar o dicionário de dados que esta dentro do acumulado do financeiro de acordo com seu ambiente.

Após atualização do dicionário de dados rodar o **UPDDISTR** para criação dos campos do **LCDPR**.

Para as versões 12.1.25 e 12.1.23 será necessário incluir as rotinas no menu via **Configurador**:

- **Cadastro de Pessoas** (FINA031)  
- **Cadastro de Imóveis** (FINA029)  
- ***Wizard* Extrator**: (FINA820)

**Saiba mais**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=520110581>
