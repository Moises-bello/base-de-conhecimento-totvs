---
article_id: 39344036902551
category: Materiais - Compras (SIGACOM)
content_hash: b484c1dfdbead97626918f26c9928f074c96ec325e4ae771e5af259e613b1df3
fetched_at: '2026-06-28T22:41:21.785021+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Falha na autenticação
  com servidor SMTP
type: support-article
updated_at: '2026-04-27T18:37:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39344036902551-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Falha-na-autentica%C3%A7%C3%A3o-com-servidor-SMTP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39344045719063) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Como corrigir o erro "Falha na autenticação com servidor SMTP" ao enviar e-mail da cotação no Novo Fluxo de Compras (PGCA010) para o fornecedor?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39344036894103)  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.2310  
  
**Solução**  
Ao tentar enviar um e-mail com o formulário de cotação para o fornecedor através do Novo Fluxo de Compras (NFC), o sistema exibe a mensagem de erro: "Falha na autenticação com servidor SMTP".

Para solucionar essa rejeição, siga as etapas de validação abaixo, em ordem:

#### **Passo 1: Atualização de Pacote (Patch) e LIB**

Para correção do problema informado, peço que por gentileza aplique o patch abaixo em seu ambiente e também realizar a atualização de sua LIB e valide se o comportamento irá persistir.  
   
A Release Oficial foi expedida e publicada na Central de Downloads. O pacote pode ser acessado no endereço abaixo:

> **Importante:** Recomendamos fortemente que você realize um backup completo e valide a aplicação primeiramente em um **ambiente de homologação/teste.**

12.1.2210:<https://r.totvs.io/p/1240523> ;  
12.1.2310:<https://r.totvs.io/p/1240524> ;  
12.1.2410:<https://r.totvs.io/p/1240521> ;  
12.1.2510:<https://r.totvs.io/p/1240522> ;  
   
- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168735)

Após atualizar, teste o envio novamente. Se o erro persistir, vá para o Passo 2.

#### **Passo 2: Validação do Parâmetro MV\_WFBRWSR**

Verifique o preenchimento do parâmetro **MV\_WFBRWSR** no Configurador (SIGACFG). Este parâmetro deve conter a URL do formulário do Workflow do Novo Fluxo de Compra.

1. Copie o link contido no conteúdo do parâmetro **MV\_WFBRWSR**.
2. Cole este link no seu navegador de internet.
3. **Validação:**

   * **Sucesso:** O link carrega corretamente no navegador, prossiga para o Passo 3.
   * **Erro:** Se o link gerar erro ao carregar, consulte a documentação de apoio: [O que fazer quando o Clique Aqui no e-mail do formulário não está habilitado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24511855484183-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-que-fazer-quando-o-Clique-Aqui-no-email-do-formul%C3%A1rio-n%C3%A3o-est%C3%A1-habilitado-Novo-Fluxo-de-Compras-NFC-PGCA010).

#### **Passo 3: Revisão das Configurações do WorkFlow**

Valide se as configurações do Workflow para o Novo Fluxo de Compras estão preenchidas corretamente no sistema. Para isso, por gentileza, consulte a documentação oficial para revisar o passo a passo da parametrização:

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como configurar o WorkFlow no Novo Fluxo de Compras - NFC (PGCA010)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19823527070871-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-configurar-o-WorkFlow-no-Novo-Fluxo-de-Compras-NFC-PGCA010)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar uma conta de e-mail para utilizar no NFC (PGCA010) ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38801704682647-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-uma-conta-de-e-mail-para-utilizar-no-NFC-PGCA010)

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como configurar o WorkFlow utilizando o e-mail dos compradores no envio dos formulários no Novo Fluxo de Compras - NFC (PGCA010)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19837259521559-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-configurar-o-WorkFlow-utilizando-o-e-mail-dos-compradores-no-envio-dos-formul%C3%A1rios-no-Novo-Fluxo-de-Compras-NFC-PGCA010)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Não foi possível autenticar no servidor SMTP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36000266177687-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-N%C3%A3o-foi-poss%C3%ADvel-autenticar-no-servidor-SMTP)

Indicamos também que assista ao WEBINAR no link abaixo para revisar todas as configurações.

[Webinar TOTVS | NFC](https://www.youtube.com/watch?v=86lRT2OmoEg)

Se as configurações estiverem corretas e o erro continuar, será necessária uma análise por parte do Suporte. Abra um ticket com a equipe de Suporte Compras e, para agilizar o atendimento, é essencial anexar as seguintes informações:

* Arquivo de **Inspetor de Objetos**.
* Print da tela de erro exibida.
* Print do conteúdo dos parâmetros de configuração de e-mail   
  ('MV\_WFDIR', 'MV\_WFDHTTP', 'MV\_WFBRWSR', 'MV\_PGCWF', 'MV\_PGCPISV', 'MV\_PGCPIPO', 'MV\_PGCSMSR', 'MV\_PGCSMPO', 'MV\_PGCTAUT','MV\_WFSNDAU','MV\_WFMLBOX')

***Saiba Mais:***

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como configurar o WorkFlow utilizando o e-mail dos compradores no envio dos formulários no Novo Fluxo de Compras - NFC (PGCA010)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19837259521559-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-configurar-o-WorkFlow-utilizando-o-e-mail-dos-compradores-no-envio-dos-formul%C3%A1rios-no-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)
