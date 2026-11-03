---
content_hash: dd25cfabee125254aff69517c8bc8101e6c4b943efc6fcb606efdf4ab5f2bb6e
fetched_at: '2026-06-29T00:10:07.811433+00:00'
page_id: '452719444'
product: rm
source: tdn-rm
title: Gerar Lotação Tributária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719444
version: 3
---

Neste processo é possível gerar a Lotação Tributária de forma automática e em massa.

Considerações para a execução:  
    
 1.      É premissa configurar a máscara para Lotação Tributária no parametrizador. Parametrizador  
    
 2.      Será executado somente para os tomadores de serviços ativos e que tiverem o campo "Tomador de serviço folha" marcado.  
    
 3.      Para preenchimento do campo "Código Tomador", será verificado o rateio do tomador (PFRATEIOTOMADOR) de todos os funcionários.  
    
 4.      Para preenchimento da Seção, será considerada a seção do funcionário, sempre preenchendo com seção centralizadora de CNPJ e de FPAS (quando utilizar quebra no Parametrizador). Parametrizador  
    
 5.      Para preenchimento do campo "Tipo de lotação" será considerada a informação digitada no momento da execução do processo.  
    
 6.      Na seleção de coligadas, serão apresentadas somente as coligadas que utilizam tomador de serviço.  
    
 7.      A cada execução do processo o sistema inclui somente as lotações tributárias não existentes.  
    
 8.      Será incluído um registro para cada filial que possua funcionários alocados no tomador de serviço.  
    
 9.      Sempre marcará o campo "Considera dados da seção**".**  
    
 10.   Para todas as seções centralizadoras de CNPJ e de FPAS o sistema inseri uma Lotação Tributária com o tomador empresa informado no parametrizador.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Lotação Tributária
