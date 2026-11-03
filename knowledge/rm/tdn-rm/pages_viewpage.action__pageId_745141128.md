---
content_hash: e84efab8103189c8964d10dbbc61c0323440a56e6d65a990427c3a5427028c6e
fetched_at: '2026-06-29T00:11:32.186213+00:00'
page_id: '745141128'
product: rm
source: tdn-rm
title: Regras do fracionamento de jobs nos processos de geração de lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=745141128
version: 22
---

Os processos de geração de lançamentos poderão ser configurados para utilizar o fracionamento de jobs, utilizando as classes à seguir:

* EduGerarLancFromParcelaSliceableData: executa o processo de geração de lançamentos com fracionamento de jobs, à partir da visão de parcelas do contrato;
* EduGerarLancFromContratoSliceableData: executa o processo de geração de lançamentos com fracionamento de jobs, à partir da visão de contrato;
* EduGeraLancSliceableData: executa o processo de geração de lançamentos em lote com fracionamento de jobs.

Para informações detalhadas sobre o fracionamento de jobs, consultar a documentação [Configuração de fracionamento de jobs.](https://tdn.totvs.com/x/lpR-I)

Os processos de geração de lançamentos poderão ser executados com ou sem fracionamentos de jobs. A regra utilizada no fracionamento mudará conforme o tipo de agrupamento configurado nos parâmetros do Educacional.

Para acessar as parametrizações deve ir pelo caminho nos parâmetros do educacional: Educacional | Integração | Financeiro | Educacional | Fin- Agrupamento

Conforme a imagem acima, os parâmetros: "Agrupamento de lançamentos (boleto)" e "Não agrupar serviços diferentes" irão ter regras específicas que irão mudar a forma como o fracionamento é realizado. À seguir, seguem alguns detalhamentos, com cenários, que exemplificarão esse fracionamento de parcelas para a geração de lançamentos.

O sistema irá considerar as diferenças nas seguintes informações, para a definição do fracionamento: serviços, contas caixa, responsáveis financeiros, datas de vencimento e tipos de parcelas.

**A partir da versão 12.1.2506,** todas as parcelas de um mesmo contrato serão sempre processadas juntas, dentro da mesma fração do Job.

A partir da versão 12.1.2506

Conforme a imagem acima, os parâmetros: "Agrupamento de lançamentos (boleto)" e "Não agrupar serviços diferentes" irão ter regras específicas que irão mudar a forma como o fracionamento é realizado. À seguir, seguem alguns detalhamentos, com cenários, que exemplificarão esse fracionamento de parcelas para a geração de lançamentos.

O sistema irá considerar as diferenças nas seguintes informações, para a definição do fracionamento: serviços, contas caixa, responsáveis financeiros, datas de vencimento e tipos de parcelas.

## Parâmetro "Não agrupar serviços diferentes" desmarcado

Agrupamento de lançamentos (boleto do tipo):

Parâmetro desmarcadoResponsável financeiro

Quando o sistema estiver configurado para realizar o agrupamento por responsável financeiro, o sistema irá separar as parcelas em grupos por responsável financeiro, considerando, também, as demais informações de contas caixa, responsáveis financeiros, datas de vencimento e tipos de parcela.

Todas as parcelas que possuem as mesmas informações ficarão juntos em um mesmo Job, no momento do fracionamento.

Se definirmos um filtro que traz 01 contrato com 06 parcelas e serviços iguais, com um responsável financeiro, teríamos a geração de1 Job, dependendo da parametrização, considerando as seguintes informações: código da conta caixa, responsável financeiro, data de vencimento e tipo da parcela.

Por exemplo:

Contrato: 001 | RA: ES-0011

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsáveis C00100 e C00200)

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 (Responsável C00300)

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra) (Responsável C00100)

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 (Responsável C00100)

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 (Responsáveis C00100 e C00300)

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 (Responsável C00300)

Será gerado apenas 1 Job com o fracionamento:

Job 01:

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsáveis C00100 e C00200)

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 (Responsável C00300)

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra) (Responsável C00100)

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 (Responsável C00100)

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 (Responsáveis C00100 e C00300)

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 (Responsável C00300)

\*\*\* Todas parcelas serão geradas em apenas um Job, pois todas as parcelas são referentes ao mesmo contrato. Então, mesmo que dentro de um contrato exista uma parcela que possui parâmetros diferentes dos demais que serão agrupados, ele será executado na mesma fração.

Se definirmos um filtro que traz 03 contratos, sendo 2 contratos com 02 parcelas e serviços iguais, com um responsável financeiro, teríamos a geração de até 01 Job, para esses dois contratos, e um outro Job para o terceiro contrato com informações diferentes, dependendo da parametrização, considerando as seguintes informações: código da conta caixa, responsável financeiro, data de vencimento e tipo da parcela.

Exemplo:

Contrato: 001 | RA: ES-0011

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00300)

Parcela: 2 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00300)

Contrato: 002 | RA: ES-0011

Parcela: 1 | Cota: 1 | Vencimento: 02/01/2023 (Responsável C00200)

Parcela: 2 | Cota: 1 | Vencimento: 02/01/2023 (Responsável C00200)

Contrato: 003 | RA: ES-0022

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00300)

Parcela: 2 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00300)

Serão gerados 2 Jobs com o fracionamento:

Job 01:

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00300) - RA: ES-0011

Parcela: 2 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00300) - RA: ES-0011

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00300) - RA: ES-0022

Parcela: 2 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00300) - RA: ES-0022

Job 02:

Parcela: 1 | Cota: 1 | Vencimento: 02/01/2023 (Responsável C00200) - RA: ES-0011

Parcela: 2 | Cota: 1 | Vencimento: 02/01/2023 (Responsável C00200) - RA: ES-0011

Contrato

Quando o sistema estiver configurado para realizar o agrupamento por contrato, o sistema irá separar as parcelas em grupos por contratos, considerando, também, as demais informações de conta caixa, responsável financeiro, data de vencimento e tipo de parcela.

Todas as parcelas que possuem as mesmas informações ficarão juntos em um mesmo Job, no momento do fracionamento.

Se definirmos um filtro que traz 01 contrato com 06 parcelas e serviços iguais, com um responsável financeiro, teríamos a geração de 1 Job, todas as parcelas de um mesmo contrato serão geradas em uma fração do Job, independente de terem informações diferentes.

Por exemplo:

Contrato: 001

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra)

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023

Será criado 01 Job com o fracionamento:

Job 01:

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra)

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023

Aluno

Quando o sistema estiver configurado para realizar o agrupamento por aluno, o sistema irá separar as parcelas em grupos por registro acadêmico do aluno, considerando, também, as demais informações de contas caixa, responsáveis financeiros, datas de vencimento e tipos de parcela.

Todas as parcelas que possuem as mesmas informações ficarão juntos em um mesmo Job, no momento do fracionamento.

Se definirmos um filtro que traz 01 contrato com 06 parcelas e serviços iguais, com um responsável financeiro, teríamos a geração de 1 Job, pois estão em um contrato

Por exemplo:

Contrato: 001 | RA: ES-0011

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra)

Será criado 1 Job com o fracionamento:

Job 01:

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra)

Se definirmos um filtro que traz 02 contrato do mesmo aluno com 02 parcelas cada de serviços iguais, com um responsável financeiro, teríamos a geração de 2 Jobs, se as seguintes informações estiverem divergentes entre as parcelas: código da conta caixa, responsável financeiro, data de vencimento e tipo da parcela.

Contrato: 001 | RA: ES-0011

Parcela: 1 | Cota: 1 | Vencimento: 01/02/2023

Parcela: 2 | Cota: 1 | Vencimento: 01/01/2023 (outro responsável financeiro)

Contrato: 002 | RA: ES-0011

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023

Parcela: 2 | Cota: 1 | Vencimento: 01/01/2023

Serão criados 2 Jobs com o fracionamento, uma para cada contrato:

Job 01:

Parcela: 1 | Cota: 1 | Vencimento: 01/02/2023 - Contrato: 001

Parcela: 2 | Cota: 1 | Vencimento: 01/01/2023 (outro responsável financeiro) - Contrato: 001

Job 2:

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 - Contrato: 002

Parcela: 2 | Cota: 1 | Vencimento: 01/01/2023 - Contrato: 002

Não agrupado

Quando o sistema estiver configurado para não agrupar boletos, o processo de geração de lançamentos, através da visão de contratos e parcelas, irá ser executado conforme a parametrização do cadastro de fracionamentos.

Quando for executado pelo processo de geração de lançamentos em lote, a quantidade de frações será definida na última etapa, tendo como valor padrão o número definido na parametrização do cadastro de fracionamentos.

Exemplo 1:

O usuário seleciona um contrato com 12 parcelas e o sistema está parametrizado, em "Segurança - Fracionamento de Jobs", para utilizar o número máximo de frações com 10.

Ao executar o processo, o sistema irá gerar 01 Job, com as 12 parcelas.

Exemplo 2:

O usuário seleciona um contrato com 10 parcelas e o sistema está parametrizado, em "Segurança - Fracionamento de Jobs", para utilizar o número máximo de frações com 02.

Ao executar o processo, o sistema irá gerar 01 Job, com 10 parcelas.

---

## Parâmetro "Não agrupar serviços diferentes" marcado

Agrupamento de lançamentos (boleto do tipo):

Parâmetro marcadoResponsável financeiro

Quando o sistema estiver configurado para realizar o agrupamento por responsável financeiro, o sistema irá separar as parcelas em grupos por responsável financeiro, considerando, também, as demais informações de serviços, contas caixa, responsáveis financeiros, datas de vencimento e tipos de parcela.

Todas as parcelas que possuem as mesmas informações ficarão juntos em um mesmo Job, no momento do fracionamento.

Se definirmos um filtro que traz 01 contrato com 06 parcelas e serviços iguais, com um responsável financeiro, teríamos a geração de 1 Job, independente da parametrização, considerando as seguintes informações: código do serviço, código da conta caixa, responsável financeiro, data de vencimento e tipo da parcela.

Por exemplo:

Contrato: 001 | RA: ES-0011

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsáveis C00100 e C00200) | Serviço: A | Conta caixa: 001

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 (Responsável C00300) | Serviço: A | Conta caixa: 001

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra) (Responsável C00100) | Serviço: A | Conta caixa: 001

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 (Responsável C00100) | Serviço: B | Conta caixa: 001

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 (Responsáveis C00100 e C00300) | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 (Responsável C00300) | Serviço: B | Conta caixa: 001

Será criado 1 Job com o fracionamento:

Job 01:

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsáveis C00100 e C00200) | Serviço: A | Conta caixa: 001

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 (Responsável C00300) | Serviço: A | Conta caixa: 001

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra) (Responsável C00100) | Serviço: A | Conta caixa: 001

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 (Responsável C00100) | Serviço: B | Conta caixa: 001

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 (Responsáveis C00100 e C00300) | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 (Responsável C00300) | Serviço: B | Conta caixa: 001

\*\*\* No caso de existir outros contratos será avaliado as parametrizações, e existindo uma parcela com as informações em comum entre eles, serão executados em um Job todas as parcelas de ambos contratos.  
Exemplo:

Contrato: 001 | RA: ES-0011

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00100) | Serviço: A | Conta caixa: 001

Parcela: 2 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00300) | Serviço: A | Conta caixa: 001

Contrato: 002 | RA: ES-0022

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00100) | Serviço: A | Conta caixa: 001

Parcela: 2 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00400) | Serviço: B | Conta caixa: 001

Será criado 1 Job com o fracionamento:

Job 01:

Contrato: 001 | RA: ES-0011

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00100) | Serviço: A | Conta caixa: 001

Parcela: 2 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00300) | Serviço: A | Conta caixa: 001

Contrato: 002 | RA: ES-0022

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00100) | Serviço: A | Conta caixa: 001

Parcela: 2 | Cota: 1 | Vencimento: 01/01/2023 (Responsável C00400) | Serviço: B | Conta caixa: 001

Contrato

Quando o sistema estiver configurado para realizar o agrupamento por contrato, o sistema irá separar as parcelas em grupos por contratos, considerando, também, as demais informações de serviços, contas caixa, responsáveis financeiros, datas de vencimento e tipos de parcela.

Todas as parcelas que possuem as mesmas informações ficarão juntos em um mesmo Job, no momento do fracionamento.

Se definirmos um filtro que traz 01 contrato com 06 parcelas e serviços iguais, com um responsável financeiro, teríamos a geração de 1 Job, independente da parametrização.

Por exemplo:

Contrato: 001

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 | Serviço: A | Conta caixa: 001

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 | Serviço: B | Conta caixa: 001

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra)| Serviço: A | Conta caixa: 001

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Será criado 01 Job com o fracionamento:

Job 01:

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 | Serviço: A | Conta caixa: 001

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 | Serviço: B | Conta caixa: 001

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra)| Serviço: A | Conta caixa: 001

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Aluno

Quando o sistema estiver configurado para realizar o agrupamento por aluno, o sistema irá separar as parcelas em grupos por registro acadêmico do aluno, considerando, também, as demais informações de contas caixa, responsáveis financeiros, datas de vencimento e tipos de parcela.

Todas as parcelas que possuem as mesmas informações ficarão juntos em um mesmo Job, no momento do fracionamento.

Se definirmos um filtro que traz 01 contrato com 06 parcelas e serviços iguais, com um responsável financeiro, teríamos a geração de 01 Job para todas as parcelas do contrato, independente da parametrização. E para mais contratos irá considerar as seguintes informações: código da conta caixa, responsável financeiro, data de vencimento e tipo da parcela.

Por exemplo:

Contrato: 001 | RA: ES-0011

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 | Serviço: A | Conta caixa: 001

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 | Serviço: B | Conta caixa: 001

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra) | Serviço: A | Conta caixa: 001

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Serão criados 01 Job com o fracionamento:

Job 01:

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 | Serviço: A | Conta caixa: 001

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 | Serviço: B | Conta caixa: 001

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra) | Serviço: A | Conta caixa: 001

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Não agrupado

No caso do sistema estiver configurado para não agrupar boletos, o Job irá seguir a parametrização do processo relacionada a quantidade máxima de frações, quando for executada a geração de lançamento pela visão de lançamentos e parcelas.

Quando for executar pela tela de geração de lançamento em lote, a quantidade de frações será aquela que o usuário informar na hora que executar o processo.

Exemplo 1:

Usuário seleciona um contrato com 12 parcelas, o sistema está parametrizado em "Segurança - Fracionamento de Jobs" para utilizar o número máximo de frações com 10.

Ao executar o processo o sistema gera 1 Job, com as 12 parcelas.

Exemplo 2:

Usuário seleciona um 10 parcelas de um determinado contrato, o sistema está parametrizado em "Segurança - Fracionamento de Jobs" para utilizar o número máximo de frações com 2.

Ao executar o processo o sistema gera 1 Jobs, com 10 parcelas.

## Parâmetro "Não agrupar serviços diferentes" desmarcado

Agrupamento de lançamentos (boleto do tipo):

Parâmetro desmarcadoResponsável financeiro

Quando o sistema estiver configurado para realizar o agrupamento por responsável financeiro, o sistema irá separar as parcelas em grupos por responsável financeiro, considerando, também, as demais informações de contas caixa, responsáveis financeiros, datas de vencimento e tipos de parcela.

Todas as parcelas que possuem as mesmas informações ficarão juntos em um mesmo job, no momento do fracionamento.

Se definirmos um filtro que traz 01 contrato com 06 parcelas e serviços iguais, com um responsável financeiro, teríamos a geração de até 05 Jobs, dependendo da parametrização, considerando as seguintes informações: código da conta caixa, responsável financeiro, data de vencimento e tipo da parcela.

Por exemplo:

Contrato: 001 | RA: ES-0011

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsáveis C00100 e C00200)

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 (Responsável C00300)

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra) (Responsável C00100)

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 (Responsável C00100)

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 (Responsáveis C00100 e C00300)

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 (Responsável C00300)

Serão criados até 05 Jobs com o fracionamento:

Job 01:

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsáveis C00100 e C00200)

Job 02:

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 (Responsável C00300)

Job 03

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra) (Responsável C00100)

Job 04:

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 (Responsável C00100)

Job 05:

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 (Responsáveis C00100 e C00300)

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 (Responsável C00300)

\*\*\* As parcelas 1, cota 1 e 2, podem ficar separadas, pois não possuem responsáveis financeiros em comum.

\*\*\* As parcelas 3, cota 1 e 2, precisam ficar juntas, pois compartilham um mesmo responsável financeiro.

Contrato

Quando o sistema estiver configurado para realizar o agrupamento por contrato, o sistema irá separar as parcelas em grupos por contratos, considerando, também, as demais informações de conta caixa, responsável financeiro, data de vencimento e tipo de parcela.

Todas as parcelas que possuem as mesmas informações ficarão juntos em um mesmo job, no momento do fracionamento.

Se definirmos um filtro que traz 01 contrato com 06 parcelas e serviços iguais, com um responsável financeiro, teríamos a geração de até 04 Jobs, dependendo da parametrização, considerando as seguintes informações: código da conta caixa, responsável financeiro, data de vencimento e tipo da parcela.

Por exemplo:

Contrato: 001

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra)

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023

Serão criados até 04 Jobs com o fracionamento:

Job 01:

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023

Job 02:

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra)

Job 03:

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023

Job 04:

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023

Aluno

Quando o sistema estiver configurado para realizar o agrupamento por aluno, o sistema irá separar as parcelas em grupos por registro acadêmico do aluno, considerando, também, as demais informações de contas caixa, responsáveis financeiros, datas de vencimento e tipos de parcela.

Todas as parcelas que possuem as mesmas informações ficarão juntos em um mesmo job, no momento do fracionamento.

Se definirmos um filtro que traz 01 contrato com 06 parcelas e serviços iguais, com um responsável financeiro, teríamos a geração de até 04 Jobs, dependendo da parametrização, considerando as seguintes informações: código da conta caixa, responsável financeiro, data de vencimento e tipo da parcela.

Por exemplo:

Contrato: 001 | RA: ES-0011

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra)

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023

Serão criados até 04 Jobs com o fracionamento:

Job 01:

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023

Job 02:

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra)

Job 03:

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023

Job 04:

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023

Não agrupado

Quando o sistema estiver configurado para não agrupar boletos, o processo de geração de lançamentos, através da visão de contratos e parcelas, irá ser executado conforme a parametrização do cadastro de fracionamentos.

Quando for executado pelo processo de geração de lançamentos em lote, a quantidade de frações será definida na última etapa, tendo como valor padrão o número definido na parametrização do cadastro de fracionamentos.

Exemplo 1:

O usuário seleciona um contrato com 12 parcelas e o sistema está parametrizado, em "Segurança - Fracionamento de Jobs", para utilizar o número máximo de frações com 10.

Ao executar o processo, o sistema irá gerar 10 jobs, sendo 08 com uma parcela e 02 com 02 parcelas.

Exemplo 2:

O usuário seleciona um contrato com 10 parcelas e o sistema está parametrizado, em "Segurança - Fracionamento de Jobs", para utilizar o número máximo de frações com 02.

Ao executar o processo, o sistema irá gerar 02 jobs, com 05 parcelas cada um.

Exemplo 3:

Quando o usuário, no processo de geração de lançamentos em lote, rodar um filtro de uma determinada matriz aplicada, sendo ela com 100 contratos, cada contrato com 6 parcelas, um total de 600 parcelas e o sistema estiver parametrizado, em "Segurança - Fracionamento de Jobs", para utilizar o número máximo de frações com 10, mas o usuário informa 06 frações na tela.

Ao executar o processo, o sistema irá gerar 06 jobs, com 100 parcelas cada um.

---

## Parâmetro "Não agrupar serviços diferentes" marcado

Agrupamento de lançamentos (boleto do tipo):

Parâmetro marcadoResponsável financeiro

Quando o sistema estiver configurado para realizar o agrupamento por responsável financeiro, o sistema irá separar as parcelas em grupos por responsável financeiro, considerando, também, as demais informações de serviços, contas caixa, responsáveis financeiros, datas de vencimento e tipos de parcela.

Todas as parcelas que possuem as mesmas informações ficarão juntos em um mesmo job, no momento do fracionamento.

Se definirmos um filtro que traz 01 contrato com 06 parcelas e serviços iguais, com um responsável financeiro, teríamos a geração de até 06 Jobs, dependendo da parametrização, considerando as seguintes informações: código do serviço, código da conta caixa, responsável financeiro, data de vencimento e tipo da parcela.

Por exemplo:

Contrato: 001 | RA: ES-0011

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsáveis C00100 e C00200) | Serviço: A | Conta caixa: 001

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 (Responsável C00300) | Serviço: A | Conta caixa: 001

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra) (Responsável C00100) | Serviço: A | Conta caixa: 001

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 (Responsável C00100) | Serviço: B | Conta caixa: 001

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 (Responsáveis C00100 e C00300) | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 (Responsável C00300) | Serviço: B | Conta caixa: 001

Serão criados até 06 Jobs com o fracionamento:

Job 01:

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 (Responsáveis C00100 e C00200) | Serviço: A | Conta caixa: 001

Job 02:

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 (Responsável C00300) | Serviço: A | Conta caixa: 001

Job 03

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra) (Responsável C00100) | Serviço: A | Conta caixa: 001

Job 04:

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 (Responsável C00100) | Serviço: B | Conta caixa: 001

Job 05:

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 (Responsáveis C00100 e C00300) | Serviço: A | Conta caixa: 001

Job 06:

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 (Responsável C00300) | Serviço: B | Conta caixa: 001

\*\*\* As parcelas 1, cota 1 e 2, podem ficar separadas, pois não possuem responsáveis financeiros em comum.

\*\*\* As parcelas 3, cota 1 e 2, podem ficar separadas, pois possuem serviços diferentes.

Contrato

Quando o sistema estiver configurado para realizar o agrupamento por contrato, o sistema irá separar as parcelas em grupos por contratos, considerando, também, as demais informações de serviços, contas caixa, responsáveis financeiros, datas de vencimento e tipos de parcela.

Todas as parcelas que possuem as mesmas informações ficarão juntos em um mesmo job, no momento do fracionamento.

Se definirmos um filtro que traz 01 contrato com 06 parcelas e serviços iguais, com um responsável financeiro, teríamos a geração de até 05 Jobs, dependendo da parametrização, considerando as seguintes informações: código da conta caixa, responsável financeiro, data de vencimento e tipo da parcela.

Por exemplo:

Contrato: 001

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 | Serviço: A | Conta caixa: 001

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 | Serviço: B | Conta caixa: 001

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra)| Serviço: A | Conta caixa: 001

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Serão criados até 05 Jobs com o fracionamento:

Job 01:

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 | Serviço: A | Conta caixa: 001

Job 02:

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 | Serviço: B | Conta caixa: 001

Job 03:

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra) | Serviço: A | Conta caixa: 001

Job 04:

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 | Serviço: A | Conta caixa: 001

Job 05:

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Aluno

Quando o sistema estiver configurado para realizar o agrupamento por aluno, o sistema irá separar as parcelas em grupos por registro acadêmico do aluno, considerando, também, as demais informações de contas caixa, responsáveis financeiros, datas de vencimento e tipos de parcela.

Todas as parcelas que possuem as mesmas informações ficarão juntos em um mesmo job, no momento do fracionamento.

Se definirmos um filtro que traz 01 contrato com 06 parcelas e serviços iguais, com um responsável financeiro, teríamos a geração de até 04 Jobs, dependendo da parametrização, considerando as seguintes informações: código da conta caixa, responsável financeiro, data de vencimento e tipo da parcela.

Por exemplo:

Contrato: 001 | RA: ES-0011

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 | Serviço: A | Conta caixa: 001

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 | Serviço: B | Conta caixa: 001

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra) | Serviço: A | Conta caixa: 001

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Serão criados até 04 Jobs com o fracionamento:

Job 01:

Parcela: 1 | Cota: 1 | Vencimento: 01/01/2023 | Serviço: A | Conta caixa: 001

Job 02:

Parcela: 1 | Cota: 2 | Vencimento: 01/01/2023 | Serviço: B | Conta caixa: 001

Job 03:

Parcela: 1 | Cota: 3 | Vencimento: 01/01/2023 (Extra) | Serviço: A | Conta caixa: 001

Job 04:

Parcela: 2 | Cota: 1 | Vencimento: 01/02/2023 | Serviço: A | Conta caixa: 001

Job 05:

Parcela: 3 | Cota: 1 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Parcela: 3 | Cota: 2 | Vencimento: 01/03/2023 | Serviço: A | Conta caixa: 001

Não agrupado

No caso do sistema estiver configurado para não agrupar boletos, o job irá seguir a parametrização do processo relacionada a quantidade máxima de frações, quando for executada a geração de lançamento pela visão de lançamentos e parcelas.

Quando for executar pela tela de geração de lançamento em lote, a quantidade de frações será aquela que o usuário informar na hora que executar o processo.

Exemplo 1:

Usuário seleciona um contrato com 12 parcelas, o sistema está parametrizado em "Segurança - Fracionamento de Jobs" para utilizar o número máximo de frações com 10.

Ao executar o processo o sistema gera 10 jobs, sendo 8 com uma parcela e 2 com 2 parcelas.

Exemplo 2:

Usuário seleciona um 10 parcelas de um determinado contrato, o sistema está parametrizado em "Segurança - Fracionamento de Jobs" para utilizar o número máximo de frações com 2.

Ao executar o processo o sistema gera 2 jobs, com 5 parcelas cada um.

Exemplo 2:

Na tela de geração de lançamento em lote, o usuário roda um filtro de uma determinada matriz aplicada, sendo ela com 100 contratos, com cada contrato com 6 parcelas, totalizando 600 parcelas. O sistema está parametrizado em "Segurança - Fracionamento de Jobs" para utilizar o número máximo de frações com 10, mas o usuário informa 6 frações na tela.

Ao executar o processo o sistema gera 6 jobs, com 100 parcelas cada um.
