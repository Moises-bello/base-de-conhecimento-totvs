---
article_id: 360020182492
category: ADVPL - Ponto de Entrada
content_hash: 815d2a6f74469c51bd0edbe9b07d999c440bc72c60ea4bbd570226df92beee01
fetched_at: '2026-06-28T22:40:11.485704+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - ADVPL -  Execauto CNTA120 executando
  pelo ponto de entrada na MATA094 '
type: support-article
updated_at: '2022-05-30T17:42:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020182492-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Execauto-CNTA120-executando-pelo-ponto-de-entrada-na-MATA094
---

**Ocorrência**Estou tentando executar uma rotina automática CNTA120 através do Ponto de entrada MVC MATA094 (Aprovação de Documentos ), após a gravação porem o sistema não está permitindo a inclusão por inconsistência de dados / campos inválidos ou obrigatórios.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Inconsistência nas dado, não conformidade na customização.  
  
**Solução**Hoje não existem restrições explicitas para execução do CNTA120 via rotina automática. Porém a execução de rotinas automáticas dentro de pontos de entrada, podem gerar resultados inesperados, a depender do escopo de variáveis, transações entre outras possibilidades técnicas.  
Não recomendamos que o cliente execute o processo como foi descrito, uma vez que a rotina MATA094 possui uma estrutura complexa e pode ocasionar problemas na execução.
