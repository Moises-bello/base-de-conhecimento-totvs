---
article_id: 27091607770775
category: GPE - eSocial - Processo Trabalhista
content_hash: 6191681e697fa6b64af36e7dbe167ccf6288918f5cf01478304d7556bb9dfda6
fetched_at: '2026-06-28T22:45:00.491159+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Como ativar a porta multi protocolo utilizando
  Middleware
type: support-article
updated_at: '2024-10-15T20:42:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27091607770775-RH-Linha-Protheus-GPE-eSocial-Como-ativar-a-porta-multi-protocolo-utilizando-Middleware
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27091607747351) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como ativar a porta multi protocolo utilizando Middleware?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**1 - Para ativar a porta multi protocolo, precisa estar com o GPE atualizado, de acordo com a pagina de [eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais);  
  
***ATENÇÃO:** CLIENTES QUE POSSUÍREM **SLAVES,** AS PARAMETRIZAÇÕES CONFORME ORIENTAÇÃO ABAIXO **DEVERÁ SER APLICADA** NOS ARQUIVOS DE CONFIGURAÇÃO **PARA CADA SLAVE**.*2 - Acesse a pasta de instalação do sistema e localize a pasta BIN/APPSERVER e abra o arquivo APPSERVER.INI;  
  
3 - Na seção [DRIVERS] adicione os parâmetros:

MULTIPROTOCOLPORT=1  
MULTIPROTOCOLPORTSECURE=0

**Exemplo:**

```
[DRIVERS]  
ACTIVE=TCP  
MULTIPROTOCOLPORT=1  
MULTIPROTOCOLPORTSECURE=0
```

4 - Na seção [GENERAL] adicionar o parâmetro:  
APP\_ENVIRONMENT=nome\_do\_ambiente

**\*\* Não é possível utilizar mais de um ambiente na porta multi protocolo, no mesmo appserver.ini**

\*\* Inserir parâmetro para apenas um ambiente.  
Após localização do nome do ambiente adicione no parâmetro, exemplo:

**Correto:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27091587382295)

**Errado:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27091607752471)

Após localização do nome do ambiente adicione no parâmetro:

5 - Reinicie os serviços do TAF (DBACCESS, APPSERVER e WS) e acesse o ambiente.  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[Artigos RH Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971467-RH-Processos-Trabalhistas)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".*
