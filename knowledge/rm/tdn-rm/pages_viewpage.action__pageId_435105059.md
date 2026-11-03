---
content_hash: 307430633da43a3e756ec939582a025076b172b547e27f8561de0728b1ac7e0b
fetched_at: '2026-06-29T00:09:47.745036+00:00'
page_id: '435105059'
product: rm
source: tdn-rm
title: Contratos de Venda - Processo - Gerar Movimento RPS - Recibo Provisório de
  Serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105059
version: 5
---

**O que é RPS?**  
O RPS é o Recibo Provisório de Serviços. Documento autorizado pelo Fisco e fornecido pelo contribuinte ao tomador do serviço contendo os dados de uma prestação de serviços que deverão ser informados ou transmitidos posteriormente ao Fisco Municipal quando não for possível a geração imediata da respectiva NFS-e.

**Como o RPS será gerado?**  
O RPS é valido por 10 dias a contar da data de sua emissão. Após a emissão do Recibo Provisório de Serviços, o prestador de serviços deverá substituí-lo por uma Nota Fiscal de Serviços Eletrônica - NFS-e no prazo de 10 dias, a contar da data de emissão do RPS.

**Qual a validade do RPS?**  
A sua Nota Fiscal deve ser preenchida com os dados cadastrais do prestador e tomador de serviço, os dados da discriminação dos serviços para somente uma atividade cadastrada no Cadastro Nacional de Atividades - CNAE, os códigos do CNAE e da lista de serviços, os dados referentes ao serviço prestado, a base de calcúlo, alíquota e o respectivo Imposto Sobre Serviços - ISS.

**Quando devo emitir o RPS?**  
Quando o prestador de serviço não dispuser de infra-estrutura de conectividade com o Fisco Municipal em tempo integral ou o sistema de geração da NFS-e estiver indisponível ou inacessível, excepcionalmente, o contribuinte deverá emitir o RPS.

**Pré-Condições:**

**1 -** Ter incluído um empreendimento e habilitado o [RPS](http://tdn.totvs.com.br/pages/viewpage.action?pageId=435104929 "Habilitar a utilização de RPS em um Empreendimento");  
**2 -** Ter permissão de acesso aos lançamentos, no módulo TOTVS Gestão financeira do BackOffice;  
**3 -** Ter Gerado uma Venda e seus Lançamentos Financeiros;  
**4 -** Ter efetuado a Baixa Parcial ou Total de um Lançamento vinculado a pré-condição 3;  
**5 -** Ter incluído um tipo de movimento no TOTVS Gestão de Estoque Compras e Faturamento com o código pertencente ao grupo **2.1.XX**. (A máscara de tipo de movimento 2.1.xx pertence ao grupo de movimentos relacionados á Pedidos de Venda);   
**6 -** Ter concebido permissão por tipo de movimento ao usuário, utilizando o contexto [TOTVS Gestão de Estoque Compras e Faturamento];  
**7 -** Para gerar o movimento RPS, é necessário que as subunidades vendidas do  empreendimento estejam com o campo [data do habite-se] preenchido  
**8 -** É necessário que  lançamentos financeiros tenham sido baixados  em uma data anterior  a informada no campo [data do habite-se] das subunidades. Mesmo que a data de vencimento de um lançamento seja superior  a data do campo [data do habite-se]  o sistema respeitará   o dado fornecido pelo campo [Data da Baixa] e  os lançamentos antes desta data tenham sofrido baixa financeira.

**Executando o processo:**

**1 -** Acesse: TOTVS Incorporação/ Contrato/ Contrato de Venda/ Processo / Gerar Movimento de RPS;  
**2 -** Informe a [Data Inicial] e a [Data Final] que  inclua a data de baixa do lançamento que atenda a pré-condição;  
**3 -** Clique no botão [Executar];  
**4 -** Selecione a Venda e acesse: Anexos/ Movimento de RPS- Recibo Provisório de Serviços. Serão exibidos os movimentos criados  para os lançamentos que tiveram baixa total ou parcial dentro do período pesquisado.

**Cancelar Movimento de RPS:**Somente será permitido cancelar o movimento de RPS, se o mesmo ainda não tiver gerado NFS-e. Caso já tenha ocorrido a geração da NFS-e, proceda os procedimentos padrões de cancelamento de NFS-e  no módulo  TOTVS Gestão de Estoque,  Compras e Faturamento para então cancelar o movimento de RPS.  
Movimentos de RPS gerados pelo módulo TOTVS Incorporação não poderão ser excluídos. Os mesmos devem ser cancelados, para manter histórico de geração de RPS.

**Cancelando um Movimento de RPS**

**1 -** Acesse: TOTVS Incorporação/ Contratos/ Contrato de Venda;  
**2 -** Selecione a Venda  e acesse: Anexo/ Movimento de RPS- Recibo Provisório de Serviços;  
**3 -** Selecione o Lançamento que deseja cancelar e acesse: Processos/ Cancelar Movimento de RPS- Recibo Provisório de Serviços;  
**4 -** Informe o [Motivo] do cancelamento e clique em [Executar].
