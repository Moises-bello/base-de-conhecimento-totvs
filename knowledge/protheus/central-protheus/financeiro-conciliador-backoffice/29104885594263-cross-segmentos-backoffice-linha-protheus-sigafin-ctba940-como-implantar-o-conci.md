---
article_id: 29104885594263
category: Financeiro - Conciliador Backoffice
content_hash: 75a1f893ff1f81307ded831721365f599f37f626476dc52629fd2efb77b29b5d
fetched_at: '2026-06-28T22:37:47.171457+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Como implantar
  o Conciliador Backoffice
type: support-article
updated_at: '2025-09-18T15:08:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29104885594263-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Como-implantar-o-Conciliador-Backoffice
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29104885562647) Tempo aproximado para leitura: **00:08 min****Dúvida**Como atualizar o sistema para acessar a nova rotina do Conciliador Backoffice?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.2210

**Importante**

```
Requisitos mínimos  
  
DbAccess versão: 21.1.1.8.  
Lib versão: 20220725.   
Atualizações CTB 12.1.33 a partir de 26/08/2022  
Utilizar escala de 100% no monitor   
(escalas diferentes não são recomendadas e poderão ocasionar alterações na tela).
```

**Solução:**Para solucionar essa dúvida, realize os seguintes passos:

**1.** **Para a utilização do conciliador, é necessária a ativação da porta multi protocolo no appserver.ini do seu ambiente Protheus.**

Na seção GENERAL, deve-se incluir a chave **“App\_Environment”**, cujo valor deve ser o nome do ambiente que os serviços rodarão.   
Na seção DRIVERS, deve-se habilitar a porta **multiprotocolo** na chave **“MultiProtocolPort”** com o valor = **1**.  
Por padrão a conexão SSL está ativa na porta **multiprotocolo**, os detalhes das configurações estão disponíveis na documentação **Application Server - Porta Multiprotocolo**. Para desabilitar a conexão por **SSL** é necessário informar a chave **“MultiProtocolPortSecure = 0”**  
Para mais informações sobre essa configuração acesse a página **Application Server - Porta Multiprotocolo**.

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29104924202263)

**2.** **Aplicação do backoffice e rodar o UPDDISTR**

* [Cross Segmento Protheus - Backoffice Linha Protheus - SIGAFIN - Atualização do Ambiente Modulo 06 Financeiro Acumulado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005363562-Cross-Segmento-Protheus-Backoffice-Linha-Protheus-SIGAFIN-Atualiza%C3%A7%C3%A3o-do-Ambiente-Modulo-06-Financeiro-Acumulado?source=search)
* [Executar UPDDISTR](https://tdn.totvs.com/display/public/framework/Upgrade+de+Release+do+Protheus+12)
* [Download backoffice 12.1.2310](https://suporte.totvs.com/portal/p/10098/download?e=1123867)
* [Download backoffice 12.1.2410](https://suporte.totvs.com/portal/p/10098/download?e=1182881)

Para simplificar a configuração inicial da rotina de conciliação, um assistente foi criado para ajudar na adaptação das estruturas das tabelas empregadas neste procedimento.

Adicionalmente, esta ferramenta permitirá a inserção inicial dos novos dados nos registros já existentes no sistema **(registros legados**). Assim, será possível aplicar a rotina de conciliação nos dados antigos do PROTHEUS.

**3.** Habilitar o parâmetro **MV\_PRJOVER** com o valor **T**.

**4.** Para executar o passo a seguir, **usuário administrador** deverá conter uma **senha cadastrada**, caso contrário não conseguirá executar o passo a seguir.

**5. Wizard WIZARDUUID**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - WIZARD de configuração do Novo Conciliador Backoffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29106222860567-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-WIZARD-de-configura%C3%A7%C3%A3o-do-Novo-Conciliador-Backoffice)

**Saiba mais**

[Conciliador Backoffice - Configuração e Instalação](https://tdn.totvs.com.br/pages/releaseview.action?pageId=638741736)

[Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Conciliação Automática no novo Conciliador Backoffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28116821508759-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Concilia%C3%A7%C3%A3o-Autom%C3%A1tica-no-novo-Conciliador-Backoffice)

[Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Conciliação Manual no novo Conciliador Backoffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28113459370903-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Concilia%C3%A7%C3%A3o-Manual-no-novo-Conciliador-Backoffice)
