---
content_hash: 3267fc72982949065abad1d897742c2b32b40b5592152a3cdda67745e9f0079a
fetched_at: '2026-06-29T00:12:00.545065+00:00'
page_id: '883658360'
product: rm
source: tdn-rm
title: Linha RM - Integração Gesplan
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=883658360
version: 29
---

Conteúdo:

# 1. Sobre

Esta documentação descreve a integração entre os módulos do TOTVS Backoffice - Linha RM e da Gesplan, com o objetivo de otimizar e automatizar o fluxo de informações entre as duas plataformas.  
A integração foi projetada para garantir uma comunicação eficiente e facilitar a gestão de dados em tempo real, proporcionando maior controle e visibilidade sobre os processos operacionais e financeiros.

# 2. Pré-requisitos

* Adquirir a oferta da Gesplan, pois toda a configuração e provisionamento do ambiente é realizada baseado no licenciamento, entre em contato com seu ESN.
* Servidores de aplicação: Windows 11, Windows Server 2019 (mínimo build 17763.3165) ou superiores.
* License Server atualizado com a última versão.
* Ambiente do ERP atualizado a partir da release 12.1.2406.

Importante

No momento da implantação é importante utilizar sempre o último patch disponível no [portal de downloads](https://suporte.totvs.com/portal/p/10098/download#000023/12.1/all/), e executar o atualizador, pois evoluções estão sendo constantemente liberadas.

# 3. Ativação

Para ativar a integração, é necessário ter em mãos o número do tenant do ambiente provisionado que foi realizado ao adquirir a oferta.  
A comunicação entre as plafatormas será realizada através do smartLink, seguindo os passos descritos na documentação .

# 4. Escopo

A integração abrange os seguintes módulos:

false

------

A comunicação entre os módulos Gestão de Caixa e Tesouraria (WFN Cash) X TOTVS Gestão Contábil e TOTVS Gestão Financeira, tem origem tanto na Gesplan quanto no RM.

O RM fará integração com o modulo de Gestão de Caixa somente com eventos financeiros, enviando dados de títulos a pagar e a receber (eventos previstos), bem como posterior o seu pagamento e recebimento (eventos realizados)

[Envio previsão financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=919061335)

[Envio realizado](https://tdn.totvs.com/pages/viewpage.action?pageId=919061438)

Carga de Dados

A carga de dados acontece minutos depois da ativação da integração e envolve as tabelas abaixo, com os seus respectivos filtros.  
O tempo de carga varia de acordo com a quantidade de registros do período.

| Tabela | Descrição | Filtro carga de dados | Pode ser global? \*\* |
| --- | --- | --- | --- |
| GCCUSTO | Cadastro de centro de custo | Tabela completa | Não |
| FCFO | Cadastro de cliente/fornecedor | Tabela completa | Sim |
| FDADOSPGTO | Dados de pagamento dos clientes/fornecedores | >= 01/01/2025 | Sim |
| FCXA | Cadastro de contas/caixas | Tabela completa | Sim |
| CCONTA | Cadastro do plano de contas contábeis | Tabela completa | Sim |
| GPAIS | Cadastro de país | Tabela completa | Nativamente global, não tem coligada |
| GETD | Cadastro de estado | Tabela completa | Nativamente global, não tem coligada |
| TFORMAPAGTO | Cadastro de meio de pagamento | Tabela completa | Não |
| GMOEDA | Cadastro de moeda | Tabela completa | Nativamente global, não tem coligada |
| GCOTACAO | Cadastro de cotações | >= 01/01/2025 | Nativamente global, não tem coligada |
| FTDO | Cadastro de Tipo de Documento | Tabela completa | Não |
| FLAN | Dados de inclusão dos lançamentos | >= 01/01/2025 | Não |
| FLANRATCCU | Rateio da inclusão dos lançamentos | >= 01/01/2025 | Não |
| FLANBAIXA | Dados de baixa dos lançamentos | >= 01/01/2025 | Não |
| FLANBAIXARATCCU | Rateio das baixas dos lançamentos | >= 01/01/2025 | Não |
| FXCX | Movimentações bancárias | >= 01/01/2025 | Não |
| CCONT | Cabeçalho das contabilizações | >= 01/01/2025 | Não |
| CPARTIDA | Partidas das contabilizações | >= 01/01/2025 | Não |

\*\* Caso o cliente configura algum cadastro como global, a coligada trafegada na integração será 0 (zero)

Haverá ainda a possibilidade de integrar os eventos financeiros do Extrato de Caixa dependendo do processo de integração desenhado entre as soluções. Nesta integração serão enviado eventos de tesouraria, como tarifas, transferências, entre outros.

------

false

------

A comunicação entre os módulos Operações Financeiras (WFN Financing) X TOTVS Gestão Contábil e TOTVS Gestão Financeira, tem origem apenas na Gesplan.

Nesta integração são enviados eventos de contrato:

Provisão do contrato: apropriação, maturação e provisão de juros, são integrados direto na contabilidade. 

Realização do contrato que movimenta conta/corrente: juros pagos e amortização, são enviados para o extrato de caixa, que pode ser não contábil ou contábil.

------

Importante

A integração destes módulos não contempla o envio do Contas a Pagar do Gesplan para o RM.

false

------

A comunicação entre os módulos Arrendamento e Locações (WFN Lease) X TOTVS Gestão Contábil, tem origem apenas na Gesplan.

------

[Clique aqui](https://produtos.totvs.com/ficha-tecnica/tudo-sobre-o-totvs-gestao-financeira-linha-gesplan/), para saber mais sobre os módulos da Gesplan.

# 5. Definições Gerais

Para garantir o sucesso da integração e evitar a quebra das regras de negócios, foram necessárias algumas definições e ajustes prévios entre o ERP e a Gesplan.

O usuário informado na integração deve existir no RM, e ter perfil com permissões nos módulos TOTVS Gestão Financeira e TOTVS Gestão Contábil, além de configurações específicas como definição de período de inclusão de lançamento contábil.
