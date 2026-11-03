---
content_hash: 62abd50e3c288c30ab0a5b5af1520a1354c2d06f6da4bcc57d620566cb132a26
fetched_at: '2026-06-29T00:11:07.021462+00:00'
page_id: '63866246'
product: rm
source: tdn-rm
title: RMCTB005_MANAD - Saldus
type: documentation
url: https://tdn.totvs.com/display/LRM/RMCTB005_MANAD+-+Saldus
version: 8
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | Totvs Gestão Contábil – **Versão:** 11.5x |
| **Processo** | : | MANAD |
| **Subprocesso** | : | Rotinas Legais |
| **Data da publicação** | : | 24/07/2013 |

MANAD é o Manual Normativo de Arquivos Digitais onde constam todas as informações para gerar o arquivo digital a ser apresentado à fiscalização da Secretaria da Receita Previdenciária quando a empresa for intimada por Auditor Fiscal da Previdência Social (AFPS).   
  
Segundo legislação vigente, as empresas que utilizam sistema de processamento eletrônico de dados para registrar seus negócios e atividades econômicas, escrituração de livros ou produção de documentos de natureza contábil, fiscal, trabalhista e previdenciária, que forem intimadas devem apresentar os arquivos digitais contendo dados relativos aos seus negócios e atividades econômicas, seguindo as especificações e orientações do MANAD (Manual Normativo de Arquivos Digitais) e de acordo com a fiscalização da SRP (Secretaria da Receita Previdenciária), bem como a documentação técnica completa e atualização de seus sistemas.   
  
Desta forma, as empresas que utilizarem o referido sistema de processamento eletrônico de dados deverão submeter previamente os arquivos digitais ao Sistema de Validação e Autenticação de Arquivos Digitais (SVA), antes de fornecê-los ao auditor fiscal requisitante, para verificar se os arquivos estão em conformidade com o padrão estabelecido no MANAD e, se for o caso, corrigir todos os erros e eventuais divergências apontadas pelo referido sistema.   
  
Fonte: <http://totvsconnect.blogspot.com.br/2011/02/como-fazer-totvs-gestao-contabil.html>   
  
**DESENVOLVIMENTO/PROCEDIMENTO**   
  
Para realizar o processo de geração do arquivo MANAD, acesse o menu "**Rotinas Legais / MANAD 1.0.0.2.**"

* Pasta **"Centralização da Escrituração**":

* + **Estabelecimento sem centralização de escrituração:** quando essa opção é a selecionada, não é possível selecionar filiais para emitir o relatório. A coligada é considerada como contribuinte.

* + **Estabelecimento centralizador de escrituração:** quando essa opção é a selecionada, é apresentado o filtro de filiais para que seja informado o estabelecimento centralizador da escrituração. A coligada é considerada como contribuinte.

* + **Estabelecimento com escrituração centralizada:** quando essa opção é a selecionada, é necessário selecionar apenas uma filial para emitir o relatório.A filial selecionada é considerada como contribuinte.

* Pasta "**Contribuinte**": Nessa pasta será possível informar os dados do contribuinte e também selecionar a finalidade do arquivo:

* + **Solicitação de Auditor-Fiscal da Secretaria da Receita Previdenciária através de MPF:** quando a finalidade do arquivo é cumprir um Mandado de Procedimento Fiscal proveniente de uma solicitação de um auditor fiscal da Secretaria da Receita Previdenciária.

* + **Entrega na Secretaria da Receita Previdenciária - Movimento anual de órgão público, conforme intimação:** quando a finalidade do arquivo é a **entrega no movimento anual de órgão público conforme intimação, junto à secretaria da receita previdenciária.**

* + **Dados Internos UF:** quando a finalidade é suprir alguma necessidade do estado.

* Pasta "**Contabilista**"**:** Nessa pasta deverão ser preenchidas todas as informações referentes ao contabilista;

* Pasta "**Informática**"**:** Nessa pasta deverão ser preenchidos os dados de início/fim da prestação dos serviços de informática da empresa responsável pelo sistema, o nome do arquivo digital que será gerado, e também o período para geração do arquivo (Data Inicial e Data Final);

* Pasta "**Escrituração Contábil**"**:** Deverá ser informado o tipo de escrituração contábil utilizada pela empresa, normalmente a escrituração contábil mais utilizada é o tipo **"Diário Geral".** O tipo de escrituração **"Diário Auxiliar"** é utilizado pelas empresas que trabalham com escrituração contábil resumida, que é permitida pela legislação;

* Pasta "**Classificação das Contas**"**:** Deverão ser informados os grupos contábeis referentes a cada tipo de conta: **Ativo, Passivo, Patrimônio Líquido, Despesas, Custos e Receitas;**

* Pasta "**Resultado do Exercício**": Nessa pasta, deverão ser preenchidas as informações referentes ao encerramento do exercício, como **Data de Apuração do Resultado**, C**ontas de Resultado** e **Histórico de Fechamento** que foi utilizado na Apuração do Resultado;

**Observação**:   
  
Na pasta **"Resultado do Exercício"** temos que informar as contas de resultado que foram encerradas. Mas neste caso temos que informar o intervalo da primeira conta re resultado (Conta Sintética), até a última conta de resultado (Conta Analítica). Por exemplo:

 

 Na tela acima foi informado a primeira conta sintética que possui o código 3 e a última conta analítica de resultado que possui o código 4.3.2.   
  
Após preencher todas as informações, deve-se clicar no botão "**OK**", então o arquivo será gerado com base nas informações passadas nesta rotina.

 **INFORMAÇÕES ADICIONAIS**   
  
Nos lançamentos que serão enviados para o MANAD, os campos **'Histórico Padrão'** e '**Complemento do Histórico'** devem estar preenchidos. Será mostrado um erro na validação referente aos lançamentos que estão sem **Complemento de Histórico** e sem **Histórico Padrão**.   
  
Ex: Vamos supor que exista uma lançamento/partida na base de dados dentro do período informado para geração do arquivo que não possui o **histórico padrão** e também não possui **complemento de histórico.** Na validação do arquivo ocorrerá mensagem de erro para este lançamento.   
  
O MANAD gerado no RM Saldus não leva as informações referentes ao Bloco "K" que deve ser gerado pelo RM Labore. Desta forma o RM Saldus gerá apenas as informações referentes ao bloco "I".   
  
O validador do MANAD, o SVA encontra-se disponível no site da Receita Federal do Brasil (RFB), no seguinte endereço http://www.recei\_Hlt336969478\_Hlt336969479ta.fazenda.gov.br/ <http://www.receita.fazenda.gov.br/>   
  
Vale ressaltar que os 'Processos' citados são definidos no perfil do usuário. Obs.: 'Cadastros' / 'Segurança' / 'Perfis' / 'Acesso a Menus' / 'RM Saldus' / 'Rotinas Legais'.
