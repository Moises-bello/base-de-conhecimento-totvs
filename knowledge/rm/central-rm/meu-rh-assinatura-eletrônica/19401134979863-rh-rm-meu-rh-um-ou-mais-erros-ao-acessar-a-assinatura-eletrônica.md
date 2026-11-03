---
article_id: 19401134979863
category: Meu RH - Assinatura Eletrônica
content_hash: fab1a1e93ff298be13091c7532bcd99d629436038fa96f0ef882ba17ba92f0f9
fetched_at: '2026-06-28T22:47:28.741232+00:00'
product: rm
section_id: 19399655101335
source: central-rm
title: RH - RM - Meu RH - Um ou mais erros ao acessar a Assinatura Eletrônica
type: support-article
updated_at: '2025-02-11T12:56:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19401134979863-RH-RM-Meu-RH-Um-ou-mais-erros-ao-acessar-a-Assinatura-Eletr%C3%B4nica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19401164690583) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao acessar o menu Assinatura Eletrônica no Meu RH, é apresentado o erro " Um ou mais erros".  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.2302.164  
  
**Causa**O erro abaixo é apresentado devido a parametrização da integração do RM com o TAE(Totvs Assinatura Eletrônica) nos parâmetros globais etapa **Integração com Totvs Assinatura Eletrônica** estar incorreta.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19435516809879)  
  
Exemplo: URL's invalidas, espaço em branco no final da URL ou símbolos como a barra no final da URL.  
  
**Solução**  
1. Acesse sistema **RM/ aba ambiente / parâmetros / parâmetros globais / item 30 " Integração com Totvs Assinatura Eletrônica".**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19401121211671)

2. Apague toda a informação preenchida   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19401164697623)  
  
3. Reinicie todos os serviços de host do RM do servidor do portal  
[Framework - Linha RM - Frame - Reiniciar Host](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000095827-Framework-Linha-RM-Frame-Reiniciar-Host)

4. Reinicie os serviços do IIS.  
  
5. Insira as URLS abaixo nos parâmetros globais etapa 30 "**integração com Totvs Assinatura Eletrônica".**

**URL de Autenticação**: [https://totvssign.totvs.app/identityintegration](https://totvssign.staging.totvs.app/identityintegration)

**URL da API de integração**: [https://totvssign.totvs.app](https://totvssign.staging.totvs.app/)

**URL de login via formulário web**: [https://totvssign.totvs.app/webapptotvssign/#/auth/login?external=true](https://totvssign.staging.totvs.app/webapptotvssign/#/auth/login?external=true)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19420040259095)

**Importante:** Certifique-se que somente a informação das URL's estarão presentes nos campos, sem espaço em branco no final das URLS ou caracteres especiais como a /.

6. Reinicie todos os serviços de host do RM do servidor do portal

7. Reinicie os serviços do IIS.  
  
**Saiba mais:** [RH - RM - Meu RH - Integração do Meu RH com o Tae(Totvs Assinatura Eletrônica)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13740154028823-RH-RM-Meu-RH-Integra%C3%A7%C3%A3o-do-Meu-RH-com-o-Tae-Totvs-assinatura-eletr%C3%B4nica-)
