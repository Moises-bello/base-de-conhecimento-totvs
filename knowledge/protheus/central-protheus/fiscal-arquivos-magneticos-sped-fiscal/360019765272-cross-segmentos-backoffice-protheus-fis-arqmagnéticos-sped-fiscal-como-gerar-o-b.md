---
article_id: 360019765272
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: c6c9710419b2f2b6d0ade2545795066773e2f2c7f26d9989cddc466ebff5c386
fetched_at: '2026-06-28T22:42:02.713528+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  - Como gerar o bloco H do Sped Fiscal?
type: support-article
updated_at: '2025-01-08T17:45:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019765272-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Como-gerar-o-bloco-H-do-Sped-Fiscal
---

**Dúvida** Como gerar o **bloco H - Inventário Físico** do **Sped Fiscal**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**O **bloco H - Inventário Físico** destina-se a informar o **inventário físico** do estabelecimento, nos casos e prazos previstos na legislação pertinente. Para que o Protheus gere o **bloco H** no **arquivo txt do Sped Fiscal** é preciso realizar o seguinte procedimento:  
  
**1.** Certifique-se que no ambiente estão aplicados os pacotes acumulados tanto do **Módulo Estoque/ Custos** quanto do **Módulo Livros Fiscais**, conforme abaixo, pois, a atualização destes pacotes garantirão que todos os fontes responsáveis pela geração do **P7** e do **SPED Fiscal** estejam atualizados de maneira equalizada:

* **[Pacote Acumulado Estoque/Custos](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/EST_expedicao_continua)**

**Acumulado Fiscal:**

* <https://tdn.totvs.com/pages/releaseview.action?pageId=525823851>

**2.** No **módulo 04 - Estoque/Custos,** através da rotina **Registro de Inventário Modelo P7 - MATR460**, gere o relatório referente ao exercício à ser entregue.

Para que as informações sejam geradas corretamente as perguntas na *wizard* de geração do relatório devem estar conforme abaixo:

**a) Data de fechamento** - Data de quando o inventário foi fechado

**Exemplo**: 31/12/2022

**b)** **Gerar arquivo de Exportação -** Sim

**c)** **Arquivo de exportação SPED FISCAL** - Data de fechamento do inventário no formato **ano/mês/dia**

**Exemplo:** 20221231  
  
**3** . Com a geração do relatório, será criada no **banco de dados tabela** com todas as informações do relatório **Registro de Inventário Modelo P7.**

A nomenclatura dessa tabela tem o  seguinte formato:  **H\_+ data de fechamento no formato ano, mês e dia +grupo +filial**, conforme exemplo abaixo:

**Exemplo: H\_20221231+GRUPO+FILIAL**

![BLOCO_H_-_ARQUIVO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360015671351)

**Importante:**

O **Sped Fiscal** só será gerado com os dados do **inventário no bloco H,** após a gravação da tabela em questão. Caso a mesma não seja gerada no **banco de dados**, é preciso avaliar o motivo com o suporte **Protheus Estoque/Custos.**  
  
**4.** Com a tabela **H\_** gerada no **banco de dados**, acesse o **Módulo 09 - Livros Fiscais** e gere o **Sped Fiscal,** se certificando que as perguntas na *wizard* de geração do **arquivo txt**, estejam conforme abaixo:

**a) Gera Inventário -** Sim  
**b) Data de fechamento do estoque** - Data do fechamento de estoque.

Exemplo: 31/12/2022  
**c) Motivo do Inventário -**  01-Final do Período.  
  
**5.** Abaixo exemplo didático do processo completo:  
![BLOCO_H.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360015671371)

Dúvidas sobre **H020** - **Campo 2** (**CST\_ICMS**), seguir o *link* abaixo:

[MP - FIS - SPED FISCAL - Como Gerar o Campo 02 - CST\_ICMS no Registro H020.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026469571-MP-FIS-SPED-FISCAL-Como-Gerar-o-Campo-02-CST-ICMS-no-Registro-H020-?source=search)

Informações adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=238035285#FIS0009_Manual_Utiliza%C3%A7%C3%A3o_SPEDFISCAL-REGISTROH010:INVENT%C3%81RIO>.
