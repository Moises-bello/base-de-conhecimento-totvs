---
article_id: 360003143831
category: Encargos
content_hash: 5e49d11bfcd58e52cc3208ad9eb7ec9f26c8525492f6c8fe6fba5d144c2c922b
fetched_at: '2026-06-28T22:46:53.435587+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - Contabilização: Erro ao obter conta Saldus'
type: support-article
updated_at: '2025-03-13T11:24:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003143831-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o-Erro-ao-obter-conta-Saldus
---

**Ocorrência**Ao gerar a contabilização da folha de pagamentos, um dos erros comuns é:   
  
**AgrupamentoContabil: Erro ao obter conta Saldus.**  
**Grupo contábil: 2112001, Integração contábil: , Integração funcionário: - Conta**  
**Saldus:**  
  
**Ambiente**RM - Totvs Folha de Pagamento - A partir da versão 11.40  
  
**Causa**Este erro acontece pois, na montagem dos dados, o sistema procura o agrupamento contábil a ser utilizado, conforme as parametrizações da contabilização, mas não encontra nenhum agrupamento refente a esta parametrização em **"Encargos | Cadastros | Cadastros Contábeis | Agrupamento de contas"**.

Isto se dá em duas situações: a primeira é quando existe a real necessidade da criação do agrupamento contábil. Também pode acontecer de existir um agrupamento com o mesmo código, mas que não tenha o campo **"Código de Integração"** preenchido.  
  
**Solução**Para solucionar este erro, caso seja necessário cadastrar um novo agrupamento, cadastre novo registro e realize a geração da contabilização novamente. Se não for o caso, deveremos verificar o motivo do sistema buscar o agrupamento incorreto que não possui o "Código de Integração" informado.   
  
Neste verificação, veja o final do log de execução do processo, onde será exibido o código do evento ou encargo que está sendo contabilizado no momento do erro:  
  
**Exemplo do log de Execução**---------------------  
**Lote: 1220120**  
**Chapa: 00001 Nome: ITAMAR MENDES DA SILVEIRA**  
**Contabilização por Seção**  
**Contabilizando Evento**  
**Verba : 0002**  
**Valor : 10000,00**  
---------------------  
  
No exemplo acima a execução da contabilização foi interrompida no evento 0002. No cadastro deste evento encontramos o agrupamento **"111"** a Crédito e o evento **"Tem integração contábil"**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360004154352/mceclip5.png)  
  
Quando o parâmetro **"Tem integração contábil"** está marcado, o **"Código de integração"** será retornado com base na seguinte regra: se o sistema **não** estiver parametrizado para utilizar cálculo por centro de custo em **"Configurações | Parametrizador | Folha Normal | Cálculo"**...  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360004157971/mceclip6.png)  
  
... o código de integração será verificado no cadastro da seção do funcionário, aba **"Dados contábeis"**, campo **"Integração contábil"**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360004157951/mceclip3.png)  
  
Porém, se o parâmetro **"Utiliza Cálculo por Centro de Custo"** estiver **marcado**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360004154332/mceclip4.png)  
  
O local onde o sistema irá buscar o **"Código de integração"** será no cadastro do centro de custo do evento, que está informado na movimentação por centro de custo no envelope de pagamento do funcionário.  
  
Movimentação por centro de custo do envelope:![](https://centraldeatendimento.totvs.com/hc/article_attachments/360004154372/mceclip0.png)  
  
Cadastro do centro de custo 02.2.1.1:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360004154392/mceclip1.png)

Nesse caso deveria ser informado um valor no campo **"Código de integração contábil"**, de forma a se obter um agrupamento que exista no cadastro de **"Agrupamentos de contas contábeis"**.  
  
  
**Importante**O processo de **"Integração por funcionário"**irá seguir os mesmos passos da rotina acima, incluindo o código de integração que está informado no cadastro do funcionário, em **"Rotinas Mensais | Dados Contábeis"**. Para utilizar a **"Integração por funcionário"** deverá marcar a flag **“Tem integração por funcionário”** no cadastro de eventos e/ou encargos.  
  
Assim, o sistema também irá verificar se no cadastro de Agrupamentos de contas contábeis os agrupamentos possuem os códigos de integração por funcionário informados.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360004154412/mceclip2.png)
