---
content_hash: dfed312f6adf19b64beb9c3c4107e5f8638002a3e359679c7461d94993112ace
fetched_at: '2026-06-29T00:09:59.318177+00:00'
page_id: '452718295'
product: rm
source: tdn-rm
title: Importação do Pis/Pasep
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718295
version: 3
---

Neste módulo será possível realizar a importação de valores de Pis/Pasep de todos os funcionários, exceto demitidos ou com rescisão calculada.

Para realizar a importação das informações acesse: Folha Mensal | Importação | Importação do Pis/Pasep.  
 Após acessar o módulo  o usuário deverá:  
 • **Informar o caminho do arquivo a ser importado:**

**PIS:** deverá conter o caminho do arquivo em extensão TXT obtido na CEF;

**PASEP:** deverá conter o arquivo FPS910 obtido no Banco do Brasil.

• **Informar o evento que fará o pagamento do PIS:**

Apenas o evento do tipo provento e que possuir o código de cálculo 125 poderá realizar o processo.

• **Informar a ação que a importação deverá ter:**

**Ignorar:** realiza a importação, mantendo a movimentação já existente;

**Substituir:** sobrepõe a informação existente pela importada;

**Somar:** somará os valores dos eventos que constam no arquivo importado aos valores dos eventos idênticos já existentes na movimentação.

Quando realizamos a importação do PASEP, o sistema cria dois campos:

• **Convênio:** deverá conter o número do convênio PASEP firmado entre o Banco do Brasil e a entidade.

• **Remessa:** deverá conter o número da remessa do arquivo.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Dicas - Abono Salarial

Layout - PIS

Layout - PASEP
