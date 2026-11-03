---
article_id: 360034836913
category: Financeiro - Manutenção de Borderô
content_hash: b4885430e71bcc7ecf6193b78649783c579181ef800ceba866c27de4665bf5d4
fetched_at: '2026-06-28T22:37:35.594046+00:00'
product: protheus
section_id: 35057515546903
source: central-protheus
title: Cross Seguimento - SIGAFIN -  FINA474 - Importação do arquivo apresenta a mensagem
  que o Banco + Agência + Conta não existe
type: support-article
updated_at: '2026-02-11T11:20:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034836913-Cross-Seguimento-SIGAFIN-FINA474-Importa%C3%A7%C3%A3o-do-arquivo-apresenta-a-mensagem-que-o-Banco-Ag%C3%AAncia-Conta-n%C3%A3o-existe
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35596671283863) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida****:**  
Na rotina **Manutenção de Extrato (FINA474)**, ao importar o arquivo de extrato bancário, é exibida a mensagem informando que **Banco + Agência + Conta não existem**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045289393)  
  
**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Financeiro - FINA474 - A partir da versão 12.1.17  
  
**Causa**  
O incidente pode ocorrer quando as **configurações de posição do Código do Banco, Agência e Conta** no arquivo não estão definidas corretamente, ou quando o campo **A6\_BLOCKED** do cadastro bancário está **em branco**.

### **Importante**

Contas bancárias cadastradas **com hífen (-)** podem gerar inconsistências no posicionamento dos campos, uma vez que o **banco não envia esse caractere** e o **Protheus também não o considera** ao gravar os dados via ***INSERT***no banco de dados.

Para corrigir essa situação, recomenda-se:

* Criar uma **nova conta sem hífen**, informando o **dígito** no campo apropriado;
* Ou utilizar o **ponto de entrada F474CTA**, responsável por ajustar as informações bancárias para a busca dos registros a conciliar.

[F474CTA - Ajustar informações bancárias para a busca dos registros a conciliar](https://tdn.totvs.com/pages/releaseview.action?pageId=776531933)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Verifique e configure corretamente as **posições do Código do Banco, Agência e Conta** no layout do arquivo de importação;
2. Certifique-se de que o campo **A6\_BLOCKED** esteja devidamente preenchido com o valor **1** ou **2**;
3. Caso a conta contenha hífen, **crie uma nova conta sem o caractere especial** ou **implemente o ponto de entrada F474CTA** para ajuste automático.
