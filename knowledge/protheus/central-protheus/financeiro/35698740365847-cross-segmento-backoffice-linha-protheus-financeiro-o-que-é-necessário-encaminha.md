---
article_id: 35698740365847
category: Financeiro
content_hash: 6dfeffbd905d5b87ab19d299d37da433e9dbebd11baf739f44e485b7e41ceddd
fetched_at: '2026-06-28T22:38:00.793681+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - Financeiro - O que é necessário
  encaminhar para análise do suporte  em casos de error.log?
type: support-article
updated_at: '2025-10-17T19:08:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35698740365847-Cross-Segmento-Backoffice-Linha-Protheus-Financeiro-O-que-%C3%A9-necess%C3%A1rio-encaminhar-para-an%C3%A1lise-do-suporte-em-casos-de-error-log
---

**Dúvida:**

Ao utilizar o sistema, foi gerado um **error log**: veja o que é necessário encaminhar para análise do suporte

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus – Financeiro  – Todas as versões  
  
  
**Solução**  
Quando ocorrer um **error log** no sistema (TOTVS Backoffice — Linha Protheus), a tela exibe apenas um resumo das chamadas de erro. Para uma análise detalhada pelo suporte, acesse a **Central de Diagnóstico** gerada pela rotina com problema, nos encaminhe inicialmente o inspetor de objetos/extrato de versão do ambiente.

Siga também estes passos:

1. Acesse o servidor onde o Protheus está instalado e entre na pasta **\system**.
2. Apague (ou mova/rename como backup) o arquivo **ERROR.LOG** existente.
3. Reproduza o erro no sistema (execute a ação que gera a falha).
4. Volte à pasta **\system** e compacte (ZIP) o novo arquivo **ERROR.LOG** gerado.
5. Anexe o ZIP ao chamado e envie para o suporte.

**Observações importantes**

* Se preferir não apagar o arquivo original, renomeie-o (por exemplo `ERROR.log.bak`) para manter um backup.
* Informe no chamado: passo executado, horário da reprodução e usuário do Protheus usado durante o teste — isso facilita a correlação dos logs.
