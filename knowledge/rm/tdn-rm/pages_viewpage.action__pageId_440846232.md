---
content_hash: cdbbb017542d14606e67728a85bf79d00b4efe6caa7748a6df4a8b281cf927ef
fetched_at: '2026-06-29T00:09:53.630754+00:00'
page_id: '440846232'
product: rm
source: tdn-rm
title: FIN - Novidades da versão 12.1.17
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440846232
version: 4
---

**12.1.17 - Registro online para Boletos criados**  
Melhoria no Processo de [Registrar Online os Boletos](http://tdn.totvs.com.br/display/LRM/Registro+Online+de+Boletos), para ser executado para boletos existentes e não remetidos.  
**12.1.17 - Criação do**[**Cubo**](http://tdn.totvs.com.br/display/LRM/Financeiro+-+Cubos)**de Valores Recebíveis/Pagáveis na data vigente pelo Vlr. Líquido**  
Criado o cubo "Valores Recebíveis/Pagáveis na data vigente pelo vlr. Líquido" para visualizar os lançamentos em aberto e parcialmente baixado de um determinado período de vencimento.  
**12.1.17 - Melhoria no**[**convênio**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388845)**para boleto online do banco Bradesco**  
Criado no convênio os campos para configuração do Registro Online de boletos do banco Bradesco.  
**12.1.17 - Melhoria na**[**Conciliação de Titulos de Cobrança**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388540)  
Adicionado o campo *Raiz do CNPJ* para melhorar a pesquisa de lançamentos para conciliação.  
**12.1.17 - Melhoria nos Anexos de Vínculos**  
Incluído na visão do anexo de [Vínculos do lançamento](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388665)o campo "Valor Vínculo" que irá exibir o valor usado para o vínculo entre os dois lançamentos.  
**12.1.17 -**[**Controlar Concorrência na baixa de Lançamentos**](http://tdn.totvs.com.br/display/LRM/Contas+a+pagar)  
Melhoria no processo de baixa para não ser gerado item de baixa duplicado quando mais de um usuário executar simultaneamente os processos referente a baixa de lançamento. Ao habilitar o parâmetro  "[Controlar Concorrência na baixa de Lançamentos](http://tdn.totvs.com.br/display/LRM/Contas+a+receber)" localizado em Contas a Pagar / Receber | Baixa | Manutenção de baixa | Baixa 2/5, somente um dos usuários conseguirá realizar a baixa com sucesso, os demais terão o processo bloqueado por concorrência.  
Caso algum lançamento fique bloqueado ao final do processo que está sendo executado, será necessário executar o processo "[Corrigir Lançamentos Bloqueados por concorrência](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388645)".  
**12.1.17 - Melhoria no**[**Repasse Automático**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388575)  
Para lançamentos do TIN, foi incluída a alternativa da contabilização do lançamento de Repasse automático ser realizada através do  default contábil da subunidade.  
**12.1.17 - Criado a coluna "Fornecedor" na visão de DDA - Débito Direto Autorizado.**  
Na visão de DDA - Débito Direto Autorizado e no processo de Conciliar Títulos em Cobrança foi criado a coluna "Fornecedor". Conforme o layout bancário de DDA será preenchido na visão as informações do arquivo de captura.  
**12.1.17 - Melhoria no**[**Retorno de Débito Automático**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388709)**.**  
Melhoria no retorno de debito automático, ao realizar uma baixa com valor A MAIOR ou A MENOR e possível jogar o valor de diferença para o campo de juros, desconto ou opcional. Também e possível gerar baixa parcial do lançamento financeiro e gerar credito de adiantamento, seguindo o mesmo modelo do retorno de cobrança.  
**12.1.17 - Registro Online na**[**inclusão de boleto**](http://tdn.totvs.com.br/display/LRM/Registro+Online+de+Boletos)**.**  
A inclusão de boleto foi ajustada para comunicar com o serviço do banco e realizar o Registro Online do boleto, alterando o status da Remessa para Registrado Online.
