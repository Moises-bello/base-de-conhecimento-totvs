---
content_hash: 39de2d8f705fad94364d0b78b36eb87d53ecda2346574a8357da3f1372741ff5
fetched_at: '2026-06-29T00:09:26.071519+00:00'
page_id: '423938247'
product: rm
source: tdn-rm
title: Processo de Combustível (Informações Especificas)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938247
version: 10
---

O objetivo de orientar sobre as mudanças do processo de venda combustíveis, para atender a Legislação do Projeto SPED Fiscal – Decretos, Protocolos, Convênio ICMS e Ajustes SINIEF que regulamentam este projeto.  
O processo de Integração com o PDV não faz parte dessa documentação.  
***Atenção!***Para viabilização do processo, é necessário aplicar o pacote de atualizações da 11.82.32 ou superior e utilizar a **Integração com o PDV e SPED Fiscal**  
***Observação*:**Processo para a geração dos registros específicos do segmento (C171, 1300, 1310, 1320, 1350, 1360 e 1370).  
Haverá a citação da integração TOTVS Gestão de Estoque, Compras e Faturamento e o TOTVS Business Connect (TBC), não sendo o objetivo desse documento a descrição e a realização desse processo de integração, abordaremos apenas sobre a Venda de combustíveis, portando as demais configurações do 'TBC' e geração dos Registros do SPED fiscal devem ser verificados na documentação sobre esse processo.

**Pré-Condições Gerais**

* Executar os Scripts liberados;
* Após a execução do script será criado um parâmetro especifico para a funcionalidade;
* Ao alterar o parâmetro e salvar, teremos as seguintes consistências para movimentos parametrizados com tipo:
  + **Tipo de Operação de ajuste – Postos de Combustíveis** **=** **1 Perda**: deve ser permitida salvar somente se o mesmo estiver parametrizado, com Efeito sobre o Saldo Atual = Diminuir, já para movimentos parametrizados;
  + **Tipo de Operação de Ajuste – Postos de Combustíveis** = **2 Ganho:** deve ser permitido salvar somente se o mesmo estiver parametrizado o Efeito sobre o Saldo Atual = Aumentar;
* Após o Script verificamos que a funcionalidade somente será visível se alguma filial da coligada estiver parametrizada com a opção (Posto Varejista);
* Esta opção deve ser visualizada na Etapa | Mov – Outros Dados;
* Realizar o cadastro de bombas pertencentes ao cliente (Bomba/ Lacre de Bomba/ Bico de Bomba/Volume de Vendas). Essas opções encontram-se localizadas:
  + Menu Cadastros | Mais.... | Combustível | Bomba
  + Menu Cadastros | Mais.... | Combustível | Lacre de Bomba
  + Menu Cadastros | Mais.... | Combustível | Bico de Bomba
  + Menu Cadastros | Mais.... | Combustível | Volume de Vendas

O cadastro da Filial também deverá ser configurada como "Posto Varejista".   
Essa opção é selecionada no campo Tipo de Operação nos Anexos do cadastro da Filial, Dados Fiscais | pasta Tipo de Estabelecimento | campo Tipo de operação com combustível.  
Após a realização de todos esses procedimento o setor Fiscal estará apto a gerar o arquivo do SPED utilizando todo o agrupamento destas informações e enviar o arquivo do SPED gerado com os novos Registros já supracitados para a validação da Receita.  
As movimentações aqui feitas poderão ser originadas do PDV (Cupom Fiscal) normalmente, utilizando a impressora fiscal.  
Ao Excluir as movimentações, todo o processo de movimentação será desfeita, inclusive no quesito estoque, exceto o processo de integração com o "TBC", esse registro não pode e não poderá ser excluído apenas consultado.  
Parâmetro no Tipo de Movimento para classificar quanto ao "Tipo de Operação de Ajuste – Postos de Combustíveis" com as opções:

* 0 - Não usa (default)
* 1 - Perda
* 2 - Ganho

**Funções do Menu Envolvidas**

Menu | Integração | Monitor da Fila de Integração  
Menu | Cadastro | Mais... | Combustível | Bomba  
Menu | Cadastro | Mais... | Combustível | Lacre de Bomba  
Menu | Cadastro | Mais... | Combustível | Bico de Bomba  
Menu | Cadastro | Mais... | Combustível | Volume de Vendas  
Menu | Cadastro | Produto | Anexos | Dados Fiscais do Produto | "Guia Tributação"  
Menu | Ambiente | Parâmetros | Mov | Outras Dados  
Menu | Cadastro Filiais | Anexos | Dados Fiscais | "Guia" Tipo de Estabelecimento.

A Movimentação de Compra e Venda será realizada normalmente da mesma forma como já é feita hoje, configurações normais.  
Já as Movimentações de ajuste de Perda e Ganho poderá ser realizada utilizando a rotina de Outras Movimentações da mesma forma como já é feita hoje, porém vale ressaltar que uma movimentação de ajuste não poderão ser confundidas com uma COMPRA E VENDA em função do novo parâmetro (Perda\Ganho).
