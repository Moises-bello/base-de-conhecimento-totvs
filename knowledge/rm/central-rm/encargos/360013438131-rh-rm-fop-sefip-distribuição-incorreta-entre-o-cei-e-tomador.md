---
article_id: 360013438131
category: Encargos
content_hash: 9548dfa5688d2ef5a968f2aee9650324f7678bed6421b2209b38e910d89de682
fetched_at: '2026-06-28T22:46:53.397918+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - SEFIP: Distribuição Incorreta entre o CEI e Tomador'
type: support-article
updated_at: '2025-03-13T11:25:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013438131-RH-RM-FOP-SEFIP-Distribui%C3%A7%C3%A3o-Incorreta-entre-o-CEI-e-Tomador
---

**Ocorrência**No módulo **Folha de Pagamento**, ao gerar a SEFIP o arquivo .RE foi gerado com os valores do CEI e Tomador (CNPJ) distribuídos incorretamente.  
   
 **Ambiente**RM - Folha de Pagamento - Todas as versões  
   
 **Causas**Este erro pode ocorrer por duas causas específicas:  
  
**01.** O evento não possui marcação no parâmetro **Segue Rateio de Tomadores**.  
**02.** Quantidade de dias incorreta no **Rateio de Tomadores** do funcionário.  
  
 **Solução**Para solucionar este caso, veja os passos abaixo.  
  
**01.** O evento não possui marcação no parâmetro **Segue Rateio de Tomadores:**  
  
É necessário que nos casos em que a empresa utiliza Tomador de Serviço, a Flag **Segue Rateio de Tomadores**esteja marcada no cadastro dos eventos. Para marcar este parâmetro, acesse o menu **Administração de Pessoal | Eventos** e faça um filtro que retorne os eventos que estão com a flag **Segue Rateio de Tomadores** desmarcada. Para parametrizar o filtro, selecione a opção no filtro **Segue rateio de tomadores** e **operador = 0**.  
  
Veja o filtro exemplificado abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009233631/mceclip0.png)  
  
Após aplicar o filtro acima, serão apresentados todos os eventos que estiverem com o parâmetro **Segue rateio de Tomadores** desmarcada. Marque a flag nos eventos que estiverem desmarcados, distribua a Sefip novamente e gere o arquivo .RE.  
  
**02.** Quantidade de dias incorreta no **Rateio de Tomadores** do funcionário.  
  
Se a causa do erro for o **Rateio de Tomadores**, primeiramente você deverá verificar se em **Configurações | Parametrizador | Folha Normal | Tomador de Serviço** se o parâmetro **Cód da fórmula do fator de proporcionalidade** está preenchido. Se ele estiver preenchido, os dias de rateio no cadastro do funcionário serão proporcionalizados, conforme dias cadastrados.  
  
Caso o parâmetro **Cód da fórmula do fator de proporcionalidade**não esteja preenchido, então será necessário verificar no cadastro do funcionário se foram informados 30 dias de rateio. Caso negativo, informe o restante dos dias totalizando 30 dias, distribua Sefip novamente e gere o arquivo .RE.
