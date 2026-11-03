---
article_id: 115013241727
category: Gestão de Pesquisa e Resultado (GPR)
content_hash: 84caf868221f874125fae6331e1fe99eacac205dc9c976e7b7e9da63ca2db41f
fetched_at: '2026-06-28T22:38:22.156988+00:00'
product: protheus
section_id: 1500001539461
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAGPR - Erro no Preview
  da Pesquisa
type: support-article
updated_at: '2023-08-17T14:27:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013241727-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAGPR-Erro-no-Preview-da-Pesquisa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16834446548759) Tempo aproximado para leitura: **00:05:00 min**

**Ocorrência**  
Erro ao selecionar o Preview da pesquisa

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.

  
**Causa**

Erro gerado no preview da pesquisa:

"O Windows não pode encontrar  
w\_pgpr000.apw?cID=DAPAgQZiGAwDwIEGYBgMA8CBBmAYDAPAgQZgGAwDxIEGDAPAgQZimJAz  
Certifique-se de que o nome foi digitado corretamente e tente novamente."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16833433506327)

A mensagem ocorre sempre que for efetuada a configuração para o uso da pesquisa do **SIGAGPR** (Gestão de Pesquisa e Resultado), e no **browse das rotinas** de cadastro, na opção "**Outras Ações**", selecionar a opção "**Preview**", que trata a visualização de uma prévia da pesquisa configurada.  
  
**Solução**

Para que esta visualização **seja possível**, é necessário que o **Web Service** e **Portal** sejam configurados, via **SRVWIZARD** - Assistente de configuração do servidor.  
Caso já esteja configurado é  preciso validar se na seção "**Environment**" do "**appserver.ini**", se existe a Tag **UrlGpr**, pois esta Tag identificará o endereço do servidor e porta que a URL está configurada, e em conjunto com as configurações do módulo, apresentará corretamente a Pesquisa **Preview**.

**Este é um modelo de como o "Environment" deve estar configurado:**

```
[PORTALGPR] ---> environment  
SourcePath=C:\P11.5\Protheus11\Protheus\apo\Portal  
RootPath=C:\P11.5\Protheus_Data  
StartPath=\system\  
x2_path=  
RpoDb=SQL  
RpoLanguage=Portuguese  
RpoVersion=110  
LocalFiles=ads  
PROTHEUSONLY=0  
Panelserver=LOCALHOST  
Panelport=1234  
HHTRIGGERON=1  
HHTriggerInterval=1  
specialkey=TOP  
TopDatabase=MSSQL7  
TopServer=localhost   
TOPALIAS=P11R5  
UrlGpr=http://localhost:90/gpr/ ---> tag UrlGpr  
REGIONALLANGUAGE=BRA
```

**SRVWIZARD** **- Assistente de configuração do servidor:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16834008251543)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16834327350935)  
  
Esta é uma configuração de **caráter técnico**, deverá ser efetuado por um **analista de infra-estrutura**. Em caso de dúvidas, acionar a equipe de Framework para auxiliar.

**Saiba Mais**

* **[Nota sobre o Preview da Pesquisa no Gestão de Pesquisa e Resultado](https://tdn.totvs.com/x/EsEGEQ)**
* **[Preview (GPRA010 - SIGAGPR)](https://tdn.totvs.com/x/ZIryHQ)**
* **[Preview (GPRA020 - SIGAGPR)](https://tdn.totvs.com/x/m_7jHQ)**
* **[Preview (GPRA030 - SIGAGPR)](https://tdn.totvs.com/x/Q7aaFQ)**
