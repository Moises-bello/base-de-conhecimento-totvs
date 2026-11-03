---
content_hash: bb54bfc3873d7d1949fb3456cd7ff7dfae90a98c03f1c87135610c4a62966ee7
fetched_at: '2026-06-29T00:08:23.141476+00:00'
page_id: '269449364'
product: rm
source: tdn-rm
title: DT - Captura do pagamento de cartão de Crédito/Debito de checkout Cielo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269449364
version: 14
---

# Captura do pagamento de cartão de Crédito/Debito Checkout Cielo

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Financeira |
| **Processo:** | Captura do pagamento de cartão de Crédito/Debito do Checkout Cielo |
| **Data da publicação:** | 12/12/2016 |

# 

### **Contexto de negócio**

A Integração foi realizada com o objetivo de facilitar o pagamento com cartão de Crédito/Débito pelo portal do Educacional com o ambiente seguro da Cielo.

# **Sistemas Envolvidos**

**Totvs Educacional**

- O Portal Educacional comunica com o ambiente seguro da Cielo, realizando o processo de baixa da parcela. O retorno de confirmação do pagamento para o financeiro é realizado pelo BackOffice da Cielo, podendo ser definido pelo usuário junto a Cielo como automática ou manual.

**Totvs Gestão Financeira**

No módulo Totvs Gestão Financeira é realizado a parametrização para pagamento utilizando o modelo Checkout Cielo. Também recebe os lançamentos e boletos vinculados de origem do Educacional para baixa.

**Ambiente Cielo**

O ambiente seguro da Cielo é utilizado para realizar a captura e envio das informações do pagamento para o RM e também para controle do usuário das transações de pagamento com cartão.

# **Fluxo da integração**

Abaixo segue um passo a passo de como utilizar o Backoffice da Cielo:

PASSO A PASSO1 - Acessar o backoffice da Cielo1 - Acessar o backoffice da Cielo1 - Acessar o backoffice da Cielo

               Acesse:  <https://cieloecommerce.cielo.com.br/Backoffice>

2 - Definindo a forma de captura de pagamento2 - Definindo a forma de captura de pagamento2 - Definindo a forma de captura de pagamentoAcessar a aba Configurações | Configurações da Loja

Opções:

OPÇÕESNunca fazer Captura AutomáticaNunca fazer Captura AutomáticaNunca fazer Captura Automática

Usuário terá sempre de entrar no backoffice da Cielo e fazer a captura manualmente para que o pagamento e a baixa do lançamento sejam concluídos.

Sempre fazer Captura Automática Sempre fazer Captura AutomáticaSempre fazer Captura Automática

Assim que o aluno confirmar o pagamento o processo de captura do pagamento será feito automaticamente e com isso a baixa do lançamento.

Somente fazer Captura Automática das transações do Baixo Risco de AntiFraude Somente fazer Captura Automática das transações do Baixo Risco de AntiFraudeSomente fazer Captura Automática das transações do Baixo Risco de AntiFraude

Através de mecanismos da Cielo, ela irá decidir quais transações de pagamento serão capturadas automaticamente ou baixada manualmente.

3 - Efetuar Captura de pagamento manualmente3 - Efetuar Captura de pagamento manualmente3 - Efetuar Captura de pagamento manualmente3.1 - Acessar a Aba Pedidos e selecionar uma venda:3.2 - Efetuar a captura do pagamento para uma transação autorizada:4 - Reenviar post de mudança de status caso a captura do pagamento não tenha efetuada a baixa do lançamento4 - Reenviar post de mudança de status caso a captura do pagamento não tenha efetuada a baixa do lançamento4 - Reenviar post de mudança de status caso a captura do pagamento não tenha efetuada a baixa do lançamento5 - Analisar log de lançamento não baixados5 - Analisar log de lançamento não baixados5 - Analisar log de lançamento não baixados

Quando uma transação de pagamento é capturada, é feito a chamada do serviço de baixa do lançamento no TOTVS Gestão Financeira. Por algum motivo de regras do sistema financeiro, o lançamento pode não ter sido baixado, como por exemplo lançamento bloqueado, diferença de debito e crédito na contabilidade, período fechado, etc.

Quando ocorre o erro não é possível apresenta-lo no site backoffice da Cielo para que o usuário possa tomar as providencias necessárias e efetuar a baixa. A Cielo apenas envia um e-mail (imagem abaixo), informando que houve uma falha na tentativa de mudança de status ou captura.

Imagem

Para identificar os erros que estão ocorrendo no momento da baixa, é necessário habilitar o log através do parâmetro “Gravar arquivo de log quando ocorrer erro no processamento de notificação e mudança de status“, presento no parametrizador | Contas a Receber | Baixa | Cartão de Crédito / Débito |Configurações Gerais 2/2”.

Parâmetro

 A gravação do log será efetuada na máquina onde está sendo executada o host, no diretório de instalação das DLLs, subdiretório “Cielo\_Checkout“. Ex.: C:\TOTVS\CorporeRM\RM.Net\Cielo\_Checkout

Log

O nome do arquivo gerado segue a seguinte regra:

                Nome: EXECCARTAOBOLETO\_1\_146\_25-11-2016\_16-49-55.txt

                Onde:

                               “EXECCARTAOBOLETO” = Identificação interna do Processo

                               “1” = Coligada do Boleto

                               “146” = Identificador do Boleto

                               “25-11-2016\_16-49-55” = Data e hora da geração do log
