---
article_id: 26786101142039
category: Financeiro - Contas a Receber - PIX
content_hash: 0916007da4b8c41f8de776929a03e0ae0f6fc8cc53659de7ceede36797994eaa
fetched_at: '2026-06-28T22:38:16.506628+00:00'
product: protheus
section_id: 1500001539301
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA890 - Monitor PIX
type: support-article
updated_at: '2025-09-12T13:30:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26786101142039-Cross-Segmentos-Backoffice-Linha-Protheus-FINA890-Monitor-PIX
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26817104595479) Tempo aproximado para leitura: 00:10:00 min**

**Dúvida**  
Como configurar o PIX a receber?

**Videos Youtube**

**How To | SIGAFIN - Configuração e Envio do título em PIX via API #totvs\_backoffice\_linha\_protheus**  
  
  
  
How To | SIGAFIN - Job Envio de e-mail dos títulos em situação PIX #totvs\_backoffice\_linha\_protheus

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

Os **Pagamentos Instantâneos (PIX)** referem-se a transferências eletrônicas de valores em que a ordem de pagamento e a disponibilidade dos fundos para o destinatário ocorrem em tempo real. Este serviço está acessível 24 horas por dia, sete dias por semana, durante todo o ano.

As transferências são realizadas diretamente da conta do pagador para a conta do recebedor, sem a necessidade de intermediários, resultando em custos de transação reduzidos.

O **PIX** pode ser utilizado de forma online, e alguns bancos implementa a comunicação através do **modelo CNAB**. O sistema está preparado para operar com **QR CODE dinâmico**.

Os **CNABs** validados com nossos clientes estarão disponíveis por meio do **CNAB Cloud** (para pagamentos) e **TDN** (para recebimentos), embora o sistema seja compatível com qualquer banco, basta realizar a **configuração do CNAB** de acordo com o manual do banco.

**Para mais informações:**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CFGX049B - Instalar o CNAB Cloud e Usabilidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048501574-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CFGX049B-Instalar-o-CNAB-Cloud-e-Usabilidade)

**Cadastros para utilização do processo**

**Wizard Pix:** O **Wizard PIX (FINA893)** é a rotina encarregada da validação das credenciais de conexão com os serviços de **Pagamentos Instantâneos** da **TOTVS** e/ou do **Banco do Brasil**.

**![Gravar_2024_10_02_11_55_41_858.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26786101105943)**

**Link Documentação:**

[Wizard de configuração de API's (FINA893)](https://tdn.totvs.com/pages/releaseview.action?pageId=725742877)

A partir da configuração desta rotina é possível realizar o envio e o recebimento dos dados de forma on-line através dos agendamentos do **JOB**:

**FINA892:**  Realizar a transmissão dos títulos que se encontram na situação de cobrança PIX.

**FINA892A:** Realizar a baixa dos títulos previamente transmitidos, com base nas informações obtidas do banco em questão.

**Saiba Mais** - [Job para envio e retorno de registros em situação de cobrança PIX.](https://tdn.totvs.com/pages/releaseview.action?pageId=742216400)

**Cadastro de Bancos**

No cadastro de **Bancos**, foi adicionado o **novo campo ISPB**, que corresponde ao Identificador do Sistema de Pagamentos Brasileiro, essencial **para o envio no CNAB Receber**.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26786117486743)**

Sobre o banco, em "**Outras Ações**", a nova opção "**Chaves PIX**" permite vincular até 20 chaves PIX por conta, sendo que apenas uma pode estar ativa a qualquer momento.

As **chaves PIX** não podem estar associadas a outro banco, uma vez que o **DICT do Bacen** assegura a integridade no sistema financeiro.

O sistema aceitará chaves do tipo: **e-mail, número de telefone celular, CNPJ** e chaves aleatórias.

![Gravar_2024_10_02_12_15_07_939.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26786101109399)

A nova tabela que armazenará as **chaves PIX dos bancos (tabela F70)** deve ter o mesmo compartilhamento da **tabela (tabela SA6)**  de cadastro de **Bancos**.

Para utilizar a integração com o Banco do Brasil, é necessário informar no cadastro o **Banco oficial (A6\_BCOOFI)** como "**001**", que é o código identificador do Banco do Brasil.

**Cadastro Parâmetros de Banco**

No cadastro, além da configuração do banco e dos campos obrigatórios, o campo "Número de Bytes" deve ser preenchido com o valor de 750, referente ao PIX.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26786117490199)**

**Cadastro de Clientes**

No cadastro de complemento de cliente (acessando "Outras Ações" e, em seguida, "Complemento do Cliente"), foram introduzidos dois novos campos: "Gera PIX" e "E-mail PIX".

No campo "Gera PIX", deve-se especificar se o cliente deseja que seus títulos sejam gerados pela rotina de faturamento utilizando a forma de pagamento PIX. As opções disponíveis são:

* **Opção 1**: O cliente não deseja receber o e-mail padrão do sistema (em desenvolvimento) contendo o QR Code do PIX, mas aceita apenas a geração do código.
* **Opção 2**: O cliente deseja utilizar o PIX e receber o e-mail padrão do sistema (em desenvolvimento) com o QR Code do PIX.
* **Opção 3**: O cliente opta por não ter seus títulos gerados automaticamente pelo faturamento na forma de pagamento PIX (opção padrão).

**![Gravar_2024_10_02_10_36_50_846.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26786101115799)**

Ou, na aba **PIX** do **Complemento do Título**, deve-se selecionar "**Sim**" no campo "**Gera PIX**".**![Gravar_2024_10_02_10_42_00_163.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26786117493911)**

**Cadastro Situação de Cobrança**

No cadastro de **Situação de Cobrança**, foi adicionada uma nova pergunta denominada "**Situação PIX**", com o intuito de identificar quais títulos, nessa situação de cobrança, são vinculados à forma de pagamento **PIX**.

O sistema permite que haja apenas uma situação de cobrança com essa característica (**Situação PIX = Sim**).

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26786101117207)**

**Monitor PIX**

Esta nova rotina é responsável pelo controle de títulos que podem ser recebidos por meio da forma de pagamento **PIX**.

Menu **Atualizações > Comunic. Bancária > menu Monitor PIX (FINA890)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26786101118359)

**Gerar o PIX via Monitor Pix**

![Gravar_2024_10_02_13_45_23_363.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26786437616279)

**Saiba mais**

[How To - Envio via PIX](https://www.youtube.com/watch?v=PTkOhnimUac)

[Pagamentos instantâneos - PIX](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)
