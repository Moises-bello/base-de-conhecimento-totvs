---
content_hash: c78cfeeb3836347b531067d861805fda58ed14564f5f37cfef81928b0ac9d146
fetched_at: '2026-06-29T00:11:07.026107+00:00'
page_id: '63866255'
product: rm
source: tdn-rm
title: RMCTB006_Instrução Normativa 86 - Saldus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=63866255
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | Totvs Gestão Contábil – **Versão:** 11.5x |
| **Processo** | : | Instrução Normativa 86 |
| **Subprocesso** | : | Rotinas Legais |
| **Data da publicação** | : | 24/07/2013 |

 **Introdução**  
   
A Instrução Normativa N.º 86 é uma das exigências da Legislação Fiscal vigente no país:   
  
"As pessoas Jurídicas que utilizarem sistemas de processamento eletrônico de dados para registrar negócios e atividades econômicas, escriturar livros ou elaborar documentos de natureza contábil/fiscal e que no balanço de 31 de dezembro do ano do calendário imediatamente anterior, possuírem patrimônio líquido superior a 2.000.000 de UFIR, ficam obrigados a apresentar aos Auditores Fiscais do Tesouro Nacional, no exercício da suas atividades, os arquivos magnéticos correspondentes, nas formas e prazos estabelecidos."

**DESENVOLVIMENTO/PROCEDIMENTO**   
  
Acesse 'Rotinas Legais' / 'Instrução Normativa 86, preencha os seguintes campos e execute o processo:   
  
**Dados relativos ao funcionário responsável pelas informações contidas nos arquivos:**

1. Nome
2. Telefone
3. CPF
4. FAX
5. E-MAIL

**Destino dos Arquivos:**  
Diretório no qual serão gravados os arquivos gerados:   
  
**Meio de Armazenamento:**

1. CD
2. Disquete
3. Conexão em Rede Local (LAN)
4. Transmissão Direta
5. Outro Meio Físico (opção default)

**Data Inicial / Data Final**  
Período relativo ao exercício base da apuração e geração dos arquivos.   
  
**Selecionar Filiais**  
Selecione a(s) filial(is) para que sejam filtradas as informações referentes a lançamentos e saldos.   
  
**Arquivos a serem gerados no diretório determinado (05 arquivos):**   
  
AnexoI01.txt - Lançamentos Contábeis;  
AnexoI02.txt - Saldos Contábeis;  
Leiame.txt;  
Tabela01.txt - Plano de Contas;  
Tabela02.txt - Centros de Custos.   
  
Em seguida no aplicativo da Receita: Sinco - Arquivos Contábeis:

* Acesse 'Arquivo' / 'Novo' / e informe os dados solicitados;
* Selecione o arquivo a ser importado (exemplo: Plano de Contas Diário Geral);
* Informe o valor dos campos 'Início' e 'Tamanho' conforme arquivo Leia-me.txt gerado pela rotina;
* Informe o Diretório do arquivo em questão, gerado pelo RM Saldus;
* Após a importação dos arquivos, acesse 'Arquivo' / 'Validar' e verifique os valores apresentados.

**INFORMAÇÕES ADICIONAIS**   
  
Foram geradas versões do Sistema e da Biblioteca com atualizações, correções e otimizações referente ao processo de geração da Instrução Normativa 86, sendo assim, somente realize a processo de citado utilizando a última versão da Biblioteca e do executável do RM Saldus. Aplicativos necessários para essas atualizações disponíveis no Portal da Totvs: <http://suporte.totvs.com/home>   
  
  
O Arquivo Leia-me.txt tem como intuito disponibilizar informações pertinentes à validação do arquivo no programa SINCO, em especial os corretos Layouts para validação de cada arquivo gerado.   
  
Somente arquivos na extensão '.txt' serão validos no SINCO.   
  
Vale ressaltar que os 'Processos' citados são definidos no perfil do usuário. Obs.: 'Cadastros' / 'Segurança' / 'Perfis' / 'Acesso a Menus' / 'RM Saldus' / 'Rotinas Legais'.   
  
O RM Saldus não realiza a geração dos arquivos auxiliares, sendo assim, durante a seleção dos arquivos no Sinco não marque as opções: Plano de Contas Diário Auxiliar, Lançamentos Diário Auxiliar e Saldus Diário Auxiliar.
