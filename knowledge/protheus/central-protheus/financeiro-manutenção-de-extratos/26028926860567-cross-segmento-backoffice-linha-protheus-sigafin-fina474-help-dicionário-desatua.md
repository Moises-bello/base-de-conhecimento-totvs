---
article_id: 26028926860567
category: Financeiro - Manutenção de Extratos
content_hash: 315f4ae3444a9592ca1cb0d29e7572077350e9954d7408de8e0731df1b4ab31b
fetched_at: '2026-06-28T22:37:31.189385+00:00'
product: protheus
section_id: 35057672519319
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA474 - HELP Dicionário
  desatualizado
type: support-article
updated_at: '2026-01-07T14:20:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26028926860567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA474-HELP-Dicion%C3%A1rio-desatualizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26028944956567) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**

Ao entrar na rotina é apresentado o help de dicionário desatualizado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26028926842263)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA474 - Todas as versões  
  
**Solução**

Ao abrir a rotina pela primeira vez, será validado se o dicionário de dados se encontra atualizado. É necessário que todos os campos abaixo existam na base de dados:

| Campo | Quando é criado |
| --- | --- |
| EE\_EXTJOB | Ao rodar o UPDDISTR da expedição contínua mais recente do módulo Financeiro (mais informações em [Pacotes de Atualização - Financeiro - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=531017758)) |
| EE\_EXTAPI | Ao rodar o UPDDISTR da expedição contínua mais recente do módulo Financeiro (mais informações em [Pacotes de Atualização - Financeiro - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=531017758)) |
| IF\_CONTA | Ao rodar o UPDDISTR da expedição contínua mais recente do módulo Financeiro (mais informações em [Pacotes de Atualização - Financeiro - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=531017758)) |
| IG\_BCOEXT | Ao rodar o UPDDISTR da expedição contínua mais recente do módulo Financeiro (mais informações em [Pacotes de Atualização - Financeiro - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=531017758)) |
| IG\_MSUIDT | Ao rodar o UPDDISTR do dicionário gerado para a tabela SIG pela rotina **WIZARDUUID** (mais informações em [Conciliador Backoffice - Configuração e Instalação](https://tdn.totvs.com/pages/viewpage.action?pageId=638741736)) |

Caso algum desses campos não exista na base, será apresentada a mensagem abaixo:

![](https://tdn.totvs.com/download/attachments/721003882/image-2024-8-29_18-4-42.png?version=1&modificationDate=1724965490610&api=v2)

## **03.****CADASTROS NECESSÁRIOS**

Dado o arquivo de extrato bancário de exemplo "FINA474.EXT" e o arquivo de configuração correspondente "FINA474.RET".

Esta configuração pode ser desenvolvida a partir das rotinas **Conf Extrato Banc** e **Extrato Febraban** no módulo **Configurador >> Ambiente,**e a definição de qual rotina utilizar para desenvolver o layout está na estrutura do layout de banco para a conta bancária envolvida nesta operação. Para mais informações sobre layout de extrato acesse - [FIN0003\_CAUT\_Layout\_para\_Conciliacao\_Automatica](http://tdn.totvs.com.br/display/PROT/FIN0003_CAUT_Layout_para_Conciliacao_Automatica)

Alguns cadastros relevantes são:

* ### **Parâmetros de Banco (FINA130)**

Este cadastro tem como finalidade configurar os parâmetros bancários utilizados em diversas operações relacionadas a comunicação bancária.

* + Efetue o cadastro da subconta conforme os processos descritos no link abaixo:  
    [Parâmetros de Bancos - FINA130](https://tdn.totvs.com.br/pages/viewpage.action?pageId=624116777)

**Saiba mais**

[FINA474 - Manutenção de Extratos Bancários](https://tdn.totvs.com/pages/releaseview.action?pageId=721003882)
