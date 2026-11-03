---
article_id: 360053501893
category: RH - MANAD
content_hash: fd2a8d6d06550b64b3bc70f7201b1f8256b788aa41842514ec0d463ab94353d9
fetched_at: '2026-06-28T22:43:33.819654+00:00'
product: protheus
section_id: 360008157193
source: central-protheus
title: RH - Linha Protheus - GPE - O que é MANAD e quais informações são geradas no
  arquivo
type: support-article
updated_at: '2021-04-06T20:21:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053501893-RH-Linha-Protheus-GPE-O-que-%C3%A9-MANAD-e-quais-informa%C3%A7%C3%B5es-s%C3%A3o-geradas-no-arquivo
---

**Dúvida**O que é MANAD e quais informações são geradas no arquivo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17.  
  
**Solução**Está disponível, na rotina “Instruções Normativas” (MATA950), a geração do arquivo magnético para a importação do Manual Normativo de Arquivos Digitais – Manad – em que serão apresentadas informações fiscais, contábeis, patrimoniais e dos trabalhadores, já contempladas as adequações para a versão 1002 do layout Manad.

Segundo legislação vigente, as empresas que utilizam sistema de processamento eletrônico de dados para registrar seus negócios e atividades econômicas, escrituração de livros ou produção de documentos de natureza contábil, fiscal, trabalhista e previdenciária que forem intimadas, devem apresentar os arquivos digitais contendo dados relativos aos seus negócios e atividades econômicas, seguindo as especificações e orientações do Manad e de acordo com a fiscalização da SRP (Secretaria da Receita Previdenciária), bem como a documentação técnica completa e atualização de seus sistemas.

**A quem se destina?** Às empresas que utilizam sistema de processamento eletrônico de dados para registrar seus negócios e atividades econômicas, escrituração de livros ou produção de documentos de natureza contábil, fiscal, trabalhista e previdenciária.

**Objetivo:** Permitir que as empresas intimadas apresentem dados relativos aos seus negócios e atividades econômicas.

**Tipos de registros gerados:**

| TIPO DO REGISTRO | DESCRIÇÃO |
| --- | --- |
| Registro tipo 0000 – Abertura do arquivo digital e identificação dos estabelecimentos do contribuinte | As informações referentes a este registro serão baseadas no Cadastro da Empresa, bem como nos parâmetros informados no assistente da rotina. apresentadas. |
| Registro tipo 0001 – Abertura do bloco 0 (abertura, identificação e referências) | Este registro indica se o bloco 0 (composto pelos registros 0050 e 0100) possui informações a serem |
| Registro tipo 0050 – Dados do contabilista | As informações apresentadas neste registro serão baseadas nos parâmetros informados no assistente da rotina. |
| Registro tipo 0100 – Dados do técnico/empresa responsável pela geração do arquivo digital | As informações apresentadas neste registro serão baseadas nos parâmetros informados no assistente da rotina. |
| Registro tipo 0990 – Encerramento do bloco 0 | Este registro indica a quantidade de linhas apresentadas no Bloco 0, incluindo o registro tipo 0990. |
| Registro tipo 9000 – Abertura do bloco 9 (controle e encerramento do arquivo digital) | Este registro indica se o bloco 9 (composto pelos registros 9900 e 9990) possui informações a serem apresentadas. |
| Registro tipo 9900 – Registro dos blocos | Este registro irá apresentar a quantidade de registros dos tipos 0, I, K e L processados. |
| Registro tipo 9990 – Encerramento do bloco 9 | Este registro indica a quantidade de linhas apresentadas no Bloco 9, incluindo o registro tipo 9990. |
| Registro tipo 9999 – Encerramento do arquivo digital | Este registro indica a quantidade total de linhas apresentadas em todo o meio magnético. |
| Registro tipo I001 – Abertura do bloco I (lançamentos contábeis) | Este registro indica se o bloco I (composto pelos registros I005, I050, I100, I150, I200 e I250) possui informações a serem apresentadas. |
| Registro tipo I005 – Identificação da escrituração contábil | As informações apresentadas neste registro serão baseadas nos parâmetros informados no assistente da rotina. |
| Registro tipo I050 – Plano de contas | Para usuários do SIGACON, as informações serão apresentadas com base no Plano de Contas cadastrado na tabela SI1. Para usuários do SIGACTB, as informações serão apresentadas com base no Plano de Contas cadastrado na tabela CT1. Em ambos os casos, somente será gerado o registro caso o parâmetro “Indicador de Movimento” do assistente da rotina, esteja preenchido com “0”, ou seja, com movimento. |
| Registro tipo I100 – Centro de custos | Para usuários do SIGACON, as informações serão apresentadas com base nos Centros de Custos cadastrados na tabela SI3. Para usuários do SIGACTB, as informações serão apresentadas com base nos Centros de Custos cadastrados na tabela CTT. Em ambos os casos, somente será gerado o registro, se o parâmetro “Indicador de Movimento”, do assistente da rotina, estiver preenchido com “0”, ou seja, com movimento, e a descrição do centro de custo não esteja em branco. |
| Registro tipo I150 – Saldos mensais | Para usuários do SIGACON, as informações serão apresentadas com base no Plano de Contas cadastrado na tabela SI1, calculando os saldos mensais de cada conta. Para usuários do SIGACTB, as informações serão apresentadas com base nos Saldos Mensais (AT7), apenas para saldos em que a classe da conta seja igual a “2” (Analítica). Em ambos os casos, somente será gerado o registro, se o parâmetro “Indicador de Movimento”, do assistente da rotina, estiver preenchido com “0”, ou seja, com movimento. |
| Registro tipo I200 – Lançamento contábil | Para usuários do SIGACON, as informações serão apresentadas com base nos lançamentos na tabela de Itens/Bonificação Financeira (AI2). Para usuários do SIGACTB, as informações serão apresentadas com base nos lançamentos na tabela de Itens/Bonificação Financeira (AT2). Em ambos os casos, somente será gerado o registro, se o parâmetro “Indicador de Movimento”, do assistente da rotina, estiver preenchido com “0”, ou seja, com movimento, e a data dos lançamentos esteja contida no período informado para geração do meio magnético. |
| Registro tipo I250 – Saldo das contas de resultado antes do encerramento | Para usuários do SIGACON, as informações serão apresentadas com base no Plano de Contas cadastrado na tabela SI1. Para usuários do SIGACTB, as informações serão apresentadas com base no Plano de Contas cadastrado na tabela CT1. Em ambos os casos somente será gerado o registro, se o parâmetro “Indicador de Movimento”, do assistente da rotina, estiver preenchido com “0”, ou seja, com movimento, buscando o saldo da(s) conta(s) de resultado informada(s) noparâmetro “Conta(s) Analítica(s) de Resultado”. |
| Registro tipo I990 – Encerramento do bloco I | Este registro indica a quantidade de linhas apresentadas no Bloco I, incluindo o registro tipo I990. |
| ***Registro tipo K001 – Abertura do bloco K (folha de pagamento)*** | ***Este registro indica se o bloco K (composto pelos registros K050, K100, K150, K200, K250 e K300) possui informações a serem apresentadas.*** |
| ***Registro tipo K050 – Cadastro de trabalhadores*** | ***Este registro é gerado com base no Cadastro de Funcionários (SRA) e Funções (SRJ).*** |
| ***Registro tipo K100 – Lotação*** | ***Este registro é gerado com base no SI3 (Usuário do SIGACON) ou no CTT (Usuários do SIGACTB).*** |
| ***Registro tipo K150 – Proventos e descontos*** | ***Este registro é gerado com base no Cadastro de Verbas (SRV).*** |
| ***Registro tipo K200 – Contabilização da folha de pagamento*** | ***Este registro refere-se à contabilização da folha de pagamento, informando o histórico de contabilização de todas as verbas. Para a sua implementação, foi necessária a criação de uma nova tabela (RCZ), para armazenar os dados da contabilização da folha de pagamento. Foi também necessário o desenvolvimento de uma rotina para compatibilização das tabelas. A rotina GPEM110A deve ser executada toda vez em que for gerado um arquivo MANAD de um período que ainda não tenha sido gerado. Ela lerá os lançamentos contábeis feitos anteriormente e os armazenará na tabela RCZ, discriminando qual verba gerou lançamentos para determinada conta contábil/centro de custo. Se houve alterações no cadastro de lançamento padronizado, o backup desta tabela (SI5/CT5) deve ser retornado para que depois seja executada a rotina GPEM110A.*** |
| ***Registro tipo K250 – Mestre de folha de pagamento*** | ***Este registro é gerado com base no Cadastro de Funcionários (SRA) e Acumulados Anuais (SRD).*** |
| ***Registro tipo K300 – Itens de folha de pagamento*** | ***Este registro é gerado com base na tabela de Acumulados Anuais (SRD).*** |
| ***Registro tipo K990 – Encerramento do bloco K*** | ***Este registro indica a quantidade de linhas apresentadas no Bloco K, incluindo o registro tipo K990.*** |
| Registro tipo L001 – Abertura do bloco L (registros de natureza financeira e orçamentária) | Este registro indica se o bloco L (composto pelo registro L050) possui informações a serem apresentadas. |
| Registro tipo L750 – Fornecedores | Serão apresentados neste registro todos os fornecedores cadastrados no sistema. |
| Registro tipo L990 – Encerramento do bloco L | Este registro indica a quantidade de linhas apresentadas no Bloco L, incluindo o registro tipo L990. |

**Observação:**Os registros destacados são aqueles que pertencem ao módulo de Folha de Pagamento.  
  
**Saiba Mais**[Artigos sobre Manad](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360008157193-RH-MANAD)
