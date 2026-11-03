---
article_id: 28061399543063
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: ac7c2f8ec682c3362d7bb2f37624b7ee3d2b4450aca9fea247c7a77085be9ef8
fetched_at: '2026-06-28T22:37:56.542999+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos > TOTVS BackOffice (Linha Protheus) > Financeiro > FINA205
  - FINA435 - Enviar E-mail das baixas realizadas ou inconsistências
type: support-article
updated_at: '2024-11-26T20:32:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28061399543063-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-Financeiro-FINA205-FINA435-Enviar-E-mail-das-baixas-realizadas-ou-inconsist%C3%AAncias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28061399498519) Tempo aproximado para leitura: **00:10:00 min****Dúvida**Como parametrizar o ambiente para enviar as baixas ou inconsistências por e-mail via CNAB **(Recebimentos e Pagamentos)?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução** **1 - É necessário ter um ambiente preparado para envio de e-mails, consulte aqui a documentação:**

Fazer a configuração do servidor de e-mail no Protheus, (**CFGSETMAIL**) caso não tenha configurado. **Mais detalhes podem ser encontrados em:** [Configuração do Servidor de E-mail/Proxy (CFGSETMAIL - SIGACFG)](https://tdn.totvs.com/pages/viewpage.action?pageId=306857939).

**2. Configurar um ou mais e-mail no paranefro MV\_RETMAIL**  
O parâmetro **MV\_RETMAIL** pode ser configurado com um ou mais endereços de e-mail, separados por ponto e vírgula. O sistema enviará um e-mail contendo um resumo dos títulos com eventuais inconsistências em anexo. Caso o parâmetro não esteja corretamente preenchido ou esteja em branco, nenhum e-mail ou resumo será enviado ou registrado.

**3. Configurar corretamente o parâmetro MV\_RELT**

O parâmetro **MV\_RELT** especifica o diretório de destino onde os relatórios são gravados quando a opção de impressão em disco é utilizada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28061399499927)

**4. Adicionar o arquivo printer.exe, localizado na pasta do SmartClient, e incluir a pasta do Appserver.**

Acesse a pasta do **SmartClient** e copie o arquivo **Printer.exe**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28061383102871)**

Cole o arquivo **Printer.exe** na pasta do **Appserver**  
  
**Saiba mais**  
[Configuração do Retorno de CNAB Automático (FINA205/FINA435)](https://tdn.totvs.com/pages/releaseview.action?pageId=471926159)[Parâmetro MV\_RELT](https://tdn.totvs.com/pages/viewpage.action?pageId=872680094)[Configuração do Servidor de E-mail/Proxy (CFGSETMAIL - SIGACFG)](https://tdn.totvs.com/pages/viewpage.action?pageId=306857939)
