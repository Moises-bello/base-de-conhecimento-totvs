---
article_id: 360025752011
category: NFe - Nota Fiscal Eletrônica
content_hash: 87a8583d6d969360ae28dc49d4623bcebb0cf30c7a1531b1841537004bab58aa
fetched_at: '2026-06-28T22:40:00.173385+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: '   Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 971 Rejeição:
  IE inválida [local de retirada/entrega]'
type: support-article
updated_at: '2021-10-08T17:21:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025752011--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-971-Rejei%C3%A7%C3%A3o-IE-inv%C3%A1lida-local-de-retirada-entrega
---

**Dúvida**Como solucionar a rejeição 971 Rejeição: IE inválida [local de retirada/entrega] ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Na **NT 2018.005 foram criadas** novas TAGs para o grupo de **retirada/entrega.**

 O **IE**é opcional para o grupo de **entrega** e de **retirada** no XML, porém se gerado passou a ser validado.

O IE deve ser da mesma UF do **CCC e deve estar vinculado ao CPNJ que consta no CCC.**

Se houver dúvidas do **IE, CNPJ e UF** consultar no link abaixo:

* **Cadastro Centralizado de Contribuinte (CCC):**

**<https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>**

* Verificar no Protheus através dos campos:

**A1\_INSCR** ou **A2\_INSCR**

* Vincular o cadastro de cliente aos campos:  
    
  + **Retirada:**  
  C5\_CLIRET e C5\_LOJARET  
    
  + **Entrega:**  
  C5\_CLIENT  
    
  Além disso será necessário verificar a configuração do parâmetro abaixo:  
    

  ```
  MV_NFEDEST
  ```

  1. *Criação*de **Parâmetros** no arquivo **SX6 – Parâmetros**:

  |  |  |
  | --- | --- |
  | **Nome da Variável** | ``` MV_NFEDEST ``` |
  | **Tipo** | ``` Lógico ``` |
  | **Descrição** | Quando habilitado, considerar Cliente, Cli. Ent. e Cli. Ret. utilizados, para compor respectivamente as tags 'dest', 'entrega' e 'retirada' da NF-e. |
  | **Valor Padrão** | ``` .F. ``` |

  ## Procedimento para Configuração

    
  **CONFIGURAÇÃO DE PARÂMETROS**  
  No **Configurador (SIGACFG)**, acesse **Ambientes/Cadastros/Parâmetros (CFGX017)**. Configure o(s) parâmetro(s) a seguir:  

  |  |  |
  | --- | --- |
  | Itens/Pastas | Descrição |
  | **Nome:** | MV\_NFEDEST |
  | **Tipo:** | ``` Lógico ``` |
  | **Cont. Por.:** | ``` .T. ``` |
  | **Descrição:** | Quando habilitado, considerar Cliente, Cli. Ent. e Cli. Ret. utilizados, para compor respectivamente as tags 'dest', 'entrega' e 'retirada' da NF-e. |

    
    
    
  + **As configurações permanecem conforme os links abaixo:**  
    
  <http://tdn.totvs.com/display/public/PROT/NfeSefaz+-+Cliente+de+Retirada+e+Cliente+de+Entrega>  
    
  <http://tdn.totvs.com/pages/releaseview.action?pageId=271850728>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024533651/mceclip1.png)

* **Cadastro de Cliente:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029024872/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029024811/mceclip1.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030325592/mceclip0.png)

* **Cadastro de Fornecedor:**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029029332/mceclip4.png)**

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029028451/mceclip5.png)**

**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029028531/mceclip6.png)**

* **Validação da Sefaz:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024522452/mceclip0.png)**

* **Conforme o Cronograma da Sefaz já entrou em homologação:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027632952/mceclip0.png)
