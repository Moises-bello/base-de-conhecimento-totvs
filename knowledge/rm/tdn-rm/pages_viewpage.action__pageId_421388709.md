---
content_hash: 872521c9239635bf6322562d7dd03a5a4286e2422f6de543232d9b80364dad33
fetched_at: '2026-06-29T00:09:18.516094+00:00'
page_id: '421388709'
product: rm
source: tdn-rm
title: FIN - Retorno de Débito Automático
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388709
version: 2
---

A importação de arquivos de retorno de Débito Automático é um processo, que consiste em baixar automaticamente os Lançamentos Financeiros por meio de importação de arquivos disponibilizados pela rede Bancária. Neste processo, a baixa será realizada automaticamente desde que o arquivo de retorno possua os dados requeridos, assim como data de crédito, valor do crédito, motivo de ocorrência específica para baixas ou quitações, entre outras informações importantes.

Tipos de Retorno:

**Febraban CNAB 150 posições**

Será utilizado na importação de retornos de Débito Automático de arquivos com 150 colunas.

Tratamento do Registo "B" padrão FEBRABAN CNAB 150  
No retorno do débito automático o sistema receberá o arquivo e caso encontre o registro "B" irá identificar o cliente/fornecedor, caso o registro não seja encontrado será retornado um log informando que o registro não foi encontrado.  
 Se o registro for encontrado ele verificará a posição 150 do registro, essa posição armazena o código do movimento (1 ou 2), sendo:

* Exclusão do cadastro do débito automático.

O registro de dados bancários de "Débito Automático" deverá ser desativado. Esse registro deverá ser retirado do default de dados bancários para o cliente.

* Cadastro do débito automático nos dados bancários do cliente.

O banco será preenchido com o banco do retorno e a agência e a conta corrente serão preenchidas com as informações retornadas nos campos Agência para Débito. Esse registro deverá ser definido como default de dados bancários para o cliente.

**Febraban  CNAB 240 posições**

Será utilizado na importação de retornos de Débito Automático de arquivos com 240 colunas.

Após a importação do retorno de Débito Automático:

* A baixa do titulo será realizada automaticamente.
* Será  gerado um item de baixa correspondente ao valor baixado. (Anexo /Baixas do Lançamento)
* O Saldo da conta caixa indicada será atualizado.
* A contabilização da baixa será realizada de acordo com o evento contábil indicado no retorno ou o   evento associado à tabela default para a contabilidade.
* No Gestão Contábil, Manutenção de Lotes, deverá haver a contabilização no lote específico para o processo.

**Parâmetros da Importação**

Nesta tela do retorno de débito automático tem a opção para definirmos a ação ser adotada quando o valor pago for a menor ou a maior e esta definição pode ser fixada nos parâmetros de cobrança eletrônica (Opções |Parâmetros | 02.02 - Cobrança Eletrônica). Portanto, esta opção somente será aplicada se a diferença entre o valor líquido do Lançamento e o valor do crédito no arquivo de retorno for inferior ao valor estipulado para baixa parcial ou Adiantamento definidos pelos parâmetros.

Exemplo

Valor líquido do Lançamento = 600,00  
 Valores do crédito do arquivo de retorno = 500,00

**Parametrização do sistema**

* Diferença para geração da baixa parcial = 50,00

Nesse caso, ao importar o retorno será gerada uma baixa parcial de 500,00, indiferente se for informado "valor a menor = desconto", porque a diferença de 100,00 é superior ao valor indicado nos parâmetros.   
 Se o valor do crédito no arquivo de retorno fosse 560,00 a diferença equivalente a 40,00 seria reconhecida como "Desconto" ou outro valor que você determinasse no momento da importação do retorno.

* Diferença para geração de Adiantamento = 150,00

Ao importar um arquivo de retorno cujo valor do credito for superior ao valor líquido do Lançamento, a ação será tomada conforme o valor informado nesse parâmetro.

Exemplo

     Valor líquido do Lançamento = 600,00  
      Valores do crédito do arquivo de retorno = 800,00

O lançamento será totalmente quitado e será gerado um lançamento do tipo "Adiantamento" pelo valor de 200,00 baixado. Consequentemente será gerado um Lançamento tipo Crédito de Adiantamento no mesmo valor.  
 Se o valor da diferença for inferior a 150,00, o sistema irá reconhecer essa diferença no campo indicado no momento da importação do retorno.

**Observação:**

O sistema oferece outro recurso (parâmetros da integração Bancária) que é considerar os valores do arquivo de retorno sobrepondo dos Lançamentos.   
 Nesse caso, os acréscimos e descontos serão destacados no arquivo de retorno e serão reconhecidos em cada lançamento no momento da importação.

Exemplo

Valor original = 100,00

Juros            =     1,00

Valor liquido = 101,00

No arquivo de retorno os juros informados foram de 1,20. Após a importação do retorno, o valor dos juros do lançamento será reconhecido por 1,20.  
 Utilizar Conta/Caixa do Lançamento: A baixa será realizada utilizando a conta caixa do lançamento ao invés de usar a conta caixa informada no momento da importação do retorno.

**Dica**

Ao importar o arquivo de retorno, o sistema identifica os lançamentos pelo IDBOLETO e produz a baixa total ou parcial de todos os Lançamentos de mesmo IDBOLETO.  

Como identificar o IDBBOLETO no arquivo de retorno? Nas posições que identificam o lançamento para baixa deverá ter o numero UM logo após a Coligada, ou seja, CODIGO DA COLIGADA(com 3 dígitos) + UM + IDBOLETO  

Exemplo   0011000000000000000006974, onde:  

001 = Código da Coligada

1 = Caracteriza que é um IDBOLETO

000000000000000006974 = IDBOLETO
