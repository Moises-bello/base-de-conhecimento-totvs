---
article_id: 26458815612183
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 311e91b8b3407970fb311572296980ed916c26567a5f10a7e27bca9191ce93a7
fetched_at: '2026-06-28T22:37:55.048377+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Diferença entre API
  e CNAB
type: support-article
updated_at: '2025-07-02T11:50:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26458815612183-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Diferen%C3%A7a-entre-API-e-CNAB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26495587897239) Tempo aproximado para leitura: **00:10:00 min**

**Dúvida**  
Qual a diferença entre API e CNAB?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.23

**Solução**

**API:** O registro online de boletos visa automatizar o processo de geração e registro dos boletos emitidos pelas empresas junto aos bancos, por meio da comunicação com APIs.

No **Financeiro**, ao incluir o **título no borderô**, se o banco estiver **configurado para utilizar API**, será ativada a opção de "**Registro online de boletos**". Nesse caso, o preenchimento dos campos "**Sub Conta" e "Espécie**" será obrigatório.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26458815562391)

Após a executar do **Job da FINA713** será enviado o registro do título no banco, gerado sem erros e poderá emitir o boleto através do **Novo Painel Gestor**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26458815568663)

Gerado o boleto para pagamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26458821079447)

**Importante**

Cada banco homologado apresenta particularidades específicas em sua configuração para a geração do boleto online, conforme as diretrizes estabelecidas pela instituição financeira.

**Este processo apenas encaminha o título ao banco e gera o boleto, não efetuando a baixa dos títulos no setor financeiro.**

O título permanecerá em aberto no financeiro. Após o pagamento, a baixa pode ser realizada utilizando as opções disponíveis no sistema: **baixa manual, compensação, baixa automática ou via CNAB.**

No caso de instituições do **Banco do Brasil**, é possível ativar o retorno via **API** por meio do **JOB FINA715 ou via Webhook,** os demais bancos estão em desenvolvimento para este tipo de retorno.

**Link documentação para configuração da API**

[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)

[Baixas Títulos (Retorno) - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=705458660#tabs-Itau)

**CNAB:** refere-se ao processo de comunicação bancária entre instituições financeiras e empresas, utilizado para a cobrança de clientes e o pagamento de fornecedores. A FEBRABAN (Federação Brasileira de Bancos) estabeleceu um padrão de arquivos, que varia em quantidade de colunas e formatos de informação, podendo ser ajustado conforme as necessidades e o nível de detalhamento de cada banco.

Incluir o **título em borderô**, gerar o **arquivo de remessa**, que conterá os **títulos do borderô** a serem enviados ao banco.

![Gravar_2024_09_18_12_02_59_41.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26458821095319)

**Importante**

**Após o envio, não é gerado o boleto no sistema; apenas é registrado o título do borderô no banco.**

Para efetuar a **baixa do título**, é necessário realizar o retorno de pagamento.

![Gravar_2024_09_18_12_25_03_692.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26458821102359)

**Link documentação para configuração do CNAB**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Principais configurações e dúvidas para uso do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7778595184407-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Principais-configura%C3%A7%C3%B5es-e-d%C3%BAvidas-para-uso-do-CNAB?source=search)
