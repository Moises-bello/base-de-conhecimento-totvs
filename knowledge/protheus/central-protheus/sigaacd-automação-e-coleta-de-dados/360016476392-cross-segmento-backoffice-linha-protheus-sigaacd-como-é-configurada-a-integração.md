---
article_id: 360016476392
category: SIGAACD - Automação e Coleta de Dados
content_hash: 4211befb7aeabebf08b280673864089fad34b7f6c5dc79273ebb6d6130aabbc9
fetched_at: '2026-06-28T22:39:10.961886+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como é configurada
  a integração do SIGAACD?
type: support-article
updated_at: '2026-06-03T17:04:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016476392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-%C3%A9-configurada-a-integra%C3%A7%C3%A3o-do-SIGAACD
---

O artigo descreve a configuração para integração do SIGAACD no TOTVS Backoffice (Linha Protheus). A solução inclui um vídeo instrutivo sobre a parametrização necessária. Destaca o aplicativo "Meu Coletor de Dados", que transforma celulares em coletores de dados para processos como conferência e inventário, oferecendo benefícios como funcionamento offline e aumento de produtividade. Para usar o SIGAACD, é necessário ajustar o arquivo appserver.ini, habilitar parâmetros específicos e cadastrar operadores na rotina ACDA010. O Módulo 46 (SIGAACD) é um módulo restrito para uso no APP ou via VTDEBUG, que simula um aplicativo, **não estando disponível nos menus padrões do "Protheus".** O artigo também fornece links para guias de referência e informações sobre coletores e impressoras homologadas.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33764664514711) Tempo estimado para leitura: **00:02:00 min**

**Dúvida**  
Como é realizada a configuração da integração do SIGAACD?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**  
Consulte nosso vídeo instrutivo sobre como configurar a parametrização para integração do SIGAACD:

No vídeo, mencionamos também o aplicativo "**Meu Coletor de Dados**", que auxiliará sua empresa na coleta de informações de forma ágil e prática. O aplicativo transforma um celular em um coletor de dados para acompanhamento de processos como: Conferência, Transferência entre Armazéns, Separação e Inventário.

**Confira alguns dos benefícios do Meu Coletor de Dados:**

* Multi-usuários
* Funcionamento Off-line
* Leitor via Bluetooth
* Captura pela câmera disponível para Android
* Menor custo-benefício
* Otimização de processos
* Aumento de produtividade

***Observação:***[***Clique aqui***](https://tdn.totvs.com/pages/viewpage.action?pageId=506994322) e consulte o Guia de Referência do APP Meu Coletor de Dados. O link contém todas as funcionalidades disponíveis para utilização do APP.

Para verificar se a empresa tem direito ao uso do APP Meu Coletor de Dados, recomendamos fortemente que entre em contato com o **Executivo de Soluções de Negócio da TOTVS.**

**Configurações necessárias para utilizar o SIGAACD:**

**OBSERVAÇÃO**: O Módulo 46 (SIGAACD) é um módulo restrito para uso no APP ou via VTDEBUG, que simula um aplicativo, **não estando disponível nos menus padrões do "Protheus".**

### **1° Passo - Incluir no arquivo de configuração appserver.ini as seguintes informações:**

```
[TELNET]
Enable=1 (igual a 1 está habilitando)
Environment=Ambiente (informar o nome do Ambiente)
Main=SIGAACD (informar o nome do Módulo)
Port=23 (informar uma porta que não esteja em uso)
```

***Observação:*** [***Clique aqui***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018771512?source=search) e saiba sobre a homologação de Coletores para uso com o ACD.

### **2° Passo - Habilitar os seguintes parâmetros:**

**MV\_INTACD=1**  
**MV\_CBPE001** até **MV\_CBPE023**, todos iguais a **.T.**

Informar o código de impressão cadastrado no ACDA060 nos parâmetros:   
**MV\_IACD01**, **MV\_IACD02**, **MV\_IACD03** e **MV\_IACD04**

### **3° Passo - Cadastrar o operador na rotina ACDA010**

Caso a empresa utilize impressora de etiquetas, basta compilar o RDMakes disponível conforme a linguagem da impressora.

**ZEBRA**  
**DATAMAX**  
**ELTRON**  
**INTERMEC**

RDMAKES

[*https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1152110*](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1152110)

![RDMAKES.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36969821755927)

Saiba Mais:

[Guia de Referência do Meu Coletor de Dados](https://tdn.totvs.com/pages/viewpage.action?pageId=506994322)

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[SIGAACD - Quais Coletores de Dados são homologados para uso no módulo Automação e Coleta de Dados (SIGAACD)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018771512-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Quais-Coletores-de-Dados-s%C3%A3o-homologados-para-uso-no-m%C3%B3dulo-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados-SIGAACD-?source=search)

[SIGAACD - MSCBPrinter - Modelos de impressoras homologadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020286872-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAACD-MSCBPrinter-Modelos-de-impressoras-homologadas-)
