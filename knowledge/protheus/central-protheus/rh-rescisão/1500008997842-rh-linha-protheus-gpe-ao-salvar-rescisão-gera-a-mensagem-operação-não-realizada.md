---
article_id: 1500008997842
category: RH - Rescisão
content_hash: 408d0838ff5112fff9a2a5c1a145947bff64a07a22a8b29ca33051e24461dc83
fetched_at: '2026-06-28T22:43:51.095051+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao salvar rescisão gera a mensagem: Operação não
  realizada - Problemas na Integração'
type: support-article
updated_at: '2025-06-25T11:52:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008997842-RH-Linha-Protheus-GPE-Ao-salvar-rescis%C3%A3o-gera-a-mensagem-Opera%C3%A7%C3%A3o-n%C3%A3o-realizada-Problemas-na-Integra%C3%A7%C3%A3o
---

**Ocorrência**Ao salvar rescisão gera a mensagem: Operação não realizada - Problemas na Integração: Data de demissão anterior a Data da ultima Disponibilidade do Funcionário Código:.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  GPE Gestão de Pessoal – Todas as versões.  
  
**Causa**Esse incidente é ocasionado pois no módulo PIMS não é permitido demitir o funcionário em uma data menor que a data da disponibilidade mais recente.  
  
**Solução**Para que seja possível efetivar a rescisão que é bloqueada pela mensagem: Operação não realizada - Problemas na Integração: Data de demissão anterior a Data da ultima Disponibilidade do Funcionário Código:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013606142/mceclip1.png)  
  
Será necessário que o funcionário tenha disponibilidade informada na aba **Disponibilidade** do **Cadastro de Funcionário** do módulo **PIMS Multicultivos**, portanto efetue a inclusão da **Situação Ativo**. **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013604142/mceclip0.png)**Com este ajuste será possível gravar a rescisão no **Gestão de Pessoal** que efetuará a integração da Situação de desligamento do Funcionário com PIMS.  
  
**Saiba Mais:**  
Para adquirir mais conhecimento acesse o(s) *link*(s) abaixo:  
[Backoffice Protheusx PIMS MultiCultivos -PIMSConnector2.1Versão 4.0Integração Backoffice Protheusx PIMS MultiCultivos](https://tdn.totvs.com/pages/viewpage.action?pageId=269438840)
