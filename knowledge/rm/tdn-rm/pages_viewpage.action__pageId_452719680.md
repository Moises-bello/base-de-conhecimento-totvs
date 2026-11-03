---
content_hash: f007a43ecc027d86614b7e73d4f51f3aae79a84483b659f089305874ffdb0fb5
fetched_at: '2026-06-29T00:10:09.487926+00:00'
page_id: '452719680'
product: rm
source: tdn-rm
title: Relatório de Exceções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719680
version: 1
---

**Relatório de Exceções**

---

As **exceções** são todas as ocorrências registradas para o funcionário no período de apuração do ponto e que possivelmente são passíveis de uma justificativa como os atrasos, extras, faltas e abonos.  
   
Utilize o relatório para reportar um conjunto de informações além das exceções, como dados das batidas e até mesmo os avisos calculados, que ficarão disponíveis de forma clara e organizada.  
   
O relatório possui os recursos de:

* Limitar as horas a serem impressas filtrando somente as horas que o funcionário executou acima de um determinado valor informado no campo NUMERO DE HORAS ACIMA DE;
* Desconsiderar faltas a compensar, atraso a compensar ou extras compensar imprimindo somente as horas que serão descontadas ou pagas ao funcionário , não mostrando as horas que serão compensadas e encaminhadas para o banco.  
   - Selecionar os avisos que deseja imprimir, ou seja, alertas como horas trabalhadas pelo funcionário superior a 10 horas ou menos que 1 hora de refeição;  
  **Observação**  
  Os avisos calculados só serão gerados ao utilizar o novo cálculo e poderão ser visualizados no espelho do funcionário.  
     
  Para flexibilizar a utilização, o layout do relatório poderá ser configurado de acordo com a necessidade da empresa através do novo gerador de relatório (RM Reports). Por exemplo, podemos configurar o relatório imprimindo ou não as justificativas e as saidas intermediárias ou mesmo reposicionar no relatório o local de assinatura.  
  **Observação**  
  A utilização desse relatório dependerá de um modelo criado pela **TOTVS**, no qual ficará disponível no momento da instalação do aplicativo RM Chronus. Basta acessar o RM Reports e realizar a importação do arquivo com a estrutura do arquivo (PTOREL01.0004 - Relatório de Exceções.TotvsReport).  
     
     
      
  **Ordenação por seção**   
     
  A ordenação por seção tem como base a quebra por seção informada limitada a mascara informada.  
     
  Se for informado a quebra com estes 6 dígitos:    
  .?  
     
  A ordenação será limitada a estes . Para ordenar integralmente as seções com o padrão 02.100.0011.0005.0028.0000.4 deverá ser usado a quebra .?.??...??.? **além de marcar a ordenação por seção.**
