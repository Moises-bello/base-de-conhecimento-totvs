---
article_id: 39955857654295
category: Comércio Exterior - Easy Import Control - Solic. de Importação
content_hash: 8cc5106462f7f486a33f305f33c321605b40f9645492a99b262a831a35901037
fetched_at: '2026-06-28T22:39:46.701010+00:00'
product: protheus
section_id: 1500001538401
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) -  SIGAEIC  - Como utilizar
  o ponto de entrada EICPSI01 para a inclusão de Solicitação de Importação (SI)?
type: support-article
updated_at: '2026-04-23T17:13:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39955857654295-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-utilizar-o-ponto-de-entrada-EICPSI01-para-a-inclus%C3%A3o-de-Solicita%C3%A7%C3%A3o-de-Importa%C3%A7%C3%A3o-SI
---

O ponto de entrada EICPSI01 no módulo Easy Import Control (SIGAEIC) permite manipular dados ou executar rotinas customizadas durante a gravação da Solicitação de Importação (SI). A função User Function EICPSI01() captura parâmetros para validações e regras de negócio personalizadas na inclusão do registro.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39955857643671) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como utilizar o ponto de entrada EICPSI01 para a inclusão de Solicitação de Importação (SI)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - *Easy Import Control* (SIGAEIC) - A partir da versão 12.1.33

**Solução**  
  
O ponto de entrada EICPSI01 é executado durante o processo de gravação da Solicitação de Importação (SI) no módulo de *Easy Import Control* (SIGAEIC). Ele permite a manipulação de dados ou a execução de rotinas customizadas no momento da inclusão do registro.

**Exemplo:**  
Utilize a sintaxe abaixo para capturar os parâmetros necessários e realizar as validações:

User Function EICPSI01()  
Local aParam := PARAMIXB  
Local lRet := .T.

// Insira aqui a regra de negócio customizada

Return lRet

**Saiba mais:**  
[EICPSI01 - Inclusão da SI - Solicitação Importação](https://tdn.totvs.com/pages/releaseview.action?pageId=6806858)
