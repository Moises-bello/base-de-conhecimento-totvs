---
article_id: 360038674513
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 183606272cd4a3db9b38f5603465b09ece70cf785b6a5f8d1829b9057c17a597
fetched_at: '2026-06-28T22:42:11.834375+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Processamento
  em MultiThread - Geração FCI
type: support-article
updated_at: '2022-08-18T14:08:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038674513-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Processamento-em-MultiThread-Gera%C3%A7%C3%A3o-FCI
---

**Dúvida**Processamento em MultiThread - Geração FCI  
  
 **Ambiente**  
Protheus – Financeiro – A partir da versão 11.80  
  
**Solução**  
**Processamento em MultiThread**  
  
Em bases grandes, quando há uma grande quantidade de produtos, o processamento da apuração pode levar um tempo considerável para ser concluído. Para reduzir o tempo de processamento é possível configurar a rotina para a execução em MultiThread, ou seja, serão criadas threads auxiliares para que seja possível processar mais de um produto simultaneamente.  
   
A ativação da execução em MultiThread é feita a partir da configuração do parâmetro **MV\_FCINTHD.**Este parâmetro indica a quantidade de threads auxiliares a serem criadas.  
   
Importante  
Por questões de segurança e para evitar consumo excessivo de memória a rotina trabalha com, no máximo, 5 threads auxiliares. Sua utilização deve ser previamente analisada pois mesmo trabalhando dentro do limite o consumo de memória com este tipo de processamento é superior ao habitual. Desta forma, é necessário verificar se o servidor não será sobrecarregado com este processo.  
   
Para acompanhamento do processamento em MultiThread serão emitidas mensagens no console conforme o progresso da rotina. Quando esta funcionalidade for ativada, será criado um diretório chamado "log\_fci" dentro do diretório especificado na chave "StartPath" do appserver.INI. Dentro deste diretório serão criados os arquivos de LOG de execução, onde serão demonstrados os produtos processados por cada uma das threads e, caso venha a ocorrer algum erro durante o processamento, este erro será registrado nestes arquivos.  
   
O nome dos arquivos de LOG é composto da seguinte forma: **fisa061 + <número da thread> + \_ + <código da empresa> + <código da filial> + \_ + <data de processamento>**.txt  
 

Para maiores informações acesse o link abaixo:

[https://tdn.totvs.com/pages/releaseview.action?pageId=185758724](https://www.google.com/url?q=https://tdn.totvs.com/pages/releaseview.action?pageId%3D185758724&sa=D&source=hangouts&ust=1573318258167000&usg=AFQjCNHxOfmHchDnVLsf5z1_q7kMqTTfGQ)
