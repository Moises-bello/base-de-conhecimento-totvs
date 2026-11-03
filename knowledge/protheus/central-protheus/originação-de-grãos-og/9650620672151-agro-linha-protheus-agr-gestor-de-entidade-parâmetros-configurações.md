---
article_id: 9650620672151
category: Originação de Grãos (OG)
content_hash: 514d5133b08c0ad1fb2ecd57eaa4a86080dcddb10312618f2b27a624b97997ad
fetched_at: '2026-06-28T22:45:39.562075+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Gestor de Entidade - Parâmetros - Configurações
type: support-article
updated_at: '2025-06-24T19:16:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9650620672151-Agro-Linha-Protheus-AGR-Gestor-de-Entidade-Par%C3%A2metros-Configura%C3%A7%C3%B5es
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20312707149719)** Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Quais são os parâmetros para alterar ou configurar **Gestor de Entidade**? **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12 **Solução**O  conteúdo dos parâmetros pode ser alterado na rotina **Parâmetros** do módulo **Configurador:**

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Descrição** | **Conteúdo padrão** |
| [MV\_AGRO002](https://tdn.totvs.com/pages/viewpage.action?pageId=370616326) | Utiliza novo modelo de comercialização. | .F. |
| [MV\_AGRO016](https://tdn.totvs.com/pages/viewpage.action?pageId=353280735) | Grupo de Aprovação padrão utilizado nos registros de negócios de cancelamento | [Vazio] |
| [MV\_AGRO031](https://tdn.totvs.com/pages/viewpage.action?pageId=384574769) | Prefixo utilizado para geração da Nota de Crédito a Cliente (NCC) através do controle de alçadas. | NCC |
| [MV\_ITMCLVL](https://tdn.totvs.com/pages/viewpage.action?pageId=233760425) | Informe 1 para utilização do Item Contábil e Classe de valor, 2 para não utilizar, ou 3 para utilizar item/classe sem obrigatoriedade de ambos. | 2 |
| [MV\_AGRO032](https://tdn.totvs.com/pages/viewpage.action?pageId=515297111) | Prefixo para gerar NDC de Contratos | NDC |
| [MV\_OGDECPS](https://tdn.totvs.com/pages/viewpage.action?pageId=268596595) | Determina a quantidade de decimais no peso romaneios | 0 |
| [MV\_OGPICPS](https://tdn.totvs.com/pages/viewpage.action?pageId=268596660) | Define o formato para campos de peso no romaneio. | @E 999,999,999 |
| [MV\_OGCTRMV](https://tdn.totvs.com/pages/viewpage.action?pageId=268595064) | Tipos de Movimentos de Processos: Transferência Simples (TRFS), Transferência Múltipla (TRFM) | TRFS|;TRFM|; |
| [MV\_AGRO208](https://tdn.totvs.com/pages/viewpage.action?pageId=471953003) | Realiza ajuste fino no calculo de complemento. | .F. |
| [MV\_OGASERS](https://tdn.totvs.com/pages/viewpage.action?pageId=248582943) | Define a série padrão a ser utilizada na geração dos documentos de saída. | [Vazio] |
| [MV\_CONDPAD](https://tdn.totvs.com/pages/viewpage.action?pageId=268594909) | Condição de Pagamento Padrão. | [Vazio] |
| [MV\_OGASERE](https://tdn.totvs.com/pages/viewpage.action?pageId=248583008) | Define a série padrão a ser utilizada na geração dos documentos de entrada. | [Vazio] |
