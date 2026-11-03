---
content_hash: 45b318a56c59ee3623fda74ecdb8a00a5e37ff7605b933fa42da283c7d2827c8
fetched_at: '2026-06-29T00:10:03.171480+00:00'
page_id: '452719037'
product: rm
source: tdn-rm
title: Relatório de Banco de Horas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719037
version: 2
---

**Relatório de Banco de Horas**

---

O banco de horas é um recurso utilizado pela grande maioria das empresas, que ao invés de pagar as extras e/ou descontar atrasos e faltas, guardam as horas no banco durante um período determinado e compensa o saldo até o final desse período. Ou seja, o banco de horas é uma forma de pagamento da hora extra, e posteriormente, ao invés do dinheiro, pode utilizar de horas de folga.  
O **TOTVS Automação de Ponto** permite gerenciar o banco de horas dos funcionários e fazer o acompanhamento através do **Relatório do Banco de horas**. Utilize o relatório para visualizar discriminadas por dia, as horas dos funcionários que possuem  banco de horas diário e o saldo determinado para esse período.  
   
Os parâmetros **'Considera saldo anterior'** e **'Considera saldo de períodos anteriores'** permitem a demonstração do saldo considerando, respectivamente, o saldo de acordo com a parametrização ou movimentação anterior do funcionário. Ou seja, a opção "Considera Saldo Anterior" o sistema busca o saldo informado nos parâmetros do funcionário, já o "Saldo de Períodos Anteriores" é o saldo do banco de horas resultante da soma das horas extras das ocorrências menos a soma dos atrasos e faltas das ocorrências dos períodos anteriores.  
   
Ao habilitar a opção **'Imprime apenas período crítico'** o relatório será gerado com base no limite de dias de compensação e serão abertos os campos data início e data fim do período crítico, que virão como default baseados no campo 'Limite de dias para Compensação' dos parâmetros do sistema. Neste caso somente serão impressas as ocorrências que se encontrarem dentro do período crítico informado.  
  
Observação  
O relatório traz a coluna data limite para compensação por data. A data limite é calculada a partir da data da inversão de saldo + limite de dias compensação. O limite de dias compensação levado em consideração primeiro é o localizado no Parametrizador > Iniciais > Compensação, se o mesmo não possui nenhum dia de limite o relatório leva em consideração o limite cadastrado no parametrizador do sindicato.  
   
Para flexibilizar a utilização, o layout do relatório poderá ser configurado de acordo com a necessidade da empresa através do novo gerador de relatório (RM Reports). Por exemplo, podemos configurar o relatório imprimindo ou não, um funcionário por página, saldo a compensar, relatório sintético ou quebrando por seção.   
**Observação**  
A utilização desse relatório dependerá de um modelo criado pela **TOTVS**, no qual ficará disponível no momento da instalação do aplicativo RM Chronus. Basta acessar o RM Reports e realizar a importação do arquivo com a estrutura do arquivo (PTOREL01.0005 - Relatório Banco de Horas .TotvsReport).
