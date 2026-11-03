---
article_id: 6420934518935
category: Escrita Fiscal - Error.log
content_hash: 374e2d9fb16c5da8394bdcda3a7095d2b6a4066892b9183c4cdc75e3f9bcc0f8
fetched_at: '2026-06-28T22:39:32.857534+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - MATRAPR - Como Excluir
  do RPO Padrão // Alerta ao Compilar :One or more files have warnings and/or errors.
  See problems and logs for details
type: support-article
updated_at: '2024-10-02T19:48:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6420934518935-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-MATRAPR-Como-Excluir-do-RPO-Padr%C3%A3o-Alerta-ao-Compilar-One-or-more-files-have-warnings-and-or-errors-See-problems-and-logs-for-details
---

**Dúvida**Como Excluir do RPO Padrão // Alerta ao compilar :One or more files have warnings and/or errors. See problems and logs for details, causando a impressão de impossibilidade de compilaçãoem **RPO**padrão.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -Livros Fiscais - release 12.1.33  
  
**Solução**

* A remoção do **MATRAPR** está em andamento,  mas apenas no próximo release **12.1.2210**, o fonte deixará de compor o **RPO**padrão, continuando apenas em **RDMAKE.**
* Em testes realizados em base padrão, a mensagem de alerta não impede a compilação, apenas avisa sobre a existência do **MATRAPR**no **RPO**padrão.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6420869519767/mceclip0.png)

* A mensagem de alerta e exibida porque o **RDMAKE**ainda está contido no **RPO**padrão e sempre será preferência do sistema. Para não ter este incidente, basta excluir o **RDMAKE** do **RPO** padrão e depois compilar a sua versão do **RDMAKE.**
* Para excluir o **RDMAKE**do **RPO**padrão, basta selecionar o arquivo .prx pelo **IDE,**clicar com o botão direito e selecionar a opção e**xcluir arquivo/recurso do RPO**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6420901590935/mceclip1.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6420882672151/mceclip3.png)

## 

## **ASSUNTOS RELACIONADOS**

* [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Relatório MATRAPR em branco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041335034--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Relat%C3%B3rio-MATRAPR-em-branco?source=search)
* [RpoCustom](https://tdn.engpro.totvs.com.br/display/tec/RpoCustom)
