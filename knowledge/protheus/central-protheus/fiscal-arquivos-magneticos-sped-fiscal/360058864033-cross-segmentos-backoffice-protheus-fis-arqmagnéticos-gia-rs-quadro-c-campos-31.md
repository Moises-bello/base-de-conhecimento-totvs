---
article_id: 360058864033
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 84862be343e263f4c72e754fd3dc6bb37644ea184b4f93b674bcfc7a22310f01
fetched_at: '2026-06-28T22:42:02.678675+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GIA RS - Quadro
  C, campos 31- Faturamento, 32 - Número de empregados no último dia do mês e 33-
  Valor da folha de salários
type: support-article
updated_at: '2022-08-18T17:22:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058864033-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GIA-RS-Quadro-C-campos-31-Faturamento-32-N%C3%BAmero-de-empregados-no-%C3%BAltimo-dia-do-m%C3%AAs-e-33-Valor-da-folha-de-sal%C3%A1rios
---

**Dúvida**Qual a configuração para escriturar no arquivo EFD ICMS/IPI no registro E115 as informações do Quadro C, campos 31- Faturamento, 32 - Número de empregados no último dia do mês e 33- Valor da folha de salários da GIA/RS.

**Ambiente**

Microsiga Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**As informações referente aos  campos 31- Faturamento, 32 - Número de empregados no último dia do mês e 33- Valor da folha de salários da GIA/RS deve ser incluídas na rotina MATA017.

-> Livros Fiscais/Atualização/SPED/Inf. Adic. Da Apur  
  
Utilizando para cada  campo o seu respectivo Código de Lançamento e valor.  
RS000031|"Quadro C" - "Faturamento"  
RS000032|"Quadro C" - "Número de empregados no último dia do mês"  
RS000033|"Quadro C" - "Valor da folha de salários"

Informações adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=286498628>
