---
content_hash: c95fb01ad673d726d1dbacc4c0e15bf52d734b05f4582505b3a2e14c23659308
fetched_at: '2026-06-29T00:10:09.398829+00:00'
page_id: '452719656'
product: rm
source: tdn-rm
title: Dicas - Abono Salarial
type: documentation
url: https://tdn.totvs.com/display/LRM/Dicas+-+Abono+Salarial
version: 2
---

**Abono Salarial**   
    
 É um benefício equivalente a 1 salário mínimo, vigente na data de pagamento, assegurado ao trabalhador cadastrado como participante do PIS/PASEP ou Cadastro Nacional de Informações Sociais – CNIS (a partir de outubro de 1988), que satisfaça as condições legais para o seu recebimento.

**Tem direito ao Abono Salarial o trabalhador que:**  
 • Estar cadastrado ha pelo menos 5 anos no PIS/PASEP.

• Ter recebido, de empregadores contribuintes do PIS/PASEP, remuneração mensal de até 2 salários mínimos médios durante o ano base que for considerado.

• Ter exercido atividade remunerada, durante pelo menos 30 dias, no ano base considerado para apuração.

• Ter seus dados informados corretamente na RAIS.

**Não tem direito ao Abono Salarial as seguintes categorias de trabalhadores:**

• Trabalhador urbano vinculado a empregador Pessoa Física.

• Trabalhador rural vinculado a empregador rural Pessoa Física.

• Diretor sem vínculo empregatício, mesmo que a empresa tenha optado pelo recolhimento do FGTS.

• Empregado doméstico. • Menores aprendizes.                                                                                                                                         (Fonte: [{+}](http://www.caixa.gov.br)<http://www.caixa.gov.br+>)  
    
    
 **Procedimentos PIS**  
 **1º Passo:**  Instalar o programa SXPIS fornecido pela CEF(Caixa Econômica Federal).

**2º Passo:**  Obter na agência conveniada com a empresa, o arquivo com as informações necessárias para o pagamento do PIS EMPRESA. Este arquivo terá um formato numérico.

**Exemplo: "12345678.912"** 

**3º Passo:** Acessar o programa SXPIS e importar o arquivo fornecido pela CEF.  

**4º Passo:**

Liberar os recursos.

Após a "Liberação dos Recursos" será gerado dentro do diretório C:\CAIXA, um arquivo texto com o mesmo nome do arquivo fornecido pela CEF. De acordo com o exemplo mencionado no passo 2 seria: "12345678.912". Este arquivo é reservado ao uso da empresa e contém os dados dos trabalhadores com o pagamento previsto para o crédito na folha de pagamento.

**Observações:**

A importação do valor do PIS será processada da seguinte forma para funcionários que tem a MESMA Data de Nascimento e número do PIS:

**1) Funcionários com chapas distintas (um ativo e um demitido):** A importação do evento de CC125 (Pagamento de PIS) se dará na movimentação somente para o funcionário que está na situação de Ativo.

**2) Funcionários com chapas distintas (os dois registros ativos):** A importação do evento de CC125 (Pagamento de PIS) se dará na movimentação somente para um dos funcionários que está na situação de Ativo.

**3) Funcionários com situação de demitido (demissão no mês, em meses anteriores e próximo mês):** A Importação não será realizada e os erros serão registrados no arquivo de Log de Inconsistências. **Procedimentos PASEP**

Caso o Banco do Brasil tenha enviado o arquivo fpsf909, verifique as pendências junto ao mesmo através do programa PASEPFOG. Se todas as pendências forem solucionadas, o Banco do Brasil enviará o arquivo fpsf910, arquivo este que deverá ser importado no Totvs Folha de Pagamento.
