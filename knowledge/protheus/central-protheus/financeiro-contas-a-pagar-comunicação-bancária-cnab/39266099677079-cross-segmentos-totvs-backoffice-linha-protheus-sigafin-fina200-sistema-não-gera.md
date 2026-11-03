---
article_id: 39266099677079
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: bb37f921e095744c11f1ae15582c2dbfd2a9f6ac29fcfeae8f1973baed27d9dc
fetched_at: '2026-06-28T22:37:55.134620+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - SIGAFIN - FINA200 - Sistema
  não gera arquivo de remessa
type: support-article
updated_at: '2026-03-25T20:18:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39266099677079-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA200-Sistema-n%C3%A3o-gera-arquivo-de-remessa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39266099659927) Tempo aproximado para leitura: 00**:05:00 min**  
  
**Ocorrência**  
Ao executar a rotina para a geração do arquivo de remessa no módulo Financeiro via WebApp, o processamento é concluído, porém o arquivo físico não é gerado ou não é salvo no diretório da máquina local do usuário.

Ambiente:  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro (SIGAFIN) - Todas as versões.

**Solução:**

Esse comportamento ocorre quando o **Web Agent** (Agente Local) não está habilitado ou está configurado incorretamente no ambiente WebApp. O Agente Local é o componente responsável por permitir que o Protheus executado via navegador (WebApp) interaja com o sistema operacional do usuário para salvar arquivos físicos, como a remessa bancária, diretamente na máquina local.

Para solucionar a ocorrência, é necessário habilitar o Agente Local nas configurações de acesso do WebApp.

**Passos:**

 Siga as instruções abaixo para habilitar o componente e permitir a geração do arquivo:

1. Acesse a tela inicial de abertura/login do seu **WebApp** do Protheus.
2. Localize e clique no botão de **Engrenagem** (Configurações) disponível na interface inicial.
3. No menu apresentado, clique na opção **"Habilita/Desabilita o Agente Local"**.
4. Confirme a habilitação do agente.
5. Acesse o sistema novamente, execute a rotina de remessa no SIGAFIN e valide se o arquivo foi salvo com sucesso no diretório de destino.

**Saiba Mais:**

[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Como habilitar o agente local no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33724882611991-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-habilitar-o-agente-local-no-Protheus)
