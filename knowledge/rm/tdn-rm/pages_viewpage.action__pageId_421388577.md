---
content_hash: 2d4898890b1bfa9c2bef6513fc4cfe451867841cd3542014114ef1f5df81abee
fetched_at: '2026-06-29T00:09:17.096786+00:00'
page_id: '421388577'
product: rm
source: tdn-rm
title: Lançamento Padrão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388577
version: 9
---

O objetivo deste processo é possibilitar a inclusão de um ou vários Lançamentos Financeiros idênticos para um ou vários Clientes/Fornecedores, simultaneamente.  
O Lançamento Padrão é processado a partir de um Lançamento Financeiro por vez,  através do menu: Processos|Manutenção de Lançamentos|Lançamento Padrão. 

**Dados para Geração de Lançamento Padrão**

Quantidade: Informar a quantidade de lançamentos que serão gerados. 

Intervalo Vencimento em Dias: O intervalo de Vencimento em dias é o intervalo entre as datas de vencimento dos lançamentos a serem gerados, a partir da data preenchida no campo "Vencimento 1ª Parcela".  
Ao alterar este campo o sistema calcula o intervalo informado de acordo com a Data de Vencimento do lançamento de origem e altera o campo  “Data de Vencimento 1ª Parcela”.

Vencimento 1ª Parcela:  Ao iniciar o processo de Lançamento Padrão a Data de Vencimento 1ª Parcela é apresentada por default calculando 30 dias a partir da data de vencimento do Lançamento de origem.

Manter o mesmo dia de vencimento: Ativando esta opção o sistema irá manter o dia informado na Data Vencimento 1ª Parcela para todos os Lançamentos gerados, mas se o vencimento coincidir com um feriado ou no final de semana irá prevalecer o que estiver configurado nos parâmetros.

Intervalo (Emissão) em Dias: É o intervalo entre as datas de emissão dos lançamentos a serem gerados, a partir da data preenchida no campo "Emissão 1ª Parcela". Ao alterar este campo o sistema calcula o intervalo informado de acordo com a Data de emissão do lançamento de origem e altera o campo  “Data de Emissão 1ª Parcela”.

Emissão 1ª Parcela: Ao iniciar o processo de Lançamento Padrão a Data Emissão 1ª Parcela é apresentada por default calculando 30 dias a partir da data de emissão do Lançamento de origem.

Manter o mesmo dia do mês de emissão:  Ativando esta opção o sistema irá manter o dia informado na data de Emissão 1ª Parcela para todos os Lançamentos gerados, mas se a emissão coincidir com um feriado ou no final de semana irá prevalecer o que estiver configurado nos parâmetros.

Taxa Embutida de Capitalização %:  A Taxa Embutida de Capitalização é um adicional mensal de juros compostos aplicado no valor original do Lançamento a partir do segundo Lançamento gerado no processo de Lançamento Padrão.   
Gerar o Segundo Número sequencialmente: Ativando esta opção, o campo "Segundo Número" dos Lançamentos gerados será preenchido em ordem sequencial.

Gerar Número Documento de acordo com as opções: Quando essa opção Não estiver marcada, os campos Número Base, Separador e Parcela Inicial ficam desabilitados para edição.   
O campo número do documento dos Lançamentos gerados será preenchido de acordo com o que estiver definido no cadastro do “Tipo de Documento” do Lançamento original. Com essa opção marcada, a geração do “número do documento” dos lançamentos padrões gerados, tomará como base os dados informados nos campos: Número Base, Separador e Parcela Inicial.

Número Base: Este campo representa o “Número do documento” dos lançamentos gerados e terá um número único para todas as parcelas.

Separador: O campo é apresentado sem seleção, se não for selecionado um separador o Número Base será apresentado junto do número da parcela, se for selecionado será apresentado separado.

Parcela Inicial: é apresentado "um" como default podendo ser alterado. O número das outras parcelas será sequencial a este.

Não gerar lançamento a cada \_\_ ocorrência (s): definir um intervalo para não gerar Lançamento.  
  
**Exemplo:**   
1º Deve-se definir a quantidade de lançamentos a serem criados (campo Quantidade).  
Neste caso vamos usar o valor “4”;

2º Em seguida definir o intervalo de emissão.   
Valor informado “30 dias”;

3º No campo “Não gerar lançamento a cada: \_\_ Ocorrências”, será informado como valor: “2”;   
Neste exemplo então, teremos apenas dois lançamentos criados no processo, visto que a cada 2 registros que deveriam ser criados, o sistema irá desconsiderar o último, respeitando o intervalo de emissão definido acima.

IDLAN 1 (Gerado)  
IDLAN 2 (Desconsiderado)  
IDLAN 3 (Gerado)  
IDLAN 4 (Desconsiderado)  
  
Histórico: Será possível  preencher este campo com texto ou variáveis como [HIS] que irá buscar o histórico do Lançamento original e preencher todos os Lançamentos gerados com estas informações.

Gerar Lançamentos para vários Clientes / Fornecedores: Se for necessário gerar Lançamento para mais de um Cliente/Fornecedor, deve-se marcar esta opção e selecionar outros Clientes/Fornecedores para geração do Lançamento Padrão, além do que está informado no Lançamento selecionado para o processo.

Tabelas Defaults: Buscar do Cliente/Fornecedor: o sistema irá preencher os campos: Filial, Departamento, Centro de Custo, Tabelas Opcionais, Tipo de Documento, Conta Caixa, Tipo Contábil e Dado de Pagamento, dos novos lançamentos, utilizando as opções informadas nas tabelas defaults do cadastro de cliente/fornecedor.

Buscar do Lançamento: o sistema irá preencher os campos: Filial, Departamento, Centro de Custo, Tabelas Opcionais, Tipo de Documento, Conta Caixa, Tipo Contábil e Dado de Pagamento, dos novos lançamentos, utilizando as opções informadas nas tabelas do lançamento de origem.

Buscar do Lançamento se não houver Default no Cliente/Fornecedor: o sistema irá preencher os campos: Filial, Departamento, Centro de Custo, Tabelas Opcionais, Tipo de Documento, Conta Caixa, Tipo Contábil e Dado de Pagamento, dos novos lançamentos, utilizando as opções informadas nas tabelas defaults do cadastro de cliente/fornecedor. Se no cadastro de Cliente/Fornecedor não constar opção para alguma dessas tabelas, o sistema irá utilizar as opções informadas nas tabelas do lançamento de origem.

Contabilidade: Buscar do Evento Contábil do Lançamento: A contabilização dos novos lançamentos será  criada a partir do Evento Contábil usado no Lançamento de origem.

Buscar do Lançamento: A contabilização dos novos lançamentos será criada a partir da contabilização do lançamento de origem.

Rateio Centro de Custo / Departamento: Buscar do Cliente/Fornecedor: Com esta opção Ativa, o rateio por Centro de Custo e Departamento dos lançamentos a serem gerados será criada a partir do default informado no cadastro do referido cliente/fornecedor.

Buscar do Lançamento: Com esta opção Ativa, o rateio por Centro de Custo e Departamento dos lançamentos a serem gerados, será o mesmo rateio informado no lançamento de origem.
