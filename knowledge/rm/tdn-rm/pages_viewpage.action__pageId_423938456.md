---
content_hash: efcfbde12055be9e283e785e26351ac2b3b0caee5de997bb0d03c6fe541e3fa8
fetched_at: '2026-06-29T00:09:27.230758+00:00'
page_id: '423938456'
product: rm
source: tdn-rm
title: Importação de Abastecimento GoodCard EcoFrotas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938456
version: 11
---

Utilizando a ferramenta de Conceito do TOTVS Business Conector é possível importar os abastecimentos gerados pelo GOOD Card através de um arquivo .txt e gerar uma apropriação para os objetos de manutenção do TOTVS Manutenção.   
Essa funcionalidade permite que as empresas que utilizem o GoodCard possam importar seus abastecimentos e ter um maior controle do que está sendo gasto.

**Parametrização e Importação do Lyout Good Card**

**1º) Parâmetro "Controla Apropriação Direta de Produtos"**

O parâmetro "Controla Apropriação Direta de Produtos", dentro dos parâmetros do TOTVS Manutenção, deverá ser marcado para que a integração com GoodCard possa ser utilizada.

**2º) Cadastro de Tipos de Movimentos de Abastecimento**  
Será necessário criar um cadastro de Tipos de Movimentos que podem ser utilizados para importar abastecimento.   
Esse movimento deverá ser criado no TOTVS Gestão de Estoque, Compras e Faturamento.   
O usuário poderá definir nos parâmetros do sistema um tipo de movimento default para Tipo de Abastecimento Posto Interno e Tipo de Abastecimento Posto Externo acessando TOTVS Manutenção | Opções | Parâmetros | Sistema | Aba - Movimentos.  
Após os movimentos de posto interno e externo serem criados os mesmos deverão ser informados dentro do parâmetro "Controla Apropriação Direta de Produtos" no TOTVS Manutenção.

|  |  |  |  |
| --- | --- | --- | --- |
| **Nome do Campo** | **Tipo** | **Obrigatório** | **Descrição** |
| CODTMVABASTECIMENTOINTERNO | VARCHAR (10) | Não | Tipo de Mvto de Abastecimento Interno |
| CODTMVABASTECIMENTOEXTERNO | VARCHAR (10) | Não | Tipo de Mvto de Abastecimento Externo |

 Será necessário configurar os tipos de movimentos da seguinte maneira:  
  Tipo dos Itens  = Ambos (Etapa Item – Identificação);      Aceitar preço zero (Etapa Item – Preços);     Utilizar Desconto marcado (Etapa Item – Valores Financeiros);   -  Afeta Desconto do Movimento marcado (Etapa Item – Valores Financeiros);     Utilizar Despesa marcado (Etapa Item – Valores Financeiros);   -  Afeta Despesa do Movimento marcado (Etapa Item – Valores Financeiros);   -  Associar objeto de oficina ao item de movimento (Etapa Manutenção).  
  
**3º) Cadastro de Tipo de Material**  
Este cadastro poderá ser acessado através do menu Cadastros | Tabelas Auxiliares | Tipo Material (GoodCard) e já virá preenchido no sistema com os dados abaixo:

| Sigla | Descrição |
| --- | --- |
| AL | Álcool |
| DI | Diesel |
| GA | Gasolina Aditivada; |
| GC | Gasolina Comum; |
| GN | GNV |
| OL | Óleo Lubrificante. |

**4º) Cadastro de Tipo de Serviço**  
Este cadastro poderá ser acessado através do menu Cadastros | Tabelas Auxiliares | Tipo Serviço (GoodCard) e já virá preenchido no sistema com os dados abaixo:

* Abastecimento;
* Troca de óleo;
* Lavagem Expressa;
* Lavagem Completa;
* Manutenção;
* Óleo Lubrificante;
* Filtro de Ar;
* Filtro de Óleo;
* Filtro Combustível;
* Extintor;
* Fluído Freio;
* Fluído Radiador;
* Conserto Pneu;
* Graxa;
* Geometria;
* Balanceamento;
* Montagem / Desmontagem Pneu;
* Manutenção em Oficina;
* Querosene.

**5º) Parâmetros do Produto – Informações Manutenção**  
Neste cadastro deve ser realizado o vinculo do Produto/Serviço do RM com o tipo de Material/Serviço do GoodCard EcoFrotas. Os parâmetros de Produto – Informações de Manutenção é um anexo do cadastro de Produto/Serviço. Não será permitido vincular mais de um produto ao material do GoodCard e mais de serviço ao mesmo código de serviço do GoodCard.  
  
**6º) Importação dos dados**  
Para realizar a importação dos dados do GoodCard EcoFrotas será necessário importar o Conceito criado, através do módulo **Integração | Conceito**. Neste Conceito deve ser configurado o caminho onde se encontra o arquivo texto do GoodCard.   
Após configurar o local do arquivo, deve-se executar o processo "Processar novo conceito" disponível na visão. Ao realizar a importação dos dados, se o layout estiver correto, deverá será criado Apropriação Direta de Produto para os registros que constam no arquivo de importação. Para visualizar a apropriação feita acesse **TOTVS Manutenção | Operações | Apropriação Direta de Produtos**  
As inconsistências encontradas serão gravadas em um log com seu respectivo detalhamento. Somente as informações localizada no campo Detalhe do Arquivo serão gravadas na apropriação. Os campos de Header e Trailler não serão gravados na base.   
Veja abaixo como é e como funciona o layout GoodCard:  
  
**Layout composto de 03 tipos de registros: Header, Detalhe e Trailler**

**Header - Primeira Linha do Arquivo de Transferência**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Posição** | **Nome do Campo** | **Tipo** | **Tamanho** | **Dec** | **Descrição** |
| 001 a 003 | ID\_Reg | A | 03 |  | ID Tipo do Registro  (000) |
| 004 a 017 | CNPJ\_Emi | A | 14 |  | CNPJ Emissor |
| 018 a 049 | ID\_Emi | A | 32 |  | Identificação Emissor |
| 050 a 057 | Dt\_Preg | A | 08 |  | Data Primeiro Registro (DDMMAAAA) |
| 058 a 061 | Hr\_PReg | A | 04 |  | Hora Primeiro Registro (HHMM) |
| 062 a 069 | Dt\_UReg | A | 08 |  | Data Ultimo Registro (DDMMAAAA) |
| 070 a 073 | Hr\_UReg | A | 04 |  | Hora Ultimo Registro (HHMM) |
| 074 a 096 | DtHr\_Gera | A | 23 |  | Data/Hora da Geração do Arquivo |
| 097 a 150 | Periodo | A | 50 |  | Período de Apuração da Informação |

*****Atenção!***:** O valor do campo ID\_reg será sempre igual a "000" para o registro HEADER

**Detalhe - Dados Transferidos**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Posição** | **Nome do Campo** | **Tipo** | **Tamanho** | **Dec** | **Descrição** |
| 001 a 003 | ID\_Reg | A | 03 |  | ID tipo do Registro (100) |
| 004 a 007 | Num\_Seq | N | 04 |  | Numero Seqüencial |
| 008 a 015 | Dt\_Trans | A | 08 |  | Data Transação (DDMMAAAA) |
| 016 a 026 | Vl\_Trans | N | 11 | 2 | Valor em Reais |
| 027 a 042 | Num\_Cart | A | 16 |  | Numero do Cartão |
| 043 a 048 | Qt\_Mater | N | 05 | 2 | Quantidade de Material Usado |
| 049 a 050 | Tp\_Mater | A | 02 |  | Tipo de Material |
| 051 a 080 | Servico | A | 30 |  | Código do Serviço |
| 081 a 091 | Tp\_Abast | N | 11 |  | Tipo do Abastecimento |
| 092 a 98 | Placa | A | 07 |  | Placa do Veículo |
| 99 a 105 | Hodom | N | 07 |  | Hodômetro Veículo no Abastecimento |
| 106 a 119 | CNPJ\_Estab | A | 14 |  | CNPJ Estabelecimento |
| 120 a 169 | Nome\_Estab | A | 50 |  | Nome do Estabelecimento |
| 170 a 199 | Info\_Ad01 | A | 30 |  | Informação Adicional 1 |
| 200 a 230 | Info\_Ad02 | A | 30 |  | Informação Adicional 2 |
| 231 a 259 | Info\_Ad03 | A | 30 |  | Informação Adicional 3 |
| 260 a 270 | Matric | A | 10 |  | Código do Motorista.  Apenas os seis primeiros caracteres serão utilizados. |
| 271 a 275 | HR\_Transação | A | 5 |  | Hora da Transação |

*****Atenção!***:** O valor do campo ID\_reg será sempre igual a "100" para os registros DETALHE.

**Trailler - Última Linha do Arquivo de Transferência**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Posição** | **Nome do Campo** | **Tipo** | **Tamanho** | **Dec** | **Descrição** |
| 001 a 003 | ID\_reg | A | 03 |  | ID Tipo do Registro (200) |
| 004 a 009 | Qt\_reg | N | 06 |  | Quantidade de Registros Enviados |
| 010 a 019 | Tot\_mater | N | 10 | 2 | Totalizador de Material Usado |
| 020 a 029 | Tot\_valor | N | 10 | 2 | Totalizador de Valor em Reais |

*******Atenção!*****:** O valor do campo ID\_reg será sempre igual a "200" para os registros TRAILLER  
  
**Veja um exemplo de layout:**  
  
00003506307000157GOODCARD                        240520110222082405201102220824/05/2011 00:00:00    24052011 a 24052011 10000010110201300000100,006035740302889818000001GCAbastecimento                 1          HMO7450000225089420590000115LOCAMINAS RENT A CAR LTDA                                                                                                                   00017     15:10  
2000000010000070,020000100,00  
  
***Importante*!**O sistema não controlará os valores carregados nos cartão GoodCard.

Informações Adicionais


* [TOTVS Business Connect - Parâmetros](http://tdn.totvs.com/pages/viewpage.action?pageId=425459433)
* [TOTVS Business Connect - Conceito](http://tdn.totvs.com/display/LRM/TOTVS+Business+Connect+-+Conceito)
